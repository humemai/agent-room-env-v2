"""Run training for DQN agent with specific parameters."""

import argparse

from agent.dqn import DQNAgent


def main(test_seed, capacity_max) -> None:
    """Run training.

    Args:
        test_seed (int): Seed for testing.
        capacity_max (int): Maximum capacity for the agent.
    """
    room_size = "xl-different-prob"
    terminates_at = 99
    num_iterations = (terminates_at + 1) * 1
    replay_buffer_size = 1
    batch_size = 1

    prob_type = (
        "non-equal-object-probs"
        if "different-prob" in room_size
        else "equal-object-probs"
    )
    root_path = (
        f"./training-results/{prob_type}/dqn/"
        f"room_size={room_size}/capacity={capacity_max}/"
    )
    if capacity_max == 768:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=768/2024-09-29 18:34:38.672435/"
    elif capacity_max == 384:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=384/2024-09-29 22:19:34.716582/"
    elif capacity_max == 192:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=192/2024-08-12 12:58:16.107541/"
    elif capacity_max == 96:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=96/2024-08-12 23:58:06.290168/"
    elif capacity_max == 48:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=48/2024-08-11 11:07:00.648864/"
    elif capacity_max == 24:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=24/2024-08-11 13:36:54.499426/"
    elif capacity_max == 12:
        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=12/2024-08-11 16:24:54.492650/"
    else:
        raise ValueError(f"Invalid capacity_max: {capacity_max}")

    params_dict = {
        "env_str": "room_env:RoomEnv-v2",
        "num_iterations": num_iterations,
        "replay_buffer_size": replay_buffer_size,
        "warm_start": batch_size,
        "batch_size": batch_size,
        "epsilon_decay_until": num_iterations,
        "max_epsilon": 1.0,
        "min_epsilon": 0.1,
        "learning_rate": 0.001,
        "capacity": {"long": capacity_max, "short": 15},
        "semantic_decay_factor": 0.8,
        "dqn_params": {
            "gcn_layer_params": {
                "type": "stare",
                "embedding_dim": 64,
                "num_layers": 2,
                "gcn_drop": 0.1,
                "triple_qual_weight": 0.8,
            },
            "relu_between_gcn_layers": True,
            "dropout_between_gcn_layers": False,
            "mlp_params": {
                "num_hidden_layers": 2,
                "dueling_dqn": True,
            },
            "use_raw_embeddings_for_qa": False,
        },
        "num_samples_for_results": {"val": 1, "test": 2},
        "plotting_interval": 100,
        "train_seed": test_seed + 5,
        "test_seed": test_seed,
        "device": "cpu",
        "env_config": {
            "question_prob": 1.0,
            "terminates_at": terminates_at,
            "randomize_observations": "all",
            "room_size": room_size,
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": 1000,
            "question_interval": 1,
            "include_walls_in_observations": True,
        },
        "default_root_dir": root_path,
        "qa_function": "llm",
        "qa_entities": "all",
        "pretrained_path": pretrained_path,
        "llm_params": {
            "model_id": "meta-llama/Meta-Llama-3.1-8B-Instruct",
            "quantization": "4bit",
            "max_new_tokens": 32,
        },
    }

    agent = DQNAgent(**params_dict)
    agent.train()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train DQN agent with specific parameters."
    )
    parser.add_argument(
        "--test_seed", type=int, required=True, help="Seed for testing."
    )
    parser.add_argument(
        "--capacity_max",
        type=int,
        required=True,
        help="Maximum capacity for the agent.",
    )

    args = parser.parse_args()

    main(args.test_seed, args.capacity_max)
