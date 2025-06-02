"""This module defines the ShortTermAgent class which uses a short-term memory
to store and retrieve observations, along with QA and exploration policies.
"""

import random
from copy import deepcopy
from datetime import datetime, timedelta
from typing import Any

from humemai.rdflib import Humemai
from rdflib import XSD, Literal, Namespace, URIRef

from .agent import Agent


class ShortTermAgent(Agent):
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
        qa_policy: str = "one_hop",
        explore_policy: str = "avoid_walls",
        num_samples_for_results: int = 10,
        save_results: bool = True,
        default_root_dir: str = "./training-results/",
    ) -> None:
        """Initialize the ShortTermAgent with the provided environment configuration,
        QA policy, and exploration policy.
        """
        params_to_save = deepcopy(locals())
        del params_to_save["self"]
        del params_to_save["__class__"]
        super().__init__(**params_to_save)

        self.qa_policy = qa_policy
        self.explore_policy = explore_policy

        # HumemAI
        self.humemai_ns = Namespace("https://humem.ai/ontology#")
        self.base_date = datetime.fromisoformat("2025-01-01T00:00:00")
        self.humemai = Humemai()

    def manage_memory(self, observations: list[list[str]], step: int) -> None:
        """Save observations to the agent's short-term memory.

        Converts observation strings to RDF URI references and adds them to
        the Humemai short-term memory with appropriate time qualifiers.

        Args:
            observations: A list of RDF triples represented as lists of strings.
                          Each inner list should contain three elements (subject,
                          predicate, object).
            step: The current time step, used to calculate the memory timestamp.

        Returns:
            None
        """
        self.humemai.clear_short_term_memories()
        triples = [[URIRef(item) for item in obs] for obs in observations]
        current_time = self.base_date + timedelta(days=step)
        qualifiers = {
            self.humemai_ns.current_time: Literal(
                current_time.isoformat(timespec="seconds"),
                datatype=XSD.dateTime,
            )
        }
        self.humemai.add_short_term_memory(triples=triples, qualifiers=qualifiers)

    def answer_question(self, question: tuple[str, str]) -> str:
        """Answer a question using the agent's knowledge base."""
        if self.qa_policy == "one_hop":
            subject = f"<{question[0]}>"
            predicate = f"<{question[1]}>"

            # *** Updated query for reified statements ***
            results = self.humemai.graph.query(
                f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX humemai: <https://humem.ai/ontology#>
                SELECT ?object
                WHERE {{
                    ?stmt rdf:type rdf:Statement ;
                            rdf:subject {subject} ;
                            rdf:predicate {predicate} ;
                            rdf:object ?object ;
                            humemai:current_time ?current_time .
                }}
                LIMIT 1
                """
            )

            for row in results:
                return str(row.object)
            return "No answer found"

        elif self.qa_policy == "random":
            # *** Updated query for reified statements ***
            query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

            SELECT ?subject ?predicate ?object
            WHERE {
                ?statement rdf:type rdf:Statement ;
                        rdf:subject ?subject ;
                        rdf:predicate ?predicate ;
                        rdf:object ?object .
                FILTER(isIRI(?subject))
            }
            """
            results = list(self.humemai.graph.query(query))
            if results:
                row = random.choice(results)
                return str(row.object)
            else:
                return "No answer found"

    def explore(self) -> str:
        """Determine movement direction based on the exploration policy."""
        if self.explore_policy == "random":
            return random.choice(["north", "south", "east", "west", "stay"])

        elif self.explore_policy == "avoid_walls":
            # *** Updated query for reified statements ***
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
            available_directions = [str(row.direction).strip("<>") for row in results]
            return (
                random.choice(available_directions) if available_directions else "stay"
            )

    def _run_test_episode(self) -> tuple[float, int]:
        """Run a single test episode.

        Executes one complete episode in the environment, tracking score and steps.

        Args:
            None

        Returns:
            tuple: (score, steps) - The final score and number of steps taken in the
            episode.
        """
        score = 0
        step = 0
        self.humemai.reset()

        # Initial step
        observations, info = self.env.reset()
        self.manage_memory(observations["room"], step)

        while True:
            # Generate action pair
            action_pair = self._generate_action_pair(observations)

            # Take a step in the environment
            observations, reward, done, truncated, info = self.env.step(action_pair)

            # Update score and step counter
            current_reward = sum(reward)
            score += current_reward
            step += 1

            # Update memory with new observations
            self.manage_memory(observations["room"], step)

            if done:
                break

        return score, step
