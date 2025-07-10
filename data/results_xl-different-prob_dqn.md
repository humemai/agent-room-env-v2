# DQN Results for xl-different-prob

Total configurations: 18
Memory sizes: [16, 32]

## Overall Results (All Memory Sizes)

| architecture_type   |   max_memory | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|-------------:|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| transformer         |           32 | rl              | all               | rl          | rl               | False               | big            |         516 |          0 |        559 |         0 |         1 |
| transformer         |           32 | rl              | all               | rl          | rl               | True                | small          |         493 |          0 |        548 |         0 |         1 |
| stare               |           32 | rl              | all               | rl          | rl               | False               | big            |         490 |         16 |        519 |        13 |         2 |
| stare               |           32 | rl              | all               | rl          | rl               | False               | small          |         489 |         15 |        533 |        21 |         3 |
| gcn                 |           32 | rl              | all               | rl          | rl               | False               | small          |         486 |         40 |        529 |         8 |         2 |
| gcn                 |           32 | rl              | all               | rl          | rl               | False               | big            |         476 |         33 |        524 |        17 |         2 |
| gcn                 |           32 | rl              | all               | rl          | rl               | True                | big            |         472 |         24 |        509 |        35 |         3 |
| stare               |           32 | rl              | all               | rl          | rl               | True                | big            |         413 |          0 |        541 |         0 |         1 |
| gcn                 |           32 | rl              | all               | rl          | rl               | True                | small          |         391 |          0 |        497 |         0 |         1 |
| transformer         |           32 | rl              | all               | rl          | rl               | False               | small          |         386 |          0 |        516 |         0 |         1 |
| transformer         |           16 | rl              | all               | rl          | rl               | False               | big            |         380 |          0 |        409 |         0 |         1 |
| stare               |           16 | rl              | all               | rl          | rl               | True                | big            |         362 |         14 |        374 |        39 |         2 |
| gcn                 |           16 | rl              | all               | rl          | rl               | False               | big            |         358 |          0 |        428 |         0 |         1 |
| transformer         |           16 | rl              | all               | rl          | rl               | True                | big            |         350 |          0 |        435 |         0 |         1 |
| stare               |           16 | rl              | all               | rl          | rl               | False               | small          |         339 |          0 |        417 |         0 |         1 |
| transformer         |           16 | rl              | all               | rl          | rl               | True                | small          |         322 |          0 |        425 |         0 |         1 |
| gcn                 |           16 | rl              | all               | rl          | rl               | True                | big            |         282 |          0 |        379 |         0 |         1 |
| gcn                 |           16 | rl              | all               | rl          | rl               | True                | small          |         278 |          0 |        304 |         0 |         1 |

## Memory Size 16

Total configurations: 8

| architecture_type   | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| transformer         | rl              | all               | rl          | rl               | False               | big            |         380 |          0 |        409 |         0 |         1 |
| stare               | rl              | all               | rl          | rl               | True                | big            |         362 |         14 |        374 |        39 |         2 |
| gcn                 | rl              | all               | rl          | rl               | False               | big            |         358 |          0 |        428 |         0 |         1 |
| transformer         | rl              | all               | rl          | rl               | True                | big            |         350 |          0 |        435 |         0 |         1 |
| stare               | rl              | all               | rl          | rl               | False               | small          |         339 |          0 |        417 |         0 |         1 |
| transformer         | rl              | all               | rl          | rl               | True                | small          |         322 |          0 |        425 |         0 |         1 |
| gcn                 | rl              | all               | rl          | rl               | True                | big            |         282 |          0 |        379 |         0 |         1 |
| gcn                 | rl              | all               | rl          | rl               | True                | small          |         278 |          0 |        304 |         0 |         1 |

## Memory Size 32

Total configurations: 10

| architecture_type   | forget_policy   | remember_policy   | qa_policy   | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|:----------------|:------------------|:------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| transformer         | rl              | all               | rl          | rl               | False               | big            |         516 |          0 |        559 |         0 |         1 |
| transformer         | rl              | all               | rl          | rl               | True                | small          |         493 |          0 |        548 |         0 |         1 |
| stare               | rl              | all               | rl          | rl               | False               | big            |         490 |         16 |        519 |        13 |         2 |
| stare               | rl              | all               | rl          | rl               | False               | small          |         489 |         15 |        533 |        21 |         3 |
| gcn                 | rl              | all               | rl          | rl               | False               | small          |         486 |         40 |        529 |         8 |         2 |
| gcn                 | rl              | all               | rl          | rl               | False               | big            |         476 |         33 |        524 |        17 |         2 |
| gcn                 | rl              | all               | rl          | rl               | True                | big            |         472 |         24 |        509 |        35 |         3 |
| stare               | rl              | all               | rl          | rl               | True                | big            |         413 |          0 |        541 |         0 |         1 |
| gcn                 | rl              | all               | rl          | rl               | True                | small          |         391 |          0 |        497 |         0 |         1 |
| transformer         | rl              | all               | rl          | rl               | False               | small          |         386 |          0 |        516 |         0 |         1 |

