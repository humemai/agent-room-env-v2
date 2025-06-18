import sys
import os
import yaml
from glob import glob
from tqdm.auto import tqdm
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json

# Create directories if they don't exist
os.makedirs("./data", exist_ok=True)
os.makedirs("./figures", exist_ok=True)


# Collect results grouped by config (excluding seed)
results_by_config = defaultdict(list)

for path in tqdm(glob("./training-results-symbolic/*/results.yaml")):
    with open(path, "r") as f:
        results = yaml.safe_load(f)

    test_mean = results["test_score"]["mean"]

    with open(path.replace("results.yaml", "train.yaml")) as f:
        hp = yaml.safe_load(f)

    room_size = hp["env_config"]["room_size"]
    qa_policy = hp["qa_policy"]
    explore_policy = hp["explore_policy"]
    forget_policy = hp.get("forget_policy", None)
    remember_policy = hp.get("remember_policy", "all")
    memory_size = hp.get("max_long_term_memory_size", None)

    config_key = (
        room_size,
        qa_policy,
        explore_policy,
        forget_policy,
        remember_policy,
        memory_size,
    )
    results_by_config[config_key].append(test_mean)

# Build a DataFrame from the aggregated results
records = []
for config, scores in sorted(results_by_config.items()):
    (
        room_size,
        qa_policy,
        explore_policy,
        forget_policy,
        remember_policy,
        memory_size,
    ) = config
    records.append(
        {
            "room_size": room_size,
            "mean_score": np.mean(scores),
            "std_score": np.std(scores),
            "qa_policy": qa_policy,
            "explore_policy": explore_policy,
            "forget_policy": forget_policy,
            "remember_policy": remember_policy,
            "memory_size": memory_size,
            "n_seeds": len(scores),
        }
    )

df = pd.DataFrame(records)
pd.set_option("display.precision", 4)

# Define all room sizes to process
room_sizes = [
    "s-different-prob",
    "m-different-prob",
    "l-different-prob",
    "xl-different-prob",
    "xxl-different-prob",
]

# Process each room size
for room_filter in room_sizes:
    print(f"\n{'='*100}")
    print(f"PROCESSING ROOM SIZE: {room_filter}")
    print(f"{'='*100}")

    # Filter for the specific room size
    df_filtered = df[df["room_size"] == room_filter].drop(columns="room_size")

    if df_filtered.empty:
        print(f"No data found for room size: {room_filter}")
        continue

    # Create separate DataFrames for each memory size
    memory_sizes = sorted(df_filtered["memory_size"].unique())
    dataframes_by_memory = {}

    print(f"Creating {len(memory_sizes)} DataFrames for memory sizes: {memory_sizes}")
    print("=" * 80)

    for memory_size in memory_sizes:
        # Filter data for this specific memory size
        memory_df = df_filtered[df_filtered["memory_size"] == memory_size].drop(
            columns="memory_size"
        )
        # Sort by mean_score in descending order
        memory_df = memory_df.sort_values(by="mean_score", ascending=False).reset_index(
            drop=True
        )

        # Store in dictionary
        dataframes_by_memory[memory_size] = memory_df

        # Display the DataFrame
        print(f"\n=== DataFrame for Memory Size: {memory_size} ===")
        print()
        print(memory_df)
        print("-" * 80)

    # Summary statistics
    print(f"\n=== SUMMARY FOR {room_filter} ===")
    print(f"Total number of memory sizes: {len(memory_sizes)}")
    print(f"Memory sizes analyzed: {memory_sizes}")

    # Find best configuration across all memory sizes for this room
    best_overall = df_filtered.loc[df_filtered["mean_score"].idxmax()]
    print(f"\nBest overall configuration for {room_filter}:")
    print(f"  Memory Size: {best_overall['memory_size']}")
    print(f"  QA Policy: {best_overall['qa_policy']}")
    print(f"  Explore Policy: {best_overall['explore_policy']}")
    print(f"  MM Forget Policy: {best_overall['forget_policy']}")
    print(f"  MM Remember Policy: {best_overall['remember_policy']}")
    print(
        f"  Score: {best_overall['mean_score']:.4f} ± {best_overall['std_score']:.4f}"
    )

    # Export each room size DataFrame to separate files
    print(f"\n=== EXPORTING FILES FOR {room_filter} ===")

    # Export global results (all data for the room size, sorted by mean_score)
    global_section = df_filtered.sort_values(
        by="mean_score", ascending=False
    ).reset_index(drop=True)

    # Save JSON file
    global_filename = f"./data/results_{room_filter}.json"
    global_section.to_json(global_filename, orient="records", indent=2)
    print(f"Global results for {room_filter} exported to {global_filename}")

    # Save single Markdown file with multiple tables for each memory size
    markdown_filename = f"./data/results_{room_filter}.md"
    markdown_content = f"# Results for {room_filter}\n\n"
    markdown_content += f"Total configurations: {len(global_section)}\n"
    markdown_content += f"Memory sizes: {memory_sizes}\n\n"
    
    # Add overall table
    markdown_content += "## Overall Results (All Memory Sizes)\n\n"
    markdown_content += global_section.to_markdown(index=False, floatfmt=".4f")
    markdown_content += "\n\n"
    
    # Add separate table for each memory size
    for memory_size in memory_sizes:
        memory_df = df_filtered[df_filtered["memory_size"] == memory_size].drop(
            columns="memory_size"
        )
        memory_df = memory_df.sort_values(by="mean_score", ascending=False).reset_index(
            drop=True
        )
        
        markdown_content += f"## Memory Size {memory_size}\n\n"
        markdown_content += f"Total configurations: {len(memory_df)}\n\n"
        markdown_content += memory_df.to_markdown(index=False, floatfmt=".4f")
        markdown_content += "\n\n"

    with open(markdown_filename, "w") as f:
        f.write(markdown_content)
    print(f"Markdown table for {room_filter} exported to {markdown_filename}")

