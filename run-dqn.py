import logging
import multiprocessing
import random
import os
import yaml
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
logger = logging.getLogger()
logger.disabled = True
logging.disable(logging.CRITICAL)

from agent import DQNAgent

# Define network size configurations
network_configs = {
    "gcn": {
        "small": {
            "embedding_dim": 32,
            "num_layers": 2,
            "num_heads": 2,
            "mlp_hidden_layers": 1,
        },
        "big": {
            "embedding_dim": 64,
            "num_layers": 4,
            "num_heads": 2,
            "mlp_hidden_layers": 1,
        },
    },
    "stare": {
        "small": {
            "embedding_dim": 32,
            "num_layers": 2,
            "num_heads": 2,
            "mlp_hidden_layers": 1,
        },
        "big": {
            "embedding_dim": 64,
            "num_layers": 2,
            "num_heads": 2,
            "mlp_hidden_layers": 1,
        },
    },
    "transformer": {
        "small": {
            "embedding_dim": 16,
            "num_layers": 2,
            "num_heads": 2,
            "mlp_hidden_layers": 1,
        },
        "big": {
            "embedding_dim": 32,
            "num_layers": 4,
            "num_heads": 4,
            "mlp_hidden_layers": 1,
        },
    },
}
default_root_dir = "training-results-dqn"


def run_dqn_experiment(params):
    (
        room_size,
        test_seed,
        architecture_type,
        max_memory,
        forget_policy,
        remember_policy,
        qa_policy,
        explore_policy,
        separate_networks,
        embedding_dim,
        num_layers,
        num_heads,
        mlp_hidden_layers,
    ) = params
    train_seed = test_seed + 5

    batch_size = 32
    terminates_at = 99
    num_total_questions = 1000
    num_episodes = 200  # should be between 100 and 500
    num_iterations = (terminates_at + 1) * num_episodes
    target_update_interval = 50  # 50 to 200 is common
    epsilon_decay_until = num_iterations // 2  # 50% of iterations
    warm_start = num_iterations // 5  # 20 percent of the iterations

    print(
        f"room_size: {room_size}, "
        f"Test seed: {test_seed}, Train seed: {train_seed}, Architecture: {architecture_type}, "
        f"Max memory: {max_memory}, Forget: {forget_policy}, Remember: {remember_policy}, "
        f"QA: {qa_policy}, Explore: {explore_policy}, "
        f"Separate networks: {separate_networks}, Embedding dim: {embedding_dim}, "
        f"Num layers: {num_layers}, Num heads: {num_heads}, MLP hidden layers: {mlp_hidden_layers}"
    )

    # Define architecture-specific parameters
    stare_params = {
        "embedding_dim": embedding_dim,
        "num_layers": num_layers,
        "gcn_drop": 0.1,
        "triple_qual_weight": 0.8,
        "silu_between_layers": True,
        "dropout_between_layers": True,
    }

    gcn_params = {
        "embedding_dim": embedding_dim,
        "num_layers": num_layers,
        "gcn_drop": 0.1,
        "silu_between_layers": True,
        "dropout_between_layers": True,
    }

    transformer_params = {
        "embedding_dim": embedding_dim,
        "dim_feedforward": embedding_dim * 4,
        "num_layers": num_layers,
        "num_heads": num_heads,
        "dropout": 0.1,
    }

    mlp_params = {"num_hidden_layers": mlp_hidden_layers, "dueling_dqn": True}

    agent = DQNAgent(
        env_config={
            "question_prob": 1.0,
            "terminates_at": terminates_at,
            "randomize_observations": "all",
            "room_size": room_size,
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": num_total_questions,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": False,
        },
        qa_policy=qa_policy,
        explore_policy=explore_policy,
        forget_policy=forget_policy,
        remember_policy=remember_policy,
        max_long_term_memory_size=max_memory,
        num_samples_for_results={"val": 5, "test": 5},
        save_results=True,
        default_root_dir=default_root_dir,
        num_iterations=num_iterations,
        replay_buffer_size=num_iterations,
        batch_size=batch_size,
        warm_start=warm_start,
        target_update_interval=target_update_interval,
        epsilon_decay_until=epsilon_decay_until,
        max_epsilon=1.0,
        min_epsilon=0.01,
        gamma=0.90,
        learning_rate=1e-4,
        architecture_type=architecture_type,
        stare_params=stare_params,
        gcn_params=gcn_params,
        transformer_params=transformer_params,
        mlp_params=mlp_params,
        validation_interval=5,
        plotting_interval=10,
        train_seed=train_seed,
        test_seed=test_seed,
        device="cpu",
        ddqn=True,
        pretrain_semantic=False,
        use_gradient_clipping=True,
        gradient_clip_value=10.0,
        separate_networks=separate_networks,
    )

    agent.train()


