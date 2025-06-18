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
    num_iterations = 10000

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
        default_root_dir="training-results-dqn",
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
        ddqn=True,# Reinforcement Learning Teaching Series

A comprehensive educational series of Jupyter notebooks teaching reinforcement learning
algorithms from fundamentals to state-of-the-art. Each notebook demonstrates different
RL paradigms using the **CarRacing-v3 environment** for consistent comparison across all
algorithms.

## 📚 Notebook Series

### 1. REINFORCE (On-Policy Policy Gradients)

- **Focus**: Pure policy gradients, Monte Carlo returns
- **Action Space**: Discrete (5 actions)
- **Key Concepts**: Policy gradient theorem, REINFORCE algorithm, high variance

### 2. Vanilla DQN (Off-Policy Value-Based)

- **Focus**: Q-learning, Bellman equations, experience replay
- **Action Space**: Discrete (5 actions)
- **Key Concepts**: Q-function approximation, target networks, ε-greedy exploration

### 3. Vanilla Actor-Critic (Bridge Methods)

- **Focus**: Combining value and policy methods, on-policy vs off-policy
- **Action Space**: Both discrete AND continuous
- **Key Concepts**: V(s) vs Q(s,a), Bellman expectation vs optimality equations
- **Variants**:
  - On-policy discrete (V-function critic)
  - Off-policy continuous (Q-function critic)

### 4. Off-Policy Continuous Control Evolution

- **Focus**: Algorithm debugging, systematic improvements, and theoretical breakthroughs
- **Action Space**: Continuous (3D action space)

**Part A: DDPG - The Foundation (and its problems)**

- Basic off-policy actor-critic for continuous control
- Key issues: overestimation bias, instability, poor exploration

**Part B: TD3 - Systematic Debugging**

- **Key Concepts**: Twin critics, delayed updates, target policy smoothing
- **Educational Focus**: How to identify and fix specific RL problems
- **Meta-Skills**: Algorithm debugging methodology, ablation studies

**Part C: SAC - Theoretical Revolution**

- **Key Concepts**: Maximum entropy framework, automatic exploration tuning
- **Focus**: Principled approach to exploration and robustness

**Part D: Algorithm Comparison & Selection**

- When to use DDPG vs TD3 vs SAC
- Performance benchmarks and practical considerations

### 5. PPO (Modern On-Policy)

- **Focus**: Trust region concepts, clipped objectives
- **Action Space**: Both discrete AND continuous
- **Key Concepts**: Importance sampling, GAE, clipped surrogate objective
- **Variants**:
  - Discrete PPO (categorical policy)
  - Continuous PPO (Gaussian policy)

## 🎯 Learning Objectives

By completing this series, you will understand:

### Core RL Paradigms

- **Monte Carlo Methods**: REINFORCE with high variance, unbiased estimates
- **Temporal Difference Learning**: DQN, Actor-Critic with bootstrapping
- **On-Policy vs Off-Policy**: Data usage patterns and sample efficiency tradeoffs
- **Value-Based vs Policy-Based**: When to learn Q(s,a) vs π(a|s) directly

### Algorithm Development Skills

- **Systematic Debugging**: How to identify and fix specific RL problems (TD3 focus)
- **Algorithm Evolution**: Understanding how research progresses incrementally
- **Performance Analysis**: Comparing algorithms fairly across environments
- **Implementation Trade-offs**: Complexity vs performance vs stability

### Practical Implementation

- **Action Space Handling**: Discrete vs continuous action implementations
- **Network Architectures**: CNN feature extraction for visual inputs
- **Training Stability**: Target networks, experience replay, clipping techniques
- **Hyperparameter Sensitivity**: Understanding what matters most for each algorithm

## 🏎️ Environment: CarRacing-v3

**Why CarRacing-v3?**

- **Visual & Intuitive**: Everyone understands driving
- **Dual Action Spaces**: Supports both discrete (5 actions) and continuous (3D) control
- **Realistic Complexity**: 96x96 RGB input with meaningful spatial structure
- **Clear Objective**: Complete the racing track
- **Fast Feedback**: Immediate visual results for debugging

**Action Spaces:**

