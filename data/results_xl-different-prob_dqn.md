# DQN Results for xl-different-prob

Total configurations: 3

| architecture_type   |   max_memory | forget_policy   | remember_policy   | qa_policy          | explore_policy   | separate_networks   | network_size   |   test_mean |   test_std |   val_mean |   val_std |   n_seeds |
|:--------------------|-------------:|:----------------|:------------------|:-------------------|:-----------------|:--------------------|:---------------|------------:|-----------:|-----------:|----------:|----------:|
| gcn                 |            4 | lru             | all               | most_recently_used | bfs              | False               | small          |           0 |          0 |          1 |         0 |         1 |
| stare               |            4 | lru             | all               | most_recently_used | bfs              | False               | small          |           0 |          0 |          1 |         0 |         1 |
| transformer         |            4 | lru             | all               | most_recently_used | bfs              | False               | small          |           0 |          0 |          1 |         0 |         1 |
