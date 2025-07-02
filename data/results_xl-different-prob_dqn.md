# DQN Results for xl-different-prob

Total configurations: 5
Memory sizes: [16, 32]

## Overall Results (All Memory Sizes)

| architecture_type   |   max_memory | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|-------------:|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| gcn                 |           32 | rl              | all               | rl          | rl               | False               | small          |         527 |          0 |        521 |         0 |         1 |
| gcn                 |           32 | rl              | all               | rl          | rl               | True                | big            |         501 |          0 |        543 |         0 |         1 |
| transformer         |           32 | rl              | all               | rl          | rl               | False               | small          |         386 |          0 |        516 |         0 |         1 |
| transformer         |           16 | rl              | all               | rl          | rl               | True                | big            |         350 |          0 |        435 |         0 |         1 |
| stare               |           16 | rl              | all               | rl          | rl               | True                | big            |         348 |          0 |        335 |         0 |         1 |

## Memory Size 16

Total configurations: 2

| architecture_type   | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| transformer         | rl              | all               | rl          | rl               | True                | big            |         350 |          0 |        435 |         0 |         1 |
| stare               | rl              | all               | rl          | rl               | True                | big            |         348 |          0 |        335 |         0 |         1 |

## Memory Size 32

Total configurations: 3

| architecture_type   | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| gcn                 | rl              | all               | rl          | rl               | False               | small          |         527 |          0 |        521 |         0 |         1 |
| gcn                 | rl              | all               | rl          | rl               | True                | big            |         501 |          0 |        543 |         0 |         1 |
| transformer         | rl              | all               | rl          | rl               | False               | small          |         386 |          0 |        516 |         0 |         1 |

