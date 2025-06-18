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
        architecture_type,  # Changed from gcn_type to architecture_type
        max_memory,
        forget_policy,
        remember_policy,
        separate_networks,
    ) = params
    train_seed = test_seed + 5
    num_iterations = 40

    print(
        f"Test seed: {test_seed}, Train seed: {train_seed}, Architecture: {architecture_type}, "
        f"Max memory: {max_memory}, Forget: {forget_policy}, Remember: {remember_policy}, "
        f"Separate networks: {separate_networks}"
    )

    # Configure dqn_params based on architecture type
    if architecture_type == "transformer":
        dqn_params = {
            "gcn_layer_params": {
                "type": "stare",  # Still needed for embedding_dim
                "embedding_dim": 4,
                "num_layers": 2,
                "gcn_drop": 0.1,
                "triple_qual_weight": 0.8,
            },
            "relu_between_gcn_layers": True,
            "dropout_between_gcn_layers": True,
            "mlp_params": {"num_hidden_layers": 1, "dueling_dqn": True},
            "architecture_type": "transformer",
            "transformer_params": {
                "num_layers": 2,
                "num_heads": 2,  # Reduced for small embedding_dim
                "dropout": 0.1,
            },
        }
    else:  # GNN architecture
        dqn_params = {
            "gcn_layer_params": {
                "type": architecture_type,  # Use the architecture_type as gcn_type
                "embedding_dim": 4,
                "num_layers": 2,
                "gcn_drop": 0.1,
                "triple_qual_weight": 0.8,
            },
            "relu_between_gcn_layers": True,
            "dropout_between_gcn_layers": True,
            "mlp_params": {"num_hidden_layers": 1, "dueling_dqn": True},
            "architecture_type": "gnn",
        }

    agent = DQNAgent(
        env_config={
            "question_prob": 1.0,
            "terminates_at": 9,
            "randomize_observations": "all",
            "room_size": "xl-different-prob",
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": 10,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": False,
        },
        qa_policy="most_recently_added",
        explore_policy="dijkstra",
        forget_policy=forget_policy,
        remember_policy=remember_policy,
        max_long_term_memory_size=max_memory,
        num_samples_for_results={"val": 2, "test": 2},
        save_results=True,
        default_root_dir="training-results-foo",
        num_iterations=num_iterations,
        replay_buffer_size=num_iterations,
        batch_size=4,
        warm_start=4,
        target_update_interval=3,
        epsilon_decay_until=num_iterations,
        max_epsilon=1.0,
        min_epsilon=0.1,
        gamma=0.90,
        learning_rate=0.001,
        dqn_params=dqn_params,
        validation_interval=1,
        plotting_interval=3,
        train_seed=train_seed,
        test_seed=test_seed,
        device="cpu",
        ddqn=True,
        pretrain_semantic=False,
        use_gradient_clipping=False,
        gradient_clip_value=1.0,
        separate_networks=separate_networks,
    )
    agent.train()


if __name__ == "__main__":
    test_seeds = [0]
    architecture_types = ["stare", "transformer"]  # Test both GNN (StarE) and Transformer
    max_memories = [8]
    policy_combinations = [("lru", "rl"), ("rl", "all"), ("rl", "rl")]

    all_combinations = []

    for seed in test_seeds:
        for arch_type in architecture_types:
            for memory in max_memories:
                for forget_policy, remember_policy in policy_combinations:
                    # Only test separate_networks=True when both policies are "rl"
                    if forget_policy == "rl" and remember_policy == "rl":
                        # Test both shared and separate networks
                        all_combinations.append(
                            (
                                seed,
                                arch_type,
                                memory,
                                forget_policy,
                                remember_policy,
                                False,
                            )
                        )
                        all_combinations.append(
                            (
                                seed,
                                arch_type,
                                memory,
                                forget_policy,
                                remember_policy,
                                True,
                            )
                        )
                    else:
                        # Only test shared networks (separate_networks=False)
                        all_combinations.append(
                            (
                                seed,
                                arch_type,
                                memory,
                                forget_policy,
                                remember_policy,
                                False,
                            )
                        )

    random.shuffle(all_combinations)

    num_processes = multiprocessing.cpu_count()  # or choose a fixed number
    num_processes = 20
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_dqn_experiment, all_combinations)
