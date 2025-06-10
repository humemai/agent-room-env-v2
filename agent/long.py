"""This module defines the LongTermAgent class which uses both short-term and
long-term memory to store and retrieve observations, along with QA, exploration, and
memory management (forget and remember) policies.
"""

from __future__ import annotations

import heapq
import random
from collections import deque
from copy import deepcopy
from datetime import datetime, timedelta
from typing import Any, Optional

from humemai.rdflib import Humemai
from rdflib import XSD, Literal, Namespace, URIRef

from .agent import Agent


class LongTermAgent(Agent):
    """
    An agent that manages both short-term and long-term memories via Humemai.
    Supports QA, exploration, and memory management (forget and remember) policies.
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
        qa_policy: str = "most_frequently_used",
        explore_policy: str = "dijkstra",
        mm_forget_policy: str = "lfu",
        mm_remember_policy: str = "all",
        max_long_term_memory_size: int = 100,
        num_samples_for_results: int = 10,
        save_results: bool = True,
        default_root_dir: str = "./training-results/",
        **kwargs: Any,
    ) -> None:
        """
        Initialize a LongTermAgent with environment configuration, QA policy,
        exploration policy, and memory management parameters.
        """
        params_to_save = deepcopy(locals())
        del params_to_save["self"]
        del params_to_save["__class__"]
        super().__init__(**params_to_save)

        assert qa_policy.lower() in [
            "most_recently_added",
            "most_recently_used",
            "most_frequently_used",
            "random",
        ], f"Invalid QA policy: {qa_policy}"
        self.qa_policy = qa_policy.lower()

        assert explore_policy.lower() in [
            "random",
            "avoid_walls",
            "bfs",
            "dijkstra",
        ], f"Invalid explore policy: {explore_policy}"
        self.explore_policy = explore_policy.lower()

        assert mm_forget_policy.lower() in [
            "fifo",
            "lru",
            "lfu",
            "random",
            "rl",  # 'rl' is a placeholder for future RL-based policies
        ], f"Invalid long-term memory management policy: {mm_forget_policy}"
        self.mm_forget_policy = mm_forget_policy.lower()

        assert mm_remember_policy.lower() in [
            "all",
            "rl",  # 'rl' is a placeholder for future RL-based policies
        ], f"Invalid long-term memory remember policy: {mm_remember_policy}"
        self.mm_remember_policy = mm_remember_policy.lower()

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
        if self.mm_remember_policy == "all":
            self.humemai.move_all_short_term_to_episodic()
        else:
            raise NotImplementedError(
                f"Memory management remember policy '{self.mm_remember_policy}' not implemented."
            )

        # assert short-term is empty
        assert (
            self.humemai.get_short_term_memory_count() == 0
        ), "Short-term memory should be empty after moving to episodic."

        # 2) While we exceed memory limits, prune one statement at a time
        while (
            self.humemai.get_long_term_memory_count() > self.max_long_term_memory_size
        ):
            if self.mm_forget_policy.lower() == "fifo":
                mem_id_to_delete = self._pick_fifo_victim()
            elif self.mm_forget_policy.lower() == "lru":
                mem_id_to_delete = self._pick_lru_victim()
            elif self.mm_forget_policy.lower() == "lfu":
                mem_id_to_delete = self._pick_lfu_victim()
            elif self.mm_forget_policy.lower() == "random":
                mem_id_to_delete = self._pick_random_victim()
            else:
                raise NotImplementedError(
                    f"Memory management forget policy '{self.mm_forget_policy}' not implemented."
                )

            if mem_id_to_delete is None:
                raise ValueError("No memory ID found for deletion.")
            self.humemai.delete_memory(Literal(mem_id_to_delete))

        # 3) Insert new observations in short-term
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
        """Earliest humemai:time_added => evict (FIFO)."""
        timestamps = self.find_unique_timestamps()
        if not timestamps:
            raise ValueError("No timestamps => cannot pick FIFO victim.")
        oldest = min(timestamps)
        mem_ids = self.find_memory_ids_by_time_added(oldest)
        if not mem_ids:
            raise ValueError(
                "No memory found at earliest timestamp => FIFO victim error."
            )
        return random.choice(mem_ids)

    def find_unique_timestamps(self) -> list[str]:
        """All distinct humemai:time_added in LTM."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT DISTINCT ?ta
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:time_added ?ta .
            }
        """
        results = self.humemai.graph.query(query)
        return [str(row.ta) for row in results]

    def find_memory_ids_by_time_added(self, t: str) -> list[int]:
        """MemIDs with time_added == t."""
        query = f"""
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            SELECT ?memory_id
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    humemai:time_added "{t}"^^xsd:dateTime ;
                    humemai:memory_id ?memory_id .
            }}
        """
        rows = list(self.humemai.graph.query(query))
        return [int(r.memory_id) for r in rows]

    # ------------------------ LRU ------------------------

    def _pick_lru_victim(self) -> Optional[int]:
        """
        Select victim using LRU policy:
        1. Find memories with oldest last_accessed value
        2. If multiple, fall back to LFU (lowest num_recalled)
        3. If still multiple, fall back to FIFO (oldest time_added)
        4. If still multiple, choose one uniformly at random
        """
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memory_id ?la ?rec ?ta
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memory_id ?memory_id ;
                    humemai:last_accessed ?la ;
                    humemai:num_recalled ?rec ;
                    humemai:time_added ?ta .
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick LRU victim.")

        # Convert to list of tuples: (memory_id, last_accessed, num_recalled, time_added)
        candidates = [
            (int(row.memory_id), str(row.la), int(row.rec), str(row.ta)) for row in rows
        ]

        # Step 1: Filter by oldest last_accessed (LRU)
        candidates.sort(key=lambda x: x[1])  # Sort by last_accessed
        oldest_la = candidates[0][1]
        lru_candidates = [c for c in candidates if c[1] == oldest_la]

        # If only one LRU candidate, we're done
        if len(lru_candidates) == 1:
            return lru_candidates[0][0]  # Return memory ID

        # Step 2: If multiple LRU candidates with same last_accessed, fall back to LFU
        # Sort by num_recalled
        lru_candidates.sort(key=lambda x: x[2])
        min_recall = lru_candidates[0][2]
        lfu_winners = [c for c in lru_candidates if c[2] == min_recall]

        # If only one LFU winner, we're done
        if len(lfu_winners) == 1:
            return lfu_winners[0][0]  # Return memory ID

        # Step 3: If still tied, fall back to FIFO
        lfu_winners.sort(key=lambda x: x[3])  # Sort by time_added
        oldest_ta = lfu_winners[0][3]
        fifo_winners = [c for c in lfu_winners if c[3] == oldest_ta]

        # Step 4: If still multiple candidates, choose one uniformly at random
        return random.choice(fifo_winners)[0]  # Return memory ID of a random candidate

    # ------------------------ LFU ------------------------

    def _pick_lfu_victim(self) -> Optional[int]:
        """
        Select victim using LFU policy:
        1. Find memories with lowest num_recalled value
        2. If multiple, fall back to LRU (oldest last_accessed)
        3. If still multiple, fall back to FIFO (oldest time_added)
        4. If still multiple, choose one uniformly at random
        """
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memory_id ?rec ?la ?ta
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memory_id ?memory_id ;
                    humemai:num_recalled ?rec ;
                    humemai:last_accessed ?la ;
                    humemai:time_added ?ta .
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick LFU victim.")

        # Convert to list of tuples: (memory_id, num_recalled, last_accessed, time_added)
        candidates = [
            (int(row.memory_id), int(row.rec), str(row.la), str(row.ta)) for row in rows
        ]

        # Step 1: Filter by lowest num_recalled (LFU)
        min_recall = min(c[1] for c in candidates)
        lfu_candidates = [c for c in candidates if c[1] == min_recall]

        # If only one LFU candidate, we're done
        if len(lfu_candidates) == 1:
            return lfu_candidates[0][0]  # Return memory ID

        # Step 2: If multiple LFU candidates with same recall count, fall back to LRU
        # Sort by oldest last_accessed
        lfu_candidates.sort(key=lambda x: x[2])
        oldest_la = lfu_candidates[0][2]
        lru_winners = [c for c in lfu_candidates if c[2] == oldest_la]

        # If only one LRU winner, we're done
        if len(lru_winners) == 1:
            return lru_winners[0][0]  # Return memory ID

        # Step 3: If still tied, fall back to FIFO
        lru_winners.sort(key=lambda x: x[3])  # Sort by time_added
        oldest_ta = lru_winners[0][3]
        fifo_winners = [c for c in lru_winners if c[3] == oldest_ta]

        # Step 4: If still multiple candidates, choose one uniformly at random
        return random.choice(fifo_winners)[0]  # Return memory ID of a random candidate

    # ------------------------ random ------------------------

    def _pick_random_victim(self) -> Optional[int]:
        """Randomly evict anything in LTM."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?memory_id
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memory_id ?memory_id ;
                    humemai:time_added ?ta .
            }
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            raise ValueError("No statements => can't pick random victim.")
        return int(random.choice(rows).memory_id)

    # -------------------------------------------------------------------------
    # QA Policy
    # -------------------------------------------------------------------------

    def answer_question(self, question: tuple[str, str]) -> str:
        """
        Answer question using self.qa_policy, then increment recall for that statement.

        Priority order:
        1. Always prioritize memories with current_time if available (without updating
           memory access)
        2. Otherwise apply specific policy:
           - most_recently_added: Choose memory with latest time_added
           - most_recently_used: Choose memory with latest last_accessed,
             breaking ties with most_recently_added
           - most_frequently_used: Choose memory with highest num_recalled,
             breaking ties with most_recently_added
           - random: Choose randomly among the other three policies
        """
        subj_str = f"<{question[0]}>"
        pred_str = f"<{question[1]}>"
        query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?stmt ?obj ?ta ?la ?rec ?ct
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject {subj_str} ;
                    rdf:predicate {pred_str} ;
                    rdf:object ?obj .
              OPTIONAL {{ ?stmt humemai:current_time ?ct. }}
              OPTIONAL {{ ?stmt humemai:time_added ?ta. }}
              OPTIONAL {{ ?stmt humemai:last_accessed ?la. }}
              OPTIONAL {{ ?stmt humemai:num_recalled ?rec. }}
            }}
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            return None

        # Step 1: Always prioritize memories with current_time (short-term memory)
        # Return directly without incrementing num_recalled or updating last_accessed
        current_time_rows = [r for r in rows if r.ct is not None]
        if current_time_rows:
            best_row = current_time_rows[0]  # Take any memory from current time
            return str(best_row.obj)

        # Step 2: Process long-term memories (with time_added property)
        valid_long_term_rows = [r for r in rows if r.ta is not None]
        if not valid_long_term_rows:
            return None  # No valid long-term memories found

        # For long-term memories, verify they have all required properties
        for row in valid_long_term_rows:
            assert row.la is not None, "last_accessed must exist for long-term memory"
            assert row.rec is not None, "num_recalled must exist for long-term memory"

        # Apply the selected policy
        if self.qa_policy == "random":
            # Randomly choose one of the three policies
            random_policy = random.choice(
                ["most_recently_added", "most_recently_used", "most_frequently_used"]
            )
            return self._apply_qa_policy(random_policy, valid_long_term_rows, question)
        else:
            return self._apply_qa_policy(self.qa_policy, valid_long_term_rows, question)

    def _apply_qa_policy(
        self, policy: str, rows: list, question: tuple[str, str]
    ) -> str:
        """Apply a specific QA policy to select the best row and update memory stats."""
        if policy == "most_recently_added":
            best_row, time_added = self._get_most_recently_added(rows)
        elif policy == "most_recently_used":
            best_row, time_added = self._get_most_recently_used(rows)
        elif policy == "most_frequently_used":
            best_row, time_added = self._get_most_frequently_used(rows)
        else:
            raise ValueError(f"Unknown QA policy: {policy}")

        obj_uri = URIRef(str(best_row.obj))

        # Update memory access stats for long-term memory
        self._update_qa_memory_access(
            subject=URIRef(question[0]),
            predicate=URIRef(question[1]),
            object_=obj_uri,
            time_added=time_added,
        )
        return str(best_row.obj)

    def _get_most_recently_added(self, rows: list) -> tuple:
        """Get row with latest time_added, breaking ties randomly."""
        # Sort by time_added, newest first
        rows.sort(key=lambda x: x.ta, reverse=True)
        newest_ta = rows[0].ta
        newest_rows = [r for r in rows if r.ta == newest_ta]

        # If multiple with same time_added, pick one randomly
        best_row = random.choice(newest_rows)
        time_added = best_row.ta
        return best_row, time_added

    def _get_most_recently_used(self, rows: list) -> tuple:
        """Get row with latest last_accessed, breaking ties with most_recently_added."""
        # Sort by last_accessed, newest first
        rows.sort(key=lambda x: x.la, reverse=True)
        newest_la = rows[0].la
        newest_rows = [r for r in rows if r.la == newest_la]

        if len(newest_rows) > 1:
            # Multiple rows with same last_accessed, break ties with most_recently_added
            best_row, _ = self._get_most_recently_added(newest_rows)
        else:
            best_row = newest_rows[0]

        time_added = best_row.ta
        return best_row, time_added

    def _get_most_frequently_used(self, rows: list) -> tuple:
        """Get row with highest num_recalled, breaking ties with most_recently_added."""
        # Sort by num_recalled, highest first
        rows.sort(key=lambda x: int(x.rec.toPython()), reverse=True)
        highest_rec = int(rows[0].rec.toPython())
        highest_rows = [r for r in rows if int(r.rec.toPython()) == highest_rec]

        if len(highest_rows) > 1:
            # Multiple rows with same num_recalled, break ties with most_recently_added
            best_row, _ = self._get_most_recently_added(highest_rows)
        else:
            best_row = highest_rows[0]

        # For updating memory access, use time_added
        time_literal = best_row.ta
        return best_row, time_literal

    def _update_qa_memory_access(
        self,
        subject: URIRef,
        predicate: URIRef,
        object_: URIRef,
        time_added: Literal,
    ) -> None:
        """Increment rnum_ecalled + update last_accessed for one triple in LTM."""
        self.humemai.increment_num_recalled(
            subject=subject,
            predicate=predicate,
            object_=object_,
            lower_time_added_bound=time_added,
            upper_time_added_bound=time_added,
        )
        new_time_lit = Literal(
            self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
        )
        self.humemai.update_last_accessed(
            subject=subject,
            predicate=predicate,
            object_=object_,
            new_time=new_time_lit,
            lower_time_added_bound=time_added,
            upper_time_added_bound=time_added,
        )

    # -------------------------------------------------------------------------
    # Exploration
    # -------------------------------------------------------------------------

    def explore(self) -> str:
        """Explore with the specified self.explore_policy.

        Returns:
            str: Direction to explore: "north", "south", "east", "west", or "stay".
        """
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
        Rooms in LTM: (agent, at_location, room, time_added=...).
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
                    humemai:time_added ?ta .
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
        """Return # of times the agent was (at_location room) in time_added-based LTM."""
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?room (COUNT(?ta) as ?vcount)
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <agent> ;
                    rdf:predicate <at_location> ;
                    rdf:object ?room ;
                    humemai:time_added ?ta .
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
            SELECT ?stmt ?ct ?ta (COALESCE(?ct, ?ta) AS ?time_value)
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <{subject}> ;
                    rdf:predicate <{predicate}> ;
                    rdf:object <{object_}> .
              OPTIONAL {{ ?stmt humemai:time_added ?ta. }}
            }}
            ORDER BY DESC(?time_value)
            LIMIT 1
        """
        rows = list(self.humemai.graph.query(query))
        if not rows:
            return
        row = rows[0]
        time_val = row.time_value
        ta_val = row.ta

        # If purely short-term => skip
        if ta_val is None:
            return
        if time_val is None:
            raise ValueError(
                f"No valid time found for ({subject}, {predicate}, {object_})."
            )

        # update
        self.humemai.increment_num_recalled(
            subject=URIRef(subject),
            predicate=URIRef(predicate),
            object_=URIRef(object_),
            lower_time_added_bound=time_val,
            upper_time_added_bound=time_val,
        )
        la_literal = Literal(
            self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
        )
        self.humemai.update_last_accessed(
            subject=URIRef(subject),
            predicate=URIRef(predicate),
            object_=URIRef(object_),
            new_time=la_literal,
            lower_time_added_bound=time_val,
            upper_time_added_bound=time_val,
        )

    # -------------------------------------------------------------------------
    # _run_test_episode
    # -------------------------------------------------------------------------

    def _run_test_episode(self) -> tuple[float, int]:
        """Test run an episode, returning total reward + steps."""

        score = 0.0
        self.current_step = 0

        self.humemai.reset()
        obs, info = self.env.reset()

        self.manage_memory(obs["room"], self.current_step)

        while True:
            action_pair = self._generate_action_pair(obs)
            obs, reward, done, truncated, info = self.env.step(action_pair)
            score += sum(reward)

            self.current_step += 1

            self.manage_memory(obs["room"], self.current_step)
            if done:
                break

        return score, self.current_step
