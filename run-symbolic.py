import itertools
import logging
import multiprocessing
import random

from rdflib import Namespace

from agent import LongTermAgent

ns = Namespace("https://humem.ai/ontology#")

# Disable logging
logging.getLogger().setLevel(logging.CRITICAL)


def run_long_term_experiment(params):
    seed, room_size, qa_policy, explore_policy, forget_policy, max_memory = params
    print(
        f"Seed: {seed}, Room size: {room_size}, QA: {qa_policy}, Explore: {explore_policy}, "
        f"MM: {forget_policy}, Max memory: {max_memory}"
    )

    agent = LongTermAgent(
        env_config={
            "question_prob": 1.0,
            "seed": seed,
            "terminates_at": 99,
            "randomize_observations": "all",
            "room_size": room_size,
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": 1000,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": False,
        },
        qa_policy=qa_policy,
        explore_policy=explore_policy,
        forget_policy=forget_policy,
        max_long_term_memory_size=max_memory,
        num_samples_for_results=1,
        default_root_dir="./training-results-symbolic/",
        save_results=True,
    )
    agent.test()


if __name__ == "__main__":
    seeds = [0, 1, 2, 3, 4]
    room_sizes = [
        "s-different-prob",
        "m-different-prob",
        "l-different-prob",
        "xl-different-prob",
        "xxl-different-prob",
    ]
    qa_policies = [
        "most_recently_added",
        "most_recently_used",
        "most_frequently_used",
    ]
    explore_policies = ["bfs", "dijkstra", "random"]
    mm_policies = ["lfu", "lru", "fifo", "random"]
    max_memories = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    all_combinations = list(
        itertools.product(
            seeds, room_sizes, qa_policies, explore_policies, mm_policies, max_memories
        )
    )

    random.shuffle(all_combinations)

    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_long_term_experiment, all_combinations)
