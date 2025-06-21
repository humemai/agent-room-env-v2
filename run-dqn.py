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
    (
        test_seed,
        architecture_type,
        max_memory,
        forget_policy,
        remember_policy,
        separate_networks,
        embedding_dim,
        num_layers,
        num_heads,
        mlp_hidden_layers,
    ) = params
    train_seed = test_seed + 5

    terminates_at = 99
    num_total_questions = 1000
    num_episodes = 100  # should be between 100 and 500
    num_iterations = (terminates_at + 1) * num_episodes
    num_target_syncs = 200  # should be between 200 and 1000
    target_update_interval = num_iterations // num_target_syncs
    epsilon_decay_until = num_iterations // 5  # 20 percent of the iterations
    warm_start = num_iterations // 5  # 20 percent of the iterations

    print(
        f"Test seed: {test_seed}, Train seed: {train_seed}, Architecture: {architecture_type}, "
        f"Max memory: {max_memory}, Forget: {forget_policy}, Remember: {remember_policy}, "
        f"Separate networks: {separate_networks}, Embedding dim: {embedding_dim}, "
        f"Num layers: {num_layers}, Num heads: {num_heads}, MLP hidden layers: {mlp_hidden_layers}"
    )

    # Define architecture-specific parameters
    stare_params = {
        "embedding_dim": embedding_dim,
        "num_layers": num_layers,
        "gcn_drop": 0.1,
        "triple_qual_weight": 0.8,
        "relu_between_layers": True,
        "dropout_between_layers": True,
    }

    gcn_params = {
        "embedding_dim": embedding_dim,
        "num_layers": num_layers,
        "gcn_drop": 0.1,
        "relu_between_layers": True,
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
            "room_size": "xl-different-prob",
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": num_total_questions,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": False,
        },
        qa_policy="most_recently_added",
        explore_policy="dijkstra",
        forget_policy=forget_policy,
        remember_policy=remember_policy,
        max_long_term_memory_size=max_memory,
        num_samples_for_results={"val": 1, "test": 5},
        save_results=True,
        default_root_dir="training-results-dqn",
        num_iterations=num_iterations,
        replay_buffer_size=num_iterations,
        batch_size=32,
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
        validation_interval=1,
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


if __name__ == "__main__":
    test_seeds = [0]
    architecture_types = [
        "stare",
        "gcn",
        "transformer",
    ]
    max_memories = [32]
    policy_combinations = [
        ("lru", "rl"),
        ("rl", "all"),
        ("rl", "rl", "separate"),
        ("rl", "rl", "non_separate"),
    ]

    network_sizes = ["small", "big"]

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

    all_combinations = []

    for seed in test_seeds:
        for arch_type in architecture_types:
            for memory in max_memories:
                for policy_combo in policy_combinations:
                    for network_size in network_sizes:
                        config = network_configs[arch_type][network_size]

                        if len(policy_combo) == 3:
                            forget_policy, remember_policy, network_type = policy_combo
                            separate_networks = network_type == "separate"
                        else:
                            forget_policy, remember_policy = policy_combo
                            separate_networks = False

                        all_combinations.append(
                            (
                                seed,
                                arch_type,
                                memory,
                                forget_policy,
                                remember_policy,
                                separate_networks,
                                config["embedding_dim"],
                                config["num_layers"],
                                config["num_heads"],
                                config["mlp_hidden_layers"],
                            )
                        )

    random.shuffle(all_combinations)

    num_processes = multiprocessing.cpu_count()  # or choose a fixed number
    num_processes = 4
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_dqn_experiment, all_combinations)