# === PLOTTING CONFIGURATION ===
include_shading = True  # Toggle shading for std deviation
log_xaxis = True
log_yaxis = False
line_width = 2.5

qa_policies = [
    "most_recently_added",
    "most_recently_used",
    "most_frequently_used",
]
explore_policies = ["dijkstra", "bfs", "random"]
mm_policies = ["lfu", "lru", "fifo", "random"]

# Generate plots for all room sizes
print(f"\n{'='*100}")
print("GENERATING PLOTS FOR ALL ROOM SIZES")
print(f"{'='*100}")

for room_size_to_plot in room_sizes:
    print(f"\nGenerating plot for {room_size_to_plot}...")

    file_path = f"./data/results_{room_size_to_plot}.json"

    # Load and prepare data
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}, skipping...")
        continue

    df_plot = pd.DataFrame(data)
    df_plot = df_plot.sort_values(
        by=["qa_policy", "explore_policy", "forget_policy", "memory_size"]
    )

    # Create 3×3 subplot grid (3 QA policies × 3 exploration policies)
    fig, axes = plt.subplots(3, 3, figsize=(24, 24), sharex=True, sharey=True)

    for i, qa_policy in enumerate(qa_policies):
        for j, explore_policy in enumerate(explore_policies):
            ax = axes[i, j]
            for forget_policy in mm_policies:
                sub_df = df_plot[
                    (df_plot["qa_policy"] == qa_policy)
                    & (df_plot["explore_policy"] == explore_policy)
                    & (df_plot["forget_policy"] == forget_policy)
                ]
                if len(sub_df) > 0:  # Check if data exists for this combination
                    x = sub_df["memory_size"]
                    y = sub_df["mean_score"]
                    yerr = sub_df["std_score"]

                    ax.plot(x, y, label=forget_policy.upper(), linewidth=line_width)
                    if include_shading:
                        ax.fill_between(x, y - yerr, y + yerr, alpha=0.2)

            # Format only the first row and the first column for titles
            if i == 0:
                ax.set_title(f"{explore_policy.upper()} exploration", fontsize=18)
            if j == 0:
                ax.text(
                    -0.2,
                    0.5,
                    f"QA: {qa_policy.replace('_', ' ').title()}",
                    rotation=90,
                    transform=ax.transAxes,
                    fontsize=18,
                    verticalalignment="center",
                )

            # Add legend to each subplot
            ax.legend(
                title="Forget Policy",
                fontsize=14,
                title_fontsize=14,
                loc="best",
            )
            ax.grid(True, which="both", linestyle="--", linewidth=0.5)
            ax.tick_params(axis="both", which="major", labelsize=14)

            if log_xaxis:
                ax.set_xscale("log")
                ax.set_xticks([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
                ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())

            if log_yaxis:
                ax.set_yscale("log")
                ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0, subs=None))
                ax.yaxis.set_minor_locator(ticker.NullLocator())
                ax.yaxis.set_major_formatter(ticker.ScalarFormatter())

    # Shared axis labels
    fig.text(
        0.5,
        0.01,
        "Long-Term Memory Capacity" + (" (log scale)" if log_xaxis else ""),
        ha="center",
        fontsize=20,
    )
    fig.text(
        0.01,
        0.5,
        "Mean Test Score" + (" (log scale)" if log_yaxis else ""),
        va="center",
        rotation="vertical",
        fontsize=20,
    )
    fig.suptitle(
        f"Mean Test Score vs. Long-Term Memory Capacity ({room_size_to_plot})",
        fontsize=24,
        y=0.99,
    )

    plt.tight_layout(rect=[0.03, 0.03, 0.98, 0.98])

    # Save plots
    pdf_path = f"./figures/agent_test_performance_{room_size_to_plot}.pdf"
    png_path = f"./figures/agent_test_performance_{room_size_to_plot}.png"

    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight")
    plt.close()  # Close the figure to free memory

    print(f"Plot saved: {pdf_path}")
    print(f"Plot saved: {png_path}")

print(f"\n{'='*100}")
print("ALL PROCESSING COMPLETE")
print(f"{'='*100}")
