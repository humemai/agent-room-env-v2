# Agent for RoomEnv-v2

- This directory contains an agent with a GNN-CB that interacts with the [RoomEnv-v2](https://github.com/humemai/room-env)

## Prerequisites

1. A unix or unix-like x86 machine
1. python 3.10 or higher.
1. Running in a virtual environment (e.g., conda, virtualenv, etc.) is highly
   recommended so that you don't mess up with the system python.
1. Install the requirements by running `pip install -r requirements.txt`

## Jupyter Notebooks

- [Training our agent (and their hyperparameters)](train-dqn.ipynb)
- [Running trained models](run-trained-models.ipynb)

## Results

| Capacity | Agent Type       | Test Score (±σ) |
| -------- | ---------------- | --------------- |
| 12       | QA-CB-Bandit     | **216 (±5)**    |
|          | **QA-LLM**       | **262 (±8)**    |
|          | HumemAI-Unified  | 152 (±7)        |
|          | HumemAI          | 160 (±30)       |
|          | Baseline         | 144 (±14)       |
| 24       | **QA-CB-Bandit** | **396 (±23)**   |
|          | QA-LLM           | 318 (±18)       |
|          | HumemAI-Unified  | 233 (±34)       |
|          | HumemAI          | 214 (±64)       |
|          | Baseline         | 138 (±52)       |
| 48       | **QA-CB-Bandit** | **488 (±15)**   |
|          | QA-LLM           | 340 (±22)       |
|          | HumemAI-Unified  | 341 (±21)       |
|          | HumemAI          | 235 (±37)       |
|          | Baseline         | 200 (±15)       |
| 96       | **QA-CB-Bandit** | **554 (±20)**   |
|          | QA-LLM           | 419 (±16)       |
|          | HumemAI-Unified  | 466 (±37)       |
|          | HumemAI          | 209 (±87)       |
|          | Baseline         | 155 (±77)       |
| 192      | **QA-CB-Bandit** | **512 (±19)**   |
|          | QA-LLM           | 306 (±31)       |
|          | HumemAI-Unified  | 482 (±14)       |
|          | HumemAI          | 176 (±115)      |
|          | Baseline         | 144 (±68)       |
