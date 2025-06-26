# DQN Results for xl-different-prob

Total configurations: 14

| architecture_type   |   max_memory | forget_policy   | remember_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|-------------:|:----------------|:------------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| stare               |           32 | lru             | rl                | False               | small          |         523 |          0 |        649 |         0 |         1 |
| gcn                 |           32 | rl              | rl                | False               | big            |         517 |          0 |        639 |         0 |         1 |
| stare               |           32 | rl              | rl                | True                | big            |         500 |          0 |        602 |         0 |         1 |
| gcn                 |           32 | rl              | rl                | False               | small          |         495 |          0 |        486 |         0 |         1 |
| gcn                 |           32 | lru             | rl                | False               | small          |         484 |          0 |        604 |         0 |         1 |
| transformer         |           32 | rl              | rl                | False               | small          |         471 |          0 |        586 |         0 |         1 |
| stare               |           32 | rl              | all               | False               | big            |         452 |          0 |        638 |         0 |         1 |
| gcn                 |           32 | rl              | all               | False               | big            |         452 |          0 |        661 |         0 |         1 |
| stare               |           32 | rl              | all               | False               | small          |         452 |          0 |        639 |         0 |         1 |
| transformer         |           32 | lru             | rl                | False               | big            |         441 |          0 |        580 |         0 |         1 |
| gcn                 |           32 | rl              | rl                | True                | big            |         237 |          0 |        313 |         0 |         1 |
| stare               |           32 | rl              | rl                | False               | big            |         201 |          0 |        404 |         0 |         1 |
| stare               |           32 | rl              | rl                | True                | small          |         162 |          0 |        248 |         0 |         1 |
| stare               |           32 | rl              | rl                | False               | small          |         140 |          0 |        338 |         0 |         1 |