```python
# Discrete (5 actions): [do_nothing, steer_left, steer_right, gas, brake]
# Continuous (3D): [steering ∈ [-1,1], gas ∈ [0,1], brake ∈ [0,1]]
```

## 📈 Algorithm Coverage Matrix

| Algorithm    | Paradigm   | Data Usage    | Action Space | Key Innovation                |
| ------------ | ---------- | ------------- | ------------ | ----------------------------- |
| REINFORCE    | On-Policy  | Fresh Only    | Discrete     | Pure policy gradients         |
| DQN          | Off-Policy | Replay Buffer | Discrete     | Deep Q-learning               |
| Actor-Critic | Both       | Both          | Both         | Value + Policy combination    |
| DDPG         | Off-Policy | Replay Buffer | Continuous   | Continuous control foundation |
| TD3          | Off-Policy | Replay Buffer | Continuous   | Systematic debugging          |
| SAC          | Off-Policy | Replay Buffer | Continuous   | Maximum entropy               |
| PPO          | On-Policy  | Fresh Only    | Both         | Stable policy updates         |

## 🛠️ Technical Implementation

### Shared Architecture Components

- **CNN Backbone**: Consistent feature extraction across algorithms
- **Preprocessing**: Frame stacking, action repeat, reward shaping
- **Visualization**: Training curves, action analysis, performance videos
- **Evaluation**: Standardized metrics and comparison framework

### Progressive Complexity

1. **Simple**: REINFORCE (basic policy network)
2. **Moderate**: DQN (Q-network + target network)
3. **Complex**: Actor-Critic (dual networks, multiple variants)
4. **Advanced**: DDPG/TD3/SAC (twin critics, target smoothing, entropy tuning)
5. **Mature**: PPO (GAE, clipping, robust implementation)

## 🎓 Educational Philosophy

### Learning Approach

- **Concepts First**: Intuitive explanations before mathematical details
- **Visual Learning**: Extensive plots, diagrams, and training visualizations
- **Hands-on Practice**: Interactive hyperparameter exploration
- **Comparative Analysis**: Side-by-side algorithm performance
- **Real Understanding**: Show both successes and failure modes

### Skill Development

- **Algorithm Intuition**: Why each method works and when it fails
- **Implementation Skills**: Clean, readable, and efficient code
- **Debugging Mindset**: How to diagnose and fix training issues
- **Research Thinking**: How algorithms evolve and improve over time

## 🚀 Getting Started

### Prerequisites

- Basic knowledge of neural networks and PyTorch
- Understanding of Markov Decision Processes (MDPs)
- Familiarity with gradient descent optimization

### Installation

```bash
pip install gymnasium[box2d] torch torchvision matplotlib numpy
```

### Recommended Learning Path

1. Start with **REINFORCE** for policy gradient intuition
2. Learn **DQN** for value-based methods and off-policy learning
3. Master **Actor-Critic** to understand the core paradigm bridges ⭐
4. Study **TD3 evolution** for algorithm development methodology 🔧
5. Complete with **PPO** for modern on-policy best practices

---

_This teaching series emphasizes deep understanding over breadth, focusing on the
fundamental paradigms that underlie all modern RL algorithms. Each section is designed
to build your intuition, technical skills, and appreciation for the elegance and
complexity of reinforcement learning._

        pretrain_semantic=False,
        use_gradient_clipping=False,
        gradient_clip_value=1.0,
    )
    agent.train()


if __name__ == "__main__":
    test_seeds = [0, 1, 2, 3, 4]
    gcn_types = ["stare"]
    max_memories = [16, 32]
    policy_combinations = [("lru", "rl"), ("rl", "all"), ("rl", "rl")]
    # policy_combinations = [("rl", "all")]

    all_combinations = list(
        itertools.product(test_seeds, gcn_types, max_memories, policy_combinations)
    )

    # Flatten the policy combinations
    all_combinations = [
        (seed, gcn_type, memory, forget_policy, remember_policy)
        for seed, gcn_type, memory, (forget_policy, remember_policy) in all_combinations
    ]

    random.shuffle(all_combinations)

    num_processes = multiprocessing.cpu_count()  # or choose a fixed number
    num_processes = 5
    with multiprocessing.Pool(num_processes) as pool:
        pool.map(run_dqn_experiment, all_combinations)
