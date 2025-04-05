"""This module defines the LongTermAgent class which uses both short-term and
long-term memory to store and retrieve observations, along with QA, exploration, and
memory management policies.
"""

from __future__ import annotations

import heapq
import random
from collections import deque
from copy import deepcopy
from datetime import datetime, timedelta
from typing import Any, Optional

import gymnasium as gym
import numpy as np
from rdflib import Graph, Literal, Namespace, URIRef, XSD

from humemai.rdflib import Humemai
from .agent import Agent
from .utils import write_yaml


class LongTermAgent(Agent):
    """
    An agent that manages both short-term and long-term memories via Humemai.
    Supports QA, exploration, and memory management policies.
    """

    def __init__(
        self,
        env_str: str = "room_env:RoomEnv-v2",
        env_config: dict[str, Any] = {
            "question_prob": 1.0,
            "seed": 42,
            "terminates_at": 99,
            "randomize_observations": "all",
            "room_size": "xl-different-prob",
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": 1000,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": False,
        },
        qa_policy: str = "latest",
        explore_policy: str = "bfs",  # "random", "avoid_walls", "bfs", "dijkstra"
        mm_policy: str = "FIFO",  # "FIFO", "LRU", "LFU", "LFU+LRU", "random", "belady"
        max_long_term_memory_size: int = 100,
        num_samples_for_results: int = 10,
        save_results: bool = True,
        default_root_dir: str = "./training-results/",
    ) -> None:
        """
        Initialize a LongTermAgent with environment configuration, QA policy,
        exploration policy, and memory management parameters.
        """
        params_to_save = deepcopy(locals())
        del params_to_save["self"]
        del params_to_save["__class__"]
        super().__init__(**params_to_save)

        self.qa_policy = qa_policy
        self.explore_policy = explore_policy
        self.mm_policy = mm_policy
        if self.mm_policy == "belady":
            assert env_config["deterministic_objects"], (
                "Belady's algorithm requires deterministic objects. "
                "Set 'deterministic_objects' to True in env_config."
            )
            assert env_config["randomize_observations"] == "none", (
                "Belady's algorithm requires deterministic observations. "
                "Set 'randomize_observations' to 'none' in env_config."
            )
            self.memory_access_log = {}  # {step: set(memory_ids)}
            self.next_access_lookup = {}  # {memory_id: [future access steps]}

        self.max_long_term_memory_size = max_long_term_memory_size

        # Track current_step to sync with environment steps
        self.current_step = 0

        # HumemAI setup
        self.humemai_ns = Namespace("https://humem.ai/ontology#")
        self.base_date = datetime.fromisoformat("2025-01-01T00:00:00")
        self.humemai = Humemai()

    # -------------------------------------------------------------------------
    # Memory Management
    # -------------------------------------------------------------------------

    def manage_memory(self, observations: list[list[str]], step: int) -> None:
        """
        Manage memory by:
          1) Move all short-term memories to episodic.
          2) Enforce memory management until total meets the size limit.
          3) Clear short-term memory.
          4) Add new short-term observations.
        """
        # 1) Move short-term => episodic
        self.humemai.move_all_short_term_to_episodic()

        # 2) While we exceed memory limits, prune one statement at a time
        while (
            self.humemai.get_long_term_memory_count() > self.max_long_term_memory_size
        ):
            if self.mm_policy.lower() == "fifo":
                mem_id_to_delete = self._pick_fifo_victim()
            elif self.mm_policy.lower() == "lru":
                mem_id_to_delete = self._pick_lru_victim()
            elif self.mm_policy.lower() == "lfu":
                mem_id_to_delete = self._pick_lfu_victim()
            elif self.mm_policy.lower() in ["lfu+lru", "lru+lfu"]:
                mem_id_to_delete = self._pick_lfu_lru_victim()
            elif self.mm_policy.lower() == "random":
                mem_id_to_delete = self._pick_random_victim()
            elif self.mm_policy.lower() == "belady":
                mem_id_to_delete = self._pick_belady_victim()
            else:
                raise NotImplementedError(
                    f"Memory management policy '{self.mm_policy}' not implemented."
                )

            if mem_id_to_delete is None:
                raise ValueError("No memory ID found for deletion.")
            self.humemai.delete_memory(Literal(mem_id_to_delete))

        # 3) Clear short-term
        self.humemai.clear_short_term_memories()

        # 4) Insert new observations in short-term
        self.current_time = self.base_date + timedelta(days=step)
        triples = [[URIRef(item) for item in obs] for obs in observations]
        qualifiers = {
            self.humemai_ns.current_time: Literal(
                self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
            )
        }
        self.humemai.add_short_term_memory(triples=triples, qualifiers=qualifiers)

    # ------------------------ FIFO ------------------------

    def _pick_fifo_victim(self) -> Optional[int]:
        """Earliest humemai:event_time => evict (FIFO)."""
        timestamps = self.find_unique_timestamps()
        if not timestamps:
            raise ValueError("No timestamps => cannot pick FIFO victim.")
        oldest = min(timestamps)
        mem_ids = self.find_memory_ids_by_event_time(oldest)
        if not mem_ids:
            raise ValueError(
                "No memory found at earliest timestamp => FIFO victim error."
            )
        return random.choice(mem_ids)

    def find_unique_timestamps(self) -> list[str]:
        """All distinct humemai:event_time in LTM."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT DISTINCT ?et
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:event_time ?et .
            }
        """
        results = self.humemai.graph.query(query)
        return [str(row.et) for row in results]

    def find_memory_ids_by_event_time(self, t: str) -> list[int]:
        """MemIDs with event_time == t."""
        query = f"""
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            SELECT ?memoryID
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    humemai:event_time "{t}"^^xsd:dateTime ;
                    humemai:memoryID ?memoryID .
            }}
        """
        rows = list(self.humemai.graph.query(query))
        return [int(r.memoryID) for r in rows]

    # ------------------------ LRU ------------------------

    def _pick_lru_victim(self) -> Optional[int]:
        """Oldest humemai:last_accessed => evict."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memoryID ?la
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
              OPTIONAL { ?stmt humemai:last_accessed ?la. }
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick LRU victim.")

        oldest_time = datetime.max
        victim = None

        for row in rows:
            mem_id = int(row.memoryID)
            la = row.la
            if la is None:
                raise ValueError(
                    f"LRU victim check failed: Memory {mem_id} is missing 'last_accessed'. "
                    "We require all LTM statements to have last_accessed."
                )
            try:
                la_dt = datetime.fromisoformat(str(la))
            except ValueError:
                raise ValueError(
                    f"LRU victim check failed: Memory {mem_id} has an unparseable last_accessed='{la_literal}'."
                )
            if la_dt < oldest_time:
                oldest_time = la_dt
                victim = mem_id

        return victim

    # ------------------------ LFU ------------------------

    def _pick_lfu_victim(self) -> Optional[int]:
        """Smallest humemai:recalled => evict. Missing => zero => immediate eviction."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memoryID ?rec
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
              OPTIONAL { ?stmt humemai:recalled ?rec. }
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick LFU victim.")

        victim = None
        lowest = None
        for row in rows:
            mem_id = int(row.memoryID)
            rec = row.rec
            if rec is None:
                raise ValueError(
                    f"LFU victim check failed: Memory {mem_id} is missing 'recalled'. "
                    "All LTM statements must have recalled."
                )
            try:
                rec_val = int(rec)
            except ValueError:
                return mem_id
            if (lowest is None) or (rec_val < lowest):
                lowest = rec_val
                victim = mem_id

        return victim

    # ------------------------ LFU+LRU ------------------------

    def _pick_lfu_lru_victim(self) -> Optional[int]:
        """
        Evict statement with the smallest (recalled / delta_days), i.e. it’s used
        less frequently and not recently. Missing recalled => 0. Missing last_accessed => big delta.
        """
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memoryID ?la ?rec
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
              OPTIONAL { ?stmt humemai:last_accessed ?la. }
              OPTIONAL { ?stmt humemai:recalled ?rec. }
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick LFU+LRU victim.")

        best_victim = None
        best_score = None  # smallest => evict
        for row in rows:
            mem_id = int(row.memoryID)
            la = row.la
            rec = row.rec
            if rec is None:
                rec_val = 0
            else:
                try:
                    rec_val = int(rec)
                except ValueError:
                    rec_val = 0

            # missing la => treat as far in the past => large delta
            if la is None:
                la_dt = self.base_date - timedelta(days=3650)
            else:
                try:
                    la_dt = datetime.fromisoformat(str(la))
                except ValueError:
                    la_dt = self.base_date - timedelta(days=3650)

            dt_days = (self.current_time - la_dt).total_seconds() / 86400.0
            if dt_days < 1.0:
                dt_days = 1.0

            score = rec_val / dt_days
            if (best_score is None) or (score < best_score):
                best_score = score
                best_victim = mem_id

        return best_victim

    # ------------------------ random ------------------------

    def _pick_random_victim(self) -> Optional[int]:
        """Randomly evict anything in LTM."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memoryID
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick random victim.")
        return int(random.choice(rows).memoryID)

    # ------------------------ Bélády (no fallback!) ------------------------

    def _pick_belady_victim(self) -> Optional[int]:
        """
        Evict the memory that has the furthest *future* access — or none at all.
        If no memory can be found (i.e. we have no precomputed info), we raise an error
        instead of falling back to another policy.
        """
        # gather all memIDs in LTM
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?memoryID
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick Belady victim.")
        memory_ids = [int(r.memoryID) for r in rows]
        print(f"Belady selection: {len(memory_ids)} possible victims")

        # check which we have precompute data for
        valid_precomputed = [m for m in memory_ids if m in self.next_access_lookup]
        print(f"  With future-access data: {len(valid_precomputed)}")

        # We track two groups: never accessed again vs next accessible
        never_accessed_again = []
        next_access_map = {}

        for memid in memory_ids:
            if memid not in self.next_access_lookup:
                # if no precompute data => we can't guess => let's be strict
                # interpret that as "never accessed again"
                never_accessed_again.append(memid)
            else:
                future_steps = [
                    st
                    for st in self.next_access_lookup[memid]
                    if st > self.current_step
                ]
                if not future_steps:
                    never_accessed_again.append(memid)
                else:
                    # store the earliest upcoming access
                    next_access_map[memid] = min(future_steps)

        # Priority 1: never accessed again => pick random
        if never_accessed_again:
            victim = random.choice(never_accessed_again)
            print(f"Belady victim: memID={victim}, never accessed again.")
            return victim

        # Priority 2: furthest next access
        if next_access_map:
            # pick the memory whose next access is the largest
            victim = max(next_access_map.items(), key=lambda kv: kv[1])[0]
            print(
                "Belady victim: memID=%d, next access step=%d "
                "(furthest in future)." % (victim, next_access_map[victim])
            )
            return victim

        # If we got here, it means memory_ids existed but
        # we have no next access times and none in never_accessed_again => weird
        raise ValueError(
            "Belady found no suitable victim. We have memories but no future-access data."
        )

    # -------------------------------------------------------------------------
    # QA Policy
    # -------------------------------------------------------------------------

    def answer_question(self, question: tuple[str, str]) -> str:
        """
        Answer question using self.qa_policy, then increment recall for that statement.
        """
        subj_str = f"<{question[0]}>"
        pred_str = f"<{question[1]}>"
        query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?stmt ?obj (COALESCE(?ct, ?et, ?ks) as ?timeVal)
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject {subj_str} ;
                    rdf:predicate {pred_str} ;
                    rdf:object ?obj .
              OPTIONAL {{ ?stmt humemai:current_time ?ct. }}
              OPTIONAL {{ ?stmt humemai:event_time ?et. }}
              OPTIONAL {{ ?stmt humemai:known_since ?ks. }}
            }}
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            return None

        if self.qa_policy == "latest":
            # pick row with largest timeVal
            valid_rows = [r for r in rows if r.timeVal is not None]
            if not valid_rows:
                return None
            valid_rows.sort(key=lambda x: x.timeVal, reverse=True)
            best_row = valid_rows[0]
        elif self.qa_policy == "oldest":
            valid_rows = [r for r in rows if r.timeVal is not None]
            if not valid_rows:
                return None
            valid_rows.sort(key=lambda x: x.timeVal)
            best_row = valid_rows[0]
        elif self.qa_policy == "random":
            best_row = random.choice(rows)
        elif self.qa_policy == "one_hop":
            best_row = rows[0]
        else:
            raise ValueError(f"Unknown QA policy {self.qa_policy}")

        best_obj = best_row.obj
        best_time = best_row.timeVal
        obj_uri = URIRef(str(best_obj))

        self._update_qa_memory_access(
            subject=URIRef(question[0]),
            predicate=URIRef(question[1]),
            object_=obj_uri,
            time_literal=best_time,
        )
        return str(obj_uri)

    def _update_qa_memory_access(
        self,
        subject: URIRef,
        predicate: URIRef,
        object_: URIRef,
        time_literal: Literal,
    ) -> None:
        """Increment recalled + update last_accessed for one triple in LTM."""
        self.humemai.increment_recalled(
            subject=subject,
            predicate=predicate,
            object_=object_,
            lower_time_bound=time_literal,
            upper_time_bound=time_literal,
        )
        new_time_lit = Literal(
            self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
        )
        self.humemai.update_last_accessed(
            subject=subject,
            predicate=predicate,
            object_=object_,
            new_time=new_time_lit,
            lower_time_bound=time_literal,
            upper_time_bound=time_literal,
        )

    # -------------------------------------------------------------------------
    # Exploration
    # -------------------------------------------------------------------------

    def explore(self) -> str:
        """Explore with the specified self.explore_policy."""
        if self.explore_policy == "random":
            return random.choice(["north", "south", "east", "west", "stay"])
        elif self.explore_policy == "avoid_walls":
            return self._explore_avoid_walls()
        elif self.explore_policy == "bfs":
            return self._explore_bfs()
        elif self.explore_policy == "dijkstra":
            return self._explore_dijkstra()
        else:
            raise ValueError(f"Invalid explore_policy: {self.explore_policy}")

    def _explore_avoid_walls(self) -> str:
        """Pick a random direction that doesn't lead to <wall> (from short-term memory)."""
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?dir
            WHERE {
              ?stmt1 rdf:type rdf:Statement ;
                     rdf:subject <agent> ;
                     rdf:predicate <at_location> ;
                     rdf:object ?room .
              ?stmt2 rdf:type rdf:Statement ;
                     rdf:subject ?room ;
                     rdf:predicate ?dir ;
                     rdf:object ?target .
              FILTER(?dir IN (<north>, <south>, <east>, <west>))
              FILTER(?target != <wall>)
            }
        """
        rows = list(self.humemai.graph.query(query))
        dirs = [str(r.dir).strip("<>") for r in rows]
        if not dirs:
            # fallback or just pick something
            return "stay"
        return random.choice(dirs)

    # -------------------------------------------------------------------------
    # BFS
    # -------------------------------------------------------------------------

    def _explore_bfs(self) -> str:
        """BFS-based exploration; tries to find an unvisited room; else fallback."""
        current_room = self._get_agent_current_room()
        visited_rooms = self._get_visited_rooms()
        adjacency = self._build_room_adjacency()

        path = self._bfs_find_new_room_with_path(current_room, adjacency, visited_rooms)
        if path:
            self._update_path_memory_access(path)
            return path[0][1]  # direction in the first edge

        # else fallback: pick least-visited or just avoid walls
        candidate_room = self._pick_least_visited_room(visited_rooms, current_room)
        if not candidate_room or candidate_room == current_room:
            return self._explore_avoid_walls()

        path2 = self._bfs_path_to_specific_room(current_room, candidate_room, adjacency)
        if path2:
            self._update_path_memory_access(path2)
            return path2[0][1]
        return self._explore_avoid_walls()

    def _bfs_find_new_room_with_path(
        self,
        start_room: str,
        adjacency: dict[str, list[tuple[str, str]]],
        visited_rooms: set[str],
    ) -> Optional[list[tuple[str, str, str]]]:
        """Find BFS path to first unvisited room."""
        queue = deque([start_room])
        parents = {start_room: None}
        while queue:
            current = queue.popleft()
            if current not in visited_rooms and current != start_room:
                return self._bfs_reconstruct_path(parents, start_room, current)
            for direction, nbr in adjacency.get(current, []):
                if nbr not in parents:
                    parents[nbr] = (current, direction)
                    queue.append(nbr)
        return None

    def _bfs_path_to_specific_room(
        self,
        start: str,
        goal: str,
        adjacency: dict[str, list[tuple[str, str]]],
    ) -> Optional[list[tuple[str, str, str]]]:
        """BFS from start to goal."""
        if start == goal:
            return []
        queue = deque([start])
        parents = {start: None}
        while queue:
            cur = queue.popleft()
            if cur == goal:
                return self._bfs_reconstruct_path(parents, start, goal)
            for d, nbr in adjacency.get(cur, []):
                if nbr not in parents:
                    parents[nbr] = (cur, d)
                    queue.append(nbr)
        return None

    def _bfs_reconstruct_path(
        self, parents: dict[str, Optional[tuple[str, str]]], start: str, goal: str
    ) -> list[tuple[str, str, str]]:
        """Reverse BFS parents to get edges: (roomX, direction, roomY)."""
        edges = []
        cur = goal
        while cur != start and cur in parents:
            link = parents[cur]
            if not link:
                break
            prev_room, direction = link
            edges.append((prev_room, direction, cur))
            cur = prev_room
        edges.reverse()
        return edges

    # -------------------------------------------------------------------------
    # Dijkstra
    # -------------------------------------------------------------------------

    def _explore_dijkstra(self) -> str:
        """Dijkstra-based exploration to unvisited or least-visited room."""
        current_room = self._get_agent_current_room()
        visited_rooms = self._get_visited_rooms()
        adjacency = self._build_room_adjacency_with_weights()

        path = self._dijkstra_find_best_unvisited(
            current_room, adjacency, visited_rooms
        )
        if path:
            self._update_path_memory_access(path)
            return path[0][1]

        # fallback
        candidate_room = self._pick_least_visited_room(visited_rooms, current_room)
        if not candidate_room or candidate_room == current_room:
            return self._explore_avoid_walls()

        path2 = self._dijkstra_path_to_room(current_room, candidate_room, adjacency)
        if path2:
            self._update_path_memory_access(path2)
            return path2[0][1]
        else:
            return self._explore_avoid_walls()

    def _dijkstra_find_best_unvisited(
        self,
        start: str,
        adjacency: dict[str, list[tuple[str, str, float]]],
        visited_rooms: set[str],
    ) -> Optional[list[tuple[str, str, str]]]:
        """Dijkstra from start, pick first unvisited with minimal cost."""
        best_cost, parent = self._dijkstra_min_cost_path(start, adjacency)
        candidates = []
        for room, cost_val in best_cost.items():
            if room not in visited_rooms and room != start and cost_val < float("inf"):
                candidates.append((room, cost_val))
        if not candidates:
            return None
        candidates.sort(key=lambda x: x[1])
        best_room = candidates[0][0]
        return self._dijkstra_reconstruct(parent, start, best_room)

    def _dijkstra_path_to_room(
        self, start: str, goal: str, adjacency: dict[str, list[tuple[str, str, float]]]
    ) -> Optional[list[tuple[str, str, str]]]:
        """Dijkstra from start to a specific goal."""
        if start == goal:
            return []
        best_cost, parent = self._dijkstra_min_cost_path(start, adjacency)
        if best_cost.get(goal, float("inf")) == float("inf"):
            return None
        return self._dijkstra_reconstruct(parent, start, goal)

    def _dijkstra_min_cost_path(
        self, start: str, adjacency: dict[str, list[tuple[str, str, float]]]
    ) -> tuple[dict[str, float], dict[str, tuple[str, str]]]:
        """Usual Dijkstra over adjacency dict."""
        best_cost = {room: float("inf") for room in adjacency}
        best_cost[start] = 0.0
        parent = {}

        heap = [(0.0, start)]
        while heap:
            cur_dist, cur_room = heapq.heappop(heap)
            if cur_dist > best_cost[cur_room]:
                continue
            for direction, nbr, edge_cost in adjacency.get(cur_room, []):
                alt = cur_dist + edge_cost
                if alt < best_cost.get(nbr, float("inf")):
                    best_cost[nbr] = alt
                    parent[nbr] = (cur_room, direction)
                    heapq.heappush(heap, (alt, nbr))
        return best_cost, parent

    def _dijkstra_reconstruct(
        self, parent: dict[str, tuple[str, str]], start: str, goal: str
    ) -> list[tuple[str, str, str]]:
        """Rebuild edges from Dijkstra parent links."""
        edges = []
        cur = goal
        while cur != start and cur in parent:
            prev_room, direction = parent[cur]
            edges.append((prev_room, direction, cur))
            cur = prev_room
        edges.reverse()
        return edges

    def _build_room_adjacency_with_weights(
        self,
    ) -> dict[str, list[tuple[str, str, float]]]:
        """
        Weighted adjacency for dijkstra: cost = 1 / (1 + # interesting objects in the target).
        """
        adjacency = {}
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?roomX ?dir ?roomY
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject ?roomX ;
                    rdf:predicate ?dir ;
                    rdf:object ?roomY .
              FILTER(?dir IN (<north>, <south>, <east>, <west>))
            }
        """
        rows = list(self.humemai.graph.query(query))
        for r in rows:
            rx = str(r.roomX)
            d = r.dir.rsplit("/", 1)[-1]
            ry = str(r.roomY)
            if ry.endswith("wall"):
                continue
            cost = 1.0 / (1.0 + self._count_interesting_objects_in_room(ry))
            adjacency.setdefault(rx, []).append((d, ry, cost))
        return adjacency

    # -------------------------------------------------------------------------
    # BFS/Dijkstra Helpers
    # -------------------------------------------------------------------------

    def _get_agent_current_room(self) -> str:
        """Agent's current room from short-term memory."""
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?room
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <agent> ;
                    rdf:predicate <at_location> ;
                    rdf:object ?room ;
                    humemai:current_time ?time .
            }
            LIMIT 1
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No short-term record of the agent's current room!")
        return str(rows[0].room)

    def _build_room_adjacency(self) -> dict[str, list[tuple[str, str]]]:
        """Unweighted adjacency for BFS."""
        adjacency = {}
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?roomX ?dir ?roomY
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject ?roomX ;
                    rdf:predicate ?dir ;
                    rdf:object ?roomY .
              FILTER(?dir IN (<north>, <south>, <east>, <west>))
            }
        """
        rows = list(self.humemai.graph.query(query))
        for r in rows:
            rx = str(r.roomX)
            d = r.dir.rsplit("/", 1)[-1]
            ry = str(r.roomY)
            if ry.endswith("wall"):
                continue
            adjacency.setdefault(rx, []).append((d, ry))
        return adjacency

    def _count_interesting_objects_in_room(self, room: str) -> int:
        """Count objects with 'sat_', 'ind_', or 'dep_' in their URI inside a room."""
        prefixes = ("sat_", "ind_", "dep_")
        query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?subj
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject ?subj ;
                    rdf:predicate <at_location> ;
                    rdf:object <{room}> .
            }}
        """
        rows = list(self.humemai.graph.query(query))
        count = 0
        for r in rows:
            s = str(r.subj)
            if any(pref in s for pref in prefixes):
                count += 1
        return count

    def _get_visited_rooms(self) -> set[str]:
        """
        Rooms in LTM: (agent, at_location, room, event_time=...).
        """
        visited = set()
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?room
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <agent> ;
                    rdf:predicate <at_location> ;
                    rdf:object ?room ;
                    humemai:event_time ?et .
            }
        """
        rows = list(self.humemai.graph.query(query))
        for r in rows:
            visited.add(str(r.room))
        return visited

    # -------------------------------------------------------------------------
    # "Least Visited" Helper
    # -------------------------------------------------------------------------

    def _pick_least_visited_room(
        self, visited_rooms: set[str], current_room: str
    ) -> Optional[str]:
        """Among visited_rooms, pick the one with the fewest LTM visits."""
        if not visited_rooms:
            return None
        room_visits = self._get_room_visit_counts()
        candidates = [r for r in visited_rooms if r != current_room]
        if not candidates:
            return None
        candidates.sort(key=lambda r: room_visits.get(r, 0))
        return candidates[0]

    def _get_room_visit_counts(self) -> dict[str, int]:
        """Return # of times the agent was (at_location room) in event_time-based LTM."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?room (COUNT(?et) as ?vcount)
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <agent> ;
                    rdf:predicate <at_location> ;
                    rdf:object ?room ;
                    humemai:event_time ?et .
            }
            GROUP BY ?room
        """
        rows = list(self.humemai.graph.query(query))
        visits = {}
        for r in rows:
            room_uri = str(r.room)
            visits[room_uri] = int(r.vcount.toPython())
        return visits

    # -------------------------------------------------------------------------
    # BFS/Dijkstra "Memory Access" increments
    # -------------------------------------------------------------------------

    def _update_path_memory_access(self, edges: list[tuple[str, str, str]]) -> None:
        """Increment recall + update last_accessed for each edge in the path."""
        for subj, pred, obj in edges:
            self._update_exploration_edge_memory(subj, pred, obj)

    def _update_exploration_edge_memory(
        self, subject: str, predicate: str, object_: str
    ) -> None:
        """
        Find the *latest* statement in LTM for (subject, predicate, object_).
        If it's only short-term, skip.
        """
        query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?stmt ?ct ?et ?ks (COALESCE(?ct, ?et, ?ks) AS ?timeVal)
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <{subject}> ;
                    rdf:predicate <{predicate}> ;
                    rdf:object <{object_}> .
              OPTIONAL {{ ?stmt humemai:current_time ?ct. }}
              OPTIONAL {{ ?stmt humemai:event_time ?et. }}
              OPTIONAL {{ ?stmt humemai:known_since ?ks. }}
            }}
            ORDER BY DESC(?timeVal)
            LIMIT 1
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            return
        row = rows[0]
        time_val = row.timeVal
        et_val = row.et
        ks_val = row.ks

        # If purely short-term => skip
        if et_val is None and ks_val is None:
            return
        if time_val is None:
            raise ValueError(
                f"No valid time found for ({subject}, {predicate}, {object_})."
            )

        # update
        self.humemai.increment_recalled(
            subject=URIRef(subject),
            predicate=URIRef(predicate),
            object_=URIRef(object_),
            lower_time_bound=time_val,
            upper_time_bound=time_val,
        )
        la_literal = Literal(
            self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
        )
        self.humemai.update_last_accessed(
            subject=URIRef(subject),
            predicate=URIRef(predicate),
            object_=URIRef(object_),
            new_time=la_literal,
            lower_time_bound=time_val,
            upper_time_bound=time_val,
        )

    # -------------------------------------------------------------------------
    # _run_test_episode
    # -------------------------------------------------------------------------

    def _run_test_episode(self) -> tuple[float, int]:
        """Test run an episode, returning total reward + steps."""
        if self.mm_policy.lower() == "belady":
            self.precompute_future_memory_accesses()

        score = 0.0
        step = 0
        self.current_step = 0

        self.humemai.reset()
        obs, info = self.env.reset()

        self.manage_memory(obs["room"], step)

        while True:
            action_pair = self._generate_action_pair(obs)
            obs, reward, done, truncated, info = self.env.step(action_pair)
            score += sum(reward)

            step += 1
            self.current_step = step

            self.manage_memory(obs["room"], step)
            if done:
                break

        return score, step

    # -------------------------------------------------------------------------
    # Belady Precomputation
    # -------------------------------------------------------------------------

    def precompute_future_memory_accesses(self):
        """Run a separate simulation with the same seed to pre-log memory usage."""
        print("Precomputing future memory accesses for Bélády...")

        from datetime import datetime

        start_t = datetime.now()

        sim_env = gym.make(self.env_str, **self.env_config)
        self.memory_access_log = {}
        self.current_step = 0

        self._enable_memory_access_tracking()

        obs, _ = sim_env.reset()
        self.manage_memory(obs["room"], self.current_step)

        sim_done = False
        total_steps = 0
        while not sim_done:
            if total_steps % 10 == 0:
                print(f"Sim step {self.current_step} (precompute).")

            act_pair = self._generate_action_pair(obs)
            obs, _, sim_done, _, _ = sim_env.step(act_pair)

            total_steps += 1
            self.current_step += 1

            self.manage_memory(obs["room"], self.current_step)

        print(f"Simulation ended after {total_steps} steps.")
        print(
            f"Processing memory access log with {len(self.memory_access_log)} entries."
        )
        self._process_memory_access_log()

        end_t = datetime.now()
        duration = (end_t - start_t).total_seconds()
        print(f"Precomputation took {duration:.2f} seconds.")
        print(
            f"Found {len(self.next_access_lookup)} unique memory IDs with future steps."
        )

        self._disable_memory_access_tracking()
        self.humemai.reset()
        self.current_step = 0

    def _process_memory_access_log(self):
        """Build next_access_lookup from memory_access_log."""
        self.next_access_lookup = {}
        steps_sorted = sorted(self.memory_access_log.keys())
        for st in steps_sorted:
            for memid in self.memory_access_log[st]:
                if memid not in self.next_access_lookup:
                    self.next_access_lookup[memid] = []
                self.next_access_lookup[memid].append(st)
        print(
            f"Built next_access_lookup for {len(self.next_access_lookup)} memory IDs."
        )

    def _enable_memory_access_tracking(self):
        """Override QA/explore to record memory usage for Bélády."""
        print("Enabling memory-access tracking (Bélády).")
        self.tracking_enabled = True
        self.current_step = 0

        self._original_answer_question = self.answer_question
        self._original_explore = self.explore

        def tracking_qa(question):
            ans = self._original_answer_question(question)
            print(f"Tracking QA access at step={self.current_step}")
            self._record_all_accessed_memories()
            return ans

        def tracking_explore():
            direction = self._original_explore()
            print(f"Tracking exploration access at step={self.current_step}")
            self._record_all_accessed_memories()
            return direction

        self.answer_question = tracking_qa
        self.explore = tracking_explore

    def _disable_memory_access_tracking(self):
        """Restore QA/explore methods."""
        print("Disabling memory-access tracking.")
        if hasattr(self, "_original_answer_question"):
            self.answer_question = self._original_answer_question
        if hasattr(self, "_original_explore"):
            self.explore = self._original_explore
        self.tracking_enabled = False

    def _record_all_accessed_memories(self):
        """
        Any statement with last_accessed == self.current_time OR recalled incremented
        at self.current_time => log it for this step.
        """
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT DISTINCT ?memoryID
            WHERE {
              {
                ?stmt rdf:type rdf:Statement ;
                      humemai:memoryID ?memoryID ;
                      humemai:last_accessed ?la .
                FILTER(str(?la) = ?current_time)
              }
              UNION
              {
                ?stmt rdf:type rdf:Statement ;
                      humemai:memoryID ?memoryID ;
                      humemai:recalled ?rec .
                ?stmt humemai:last_accessed ?la .
                FILTER(str(?la) = ?current_time)
              }
            }
        """
        ct_str = self.current_time.isoformat(timespec="seconds")
        rows = list(
            self.humemai.graph.query(
                query, initBindings={"current_time": Literal(ct_str)}
            )
        )
        if self.current_step not in self.memory_access_log:
            self.memory_access_log[self.current_step] = set()

        print(f"Found {len(rows)} memories accessed at step {self.current_step}")
        for r in rows:
            self.memory_access_log[self.current_step].add(int(r.memoryID))
