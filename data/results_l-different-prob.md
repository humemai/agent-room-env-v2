# Results for l-different-prob

Total configurations: 297
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|         754 |         83 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|         745 |         57 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|         742 |         60 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|         742 |         60 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|         742 |         60 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|         741 |         40 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|         739 |         53 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|         736 |         56 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|         736 |         51 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|         733 |         58 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|         732 |         54 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|         731 |         50 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|         730 |         50 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|         730 |         50 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|         730 |         50 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|         728 |         56 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|         728 |         45 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|         726 |         51 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|         726 |         49 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|         723 |         64 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|         722 |         35 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|         720 |         62 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|         719 |         68 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|         719 |         41 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|         717 |         67 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|         714 |         57 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|         711 |         65 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|         711 |         65 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|         711 |         65 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|         711 |         52 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|         707 |         58 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|         707 |         50 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|         705 |         64 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|         705 |         39 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|         704 |         57 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|         704 |         63 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|         702 |         63 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|         701 |         62 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|         701 |         57 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|         701 |         62 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|         701 |         62 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|         700 |         58 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|         698 |         41 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|         697 |         53 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|         696 |         50 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|         696 |         62 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|         696 |         60 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|         694 |         39 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|         691 |         59 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|         689 |         49 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|         688 |         30 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|         687 |         59 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|         687 |         56 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|         678 |        104 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|         673 |         54 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|         673 |         57 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|         668 |         61 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|         668 |         76 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|         666 |         43 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|         663 |         52 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|         655 |         76 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|         654 |         60 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|         654 |         74 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|         652 |         72 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|         647 |         47 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|         643 |         69 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|         643 |         54 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|         641 |         40 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|         638 |         51 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|         637 |         77 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|         634 |         32 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|         632 |         29 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|         631 |         35 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|         631 |         29 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|         631 |         28 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|         630 |         29 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|         630 |         32 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|         630 |         32 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|         630 |         32 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|         630 |         32 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|         630 |         32 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|         630 |         32 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|         630 |         30 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|         627 |         90 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|         625 |         43 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|         622 |         31 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|         620 |         36 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|         616 |         60 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|         605 |         93 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|         600 |         50 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|         598 |         21 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|         597 |         41 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|         590 |        132 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|         590 |         28 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|         579 |         31 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|         570 |        111 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|         567 |        125 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|         532 |         58 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|         532 |         61 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|         530 |         85 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|         522 |         36 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|         522 |         61 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|         510 |         39 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|         510 |         80 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|         509 |         68 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|         503 |         37 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|         496 |         83 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|         494 |         52 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|         493 |         52 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|         484 |         43 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|         483 |         57 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|         475 |         40 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|         462 |         65 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|         459 |         40 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|         452 |         67 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|         434 |         17 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|         429 |         28 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|         427 |         69 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|         427 |        105 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|         427 |         69 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|         420 |        128 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|         412 |        134 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|         410 |         52 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|         407 |         81 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|         403 |         65 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|         400 |        128 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|         399 |         79 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|         398 |         69 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|         396 |         45 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|         392 |        141 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|         392 |        141 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|         392 |        141 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|         392 |         82 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|         391 |         83 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|         391 |         83 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|         389 |        134 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|         389 |        134 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|         389 |         89 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|         389 |         89 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|         389 |         53 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|         389 |         89 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|         388 |        131 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|         381 |         54 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|         381 |         78 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|         379 |         91 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|         372 |         87 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|         370 |        118 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|         368 |        133 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|         368 |        134 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|         363 |         57 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|         358 |         65 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|         356 |         67 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|         354 |         70 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|         353 |         74 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|         353 |         74 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|         353 |         74 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|         353 |         61 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|         352 |        112 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|         348 |        110 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|         348 |         60 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|         343 |         91 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|         341 |         71 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|         339 |         37 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|         339 |         37 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|         338 |         98 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|         336 |         88 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|         334 |        102 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|         324 |         55 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|         323 |         52 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|         320 |         74 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|         315 |          8 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|         306 |         45 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|         305 |         70 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|         300 |         12 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|         300 |         12 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|         299 |         78 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|         299 |         19 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|         299 |         19 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|         298 |         82 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|         293 |         96 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|         288 |         16 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|         288 |         27 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|         286 |         64 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|         285 |         42 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|         280 |         68 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|         280 |         50 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|         280 |         85 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|         276 |         22 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|         267 |         46 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|         266 |         74 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|         244 |         62 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|         241 |         59 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|         239 |         58 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|         237 |         49 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|         234 |        114 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|         231 |         54 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|         225 |         31 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|         222 |         22 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|         207 |         21 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|         207 |         20 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|         206 |         33 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|         205 |         14 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|         204 |         14 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|         203 |         11 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|         202 |         41 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|         198 |         17 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|         196 |         96 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|         193 |         57 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|         188 |         82 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|         182 |         58 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|         182 |         86 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|         182 |         61 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|         182 |         61 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|         180 |         68 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|         161 |         40 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|         161 |         40 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|         160 |         29 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|         154 |         35 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|         154 |         35 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|         154 |         35 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|         152 |         55 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|         146 |         30 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|         145 |         40 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|         141 |         14 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|         140 |         25 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|         139 |         18 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|         139 |         14 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|         139 |         26 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|         138 |         14 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|         138 |         53 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|         137 |         30 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|         137 |         30 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|         135 |         22 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|         133 |         24 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|         133 |         24 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|         131 |         40 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|         129 |         56 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|         127 |         39 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|         123 |         24 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|         122 |         41 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|         122 |         41 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|         115 |         22 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|         113 |         26 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|         113 |         35 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|         113 |         35 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|         105 |         20 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|         105 |         20 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|         105 |         26 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|         100 |         13 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|          98 |         11 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|          97 |         16 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|          97 |         16 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|          96 |         15 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|          96 |         15 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|          92 |         42 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|          92 |         42 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|          87 |         14 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|          86 |         24 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|          86 |         25 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|          85 |         33 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|          85 |         37 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|          84 |         22 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|          83 |         37 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|          83 |         37 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|          81 |         36 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|          75 |         18 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|          75 |         18 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|          75 |         18 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|          75 |         18 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|          75 |         18 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|          75 |         18 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|          75 |         18 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|          75 |         18 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|          75 |         18 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|          75 |         18 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|          75 |         18 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|          75 |         18 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|          72 |         20 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|          72 |         20 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|          72 |         20 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|          70 |         16 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|          70 |         16 | most_recently_added  | random           | lru             | all               |             0 |         5 |
|          70 |         16 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|          70 |         16 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|          70 |         16 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|          70 |         16 | most_frequently_used | random           | lfu             | all               |             0 |         5 |
|          70 |         28 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|          70 |         28 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|          56 |         23 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|          56 |         23 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|          56 |         23 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|          56 |         23 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|          56 |         23 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|          56 |         23 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|          55 |         19 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|          55 |         19 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|          55 |         19 | most_recently_added  | random           | fifo            | all               |             0 |         5 |

