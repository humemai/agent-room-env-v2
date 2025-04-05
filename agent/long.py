"""This module defines the LongTermAgent class which uses both short-term and
long-term memory to store and retrieve observations, along with QA, exploration, and
memory management policies.
"""

from __future__ import annotations

import heapq
import random
import shutil
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
            # Initialize tracking structures for Belady's algorithm
            self.memory_access_log = {}  # {step: set(memory_ids)}
            self.next_access_lookup = {}  # {memory_id: [future access steps]}

        self.max_long_term_memory_size = max_long_term_memory_size

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
          2) Enforce memory management until the total meets the size limit.
          3) Clear short-term memory.
          4) Add new short-term observations.
        """

        # 1) Move all short-term => episodic (so they can be pruned)
        self.humemai.move_all_short_term_to_episodic()

        # 2) While we exceed memory limits, prune exactly one statement
        while (
            self.humemai.get_long_term_memory_count() > self.max_long_term_memory_size
        ):
            # Depending on mm_policy, choose one statement to remove
            if self.mm_policy.lower() == "fifo":
                # same as before
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
                # If we somehow have no candidate, break to avoid infinite loop
                raise ValueError(
                    "No memory ID found for deletion. Check your memory management policy."
                )
            # Remove that statement from memory
            self.humemai.delete_memory(Literal(mem_id_to_delete))

        # 3) Clear all short-term memories
        self.humemai.clear_short_term_memories()

        # 4) Add the new observations to short-term memory
        triples = [[URIRef(item) for item in obs] for obs in observations]
        self.current_time = self.base_date + timedelta(days=step)
        qualifiers = {
            self.humemai_ns.current_time: Literal(
                self.current_time.isoformat(timespec="seconds"),
                datatype=XSD.dateTime,
            )
        }
        self.humemai.add_short_term_memory(triples=triples, qualifiers=qualifiers)

    # ------------------------ FIFO ------------------------

    def _pick_fifo_victim(self) -> Optional[int]:
        """
        For FIFO, we remove the statement with the earliest humemai:event_time. If
        multiple share the same earliest time, pick one at random.
        """
        timestamps = self.find_unique_timestamps()
        if not timestamps:
            raise ValueError(
                "No timestamps found in long-term memory. Cannot pick FIFO victim."
            )
        # earliest
        target_timestamp = min(timestamps)
        memory_ids = self.find_memory_ids_by_event_time(target_timestamp)
        if not memory_ids:
            raise ValueError(
                "No memory IDs found for the earliest timestamp. Cannot pick FIFO victim."
            )
        # random tie-break
        return random.choice(memory_ids)

    def find_unique_timestamps(self) -> list[str]:
        """
        Return a list of distinct event_time values from the RDF graph.
        """
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT DISTINCT ?event_time
            WHERE {
                ?statement rdf:type rdf:Statement ;
                           humemai:event_time ?event_time .
            }
        """
        results = self.humemai.graph.query(query)
        return [str(row.event_time) for row in results]

    def find_memory_ids_by_event_time(self, event_time: str) -> list[int]:
        """
        Find memoryIDs of statements that match a given event_time.

        Args:
            event_time: A string (ISO format) representing the event_time.

        Returns:
            A list of integers representing memoryIDs.
        """
        query = f"""
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            SELECT ?memoryID
            WHERE {{
                ?statement rdf:type rdf:Statement ;
                           humemai:event_time "{event_time}"^^xsd:dateTime ;
                           humemai:memoryID ?memoryID .
            }}
        """
        results = self.humemai.graph.query(query)
        return [int(row.memoryID) for row in results]

    # ------------------------ LRU ------------------------

    def _pick_lru_victim(self) -> Optional[int]:
        """
        For LRU, remove the statement with the smallest (oldest) humemai:last_accessed.
        """
        # Query all statements in long-term memory with their memoryID & last_accessed
        # We only consider statements that have humemai:event_time => truly in LTM
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?memoryID ?la
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
              OPTIONAL { ?stmt humemai:last_accessed ?la. }
            }
        """
        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError(
                "No statements found in long-term memory. Cannot pick LRU victim."
            )

        # We pick the row with the earliest last_accessed. If last_accessed is missing,
        # treat it as extremely old so that it gets removed first.
        best_mem_id = None
        oldest_dt = datetime.max

        for row in results:
            mem_id = int(row.memoryID)
            la_literal = row.la
            if la_literal is None:
                # no last_accessed => treat as oldest
                return mem_id
            try:
                la_time = datetime.fromisoformat(str(la_literal))
            except ValueError:
                # if it fails to parse, remove it
                return mem_id

            # track the minimum last_accessed
            if la_time < oldest_dt:
                oldest_dt = la_time
                best_mem_id = mem_id

        return best_mem_id

    # ------------------------ LFU ------------------------

    def _pick_lfu_victim(self) -> Optional[int]:
        """
        For LFU, remove the statement with the smallest humemai:recalled. If
        humemai:recalled is missing, treat it as zero => victim candidate.
        """
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?memoryID ?rec
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
              OPTIONAL { ?stmt humemai:recalled ?rec. }
            }
        """
        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError(
                "No statements found in long-term memory. Cannot pick LFU victim."
            )

        best_mem_id = None
        best_recall = None  # we want the smallest, so track "lowest so far"

        for row in results:
            mem_id = int(row.memoryID)
            rec_count = row.rec
            if rec_count is None:
                # treat missing "recalled" as zero
                return mem_id
            try:
                rec_count = int(rec_count)
            except ValueError:
                # can't parse => treat as zero
                return mem_id

            if best_recall is None or rec_count < best_recall:
                best_recall = rec_count
                best_mem_id = mem_id

        return best_mem_id

    # ------------------------ LFU+LRU ------------------------

    def _pick_lfu_lru_victim(self) -> Optional[int]:
        """
        For the hybrid, remove the statement with the smallest score:
            score = recalled / delta_days
        where delta_days = (current_time - last_accessed) in days.
        If last_accessed is missing, or recalled is missing, treat them in ways
        that bias removal:
        - missing last_accessed => treat as a large old date => big delta => higher denominator => smaller score
        - missing recalled => treat as 0 => zero numerator => score=0 => remove quickly

        We remove whichever statement has the lowest score.
        """

        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?memoryID ?la ?rec
            WHERE {
            ?stmt rdf:type rdf:Statement ;
                    humemai:memoryID ?memoryID ;
                    humemai:event_time ?et .
            OPTIONAL { ?stmt humemai:last_accessed ?la. }
            OPTIONAL { ?stmt humemai:recalled ?rec. }
            }
        """
        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError(
                "No statements found in long-term memory. Cannot pick LFU+LRU victim."
            )

        best_mem_id = None
        best_score = None  # track the "lowest" ratio => victim

        for row in results:
            mem_id = int(row.memoryID)
            la_literal = row.la
            rec_count = row.rec

            # If recalled is missing => treat as zero
            if rec_count is None:
                rec_count = 0
            else:
                try:
                    rec_count = int(rec_count)
                except ValueError:
                    rec_count = 0

            # If last_accessed is missing => treat as far in the past => large delta
            if la_literal is None:
                la_time = self.base_date - timedelta(days=3650)
            else:
                try:
                    la_time = datetime.fromisoformat(str(la_literal))
                except ValueError:
                    la_time = self.base_date - timedelta(days=3650)

            # Compute delta_time in *days* instead of seconds
            # Option 1: purely integer days (truncates fractional days):
            #   dt_days = (self.current_time.date() - la_time.date()).days
            #
            # Option 2: keep fractional days using total_seconds() / 86400:
            dt_days = (self.current_time - la_time).total_seconds() / 86400.0
            if dt_days < 1.0:
                dt_days = 1.0  # avoid division by zero or sub-day illusions

            score = rec_count / dt_days  # "lowest" => remove
            if best_score is None or score < best_score:
                best_score = score
                best_mem_id = mem_id

        return best_mem_id

    # ------------------------ random ------------------------

    def _pick_random_victim(self) -> Optional[int]:
        """
        For random victim selection, simply pick a random statement from long-term memory.
        We only consider statements that have humemai:event_time (truly in LTM).
        """
        # Query all statements in long-term memory with their memoryID
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
        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError(
                "No statements found in long-term memory. Cannot pick random victim."
            )

        # Randomly select one memory ID
        random_row = random.choice(results)
        return int(random_row.memoryID)

    # ------------------------ Bélády ------------------------

    def _pick_belady_victim(self) -> Optional[int]:
        """Select memory that won't be needed for longest time in future"""
        # Get all memory IDs in LTM
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
        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError("No statements in long-term memory for Bélády selection")

        memory_ids = [int(row.memoryID) for row in results]

        # Add debugging info
        print(f"Belady selection: Found {len(memory_ids)} memories in LTM")

        # Count how many precomputed entries are still valid
        valid_precomputed = sum(1 for m in memory_ids if m in self.next_access_lookup)
        print(
            f"Belady selection: {valid_precomputed}/{len(memory_ids)} have precomputed data"
        )

        # Find next access time for each memory
        never_accessed_again = []
        next_access = {}

        for memory_id in memory_ids:
            if memory_id not in self.next_access_lookup:
                # Memory will never be accessed again
                never_accessed_again.append(memory_id)
                continue

            # Get future accesses only
            future_steps = [
                step
                for step in self.next_access_lookup[memory_id]
                if step > self.current_step
            ]

            if not future_steps:
                # No future accesses
                never_accessed_again.append(memory_id)
            else:
                # Store next access time
                next_access[memory_id] = min(future_steps)

        # First priority: memories never accessed again
        if never_accessed_again:
            victim = random.choice(never_accessed_again)
            print(f"Belady selection: Memory {victim} never accessed again")
            return victim

        # Second priority: memory with furthest next access
        if next_access:
            victim = max(next_access.items(), key=lambda x: x[1])[0]
            print(
                f"Belady selection: Memory {victim} next accessed at step {next_access[victim]}"
            )
            return victim

        # Fallback to LRU if nothing else works
        print("Belady selection: Falling back to LRU")
        return self._pick_lru_victim()

    # -------------------------------------------------------------------------
    # QA Policy
    # -------------------------------------------------------------------------

    def answer_question(self, question: tuple[str, str]) -> str:
        """
        Answer a question based on the agent's memory using the specified QA policy, and
        increment 'recalled' only for the one statement (exact triple + exact timeVal).
        """

        subject_str = f"<{question[0]}>"
        predicate_str = f"<{question[1]}>"

        # Query for the statement, object, and timeVal (coalescing current_time /
        # event_time). Each row is one reified statement.
        query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?stmt ?object (COALESCE(?ct, ?et, ?ks) AS ?timeVal)
            WHERE {{
            ?stmt rdf:type rdf:Statement ;
                    rdf:subject {subject_str} ;
                    rdf:predicate {predicate_str} ;
                    rdf:object ?object .
            OPTIONAL {{ ?stmt humemai:current_time ?ct. }}
            OPTIONAL {{ ?stmt humemai:event_time ?et. }}
            OPTIONAL {{ ?stmt humemai:known_since ?ks. }}
            }}
        """
        results = list(self.humemai.graph.query(query))
        if not results:
            return None

        # Depending on qa_policy, pick exactly one row
        best_row = None

        if self.qa_policy == "latest":
            valid_rows = [r for r in results if r.timeVal is not None]
            if not valid_rows:
                return None
            # Sort descending by timeVal, pick the first
            valid_rows.sort(key=lambda r: r.timeVal, reverse=True)
            best_row = valid_rows[0]

        elif self.qa_policy == "oldest":
            valid_rows = [r for r in results if r.timeVal is not None]
            if not valid_rows:
                return None
            # Sort ascending, pick the first
            valid_rows.sort(key=lambda r: r.timeVal)
            best_row = valid_rows[0]

        elif self.qa_policy == "random":
            best_row = random.choice(results)

        elif self.qa_policy == "one_hop":
            # Just pick the first row
            best_row = results[0]

        else:
            raise ValueError("Invalid QA policy")

        if best_row is None:
            return None

        best_obj = best_row.object
        best_timeVal = best_row.timeVal  # an rdflib Literal, hopefully xsd:dateTime

        # If best_obj is a URIRef, we treat it as is; if it's a Literal, handle accordingly.
        best_obj_uri = URIRef(str(best_obj))

        self._update_qa_memory_access(
            subject=URIRef(question[0]),
            predicate=URIRef(question[1]),
            object_=best_obj_uri,
            time_literal=best_timeVal,
        )

        # Return the chosen best object as a string
        return str(best_obj_uri)

    def _update_qa_memory_access(
        self, subject: URIRef, predicate: URIRef, object_: URIRef, time_literal: Literal
    ) -> None:
        """
        Increments the 'recalled' counter and updates 'last_accessed' for a single
        triple in the LTM (defined by subject, predicate, object_).
        """
        # Increment recalled
        self.humemai.increment_recalled(
            subject=subject,
            predicate=predicate,
            object_=object_,
            lower_time_bound=time_literal,
            upper_time_bound=time_literal,
        )
        # Update last_accessed with the current time (using self.current_time)
        new_time_literal = Literal(
            self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
        )
        self.humemai.update_last_accessed(
            subject=subject,
            predicate=predicate,
            object_=object_,
            new_time=new_time_literal,
            lower_time_bound=time_literal,
            upper_time_bound=time_literal,
        )

    # -------------------------------------------------------------------------
    # Exploration Policies
    # -------------------------------------------------------------------------

    def explore(self) -> str:
        """
        Determine movement direction based on the exploration policy.
        Supported policies: "random", "avoid_walls", "bfs", "dijkstra".

        Returns:
            A string direction (e.g. "north", "south", "east", "west", or "stay").
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
            raise ValueError("Invalid exploration policy")

    # --- Random-with-Wall-Avoidance ---

    def _explore_avoid_walls(self) -> str:
        """
        Uses short-term memory to select a random direction that does not lead to a
        wall.

        Returns:
            A direction string
        """
        query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX humemai: <https://humem.ai/ontology#>
            SELECT ?direction
            WHERE {
              ?st1 rdf:type rdf:Statement ;
                   rdf:subject <agent> ;
                   rdf:predicate <at_location> ;
                   rdf:object ?current_location .
              ?st2 rdf:type rdf:Statement ;
                   rdf:subject ?current_location ;
                   rdf:predicate ?direction ;
                   rdf:object ?target .
              FILTER(?direction IN (<north>, <south>, <east>, <west>))
              FILTER(?target != <wall>)
            }
        """
        results = list(self.humemai.graph.query(query))
        possible_dirs = [str(row.direction).strip("<>") for row in results]

        if not possible_dirs:
            raise ValueError(
                "No valid directions found in short-term memory. "
                "Consider using a different exploration policy."
            )
        return random.choice(possible_dirs)

    # -------------------------------------------------------------------------
    # BFS: Return Full Path of Edges, Then Update Memory
    # -------------------------------------------------------------------------

    def _explore_bfs(self) -> str:
        """
        Modified BFS strategy:
          1. BFS to find the first unvisited room, returning the full path of edges.
          2. If no unvisited rooms remain, pick the 'least visited' room, BFS to it.
          3. Update memory for each edge in that path, then return the direction of
             the first edge.
        """
        current_room = self._get_agent_current_room()

        visited_rooms = self._get_visited_rooms()
        adjacency = self._build_room_adjacency()

        # 1) BFS to find a path to some unvisited room
        path_to_unvisited = self._bfs_find_new_room_with_path(
            current_room, adjacency, visited_rooms
        )
        if path_to_unvisited:
            self._update_path_memory_access(path_to_unvisited)
            # Return direction of first edge
            return path_to_unvisited[0][1]  # (subj, direction, obj)

        # 2) If no unvisited found, pick the least visited fallback
        least_visited_room = self._pick_least_visited_room(visited_rooms, current_room)
        if not least_visited_room or least_visited_room == current_room:
            # If everything is visited or fallback fails
            return self._explore_avoid_walls()

        # BFS path to that "least visited" room
        path_to_known = self._bfs_path_to_specific_room(
            current_room, least_visited_room, adjacency
        )
        if path_to_known:
            self._update_path_memory_access(path_to_known)
            return path_to_known[0][1]  # first edge direction
        else:
            return self._explore_avoid_walls()

    def _bfs_find_new_room_with_path(
        self,
        start_room: str,
        adjacency: dict[str, list[tuple[str, str]]],
        visited_rooms: set[str],
    ) -> list[tuple[str, str, str]] | None:
        """
        BFS from start_room to find the first unvisited room. Returns the list of edges
        (subjectRoom, direction, objectRoom) or None if not found.
        """
        parents = {start_room: None}  # room -> (parentRoom, directionUsed)
        queue = deque([start_room])

        while queue:
            current = queue.popleft()
            # If we found an unvisited room (that's not the start)
            if current not in visited_rooms and current != start_room:
                # reconstruct edges
                return self._bfs_reconstruct_path(parents, start_room, current)

            # expand neighbors
            for direction, neighbor in adjacency.get(current, []):
                if neighbor not in parents:
                    parents[neighbor] = (current, direction)
                    queue.append(neighbor)

        return None

    def _bfs_path_to_specific_room(
        self,
        start_room: str,
        goal_room: str,
        adjacency: dict[str, list[tuple[str, str]]],
    ) -> list[tuple[str, str, str]] | None:
        """
        BFS from start_room to goal_room, returning a list of edges (subjectRoom,
        direction, objectRoom). Returns None if no path.
        """
        if start_room == goal_room:
            return []

        parents = {start_room: None}
        queue = deque([start_room])

        while queue:
            current = queue.popleft()
            if current == goal_room:
                return self._bfs_reconstruct_path(parents, start_room, goal_room)

            for direction, neighbor in adjacency.get(current, []):
                if neighbor not in parents:
                    parents[neighbor] = (current, direction)
                    queue.append(neighbor)

        return None

    def _bfs_reconstruct_path(
        self, parents: dict[str, tuple[str | None, str | None]], start: str, goal: str
    ) -> list[tuple[str, str, str]]:
        """
        Reconstruct BFS path from start->...->goal as a list of edges
        (subjectRoom, direction, objectRoom).
        """
        edges = []
        current = goal
        while current != start and current in parents:
            prev_dir = parents[current]
            if prev_dir is None:
                break
            (prev_room, direction) = prev_dir
            if prev_room is None:
                break
            edges.append((prev_room, direction, current))
            current = prev_room
        edges.reverse()
        return edges

    # -------------------------------------------------------------------------
    # Dijkstra: Return Full Path, Then Update Memory
    # -------------------------------------------------------------------------

    def _explore_dijkstra(self) -> str:
        """
        Modified Dijkstra strategy:
          1. Attempt to find a path to an *unvisited* room with minimal cost.
          2. If no unvisited remains, pick the least visited room, path to it.
          3. Update memory for each edge in that path, then return the first direction.
        """
        current_room = self._get_agent_current_room()

        visited_rooms = self._get_visited_rooms()
        adjacency = self._build_room_adjacency_with_weights(visited_rooms)

        # 1) Find the best unvisited room, get full path
        path_to_unvisited = self._dijkstra_find_best_unvisited_room_with_path(
            current_room, adjacency, visited_rooms
        )
        if path_to_unvisited:
            self._update_path_memory_access(path_to_unvisited)
            return path_to_unvisited[0][1]  # direction of first edge

        # 2) No unvisited left, fallback to least visited
        least_visited_room = self._pick_least_visited_room(visited_rooms, current_room)
        if not least_visited_room or least_visited_room == current_room:
            return self._explore_avoid_walls()

        # 3) Dijkstra to that known room
        path_to_known = self._dijkstra_path_to_specific_room(
            current_room, least_visited_room, adjacency
        )
        if path_to_known:
            self._update_path_memory_access(path_to_known)
            return path_to_known[0][1]
        else:
            return self._explore_avoid_walls()

    def _dijkstra_find_best_unvisited_room_with_path(
        self,
        start_room: str,
        adjacency: dict[str, list[tuple[str, str, float]]],
        visited_rooms: set[str],
    ) -> list[tuple[str, str, str]] | None:
        """
        Runs Dijkstra from start_room, among all reachable rooms pick the FIRST
        unvisited with minimal cost. Returns the full path (list of edges) or None if
        none is found.
        """
        best_cost, parent = self._dijkstra_min_cost_path(start_room, adjacency)

        # among all reachable rooms, find unvisited with minimal cost
        candidates = []
        for room, cost_val in best_cost.items():
            if (
                (room not in visited_rooms)
                and (room != start_room)
                and (cost_val < float("inf"))
            ):
                candidates.append((room, cost_val))

        if not candidates:
            return None

        # pick the minimal cost
        candidates.sort(key=lambda x: x[1])
        best_room, _ = candidates[0]
        return self._dijkstra_reconstruct_full_path(parent, start_room, best_room)

    def _dijkstra_path_to_specific_room(
        self,
        start_room: str,
        goal_room: str,
        adjacency: dict[str, list[tuple[str, str, float]]],
    ) -> list[tuple[str, str, str]] | None:
        """
        Run Dijkstra from start_room to goal_room. Returns full path (list of edges) or
        None if no path is found.
        """
        if start_room == goal_room:
            return []

        best_cost, parent = self._dijkstra_min_cost_path(start_room, adjacency)
        if best_cost.get(goal_room, float("inf")) == float("inf"):
            return None

        return self._dijkstra_reconstruct_full_path(parent, start_room, goal_room)

    def _dijkstra_min_cost_path(
        self, start_room: str, adjacency: dict[str, list[tuple[str, str, float]]]
    ) -> tuple[dict[str, float], dict[str, tuple[str, str]]]:
        """
        Standard Dijkstra from start_room, returning:
          - best_cost[room]: minimal cumulative cost from start_room to room
          - parent[room]: (previous_room, direction_used)
        """
        best_cost = {}
        parent = {}

        # initialize
        for room in adjacency:
            best_cost[room] = float("inf")
        best_cost[start_room] = 0.0

        pq = [(0.0, start_room)]
        while pq:
            current_cost, current_room = heapq.heappop(pq)
            if current_cost > best_cost[current_room]:
                continue

            for direction, neighbor, edge_cost in adjacency.get(current_room, []):
                candidate = current_cost + edge_cost
                if candidate < best_cost.get(neighbor, float("inf")):
                    best_cost[neighbor] = candidate
                    parent[neighbor] = (current_room, direction)
                    heapq.heappush(pq, (candidate, neighbor))

        return best_cost, parent

    def _dijkstra_reconstruct_full_path(
        self, parent: dict[str, tuple[str, str]], start_room: str, goal_room: str
    ) -> list[tuple[str, str, str]]:
        """
        Reconstruct the path from start_room to goal_room using the 'parent' dict
        from Dijkstra. Returns a list of edges (subjRoom, direction, objRoom).
        """
        edges = []
        current = goal_room
        while current != start_room and current in parent:
            prev_room, direction = parent[current]
            edges.append((prev_room, direction, current))
            current = prev_room
        edges.reverse()
        return edges

    # -------------------------------------------------------------------------
    # Shared BFS/Dijkstra Helpers
    # -------------------------------------------------------------------------

    def _get_agent_current_room(self) -> str | None:
        """
        Query short-term memory to find the agent's current room. Returns the room's URI
        as a string, or None if not found.
        """
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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
        results = self.humemai.graph.query(query)
        for row in results:
            return str(row.room)

        # If we reach here, no current room was found
        raise ValueError("Agent's current room not found in short-term memory.")

    def _build_room_adjacency(self) -> dict[str, list[tuple[str, str]]]:
        """
        Build an adjacency mapping: for each roomX, list of (direction, roomY). Skips
        edges that lead to <wall>.
        """
        adjacency = {}
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?roomX ?dir ?roomY
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject ?roomX ;
                    rdf:predicate ?dir ;
                    rdf:object ?roomY .
              FILTER(?dir IN (<north>, <south>, <east>, <west>))
            }
        """
        results = self.humemai.graph.query(query)
        for row in results:
            roomX = str(row.roomX)
            dir_str = row.dir.split("/")[-1]  # <north> -> 'north'
            roomY = str(row.roomY)
            if roomY.endswith("wall"):
                continue
            if roomX not in adjacency:
                adjacency[roomX] = []
            adjacency[roomX].append((dir_str, roomY))
        return adjacency

    def _build_room_adjacency_with_weights(
        self, visited_rooms: set[str]
    ) -> dict[str, list[tuple[str, str, float]]]:
        """
        Build weighted adjacency: roomX -> [(direction, roomY, cost)].
        cost = 1 / (1 + count_interesting_objects_in(roomY)).
        """
        adjacency = {}
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?roomX ?dir ?roomY
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject ?roomX ;
                    rdf:predicate ?dir ;
                    rdf:object ?roomY .
              FILTER(?dir IN (<north>, <south>, <east>, <west>))
            }
        """
        results = self.humemai.graph.query(query)
        for row in results:
            roomX = str(row.roomX)
            dir_str = row.dir.split("/")[-1]
            roomY = str(row.roomY)
            if roomY.endswith("wall"):
                continue

            # cost function: 1 / (1 + # of interesting objects in roomY)
            count_objs = self._count_interesting_objects_in_room(roomY)
            cost = 1.0 / (1.0 + count_objs)

            if roomX not in adjacency:
                adjacency[roomX] = []
            adjacency[roomX].append((dir_str, roomY, cost))

        return adjacency

    def _count_interesting_objects_in_room(self, room: str) -> int:
        """
        Count "interesting" objects in a room. We define them as URIs containing
        'sat_', 'ind_', or 'dep_'.
        """
        prefixes = ("sat_", "ind_", "dep_")
        query = f"""
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?subj
            WHERE {{
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject ?subj ;
                    rdf:predicate <at_location> ;
                    rdf:object <{room}> .
            }}
        """
        results = self.humemai.graph.query(query)
        count = 0
        for row in results:
            subj_str = str(row.subj)
            if any(pref in subj_str for pref in prefixes):
                count += 1
        return count

    def _get_visited_rooms(self) -> set[str]:
        """
        Return a set of rooms that the agent has visited in long-term memory, defined by
        (agent, at_location, room, event_time=...).
        """
        visited = set()
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?room
            WHERE {
              ?stmt rdf:type rdf:Statement ;
                    rdf:subject <agent> ;
                    rdf:predicate <at_location> ;
                    rdf:object ?room ;
                    humemai:event_time ?et .
            }
        """
        results = self.humemai.graph.query(query)
        for row in results:
            visited.add(str(row.room))
        return visited

    # -------------------------------------------------------------------------
    # "Least Visited" Fallback Helpers
    # -------------------------------------------------------------------------

    def _pick_least_visited_room(
        self, visited_rooms: set[str], current_room: str
    ) -> str | None:
        """
        Among visited_rooms, pick the one with the minimal visit count. Exclude
        current_room from the candidates. Returns the chosen room's URI or None if none.
        """
        room_visit_counts = self._get_room_visit_counts()

        # Candidate rooms: visited, but not agent's current
        candidates = [r for r in visited_rooms if r != current_room]
        if not candidates:
            return None

        # Sort by ascending visit count, pick the first
        candidates.sort(key=lambda r: room_visit_counts.get(r, 0))
        return candidates[0]

    def _get_room_visit_counts(self) -> dict[str, int]:
        """
        Returns {roomURI: visit_count} for all times the agent was at_location roomURI
        in long-term memory (with event_time).
        """
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
        results = self.humemai.graph.query(query)
        room_visits = {}
        for row in results:
            room_uri = str(row.room)
            visit_count = int(row.vcount.toPython())
            room_visits[room_uri] = visit_count
        return room_visits

    # -------------------------------------------------------------------------
    # Updating Memory Access for BFS/Dijkstra Paths
    # -------------------------------------------------------------------------

    def _update_path_memory_access(self, edges: list[tuple[str, str, str]]) -> None:
        """
        For each edge (roomX, direction, roomY) in the BFS / Dijkstra path,
        update 'recalled' and 'last_accessed' for the *latest* statement in LTM
        that has (subject=roomX, predicate=direction, object=roomY).
        Short-term statements (with only current_time, no event_time) are skipped.
        """
        for subj, pred, obj in edges:
            self._update_exploration_edge_memory(subj, pred, obj)

    def _update_exploration_edge_memory(
        self, subject: str, predicate: str, object_: str
    ) -> None:
        """
        Locate the *latest* memory statement in LTM for (subject, predicate, object).
        That means we pick the statement with the largest timeVal among those that have
        an event_time or known_since (i.e. not purely short-term). If only short-term
        memory is found or none is found, we skip.
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

        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError(
                f"No statement found for ({subject}, {predicate}, {object_})."
            )

        row = results[0]
        time_val = row.timeVal  # This is COALESCE(?ct, ?et, ?ks)
        et_val = row.et
        ks_val = row.ks
        # If it's purely short-term, that means ?ct is set, but ?et and ?ks are both None
        if et_val is None and ks_val is None:
            assert row.ct is not None
            # This means we have only ?ct => short-term memory => skip
            return
        if time_val is None:
            raise ValueError(
                f"No valid time found for ({subject}, {predicate}, {object_})."
            )

        # If we are here, it's LTM => safe to update
        self.humemai.increment_recalled(
            subject=URIRef(subject),
            predicate=URIRef(predicate),
            object_=URIRef(object_),
            lower_time_bound=time_val,
            upper_time_bound=time_val,
        )

        # Update last_accessed with the agent's current time
        new_time_literal = Literal(
            self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
        )
        self.humemai.update_last_accessed(
            subject=URIRef(subject),
            predicate=URIRef(predicate),
            object_=URIRef(object_),
            new_time=new_time_literal,
            lower_time_bound=time_val,
            upper_time_bound=time_val,
        )

    # -------------------------------------------------------------------------
    # Env Testing Example
    # -------------------------------------------------------------------------

    def _run_test_episode(self) -> tuple[float, int]:
        """
        Execute a single test episode in the environment, returning total score and step
        count.
        """
        # For Belady's algorithm, precompute future memory accesses
        if self.mm_policy.lower() == "belady":
            self.precompute_future_memory_accesses()

        score = 0.0
        step = 0
        self.humemai.reset()

        observations, info = self.env.reset()
        self.manage_memory(observations["room"], step)

        while True:
            action_pair = self._generate_action_pair(observations)
            observations, reward, done, truncated, info = self.env.step(action_pair)
            score += sum(reward)
            step += 1
            self.manage_memory(observations["room"], step)
            if done:
                break

        return score, step

    def precompute_future_memory_accesses(self):
        """Run a simulation episode to record all memory accesses"""
        print("Precomputing future memory accesses for Bélády's algorithm...")

        # Record the simulation start time
        start_time = datetime.now()

        # Clone the environment with the same seed
        sim_env = gym.make(self.env_str, **self.env_config)

        # Reset tracking structures
        self.memory_access_log = {}
        self.current_step = 0

        # Enable access tracking
        self._enable_memory_access_tracking()

        # Run a complete simulation episode
        sim_obs, _ = sim_env.reset()
        self.manage_memory(sim_obs["room"], self.current_step)

        # Track how many steps the simulation needed
        total_steps = 0
        while True:
            if total_steps % 10 == 0:
                print(f"Simulation step {self.current_step}")

            action_pair = self._generate_action_pair(sim_obs)
            sim_obs, _, sim_done, _, _ = sim_env.step(action_pair)
            self.current_step += 1
            total_steps += 1
            self.manage_memory(sim_obs["room"], self.current_step)
            if sim_done:
                break

        # Process the access log
        print(
            f"Processing memory access log: {len(self.memory_access_log)} steps recorded"
        )
        self._process_memory_access_log()

        # Calculate and print simulation stats
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"Precomputation complete: {total_steps} steps in {duration:.2f} seconds")
        print(f"Recorded {len(self.next_access_lookup)} unique memory IDs")

        # Cleanup and reset
        self._disable_memory_access_tracking()
        self.humemai.reset()
        self.current_step = 0

    def _process_memory_access_log(self):
        """Process raw memory access log into a next-access lookup table"""
        print(f"Memory access log has {len(self.memory_access_log)} steps")

        # Create lookup: {memory_id: [ordered list of access times]}
        self.next_access_lookup = {}

        # Sort steps in ascending order
        sorted_steps = sorted(self.memory_access_log.keys())

        for step in sorted_steps:
            for memory_id in self.memory_access_log[step]:
                if memory_id not in self.next_access_lookup:
                    self.next_access_lookup[memory_id] = []
                self.next_access_lookup[memory_id].append(step)

        print(f"Created next-access lookup for {len(self.next_access_lookup)} memories")

    def _enable_memory_access_tracking(self):
        """Enable tracking for Bélády's algorithm simulation"""
        print("Enabling memory access tracking")
        self.tracking_enabled = True
        self.current_step = 0

        # Original methods we'll restore later
        self._original_handle_qa = self.answer_question
        self._original_explore = self.explore

        # Override with tracking versions
        def tracking_qa(question):
            answer = self._original_handle_qa(question)
            # After answering, log any memory accesses
            print(f"Recording QA access at step {self.current_step}")
            self._record_all_accessed_memories()
            return answer

        def tracking_explore():
            direction = self._original_explore()
            # After exploring, log any memory accesses
            print(f"Recording exploration access at step {self.current_step}")
            self._record_all_accessed_memories()
            return direction

        # Replace methods with tracking versions
        self.answer_question = tracking_qa
        self.explore = tracking_explore

    def _disable_memory_access_tracking(self):
        """Disable tracking and restore original methods"""
        print("Disabling memory access tracking")
        if hasattr(self, "_original_handle_qa"):
            self.answer_question = self._original_handle_qa
            self.explore = self._original_explore
        self.tracking_enabled = False

    def _record_all_accessed_memories(self):
        """Record all memories with updated 'last_accessed' at current step"""
        # More comprehensive query to capture all accessed memories
        query = """
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT DISTINCT ?memoryID
            WHERE {
              {
                # Capture memories by last_accessed
                ?stmt rdf:type rdf:Statement ;
                      humemai:memoryID ?memoryID ;
                      humemai:last_accessed ?la .
                FILTER(str(?la) = ?current_time)
              }
              UNION
              {
                # Also capture memories by recalled increment
                ?stmt rdf:type rdf:Statement ;
                      humemai:memoryID ?memoryID ;
                      humemai:recalled ?rec .
                # Only if they have been accessed recently
                ?stmt humemai:last_accessed ?la .
                FILTER(str(?la) = ?current_time)
              }
            }
        """
        # Bind the current time as parameter to avoid string interpolation
        current_time = self.current_time.isoformat(timespec="seconds")
        results = list(
            self.humemai.graph.query(
                query, initBindings={"current_time": Literal(current_time)}
            )
        )

        if not self.current_step in self.memory_access_log:
            self.memory_access_log[self.current_step] = set()

        # Add debugging info
        print(f"Found {len(results)} memories accessed at step {self.current_step}")
        for row in results:
            memory_id = int(row.memoryID)
            self.memory_access_log[self.current_step].add(memory_id)
