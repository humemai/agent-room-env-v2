import itertools
import multiprocessing
import shutil
from copy import deepcopy
from datetime import datetime, timedelta
import random
from typing import Any

import numpy as np
import gymnasium as gym
from rdflib import BNode, XSD, Graph, Literal, Namespace, URIRef

from humemai.rdflib import Humemai

import logging
from agent import ShortTermAgent, LongTermAgent

ns = Namespace("https://humem.ai/ontology#")

# Disable logging
logging.getLogger().setLevel(logging.CRITICAL)


def run_short_term_experiment(params: tuple[int, str, str, str]) -> None:
    seed, room_size, qa_policy, explore_policy = params

    print(
        f"Seed: {seed}, Room size: {room_size}, QA policy: {qa_policy}, "
        f"Explore policy: {explore_policy}"
    )

    agent = ShortTermAgent(
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
        num_samples_for_results=10,
    )

    agent.test()


def run_long_term_experiment(params):
    seed, room_size, qa_policy, explore_policy, mm_policy, max_memory = params
    print(
        f"Seed: {seed}, Room size: {room_size}, QA: {qa_policy}, Explore: {explore_policy}, "
        f"MM: {mm_policy}, Max memory: {max_memory}"
    )

    agent = LongTermAgent(
        env_config={
            "question_prob": 1.0,
            "seed": seed,
            "terminates_at": 99,
            "randomize_observations": "none",
            "room_size": room_size,
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": 1000,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": True,
        },
        qa_policy=qa_policy,
        explore_policy=explore_policy,
        mm_policy=mm_policy,
        max_long_term_memory_size=max_memory,
        num_samples_for_results=1,
        default_root_dir="./foo/",
        save_results=False,
    )
    agent.test()


if __name__ == "__main__":
    seeds = [0, 1, 2, 3, 4]
    room_sizes = [
        "xxl-different-prob",
        "xl-different-prob",
        "l-different-prob",
        "m-different-prob",
        "s-different-prob",
        "xs-different-prob",
    ]
    qa_policies = ["one_hop"]
    explore_policies = ["avoid_walls"]

    all_combinations = list(
        itertools.product(seeds, room_sizes, qa_policies, explore_policies)
    )

    num_processes = multiprocessing.cpu_count()  # or manually set, e.g., 8
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_short_term_experiment, all_combinations)

    seeds = [0, 1, 2, 3, 4]
    room_sizes = [
        "xxl-different-prob",
        "xl-different-prob",
        "l-different-prob",
        "m-different-prob",
        "s-different-prob",
        "xs-different-prob",
    ]
    qa_policies = ["latest"]
    explore_policies = ["dijkstra"]
    mm_policies = ["lfu"]
    max_memories = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    all_combinations = list(
        itertools.product(
            seeds, room_sizes, qa_policies, explore_policies, mm_policies, max_memories
        )
    )

    num_processes = multiprocessing.cpu_count()  # or choose a fixed number
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_experiment, all_combinations)
