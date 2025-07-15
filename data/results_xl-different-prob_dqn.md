# DQN Results for xl-different-prob

Total configurations: 4
Memory sizes: [32, 64]

## Overall Results (All Memory Sizes)

| architecture_type   |   max_memory | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|-------------:|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| stare               |           64 | rl              | all               | rl          | rl               | False               | big            |         564 |          0 |        625 |         0 |         1 |
| stare               |           64 | rl              | all               | rl          | rl               | False               | small          |         547 |          0 |        631 |         0 |         1 |
| stare               |           32 | rl              | all               | rl          | rl               | False               | big            |         497 |         34 |        544 |         3 |         2 |
| stare               |           32 | rl              | all               | rl          | rl               | False               | small          |         485 |         44 |        553 |        22 |         2 |

## Memory Size 32

Total configurations: 2

| architecture_type   | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| stare               | rl              | all               | rl          | rl               | False               | big            |         497 |         34 |        544 |         3 |         2 |
| stare               | rl              | all               | rl          | rl               | False               | small          |         485 |         44 |        553 |        22 |         2 |

## Memory Size 64

Total configurations: 2

| architecture_type   | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| stare               | rl              | all               | rl          | rl               | False               | big            |         564 |          0 |        625 |         0 |         1 |
| stare               | rl              | all               | rl          | rl               | False               | small          |         547 |          0 |        631 |         0 |         1 |

