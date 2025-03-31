"""This module defines the LongTermAgent class which uses both short-term and
long-term memory to store and retrieve observations, along with QA, exploration,
and memory management policies.
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
        explore_policy: str = "bfs",  # "random", "avoid_walls", "bfs", or "dijkstra"
        mm_policy: str = "FIFO",
        max_long_term_memory_size: int = 100,
        num_samples_for_results: int = 10,
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
        self.max_long_term_memory_size = max_long_term_memory_size

        # HumemAI setup
        self.humemai_ns = Namespace("https://humem.ai/ontology#")
        self.base_date = datetime.fromisoformat("2025-01-01T00:00:00")
        self.humemai = Humemai()

    # -------------------------------------------------------------------------
    # Memory Management
    # -------------------------------------------------------------------------

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

    def manage_memory(self, observations: list[list[str]], step: int) -> None:
        """
        Manage memory by:
          1) Converting short-term memories to episodic.
          2) Enforcing a memory management policy until the total meets the size limit.
          3) Clearing short-term memory and adding new observations.
        """

        if self.mm_policy == "FIFO":
            self.humemai.move_all_short_term_to_episodic()

            # Enforce memory management until we meet the size limit
            while (
                self.humemai.get_long_term_memory_count()
                > self.max_long_term_memory_size
            ):
                timestamps = self.find_unique_timestamps()

                target_timestamp = min(timestamps)

                memory_ids = self.find_memory_ids_by_event_time(target_timestamp)

                # Randomly remove one memory from those that share the chosen timestamp
                mem_id_to_delete = random.choice(memory_ids)
                self.humemai.delete_memory(Literal(mem_id_to_delete))

            # Clear short-term and add new observations
            self.humemai.clear_short_term_memories()
            triples = [[URIRef(item) for item in obs] for obs in observations]
            self.current_time = self.base_date + timedelta(days=step)
            qualifiers = {
                self.humemai_ns.current_time: Literal(
                    self.current_time.isoformat(timespec="seconds"),
                    datatype=XSD.dateTime,
                )
            }
            self.humemai.add_short_term_memory(triples=triples, qualifiers=qualifiers)

        else:
            raise NotImplementedError(
                f"Memory management policy '{self.mm_policy}' not implemented."
            )

    # -------------------------------------------------------------------------
    # QA Policy
    # -------------------------------------------------------------------------

    def answer_question(self, question: tuple[str, str]) -> str:
        """
        Answer a question based on the agent's memory using the specified QA policy,
        and increment 'recalled' only for the one statement (exact triple + exact timeVal).
        """

        subject_str = f"<{question[0]}>"
        predicate_str = f"<{question[1]}>"

        # Query for the statement, object, and timeVal (coalescing current_time / event_time).
        # Each row is one reified statement.
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
            return "No answer found"

        # Depending on qa_policy, pick exactly one row
        best_row = None

        if self.qa_policy == "latest":
            valid_rows = [r for r in results if r.timeVal is not None]
            if not valid_rows:
                return "No answer found"
            # Sort descending by timeVal, pick the first
            valid_rows.sort(key=lambda r: r.timeVal, reverse=True)
            best_row = valid_rows[0]

        elif self.qa_policy == "oldest":
            valid_rows = [r for r in results if r.timeVal is not None]
            if not valid_rows:
                return "No answer found"
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
            return "No answer found"

        best_obj = best_row.object
        best_timeVal = best_row.timeVal  # an rdflib Literal, hopefully xsd:dateTime

        # If your object is a URIRef, wrap it as URIRef(). If it's a Literal, pass directly.
        # For demonstration, let's assume best_obj is a URI.
        # If you know it's sometimes a Literal, handle accordingly:
        #    if isinstance(best_obj, Literal): ...
        best_obj_uri = URIRef(str(best_obj))

        self._update_qa_memory_access(
            subject=URIRef(question[0]),
            predicate=URIRef(question[1]),
            object_=best_obj_uri,
            time_literal=best_timeVal,
        )

        # Return the chosen best object as a string (or as is)
        return str(best_obj_uri)

    def _update_qa_memory_access(
        self, subject: URIRef, predicate: URIRef, object_: URIRef, time_literal: Literal
    ) -> None:
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

    def _update_exploration_memory_access(
        self, current_room: str, direction: str
    ) -> None:
        """
        Update memory access for exploration decisions.

        This function searches for a reified memory statement with:
        - rdf:subject = current_room
        - rdf:predicate = direction
        and that has either an 'event_time' or 'current_time' qualifier.

        It orders the results by COALESCE(event_time, current_time) in descending order.
        If the returned statement has only a current_time (i.e. short-term memory),
        the update is skipped. Otherwise, it uses the event_time as the timestamp for
        updating the memory access counters.

        Note: Since we're no longer using a next_room, the update will apply to the memory
        edge (current_room, direction) regardless of its object.
        """
        # Query for matching reified statements with an event_time qualifier.
        # (Assuming that the RDF graph stores simple string values for properties.)
        query = f"""
            PREFIX humemai: <https://humem.ai/ontology#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

            SELECT ?stmt ?event_time ?current_time
            WHERE {{
                ?stmt rdf:type rdf:Statement ;
                    rdf:subject <{current_room}> ;
                    rdf:predicate <{direction}> .
                OPTIONAL {{ ?stmt humemai:event_time ?event_time }}
                OPTIONAL {{ ?stmt humemai:current_time ?current_time }}
                FILTER(BOUND(?event_time) || BOUND(?current_time))
            }}
            ORDER BY DESC(COALESCE(?event_time, ?current_time))
            LIMIT 1
        """

        results = list(self.humemai.graph.query(query))
        if not results:
            raise ValueError(
                f"No matching memory found for {current_room} -> {direction}"
            )

        best_result = results[0]
        event_time = best_result.event_time
        current_time = best_result.current_time

        if current_time and not event_time:
            # This is a short-term memory → skip
            return

        if not event_time:
            raise ValueError(
                "Expected at least event_time or current_time, but got neither."
            )

        # Update memory access information using the helper methods provided by humemai.
        # Increment the recalled counter for the matching memory.
        self.humemai.increment_recalled(
            subject=URIRef(current_room),
            predicate=URIRef(direction),
            object_=None,
            lower_time_bound=event_time,
            upper_time_bound=event_time,
        )

        # Update the last_accessed qualifier with the current time.
        # (Assumes self.current_time is a string with an ISO-formatted datetime.)
        self.humemai.update_last_accessed(
            subject=URIRef(current_room),
            predicate=URIRef(direction),
            object_=None,
            new_time=Literal(self.current_time.isoformat(), datatype=XSD.dateTime),
            lower_time_bound=event_time,
            upper_time_bound=event_time,
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
            raise ValueError("No valid directions available. Agent may be stuck.")
        else:
            # Randomly select one of the valid directions

            return random.choice(possible_dirs)

    # --- BFS with fallback to "least visited" ---

    def _explore_bfs(self) -> str:
        """
        Modified BFS strategy:
          1. Find the first unvisited room as usual.
          2. If no unvisited rooms remain, pick the 'least visited' room.
          3. Return the direction for the first step on the path to that room.
        """
        current_room = self._get_agent_current_room()
        if not current_room:
            raise ValueError("Agent's current room not found.")

        visited_rooms = self._get_visited_rooms()
        adjacency = self._build_room_adjacency()

        # Step 1: normal BFS to find a new (unvisited) room
        target_room, direction = self._bfs_find_new_room(
            current_room, adjacency, visited_rooms
        )
        if target_room is not None:
            # Found an unvisited node
            self._update_exploration_memory_access(current_room, direction)
            return direction

        # Step 2: fallback if everything is visited -> pick least visited
        least_visited_room = self._pick_least_visited_room(visited_rooms, current_room)
        if not least_visited_room or least_visited_room == current_room:
            return self._explore_avoid_walls()

        # Step 3: BFS path to that best visited room
        direction = self._bfs_path_first_step(
            current_room, least_visited_room, adjacency
        )
        self._update_exploration_memory_access(current_room, direction)

        return direction

    def _bfs_find_new_room(
        self,
        start_room: str,
        adjacency: dict[str, list[tuple[str, str]]],
        visited_rooms: set[str],
    ) -> tuple[str | None, str]:
        """
        BFS from start_room to find the first room not in visited_rooms.
        Returns (target_room, direction_of_first_step) or (None, None) if none found.
        """
        if start_room not in adjacency:
            return (None, None)

        parents: dict[str, tuple[str | None, str | None]] = {start_room: (None, None)}
        queue = deque([start_room])
        while queue:
            target_room = queue.popleft()
            # If we reach a room not in visited_rooms (and not the start), we stop
            if target_room not in visited_rooms and target_room != start_room:
                direction = self._get_first_step(start_room, target_room, parents)
                return (target_room, direction)

            for dir_str, neighbor in adjacency.get(target_room, []):
                if neighbor not in parents:  # unvisited in BFS sense
                    parents[neighbor] = (target_room, dir_str)
                    queue.append(neighbor)
        return (None, None)

    def _bfs_path_first_step(
        self,
        start_room: str,
        goal_room: str,
        adjacency: dict[str, list[tuple[str, str]]],
    ) -> str:
        """
        BFS from start_room to goal_room. Returns the direction for the first step.
        If BFS fails or there's no path, defaults to explore_avoid_walls.
        """
        # If already in goal room, now fallback to explore_avoid_walls
        if start_room == goal_room:
            return self._explore_avoid_walls()

        parents: dict[str, tuple[str | None, str | None]] = {start_room: (None, None)}
        queue = deque([start_room])

        while queue:
            current = queue.popleft()
            if current == goal_room:
                return self._get_first_step(start_room, goal_room, parents)

            for dir_str, neighbor in adjacency.get(current, []):
                if neighbor not in parents:
                    parents[neighbor] = (current, dir_str)
                    queue.append(neighbor)

        # Fall back to explore_avoid_walls
        return self._explore_avoid_walls()

    # --- Dijkstra with fallback to "least visited" ---

    def _explore_dijkstra(self) -> str:
        """
        Modified Dijkstra strategy:
          1. Attempt to find an *unvisited* room with the lowest total cost.
          2. If no unvisited rooms remain, pick the least visited room.
          3. Return the direction for the first step of that path.
        """
        current_room = self._get_agent_current_room()
        if not current_room:
            raise ValueError("Agent's current room not found.")

        visited_rooms = self._get_visited_rooms()
        adjacency = self._build_room_adjacency_with_weights(visited_rooms)

        # 1. Try to find best unvisited room
        best_unvisited_room, direction = self._dijkstra_find_best_unvisited_room(
            current_room, adjacency
        )

        if best_unvisited_room is not None:
            # Found an unvisited node
            self._update_exploration_memory_access(current_room, direction)
            return direction

        # 2. Otherwise, pick the least visited fallback
        target_visited_room = self._pick_least_visited_room(visited_rooms, current_room)
        if not target_visited_room or target_visited_room == current_room:
            return self._explore_avoid_walls()

        # 3. Dijkstra path from current_room to target_visited_room
        direction = self._dijkstra_path_first_step(
            current_room, target_visited_room, adjacency
        )
        self._update_exploration_memory_access(current_room, direction)

        return direction

    def _dijkstra_find_best_unvisited_room(
        self, start_room: str, adjacency: dict[str, list[tuple[str, str, float]]]
    ) -> tuple[str, str]:
        """
        Runs Dijkstra from start_room, then picks the unvisited room with the minimal
        cost. Returns (best_room, direction_for_first_step). If no unvisited room is
        found, returns (None, None).
        """
        best_cost, parent = self._dijkstra_min_cost_path(start_room, adjacency)
        visited = self._get_visited_rooms()

        # Among all rooms, pick the unvisited (and not the start) with minimal cost
        candidates = [
            (room, cost)
            for room, cost in best_cost.items()
            if room != start_room and room not in visited and cost != float("inf")
        ]
        if not candidates:
            return (None, None)

        best_room, _ = min(candidates, key=lambda x: x[1])
        direction = self._dijkstra_reconstruct_first_step(start_room, best_room, parent)
        return (best_room, direction)

    def _dijkstra_path_first_step(
        self,
        start_room: str,
        goal_room: str,
        adjacency: dict[str, list[tuple[str, str, float]]],
    ) -> str:
        """
        Run Dijkstra from start_room to goal_room, then return the first step's direction.
        If no path is found or start_room == goal_room, defaults to explore_avoid_walls.
        """
        if start_room == goal_room:
            return self._explore_avoid_walls()

        best_cost, parent = self._dijkstra_min_cost_path(start_room, adjacency)
        if best_cost.get(goal_room, float("inf")) == float("inf"):
            return self._explore_avoid_walls()

        return self._dijkstra_reconstruct_first_step(start_room, goal_room, parent)

    def _dijkstra_min_cost_path(
        self, start_room: str, adjacency: dict[str, list[tuple[str, str, float]]]
    ) -> tuple[dict[str, float], dict[str, tuple[str, str]]]:
        """
        Standard Dijkstra from start_room, returning:
          - best_cost[room]: minimal cumulative cost from start_room to room
          - parent[room] = (previous_room, direction)
        """
        best_cost: dict[str, float] = {}
        parent: dict[str, tuple[str, str]] = {}

        # Initialize costs
        for room in adjacency:
            best_cost[room] = float("inf")
        best_cost[start_room] = 0.0

        pq = [(0.0, start_room)]
        while pq:
            current_cost, current_room = heapq.heappop(pq)
            if current_cost > best_cost[current_room]:
                continue

            for dir_str, neighbor, edge_cost in adjacency.get(current_room, []):
                candidate = current_cost + edge_cost
                if candidate < best_cost.get(neighbor, float("inf")):
                    best_cost[neighbor] = candidate
                    parent[neighbor] = (current_room, dir_str)
                    heapq.heappush(pq, (candidate, neighbor))

        return best_cost, parent

    def _dijkstra_reconstruct_first_step(
        self, start_room: str, goal_room: str, parent: dict[str, tuple[str, str]]
    ) -> str:
        """
        Backtrack from goal_room to start_room using 'parent' dictionary,
        then return the direction from start_room to the second room in that path.
        """
        path = []
        current = goal_room
        while current in parent and current != start_room:
            prev_room, dir_used = parent[current]
            path.append((prev_room, current, dir_used))
            current = prev_room

        # If we never made it back to start_room
        if not path or current != start_room:
            return self._explore_avoid_walls()

        # The last item in path is (start_room, second_room, direction_out_of_start_room).
        return path[-1][2] or self._explore_avoid_walls()

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
        return None

    def _build_room_adjacency(self) -> dict[str, list[tuple[str, str]]]:
        """
        Build an adjacency mapping: for each roomX, list of (direction, roomY), skipping
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
            dir_str = row.dir.split("/")[-1]  # e.g. <north> -> "north"
            roomY = str(row.roomY)
            # skip if leads to wall
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
        Build weighted adjacency: roomX -> [(direction, roomY, cost)]. For each edge,
        cost = 1/(1 + count_objs_in_roomY).
        """
        adjacency: dict[str, list[tuple[str, str, float]]] = {}
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

            # Simple cost: 1 / (1 + number_of_interesting_objects)
            count_objs = self._count_interesting_objects_in_room(roomY)
            cost = 1.0 / (1.0 + count_objs)

            if roomX not in adjacency:
                adjacency[roomX] = []
            adjacency[roomX].append((dir_str, roomY, cost))

        return adjacency

    def _count_interesting_objects_in_room(self, room: str) -> int:
        """
        Count "interesting" objects in a room. We define objects as interesting if their
        URI contains one of the prefixes: "sat_", "ind_", or "dep_".
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
        Among *visited* rooms, pick the one with the minimal visit count. Exclude the
        agent's current room from the candidates. Returns the chosen room's URI or None
        if no candidate found.
        """
        room_visit_counts = self._get_room_visit_counts()

        # Candidate rooms: visited, but not the agent's current
        candidate_rooms = [r for r in visited_rooms if r != current_room]
        if not candidate_rooms:
            return None

        # Sort by ascending visit count, then pick the first
        candidate_rooms.sort(key=lambda r: room_visit_counts.get(r, 0))
        return candidate_rooms[0]

    def _get_room_visit_counts(self) -> dict[str, int]:
        """
        Returns a dict {roomURI: visit_count}, counting all times that (agent,
        at_location, roomURI) appears (across any event_time).
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
    # Generic Helper for BFS Path Reconstruction
    # -------------------------------------------------------------------------

    def _get_first_step(
        self,
        start_room: str,
        goal_room: str,
        parents: dict[str, tuple[str | None, str | None]],
    ) -> str:
        """
        Backtrack from goal_room to start_room using the BFS 'parents' mapping, then
        return the direction used for the initial move out of start_room.
        """
        path: list[tuple[str | None, str, str | None]] = []
        current = goal_room
        while current != start_room:
            prev_room, dir_to_current = parents[current]
            if prev_room is None:
                break
            path.append((prev_room, current, dir_to_current))
            current = prev_room
        if not path:
            return self._explore_avoid_walls()

        # The last element in path is the first step from start_room
        return path[-1][2] or self._explore_avoid_walls()

    # -------------------------------------------------------------------------
    # Env Testing Example
    # -------------------------------------------------------------------------

    def _run_test_episode(self) -> tuple[float, int]:
        """
        Execute a single test episode in the environment, returning total score and step
        count.
        """
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
