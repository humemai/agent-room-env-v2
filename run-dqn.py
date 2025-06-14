import itertools
import logging
import multiprocessing
import random

import matplotlib

matplotlib.use("Agg")
logger = logging.getLogger()
logger.disabled = True
logging.disable(logging.CRITICAL)

from agent import DQNAgent


def run_dqn_experiment(params):
    test_seed, gcn_type, max_memory, forget_policy, remember_policy = params
    train_seed = test_seed + 5
    num_iterations = 20000

    print(
        f"Test seed: {test_seed}, Train seed: {train_seed}, GCN: {gcn_type}, "
        f"Max memory: {max_memory}, Forget: {forget_policy}, Remember: {remember_policy}"
    )

    agent = DQNAgent(
        env_config={
            "question_prob": 1.0,
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
        qa_policy="most_recently_added",
        explore_policy="dijkstra",
        forget_policy=forget_policy,
        remember_policy=remember_policy,
        max_long_term_memory_size=max_memory,
        num_samples_for_results={"val": 5, "test": 10},
        save_results=True,
        default_root_dir="training-results",
        num_iterations=num_iterations,
        replay_buffer_size=num_iterations,
        batch_size=32,
        warm_start=32,
        target_update_interval=10,
        epsilon_decay_until=num_iterations,
        max_epsilon=1.0,
        min_epsilon=0.1,
        gamma=0.90,
        learning_rate=0.001,
        dqn_params={
            "gcn_layer_params": {
                "type": gcn_type,
                "embedding_dim": 64,
                "num_layers": 2,
                "gcn_drop": 0.1,
                "triple_qual_weight": 0.8,
            },
            "relu_between_gcn_layers": True,
            "dropout_between_gcn_layers": True,
            "mlp_params": {"num_hidden_layers": 2, "dueling_dqn": True},
        },
        validation_interval=1,
        plotting_interval=20,
        train_seed=train_seed,
        test_seed=test_seed,
        device="cpu",
        ddqn=True,
        pretrain_semantic=False,
    )
    agent.train()


if __name__ == "__main__":
    test_seeds = [0, 1, 2, 3, 4]
    gcn_types = ["stare"]
    max_memories = [16, 32, 64]
    forget_policies = ["lru", "rl"]
    remember_policies = ["all", "rl"]

    all_combinations = list(
        itertools.product(
            test_seeds, gcn_types, max_memories, forget_policies, remember_policies
        )
    )

    random.shuffle(all_combinations)

    num_processes = multiprocessing.cpu_count()  # or choose a fixed number
    num_processes = 16
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_dqn_experiment, all_combinations)