## Memory Size 0

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          75 |         18 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          75 |         18 | most_frequently_used | bfs              | lru             | all               |         5 |
|          75 |         18 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          75 |         18 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          75 |         18 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          75 |         18 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          75 |         18 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          75 |         18 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          75 |         18 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          75 |         18 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          75 |         18 | most_recently_added  | bfs              | lru             | all               |         5 |
|          75 |         18 | most_recently_used   | bfs              | lru             | all               |         5 |
|          70 |         16 | most_recently_used   | random           | lfu             | all               |         5 |
|          70 |         16 | most_recently_used   | random           | lru             | all               |         5 |
|          70 |         16 | most_recently_added  | random           | lfu             | all               |         5 |
|          70 |         16 | most_frequently_used | random           | lfu             | all               |         5 |
|          70 |         16 | most_frequently_used | random           | lru             | all               |         5 |
|          70 |         16 | most_recently_added  | random           | lru             | all               |         5 |
|          56 |         23 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          56 |         23 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          56 |         23 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          56 |         23 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          56 |         23 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          56 |         23 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          55 |         19 | most_frequently_used | random           | fifo            | all               |         5 |
|          55 |         19 | most_recently_added  | random           | fifo            | all               |         5 |
|          55 |         19 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 2

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         222 |         22 | most_recently_added  | random           | lfu             | all               |         5 |
|         182 |         61 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         182 |         61 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         180 |         68 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         154 |         35 | most_recently_used   | random           | lfu             | all               |         5 |
|         154 |         35 | most_frequently_used | random           | lfu             | all               |         5 |
|         138 |         53 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         129 |         56 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         122 |         41 | most_frequently_used | random           | lru             | all               |         5 |
|         122 |         41 | most_recently_used   | random           | lru             | all               |         5 |
|         113 |         26 | most_recently_added  | bfs              | lru             | all               |         5 |
|         113 |         35 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         113 |         35 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         105 |         20 | most_frequently_used | bfs              | lru             | all               |         5 |
|         105 |         20 | most_recently_used   | bfs              | lru             | all               |         5 |
|         105 |         26 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         100 |         13 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          98 |         11 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          96 |         15 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          96 |         15 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          92 |         42 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          92 |         42 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          86 |         24 | most_recently_added  | random           | lru             | all               |         5 |
|          81 |         36 | most_recently_added  | random           | fifo            | all               |         5 |
|          72 |         20 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          70 |         28 | most_frequently_used | random           | fifo            | all               |         5 |
|          70 |         28 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 4

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         305 |         70 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         299 |         78 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         280 |         85 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         244 |         62 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         239 |         58 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         237 |         49 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         234 |        114 | most_frequently_used | random           | lfu             | all               |         5 |
|         188 |         82 | most_recently_used   | random           | lfu             | all               |         5 |
|         182 |         86 | most_recently_added  | random           | lfu             | all               |         5 |
|         161 |         40 | most_recently_used   | bfs              | lru             | all               |         5 |
|         161 |         40 | most_frequently_used | bfs              | lru             | all               |         5 |
|         154 |         35 | most_recently_added  | bfs              | lru             | all               |         5 |
|         137 |         30 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         137 |         30 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         133 |         24 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         133 |         24 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         123 |         24 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         115 |         22 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          97 |         16 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          97 |         16 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          87 |         14 | most_recently_added  | random           | fifo            | all               |         5 |
|          85 |         33 | most_recently_added  | random           | lru             | all               |         5 |
|          84 |         22 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          83 |         37 | most_recently_used   | random           | fifo            | all               |         5 |
|          83 |         37 | most_frequently_used | random           | fifo            | all               |         5 |
|          72 |         20 | most_frequently_used | random           | lru             | all               |         5 |
|          72 |         20 | most_recently_used   | random           | lru             | all               |         5 |

