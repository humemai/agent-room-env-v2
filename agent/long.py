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
        explore_policy: str = "bfs",  # "random", "avoid_walls", "bfs", "dijkstra"
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
            # We found a path to an unvisited room
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
        cost = 1 / (1 + count_interesting_objects_in roomY).
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
        print(edges)
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
        # If it's purely short-term, that means ?ct is set, but ?et and ?ks are both
        # None. So we check that condition and skip.
        if et_val is None and ks_val is None:
            assert row.ct is not None
            # This means we have only ?ct => short-term memory => skip
            return

        if time_val is None:
            raise ValueError(
                f"No valid time found for ({subject}, {predicate}, {object_})."
            )

        # If we're here, we have an LTM statement with either event_time or known_since
        # => it’s safe to increment recalled and update last_accessed.

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