def extract_experiment_params(train_yaml_path):
    """Extract experiment parameters from train.yaml file."""
    try:
        with open(train_yaml_path, "r") as f:
            data = yaml.safe_load(f)

        # Extract all the parameters that define a unique experiment
        return {
            "room_size": data["env_config"]["room_size"],
            "test_seed": data["kwargs"]["test_seed"],
            "train_seed": data["kwargs"]["train_seed"],
            "architecture_type": data["kwargs"]["architecture_type"],
            "max_memory": data["max_long_term_memory_size"],
            "forget_policy": data["forget_policy"],
            "remember_policy": data["remember_policy"],
            "qa_policy": data["qa_policy"],
            "explore_policy": data["explore_policy"],
            "separate_networks": data["kwargs"]["separate_networks"],
            "embedding_dim": data["kwargs"][
                f"{data['kwargs']['architecture_type']}_params"
            ]["embedding_dim"],
            "num_layers": data["kwargs"][
                f"{data['kwargs']['architecture_type']}_params"
            ]["num_layers"],
            "num_heads": data["kwargs"]
            .get("transformer_params", {})
            .get(
                "num_heads", data["kwargs"].get("stare_params", {}).get("num_heads", 0)
            ),
            "mlp_hidden_layers": data["kwargs"]["mlp_params"]["num_hidden_layers"],
        }
    except (FileNotFoundError, KeyError, yaml.YAMLError):
        return None


def is_experiment_completed(params, default_root_dir):
    """Check if an experiment with the given parameters is already completed."""
    (
        room_size,
        test_seed,
        architecture_type,
        max_memory,
        forget_policy,
        remember_policy,
        qa_policy,
        explore_policy,
        separate_networks,
        embedding_dim,
        num_layers,
        num_heads,
        mlp_hidden_layers,
    ) = params

    train_seed = test_seed + 5

    # Check all subdirectories in the results directory
    results_dir = Path(default_root_dir)
    if not results_dir.exists():
        return False

    for subdir in results_dir.iterdir():
        if not subdir.is_dir():
            continue

        train_yaml_path = subdir / "train.yaml"
        results_yaml_path = subdir / "results.yaml"

        # Check if experiment is completed (has results.yaml)
        if not results_yaml_path.exists():
            continue

        # Extract parameters from existing experiment
        existing_params = extract_experiment_params(train_yaml_path)
        if existing_params is None:
            continue

        # Compare all parameters
        if (
            existing_params["room_size"] == room_size
            and existing_params["test_seed"] == test_seed
            and existing_params["train_seed"] == train_seed
            and existing_params["architecture_type"] == architecture_type
            and existing_params["max_memory"] == max_memory
            and existing_params["forget_policy"] == forget_policy
            and existing_params["remember_policy"] == remember_policy
            and existing_params["qa_policy"] == qa_policy
            and existing_params["explore_policy"] == explore_policy
            and existing_params["separate_networks"] == separate_networks
            and existing_params["embedding_dim"] == embedding_dim
            and existing_params["num_layers"] == num_layers
            and existing_params["num_heads"] == num_heads
            and existing_params["mlp_hidden_layers"] == mlp_hidden_layers
        ):
            return True

    return False


if __name__ == "__main__":
    num_processes = 2
    room_sizes = ["xl-different-prob"]
    test_seeds = [0, 1, 2, 3, 4]
    architecture_types = [
        "stare",
        "gcn",
        "transformer",
    ]
    max_memories = [16, 32]
    policy_combinations = [
        # (forget, remember, qa, explore, separate_networks)
        ("rl", "all", "rl", "rl", False),
        ("rl", "all", "rl", "rl", True),
    ]

    network_sizes = ["small", "big"]

    all_combinations = []

    for room_size in room_sizes:
        for seed in test_seeds:
            for arch_type in architecture_types:
                for memory in max_memories:
                    for policy_combo in policy_combinations:
                        for network_size in network_sizes:
                            config = network_configs[arch_type][network_size]

                            (
                                forget_policy,
                                remember_policy,
                                qa_policy,
                                explore_policy,
                                separate_networks,
                            ) = policy_combo

                            params = (
                                room_size,
                                seed,
                                arch_type,
                                memory,
                                forget_policy,
                                remember_policy,
                                qa_policy,
                                explore_policy,
                                separate_networks,
                                config["embedding_dim"],
                                config["num_layers"],
                                config["num_heads"],
                                config["mlp_hidden_layers"],
                            )

                            # Only add if not already completed
                            if not is_experiment_completed(params, default_root_dir):
                                all_combinations.append(params)
                            else:
                                print(
                                    f"Skipping already completed experiment: {params}"
                                )

    random.shuffle(all_combinations)

    print(f"Total combinations to run: {len(all_combinations)}")
    print(f"Running experiments with {num_processes} processes")

    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_dqn_experiment, all_combinations)