## Memory Size 8

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         462 |         65 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         434 |         17 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         410 |         52 | most_recently_used   | random           | lfu             | all               |         5 |
|         381 |         78 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         379 |         91 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         372 |         87 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         363 |         57 | most_frequently_used | random           | lfu             | all               |         5 |
|         353 |         61 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         315 |          8 | most_recently_added  | bfs              | lru             | all               |         5 |
|         306 |         45 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         288 |         16 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         288 |         27 | most_recently_used   | bfs              | lru             | all               |         5 |
|         285 |         42 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         276 |         22 | most_frequently_used | bfs              | lru             | all               |         5 |
|         266 |         74 | most_recently_added  | random           | lfu             | all               |         5 |
|         241 |         59 | most_recently_added  | random           | lru             | all               |         5 |
|         206 |         33 | most_frequently_used | random           | lru             | all               |         5 |
|         202 |         41 | most_recently_used   | random           | lru             | all               |         5 |
|         146 |         30 | most_frequently_used | random           | fifo            | all               |         5 |
|         141 |         14 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         140 |         25 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         139 |         18 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         139 |         14 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         139 |         26 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         138 |         14 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          86 |         25 | most_recently_used   | random           | fifo            | all               |         5 |
|          85 |         37 | most_recently_added  | random           | fifo            | all               |         5 |

