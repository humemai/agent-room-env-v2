import json
import os
from collections import defaultdict
from glob import glob

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import yaml
from tqdm.auto import tqdm

# Create directories if they don't exist
os.makedirs("./data", exist_ok=True)
os.makedirs("./figures", exist_ok=True)

# Collect results grouped by config (excluding seed)
results_by_config = defaultdict(list)

for path in tqdm(glob("./training-results-dqn/*/results.yaml")):
    with open(path, "r") as f:
        results = yaml.safe_load(f)

    test_mean = results["test_score"]["mean"]
    val_mean = max([val["mean"] for val in results["validation_score"]])

    with open(path.replace("results.yaml", "train.yaml")) as f:
        hp = yaml.safe_load(f)

    # Extract environment size from env_config
    room_size = hp["env_config"]["room_size"]
    
    # Extract parameters from kwargs section for DQN
    kwargs = hp.get("kwargs", {})
    architecture_type = kwargs["architecture_type"]
    max_memory = hp["max_long_term_memory_size"]
    forget_policy = hp.get("forget_policy", None)
    remember_policy = hp.get("remember_policy", "all")
    separate_networks = kwargs.get("separate_networks", False)

    # Extract network configuration parameters from kwargs
    if architecture_type == "stare":
        params = kwargs.get("stare_params", {})
    elif architecture_type == "gcn":
        params = kwargs.get("gcn_params", {})
    elif architecture_type == "transformer":
        params = kwargs.get("transformer_params", {})
    else:
        params = {}

    embedding_dim = params.get("embedding_dim", kwargs.get("embedding_dim", None))
    num_layers = params.get("num_layers", kwargs.get("num_layers", None))

    # Create network size label based on embedding_dim and num_layers
    if architecture_type == "transformer":
        if embedding_dim == 16 and num_layers == 2:
            network_size = "small"
        elif embedding_dim == 32 and num_layers == 4:
            network_size = "big"
        else:
            network_size = "custom"
    else:  # gcn or stare
        if embedding_dim == 32 and num_layers == 2:
            network_size = "small"
        elif embedding_dim == 64 and (num_layers == 4 or num_layers == 2):
            network_size = "big"
        else:
            network_size = "custom"

    config_key = (
        room_size,
        architecture_type,
        max_memory,
        forget_policy,
        remember_policy,
        separate_networks,
        network_size,
    )
    results_by_config[config_key].append((test_mean, val_mean))

# Build a DataFrame from the aggregated results
records = []
for config, score_pairs in sorted(results_by_config.items()):
    (
        room_size,
        architecture_type,
        max_memory,
        forget_policy,
        remember_policy,
        separate_networks,
        network_size,
    ) = config
    test_scores = [pair[0] for pair in score_pairs]
    val_scores = [pair[1] for pair in score_pairs]
    records.append(
        {
            "room_size": room_size,
            "architecture_type": architecture_type,
            "max_memory": max_memory,
            "forget_policy": forget_policy,
            "remember_policy": remember_policy,
            "separate_networks": separate_networks,
            "network_size": network_size,
            "test_mean": np.mean(test_scores),
            "test_std": np.std(test_scores),
            "val_mean": np.mean(val_scores),
            "val_std": np.std(val_scores),
            "n_seeds": len(score_pairs),
        }
    )

df = pd.DataFrame(records)
pd.set_option("display.precision", 4)

# Define room sizes to process (environment sizes)
room_sizes = df["room_size"].unique() if not df.empty else []

# Process each room size (environment size)
for room_filter in room_sizes:
    print(f"\n{'='*100}")
    print(f"PROCESSING ENVIRONMENT SIZE: {room_filter}")
    print(f"{'='*100}")

    # Filter for the specific room size
    df_filtered = df[df["room_size"] == room_filter].drop(columns="room_size")

    if df_filtered.empty:
        print(f"No data found for room size: {room_filter}")
        continue

    # Sort by mean_score in descending order
    df_sorted = df_filtered.sort_values(by="test_mean", ascending=False).reset_index(drop=True)

    print(f"Total configurations: {len(df_sorted)}")
    print()
    print(df_sorted)

    # Find best configuration for this environment size
    best_overall = df_sorted.iloc[0]
    print(f"\nBest configuration for {room_filter}:")
    print(f"  Architecture: {best_overall['architecture_type']}")
    print(f"  Network Size: {best_overall['network_size']}")
    print(f"  Max Memory: {best_overall['max_memory']}")
    print(f"  Forget Policy: {best_overall['forget_policy']}")
    print(f"  Remember Policy: {best_overall['remember_policy']}")
    print(f"  Separate Networks: {best_overall['separate_networks']}")
    print(f"  Test Score: {best_overall['test_mean']:.4f} ± {best_overall['test_std']:.4f}")
    print(f"  Val Score: {best_overall['val_mean']:.4f} ± {best_overall['val_std']:.4f}")

    # Export results
    print(f"\n=== EXPORTING FILES FOR {room_filter} ===")

    # Save JSON file
    json_filename = f"./data/results_{room_filter}_dqn.json"
    df_sorted.to_json(json_filename, orient="records", indent=2)
    print(f"Results for {room_filter} exported to {json_filename}")

    # Save Markdown file
    markdown_filename = f"./data/results_{room_filter}_dqn.md"
    markdown_content = f"# DQN Results for {room_filter}\n\n"
    markdown_content += f"Total configurations: {len(df_sorted)}\n\n"
    markdown_content += df_sorted.to_markdown(index=False, floatfmt=".0f")
    markdown_content += "\n"

    with open(markdown_filename, "w") as f:
        f.write(markdown_content)
    print(f"Markdown table for {room_filter} exported to {markdown_filename}")

print(f"\n{'='*100}")
print("ALL DQN PROCESSING COMPLETE")
print(f"{'='*100}")