## Memory Size 16

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         570 |        111 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         532 |         58 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         532 |         61 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         530 |         85 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         522 |         61 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         522 |         36 | most_recently_added  | bfs              | lru             | all               |         5 |
|         510 |         80 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         496 |         83 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         494 |         52 | most_frequently_used | bfs              | lru             | all               |         5 |
|         493 |         52 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         483 |         57 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         459 |         40 | most_recently_used   | bfs              | lru             | all               |         5 |
|         368 |        134 | most_recently_added  | random           | lfu             | all               |         5 |
|         352 |        112 | most_recently_used   | random           | lfu             | all               |         5 |
|         298 |         82 | most_recently_added  | random           | lru             | all               |         5 |
|         280 |         68 | most_frequently_used | random           | lru             | all               |         5 |
|         280 |         50 | most_frequently_used | random           | lfu             | all               |         5 |
|         267 |         46 | most_recently_used   | random           | lru             | all               |         5 |
|         207 |         21 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         207 |         20 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         205 |         14 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         204 |         14 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         203 |         11 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         198 |         17 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         135 |         22 | most_frequently_used | random           | fifo            | all               |         5 |
|         131 |         40 | most_recently_added  | random           | fifo            | all               |         5 |
|         127 |         39 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 32

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         707 |         50 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         696 |         50 | most_recently_used   | bfs              | lru             | all               |         5 |
|         696 |         62 | most_recently_added  | bfs              | lru             | all               |         5 |
|         678 |        104 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         668 |         76 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         637 |         77 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         627 |         90 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         616 |         60 | most_frequently_used | bfs              | lru             | all               |         5 |
|         605 |         93 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         598 |         21 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         590 |        132 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         567 |        125 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         429 |         28 | most_frequently_used | random           | lfu             | all               |         5 |
|         403 |         65 | most_recently_added  | random           | lfu             | all               |         5 |
|         392 |         82 | most_recently_used   | random           | lru             | all               |         5 |
|         370 |        118 | most_recently_added  | random           | lru             | all               |         5 |
|         339 |         37 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         339 |         37 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         324 |         55 | most_frequently_used | random           | lru             | all               |         5 |
|         323 |         52 | most_recently_used   | random           | lfu             | all               |         5 |
|         300 |         12 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         300 |         12 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         299 |         19 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         299 |         19 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         160 |         29 | most_recently_used   | random           | fifo            | all               |         5 |
|         152 |         55 | most_recently_added  | random           | fifo            | all               |         5 |
|         145 |         40 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 64

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         719 |         41 | most_recently_added  | bfs              | lru             | all               |         5 |
|         705 |         39 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         700 |         58 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         698 |         41 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         691 |         59 | most_recently_used   | bfs              | lru             | all               |         5 |
|         688 |         30 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         687 |         59 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         666 |         43 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         600 |         50 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         597 |         41 | most_frequently_used | bfs              | lru             | all               |         5 |
|         590 |         28 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         579 |         31 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         510 |         39 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         509 |         68 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         503 |         37 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         484 |         43 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         475 |         40 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         452 |         67 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         412 |        134 | most_recently_used   | random           | lru             | all               |         5 |
|         381 |         54 | most_recently_added  | random           | lfu             | all               |         5 |
|         368 |        133 | most_recently_added  | random           | lru             | all               |         5 |
|         348 |        110 | most_recently_used   | random           | lfu             | all               |         5 |
|         341 |         71 | most_frequently_used | random           | lfu             | all               |         5 |
|         338 |         98 | most_frequently_used | random           | lru             | all               |         5 |
|         225 |         31 | most_frequently_used | random           | fifo            | all               |         5 |
|         193 |         57 | most_recently_added  | random           | fifo            | all               |         5 |
|         182 |         58 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 128

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         754 |         83 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         739 |         53 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         731 |         50 | most_recently_added  | bfs              | lru             | all               |         5 |
|         723 |         64 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         722 |         35 | most_recently_used   | bfs              | lru             | all               |         5 |
|         702 |         63 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         701 |         57 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         697 |         53 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         694 |         39 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         689 |         49 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         668 |         61 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         654 |         60 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         652 |         72 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         647 |         47 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         643 |         69 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         643 |         54 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         641 |         40 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         638 |         51 | most_frequently_used | bfs              | lru             | all               |         5 |
|         407 |         81 | most_frequently_used | random           | lfu             | all               |         5 |
|         400 |        128 | most_recently_added  | random           | lru             | all               |         5 |
|         398 |         69 | most_frequently_used | random           | lru             | all               |         5 |
|         348 |         60 | most_recently_used   | random           | lru             | all               |         5 |
|         343 |         91 | most_recently_added  | random           | lfu             | all               |         5 |
|         334 |        102 | most_recently_used   | random           | lfu             | all               |         5 |
|         286 |         64 | most_recently_added  | random           | fifo            | all               |         5 |
|         231 |         54 | most_recently_used   | random           | fifo            | all               |         5 |
|         196 |         96 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 256

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         745 |         57 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         741 |         40 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         736 |         56 | most_recently_used   | bfs              | lru             | all               |         5 |
|         736 |         51 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         714 |         57 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         711 |         52 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         704 |         57 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         696 |         60 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         687 |         56 | most_recently_added  | bfs              | lru             | all               |         5 |
|         673 |         54 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         673 |         57 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         663 |         52 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         655 |         76 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         654 |         74 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         631 |         35 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         625 |         43 | most_frequently_used | bfs              | lru             | all               |         5 |
|         622 |         31 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         620 |         36 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         427 |         69 | most_frequently_used | random           | lru             | all               |         5 |
|         427 |        105 | most_recently_added  | random           | lru             | all               |         5 |
|         427 |         69 | most_frequently_used | random           | lfu             | all               |         5 |
|         420 |        128 | most_recently_added  | random           | lfu             | all               |         5 |
|         396 |         45 | most_frequently_used | random           | fifo            | all               |         5 |
|         389 |         53 | most_recently_added  | random           | fifo            | all               |         5 |
|         336 |         88 | most_recently_used   | random           | lfu             | all               |         5 |
|         320 |         74 | most_recently_used   | random           | lru             | all               |         5 |
|         293 |         96 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 512

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         733 |         58 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         732 |         54 | most_recently_used   | bfs              | lru             | all               |         5 |
|         728 |         56 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         728 |         45 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         726 |         51 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         726 |         49 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         720 |         62 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         719 |         68 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         717 |         67 | most_recently_added  | bfs              | lru             | all               |         5 |
|         707 |         58 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         705 |         64 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         704 |         63 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         634 |         32 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         632 |         29 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         631 |         28 | most_frequently_used | bfs              | lru             | all               |         5 |
|         631 |         29 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         630 |         29 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         630 |         30 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         399 |         79 | most_frequently_used | random           | fifo            | all               |         5 |
|         391 |         83 | most_frequently_used | random           | lfu             | all               |         5 |
|         391 |         83 | most_frequently_used | random           | lru             | all               |         5 |
|         389 |        134 | most_recently_added  | random           | lfu             | all               |         5 |
|         389 |        134 | most_recently_added  | random           | lru             | all               |         5 |
|         388 |        131 | most_recently_added  | random           | fifo            | all               |         5 |
|         358 |         65 | most_recently_used   | random           | lfu             | all               |         5 |
|         356 |         67 | most_recently_used   | random           | lru             | all               |         5 |
|         354 |         70 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 1024

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         742 |         60 | most_recently_used   | bfs              | lru             | all               |         5 |
|         742 |         60 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         742 |         60 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         730 |         50 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         730 |         50 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         730 |         50 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         711 |         65 | most_recently_added  | bfs              | lru             | all               |         5 |
|         711 |         65 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         711 |         65 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         701 |         62 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         701 |         62 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         701 |         62 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         630 |         32 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         630 |         32 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         630 |         32 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         630 |         32 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         630 |         32 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         630 |         32 | most_frequently_used | bfs              | lru             | all               |         5 |
|         392 |        141 | most_recently_added  | random           | fifo            | all               |         5 |
|         392 |        141 | most_recently_added  | random           | lru             | all               |         5 |
|         392 |        141 | most_recently_added  | random           | lfu             | all               |         5 |
|         389 |         89 | most_frequently_used | random           | fifo            | all               |         5 |
|         389 |         89 | most_frequently_used | random           | lru             | all               |         5 |
|         389 |         89 | most_frequently_used | random           | lfu             | all               |         5 |
|         353 |         74 | most_recently_used   | random           | fifo            | all               |         5 |
|         353 |         74 | most_recently_used   | random           | lfu             | all               |         5 |
|         353 |         74 | most_recently_used   | random           | lru             | all               |         5 |

