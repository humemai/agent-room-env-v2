# Results for xl-different-prob

Total configurations: 528
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|         650 |         23 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|         650 |         35 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|         649 |         39 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | random          | all               |          1024 |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|         642 |         66 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|         642 |         27 | most_recently_added  | dijkstra         | random          | all               |           512 |         5 |
|         641 |         28 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|         641 |         28 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|         640 |         26 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|         639 |         23 | most_recently_added  | bfs              | random          | all               |          1024 |         5 |
|         639 |         23 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|         639 |         23 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|         639 |         23 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|         638 |         21 | most_recently_added  | bfs              | random          | all               |           512 |         5 |
|         636 |         22 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|         634 |         44 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|         633 |         30 | random               | bfs              | lru             | all               |           256 |         5 |
|         633 |         20 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|         633 |         20 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|         631 |         61 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|         630 |         44 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|         628 |         34 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|         624 |         46 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|         623 |         33 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|         619 |         42 | random               | dijkstra         | lfu             | all               |           256 |         5 |
|         616 |         48 | most_recently_added  | bfs              | random          | all               |           256 |         5 |
|         614 |         51 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|         614 |         50 | most_recently_used   | bfs              | random          | all               |          1024 |         5 |
|         614 |         50 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|         614 |         50 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|         614 |         50 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|         612 |         31 | random               | bfs              | lfu             | all               |           256 |         5 |
|         611 |         48 | most_recently_used   | bfs              | random          | all               |           512 |         5 |
|         611 |         50 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|         610 |         50 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|         610 |         40 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|         609 |         49 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|         608 |         49 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|         607 |         58 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|         607 |         46 | random               | dijkstra         | lru             | all               |           512 |         5 |
|         607 |         47 | random               | dijkstra         | lfu             | all               |           512 |         5 |
|         606 |         39 | random               | dijkstra         | lru             | all               |           256 |         5 |
|         606 |         33 | random               | bfs              | fifo            | all               |           256 |         5 |
|         604 |         46 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|         603 |         61 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|         603 |         37 | random               | dijkstra         | random          | all               |           512 |         5 |
|         603 |         41 | random               | dijkstra         | fifo            | all               |           512 |         5 |
|         602 |         33 | random               | dijkstra         | fifo            | all               |           256 |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | random          | all               |          1024 |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|         602 |         30 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|         601 |         33 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|         599 |         43 | random               | dijkstra         | lfu             | all               |          1024 |         5 |
|         599 |         43 | random               | dijkstra         | fifo            | all               |          1024 |         5 |
|         599 |         43 | random               | dijkstra         | lru             | all               |          1024 |         5 |
|         599 |         43 | random               | dijkstra         | random          | all               |          1024 |         5 |
|         598 |         26 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|         597 |         37 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|         597 |         56 | random               | bfs              | lfu             | all               |           128 |         5 |
|         595 |         40 | random               | bfs              | fifo            | all               |           512 |         5 |
|         595 |         36 | random               | bfs              | lru             | all               |          1024 |         5 |
|         595 |         36 | random               | bfs              | lfu             | all               |          1024 |         5 |
|         595 |         36 | random               | bfs              | random          | all               |          1024 |         5 |
|         595 |         41 | random               | bfs              | random          | all               |           512 |         5 |
|         595 |         36 | random               | bfs              | fifo            | all               |          1024 |         5 |
|         594 |         42 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|         594 |         33 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|         594 |         33 | random               | bfs              | lfu             | all               |           512 |         5 |
|         593 |         35 | random               | bfs              | lru             | all               |           512 |         5 |
|         592 |         29 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|         592 |         29 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|         591 |         43 | most_recently_used   | dijkstra         | random          | all               |           512 |         5 |
|         591 |         43 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|         590 |         51 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|         589 |         44 | random               | bfs              | lru             | all               |           128 |         5 |
|         587 |         46 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|         586 |         39 | random               | dijkstra         | lru             | all               |           128 |         5 |
|         584 |         34 | most_frequently_used | bfs              | random          | all               |           512 |         5 |
|         584 |         72 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|         583 |         46 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|         583 |         89 | most_recently_added  | dijkstra         | random          | all               |           256 |         5 |
|         580 |         29 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|         579 |         60 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|         578 |         36 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|         578 |         71 | random               | dijkstra         | random          | all               |           256 |         5 |
|         577 |         29 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|         577 |         29 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|         575 |         28 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|         575 |         28 | most_frequently_used | bfs              | random          | all               |          1024 |         5 |
|         575 |         28 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|         575 |         28 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|         575 |         33 | random               | dijkstra         | lfu             | all               |           128 |         5 |
|         570 |         24 | random               | bfs              | random          | all               |           256 |         5 |
|         570 |         36 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|         568 |         27 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|         567 |         25 | random               | bfs              | lfu             | all               |            64 |         5 |
|         566 |         41 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|         563 |         39 | most_frequently_used | dijkstra         | random          | all               |           512 |         5 |
|         562 |         62 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | random          | all               |          1024 |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|         558 |         43 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|         558 |         43 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|         555 |         44 | random               | dijkstra         | lfu             | all               |            64 |         5 |
|         550 |         90 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|         549 |         53 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|         546 |         17 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|         545 |         27 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|         543 |         67 | most_frequently_used | dijkstra         | random          | all               |           256 |         5 |
|         542 |        100 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|         539 |         21 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|         539 |         51 | most_recently_used   | bfs              | random          | all               |           256 |         5 |
|         539 |         48 | random               | dijkstra         | lru             | all               |            64 |         5 |
|         536 |         14 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|         536 |         48 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|         534 |         48 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|         531 |         41 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|         529 |         29 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|         529 |         63 | most_frequently_used | bfs              | random          | all               |           256 |         5 |
|         527 |         53 | random               | bfs              | lru             | all               |            64 |         5 |
|         526 |         31 | most_recently_used   | dijkstra         | random          | all               |           256 |         5 |
|         524 |         89 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|         512 |         57 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|         507 |         32 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|         498 |         35 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|         490 |         53 | random               | bfs              | lfu             | all               |            32 |         5 |
|         485 |         21 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|         483 |         42 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|         482 |         53 | random               | bfs              | fifo            | all               |           128 |         5 |
|         479 |         63 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|         467 |         20 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|         467 |         24 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|         464 |         29 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|         463 |         51 | random               | dijkstra         | fifo            | all               |           128 |         5 |
|         455 |         18 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|         448 |         46 | random               | bfs              | random          | all               |           128 |         5 |
|         448 |         26 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|         447 |         38 | random               | bfs              | lru             | all               |            32 |         5 |
|         445 |         18 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|         429 |         34 | most_recently_added  | dijkstra         | random          | all               |           128 |         5 |
|         428 |         70 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|         427 |         58 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|         419 |         51 | random               | dijkstra         | lru             | all               |            32 |         5 |
|         416 |         27 | most_recently_used   | bfs              | random          | all               |           128 |         5 |
|         412 |        148 | random               | dijkstra         | lfu             | all               |            32 |         5 |
|         408 |         29 | random               | dijkstra         | random          | all               |           128 |         5 |
|         405 |         52 | most_recently_used   | dijkstra         | random          | all               |           128 |         5 |
|         405 |         23 | most_recently_added  | bfs              | random          | all               |           128 |         5 |
|         403 |         48 | most_frequently_used | dijkstra         | random          | all               |           128 |         5 |
|         399 |         50 | most_frequently_used | bfs              | random          | all               |           128 |         5 |
|         396 |         88 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|         394 |         93 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|         362 |         92 | random               | bfs              | lfu             | all               |            16 |         5 |
|         354 |        116 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|         351 |         72 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|         351 |         45 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|         338 |         24 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|         338 |         62 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|         337 |         33 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|         332 |         35 | random               | dijkstra         | lru             | all               |            16 |         5 |
|         328 |        129 | random               | dijkstra         | lfu             | all               |            16 |         5 |
|         326 |         48 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|         325 |         24 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|         324 |         42 | random               | dijkstra         | fifo            | all               |            64 |         5 |
|         323 |         21 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|         311 |         43 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|         310 |         43 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|         309 |         31 | random               | bfs              | fifo            | all               |            64 |         5 |
|         306 |         24 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|         304 |         40 | most_frequently_used | bfs              | random          | all               |            64 |         5 |
|         301 |         76 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|         297 |         23 | most_recently_added  | bfs              | random          | all               |            64 |         5 |
|         295 |         30 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|         295 |         70 | random               | bfs              | lfu             | all               |             8 |         4 |
|         291 |         24 | most_recently_used   | bfs              | random          | all               |            64 |         5 |
|         284 |        116 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|         281 |         53 | random               | bfs              | lru             | all               |            16 |         5 |
|         278 |         84 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|         276 |         33 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|         276 |         43 | most_recently_added  | dijkstra         | random          | all               |            64 |         5 |
|         273 |         12 | random               | dijkstra         | random          | all               |            64 |         5 |
|         271 |         52 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|         271 |         68 | random               | dijkstra         | lfu             | all               |             8 |         5 |
|         271 |         74 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|         267 |         21 | most_recently_used   | dijkstra         | random          | all               |            64 |         5 |
|         262 |         28 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|         260 |         34 | most_frequently_used | dijkstra         | random          | all               |            64 |         5 |
|         255 |        158 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|         254 |         76 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|         252 |        107 | random               | random           | lfu             | all               |           128 |         5 |
|         251 |         74 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|         250 |         24 | random               | bfs              | random          | all               |            64 |         5 |
|         246 |         35 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|         246 |         25 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|         240 |         75 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|         233 |        105 | random               | random           | random          | all               |           512 |         5 |
|         232 |        103 | random               | random           | random          | all               |          1024 |         5 |
|         232 |        103 | random               | random           | fifo            | all               |          1024 |         5 |
|         232 |        103 | random               | random           | lru             | all               |          1024 |         5 |
|         232 |        103 | random               | random           | lfu             | all               |          1024 |         5 |
|         230 |        101 | random               | random           | lru             | all               |           512 |         5 |
|         230 |        101 | random               | random           | lfu             | all               |           512 |         5 |
|         228 |         96 | random               | random           | lru             | all               |           128 |         5 |
|         228 |         99 | random               | random           | fifo            | all               |           512 |         5 |
|         219 |         95 | random               | random           | lfu             | all               |           256 |         5 |
|         218 |         61 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|         218 |         61 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|         218 |         61 | most_frequently_used | random           | random          | all               |          1024 |         5 |
|         218 |         61 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|         218 |         42 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|         216 |         95 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|         215 |         57 | most_frequently_used | random           | random          | all               |           512 |         5 |
|         215 |        103 | random               | random           | random          | all               |           256 |         5 |
|         213 |         79 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|         213 |         79 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|         213 |         79 | most_recently_added  | random           | random          | all               |          1024 |         5 |
|         213 |         79 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|         213 |         59 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|         213 |         59 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|         213 |         98 | random               | random           | lru             | all               |           256 |         5 |
|         213 |         42 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|         212 |         41 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|         211 |         27 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|         210 |         55 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|         207 |         25 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|         205 |         91 | random               | random           | random          | all               |           128 |         5 |
|         204 |         84 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|         203 |         20 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|         203 |         54 | most_recently_added  | random           | random          | all               |           256 |         5 |
|         203 |         26 | most_recently_added  | random           | random          | all               |           128 |         5 |
|         202 |         72 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|         201 |         72 | most_recently_added  | random           | random          | all               |           512 |         5 |
|         201 |         70 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|         201 |         70 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|         200 |         51 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|         200 |         27 | most_recently_added  | bfs              | random          | all               |            32 |         5 |
|         199 |         23 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|         199 |         48 | random               | random           | fifo            | all               |           256 |         5 |
|         198 |         21 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|         197 |         56 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|         195 |         31 | random               | dijkstra         | fifo            | all               |            32 |         5 |
|         195 |         72 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|         190 |         19 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|         188 |         83 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|         187 |         62 | most_frequently_used | random           | random          | all               |           256 |         5 |
|         187 |         76 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|         187 |         71 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|         184 |         51 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|         180 |         63 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|         180 |         79 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|         179 |         25 | most_recently_added  | dijkstra         | random          | all               |            32 |         5 |
|         178 |         18 | random               | bfs              | fifo            | all               |            32 |         5 |
|         175 |         78 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|         174 |         75 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|         174 |         61 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|         173 |         90 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|         172 |         48 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|         170 |         90 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|         170 |         17 | random               | dijkstra         | random          | all               |            32 |         5 |
|         169 |         28 | most_frequently_used | bfs              | random          | all               |            32 |         5 |
|         169 |         65 | random               | random           | lru             | all               |            32 |         5 |
|         168 |         16 | random               | dijkstra         | lru             | all               |             8 |         5 |
|         168 |         49 | most_frequently_used | random           | random          | all               |           128 |         5 |
|         167 |         53 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|         166 |         37 | random               | bfs              | lru             | all               |             8 |         5 |
|         165 |         20 | most_recently_used   | dijkstra         | random          | all               |            32 |         5 |
|         165 |         42 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|         165 |         54 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|         165 |         33 | most_recently_used   | bfs              | random          | all               |            32 |         5 |
|         164 |         65 | random               | random           | fifo            | all               |           128 |         5 |
|         162 |         68 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|         161 |         69 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|         159 |         55 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|         159 |         30 | most_frequently_used | dijkstra         | random          | all               |            32 |         5 |
|         159 |         65 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|         158 |         23 | random               | bfs              | random          | all               |            32 |         5 |
|         158 |         98 | random               | random           | lfu             | all               |            16 |         5 |
|         158 |         28 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|         149 |         21 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|         149 |         20 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|         148 |         15 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|         148 |         15 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|         146 |         73 | most_recently_used   | random           | random          | all               |           256 |         5 |
|         145 |         25 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|         143 |         60 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|         142 |         11 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|         140 |         46 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|         137 |         64 | random               | random           | lfu             | all               |            32 |         5 |
|         134 |         58 | random               | random           | lfu             | all               |            64 |         5 |
|         134 |         40 | random               | bfs              | lfu             | all               |             4 |         5 |
|         129 |         42 | most_recently_used   | random           | random          | all               |           512 |         5 |
|         129 |        108 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|         128 |         42 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|         127 |         52 | random               | random           | lru             | all               |            64 |         5 |
|         127 |         43 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|         126 |         40 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|         126 |         63 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|         126 |          8 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|         125 |         38 | most_recently_used   | random           | random          | all               |          1024 |         5 |
|         125 |         38 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|         125 |         38 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|         125 |          8 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|         125 |         38 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|         124 |         36 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|         123 |         64 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|         123 |         50 | most_frequently_used | random           | random          | all               |            64 |         5 |
|         123 |         10 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|         123 |         10 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|         122 |         33 | most_frequently_used | random           | random          | all               |            32 |         5 |
|         118 |         55 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|         116 |         15 | random               | dijkstra         | random          | all               |            16 |         5 |
|         116 |         70 | random               | random           | lfu             | all               |             8 |         5 |
|         115 |         10 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|         114 |         11 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|         114 |         74 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|         113 |         69 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|         111 |         40 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|         110 |         23 | random               | dijkstra         | fifo            | all               |            16 |         5 |
|         108 |         21 | random               | bfs              | fifo            | all               |            16 |         5 |
|         108 |         28 | random               | bfs              | random          | all               |            16 |         5 |
|         107 |         59 | most_recently_used   | random           | random          | all               |            64 |         5 |
|         107 |         32 | random               | bfs              | lfu             | all               |             2 |         5 |
|         107 |         62 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|         105 |         35 | random               | random           | fifo            | all               |            64 |         5 |
|         105 |         65 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|         104 |         71 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|         102 |         48 | most_recently_added  | random           | random          | all               |            64 |         5 |
|         101 |         11 | most_recently_added  | bfs              | random          | all               |            16 |         5 |
|          99 |         41 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|          98 |         40 | most_recently_used   | random           | random          | all               |           128 |         5 |
|          98 |         39 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|          98 |         49 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|          98 |         39 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|          96 |         25 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|          95 |         16 | most_frequently_used | bfs              | random          | all               |            16 |         5 |
|          95 |         45 | random               | random           | lru             | all               |            16 |         5 |
|          94 |         57 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|          94 |         16 | most_recently_used   | bfs              | random          | all               |            16 |         5 |
|          91 |         39 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|          90 |         20 | most_recently_used   | dijkstra         | random          | all               |            16 |         5 |
|          90 |         33 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|          88 |         11 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|          88 |         24 | random               | random           | random          | all               |            64 |         5 |
|          88 |         27 | most_frequently_used | dijkstra         | random          | all               |            16 |         5 |
|          88 |         20 | random               | random           | random          | all               |            32 |         5 |
|          87 |         50 | random               | dijkstra         | lfu             | all               |             4 |         5 |
|          87 |         19 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|          87 |         25 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|          85 |         34 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|          85 |         12 | most_frequently_used | bfs              | random          | all               |             8 |         5 |
|          83 |         14 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|          83 |         15 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|          82 |         17 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|          81 |         35 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|          79 |          8 | most_recently_used   | bfs              | random          | all               |             8 |         5 |
|          78 |         21 | most_recently_added  | random           | random          | all               |            32 |         5 |
|          77 |         25 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|          76 |         11 | random               | bfs              | fifo            | all               |             8 |         5 |
|          75 |         31 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|          72 |         15 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|          72 |         15 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|          71 |         17 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|          71 |         14 | random               | bfs              | lru             | all               |             4 |         5 |
|          70 |         10 | random               | dijkstra         | fifo            | all               |             8 |         5 |
|          70 |         16 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|          70 |         51 | random               | dijkstra         | lfu             | all               |             2 |         5 |
|          70 |         15 | random               | dijkstra         | random          | all               |             8 |         5 |
|          69 |         16 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|          69 |         16 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|          68 |         22 | random               | random           | lfu             | all               |             4 |         5 |
|          68 |         23 | most_recently_added  | dijkstra         | random          | all               |            16 |         5 |
|          66 |          5 | most_recently_used   | random           | random          | all               |            16 |         5 |
|          66 |         26 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|          65 |         24 | random               | dijkstra         | lru             | all               |             4 |         5 |
|          64 |         20 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|          64 |         14 | random               | random           | fifo            | all               |            16 |         5 |
|          63 |          5 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|          63 |         24 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|          61 |         15 | most_recently_added  | bfs              | random          | all               |             8 |         5 |
|          61 |         25 | most_frequently_used | random           | random          | all               |            16 |         5 |
|          61 |          6 | most_recently_used   | dijkstra         | random          | all               |             8 |         5 |
|          61 |         21 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|          61 |         21 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|          60 |          3 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|          60 |          9 | most_frequently_used | dijkstra         | random          | all               |             8 |         5 |
|          59 |          9 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|          58 |         33 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|          58 |         14 | most_frequently_used | bfs              | random          | all               |             4 |         5 |
|          58 |         14 | most_recently_used   | bfs              | random          | all               |             4 |         5 |
|          58 |         34 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|          58 |         14 | random               | bfs              | random          | all               |             8 |         5 |
|          57 |         16 | random               | random           | fifo            | all               |            32 |         5 |
|          56 |         12 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|          56 |         12 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|          55 |         17 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|          55 |         17 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|          54 |         10 | most_recently_added  | dijkstra         | random          | all               |             8 |         5 |
|          54 |         14 | random               | dijkstra         | fifo            | all               |             4 |         5 |
|          54 |          7 | random               | bfs              | fifo            | all               |             4 |         5 |
|          54 |         33 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|          53 |         22 | random               | dijkstra         | random          | all               |             4 |         5 |
|          52 |         19 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|          52 |         19 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|          52 |         13 | most_recently_added  | random           | random          | all               |            16 |         5 |
|          51 |         29 | most_recently_used   | random           | random          | all               |            32 |         5 |
|          51 |         15 | random               | bfs              | lru             | all               |             2 |         5 |
|          50 |          6 | most_recently_used   | random           | random          | all               |             8 |         5 |
|          48 |         17 | most_recently_added  | bfs              | random          | all               |             4 |         5 |
|          47 |         15 | random               | random           | random          | all               |            16 |         5 |
|          47 |          8 | random               | bfs              | random          | all               |             4 |         5 |
|          47 |         23 | most_recently_added  | dijkstra         | random          | all               |             4 |         5 |
|          46 |         34 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|          45 |         14 | most_frequently_used | random           | random          | all               |             8 |         5 |
|          45 |         27 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|          45 |         27 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|          44 |         13 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|          44 |         13 | random               | random           | fifo            | all               |             8 |         5 |
|          43 |         21 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|          43 |         20 | random               | random           | lru             | all               |             4 |         5 |
|          42 |         15 | random               | dijkstra         | lru             | all               |             2 |         5 |
|          42 |         21 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|          41 |         20 | random               | random           | lru             | all               |             8 |         5 |
|          41 |         19 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|          40 |         19 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|          40 |         13 | random               | bfs              | random          | all               |             2 |         5 |
|          40 |         14 | random               | random           | lfu             | all               |             2 |         5 |
|          40 |         24 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|          40 |         24 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|          39 |         12 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|          39 |         12 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|          39 |         10 | most_recently_added  | bfs              | random          | all               |             2 |         5 |
|          39 |          6 | random               | random           | random          | all               |             8 |         5 |
|          38 |          5 | most_recently_added  | random           | random          | all               |             8 |         5 |
|          38 |         13 | most_recently_added  | random           | random          | all               |             2 |         5 |
|          37 |         10 | random               | bfs              | fifo            | all               |             2 |         5 |
|          37 |         19 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|          36 |         17 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|          36 |         21 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|          35 |         19 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|          35 |         18 | random               | random           | random          | all               |             4 |         5 |
|          34 |         14 | most_frequently_used | dijkstra         | random          | all               |             4 |         5 |
|          34 |         14 | most_recently_used   | dijkstra         | random          | all               |             4 |         5 |
|          34 |          9 | most_recently_added  | dijkstra         | random          | all               |             2 |         5 |
|          34 |         20 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|          34 |         20 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|          34 |          9 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|          33 |          8 | most_recently_used   | dijkstra         | random          | all               |             2 |         5 |
|          33 |          8 | most_frequently_used | dijkstra         | random          | all               |             2 |         5 |
|          33 |         15 | most_recently_used   | bfs              | random          | all               |             2 |         5 |
|          33 |         15 | most_frequently_used | bfs              | random          | all               |             2 |         5 |
|          33 |         14 | random               | random           | fifo            | all               |             2 |         5 |
|          33 |          8 | random               | dijkstra         | random          | all               |             2 |         5 |
|          33 |         11 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|          33 |         11 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|          33 |          8 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|          33 |         11 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | random               | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | random               | dijkstra         | lfu             | all               |             0 |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|          33 |         11 | random               | dijkstra         | lru             | all               |             0 |         5 |
|          33 |         11 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | random               | bfs              | lfu             | all               |             0 |         5 |
|          33 |         11 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|          33 |         15 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|          31 |          9 | most_frequently_used | random           | random          | all               |             2 |         5 |
|          31 |          9 | most_recently_used   | random           | random          | all               |             2 |         5 |
|          30 |          7 | random               | random           | random          | all               |             2 |         5 |
|          29 |          8 | most_recently_added  | random           | random          | all               |             4 |         5 |
|          29 |         11 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|          29 |         11 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|          29 |          7 | random               | random           | lru             | all               |             2 |         5 |
|          28 |         12 | most_frequently_used | random           | random          | all               |             4 |         5 |
|          28 |         10 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|          27 |          9 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|          27 |          6 | random               | dijkstra         | fifo            | all               |             2 |         5 |
|          27 |          8 | random               | random           | fifo            | all               |             4 |         5 |
|          26 |          4 | most_recently_added  | random           | random          | all               |             0 |         5 |
|          26 |          4 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | most_recently_added  | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | most_frequently_used | random           | random          | all               |             0 |         5 |
|          26 |          4 | most_recently_used   | random           | random          | all               |             0 |         5 |
|          26 |          4 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | random               | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | random               | random           | random          | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | random          | all               |             0 |         5 |
|          25 |         11 | random               | dijkstra         | random          | all               |             0 |         5 |
|          25 |         11 | random               | bfs              | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | random               | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | random               | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|          24 |          8 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|          24 |          8 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|          24 |          9 | most_recently_used   | random           | random          | all               |             4 |         5 |
|          23 |          5 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|          23 |          5 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|          21 |          6 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|          21 |          6 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|          18 |          5 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|          18 |          5 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|          18 |          5 | most_frequently_used | random           | lfu             | all               |             0 |         5 |
|          18 |          5 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|          18 |          5 | random               | random           | lfu             | all               |             0 |         5 |
|          18 |          5 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|          18 |          5 | random               | random           | lru             | all               |             0 |         5 |
|          18 |          5 | most_recently_added  | random           | lru             | all               |             0 |         5 |

## Memory Size 0

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          33 |         11 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_frequently_used | bfs              | lru             | all               |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          33 |         11 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_recently_added  | bfs              | lru             | all               |         5 |
|          33 |         11 | random               | dijkstra         | lru             | all               |         5 |
|          33 |         11 | random               | dijkstra         | lfu             | all               |         5 |
|          33 |         11 | random               | bfs              | lru             | all               |         5 |
|          33 |         11 | random               | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          33 |         11 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_recently_used   | bfs              | lru             | all               |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          26 |          4 | most_frequently_used | random           | fifo            | all               |         5 |
|          26 |          4 | most_frequently_used | random           | random          | all               |         5 |
|          26 |          4 | random               | random           | random          | all               |         5 |
|          26 |          4 | random               | random           | fifo            | all               |         5 |
|          26 |          4 | most_recently_used   | random           | random          | all               |         5 |
|          26 |          4 | most_recently_used   | random           | fifo            | all               |         5 |
|          26 |          4 | most_recently_added  | random           | random          | all               |         5 |
|          26 |          4 | most_recently_added  | random           | fifo            | all               |         5 |
|          25 |         11 | random               | dijkstra         | random          | all               |         5 |
|          25 |         11 | random               | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_recently_added  | bfs              | random          | all               |         5 |
|          25 |         11 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          25 |         11 | most_frequently_used | bfs              | random          | all               |         5 |
|          25 |         11 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          25 |         11 | random               | bfs              | random          | all               |         5 |
|          25 |         11 | random               | bfs              | fifo            | all               |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          25 |         11 | most_recently_used   | bfs              | random          | all               |         5 |
|          18 |          5 | most_frequently_used | random           | lfu             | all               |         5 |
|          18 |          5 | most_frequently_used | random           | lru             | all               |         5 |
|          18 |          5 | most_recently_added  | random           | lfu             | all               |         5 |
|          18 |          5 | most_recently_added  | random           | lru             | all               |         5 |
|          18 |          5 | most_recently_used   | random           | lfu             | all               |         5 |
|          18 |          5 | most_recently_used   | random           | lru             | all               |         5 |
|          18 |          5 | random               | random           | lfu             | all               |         5 |
|          18 |          5 | random               | random           | lru             | all               |         5 |

## Memory Size 2

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         107 |         32 | random               | bfs              | lfu             | all               |         5 |
|          98 |         39 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          98 |         39 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          75 |         31 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          70 |         51 | random               | dijkstra         | lfu             | all               |         5 |
|          58 |         33 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          58 |         34 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          54 |         33 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          52 |         19 | most_recently_used   | bfs              | lru             | all               |         5 |
|          52 |         19 | most_frequently_used | bfs              | lru             | all               |         5 |
|          51 |         15 | random               | bfs              | lru             | all               |         5 |
|          44 |         13 | most_recently_added  | bfs              | lru             | all               |         5 |
|          42 |         15 | random               | dijkstra         | lru             | all               |         5 |
|          41 |         19 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          40 |         13 | random               | bfs              | random          | all               |         5 |
|          40 |         14 | random               | random           | lfu             | all               |         5 |
|          40 |         24 | most_frequently_used | random           | lfu             | all               |         5 |
|          40 |         24 | most_recently_used   | random           | lfu             | all               |         5 |
|          39 |         12 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          39 |         10 | most_recently_added  | bfs              | random          | all               |         5 |
|          39 |         12 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          38 |         13 | most_recently_added  | random           | random          | all               |         5 |
|          37 |         10 | random               | bfs              | fifo            | all               |         5 |
|          36 |         17 | most_recently_added  | random           | lfu             | all               |         5 |
|          34 |          9 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          34 |         20 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          34 |         20 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          34 |          9 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          33 |          8 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          33 |          8 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          33 |         15 | most_frequently_used | bfs              | random          | all               |         5 |
|          33 |         14 | random               | random           | fifo            | all               |         5 |
|          33 |         15 | most_recently_used   | bfs              | random          | all               |         5 |
|          33 |          8 | random               | dijkstra         | random          | all               |         5 |
|          33 |          8 | most_recently_added  | random           | lru             | all               |         5 |
|          33 |         15 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          31 |          9 | most_recently_used   | random           | random          | all               |         5 |
|          31 |          9 | most_frequently_used | random           | random          | all               |         5 |
|          30 |          7 | random               | random           | random          | all               |         5 |
|          29 |         11 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          29 |         11 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          29 |          7 | random               | random           | lru             | all               |         5 |
|          27 |          9 | most_recently_added  | random           | fifo            | all               |         5 |
|          27 |          6 | random               | dijkstra         | fifo            | all               |         5 |
|          23 |          5 | most_recently_used   | random           | lru             | all               |         5 |
|          23 |          5 | most_frequently_used | random           | lru             | all               |         5 |
|          21 |          6 | most_frequently_used | random           | fifo            | all               |         5 |
|          21 |          6 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 4

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         162 |         68 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         161 |         69 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         159 |         65 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         134 |         40 | random               | bfs              | lfu             | all               |         5 |
|          99 |         41 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          94 |         57 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          87 |         19 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          87 |         50 | random               | dijkstra         | lfu             | all               |         5 |
|          85 |         34 | most_frequently_used | random           | lfu             | all               |         5 |
|          83 |         14 | most_recently_added  | random           | lfu             | all               |         5 |
|          81 |         35 | most_recently_used   | random           | lfu             | all               |         5 |
|          71 |         14 | random               | bfs              | lru             | all               |         5 |
|          69 |         16 | most_frequently_used | bfs              | lru             | all               |         5 |
|          69 |         16 | most_recently_used   | bfs              | lru             | all               |         5 |
|          68 |         22 | random               | random           | lfu             | all               |         5 |
|          65 |         24 | random               | dijkstra         | lru             | all               |         5 |
|          64 |         20 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          63 |          5 | most_recently_added  | bfs              | lru             | all               |         5 |
|          61 |         21 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          61 |         21 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          60 |          3 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          59 |          9 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          58 |         14 | most_recently_used   | bfs              | random          | all               |         5 |
|          58 |         14 | most_frequently_used | bfs              | random          | all               |         5 |
|          56 |         12 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          56 |         12 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          55 |         17 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          55 |         17 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          54 |         14 | random               | dijkstra         | fifo            | all               |         5 |
|          54 |          7 | random               | bfs              | fifo            | all               |         5 |
|          53 |         22 | random               | dijkstra         | random          | all               |         5 |
|          48 |         17 | most_recently_added  | bfs              | random          | all               |         5 |
|          47 |         23 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          47 |          8 | random               | bfs              | random          | all               |         5 |
|          45 |         27 | most_recently_used   | random           | lru             | all               |         5 |
|          45 |         27 | most_frequently_used | random           | lru             | all               |         5 |
|          43 |         21 | most_recently_added  | random           | lru             | all               |         5 |
|          43 |         20 | random               | random           | lru             | all               |         5 |
|          35 |         18 | random               | random           | random          | all               |         5 |
|          34 |         14 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          34 |         14 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          29 |          8 | most_recently_added  | random           | random          | all               |         5 |
|          28 |         12 | most_frequently_used | random           | random          | all               |         5 |
|          28 |         10 | most_recently_added  | random           | fifo            | all               |         5 |
|          27 |          8 | random               | random           | fifo            | all               |         5 |
|          24 |          8 | most_frequently_used | random           | fifo            | all               |         5 |
|          24 |          8 | most_recently_used   | random           | fifo            | all               |         5 |
|          24 |          9 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 8

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         311 |         43 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         295 |         70 | random               | bfs              | lfu             | all               |         4 |
|         278 |         84 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         276 |         33 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         271 |         68 | random               | dijkstra         | lfu             | all               |         5 |
|         251 |         74 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         240 |         75 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         180 |         63 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         168 |         16 | random               | dijkstra         | lru             | all               |         5 |
|         166 |         37 | random               | bfs              | lru             | all               |         5 |
|         158 |         28 | most_recently_added  | bfs              | lru             | all               |         5 |
|         149 |         21 | most_frequently_used | bfs              | lru             | all               |         5 |
|         149 |         20 | most_recently_used   | bfs              | lru             | all               |         5 |
|         148 |         15 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         148 |         15 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         142 |         11 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         118 |         55 | most_recently_added  | random           | lfu             | all               |         5 |
|         116 |         70 | random               | random           | lfu             | all               |         5 |
|         107 |         62 | most_frequently_used | random           | lfu             | all               |         5 |
|          98 |         49 | most_recently_used   | random           | lfu             | all               |         5 |
|          88 |         11 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          85 |         12 | most_frequently_used | bfs              | random          | all               |         5 |
|          83 |         15 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          79 |          8 | most_recently_used   | bfs              | random          | all               |         5 |
|          76 |         11 | random               | bfs              | fifo            | all               |         5 |
|          72 |         15 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          72 |         15 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          71 |         17 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          70 |         10 | random               | dijkstra         | fifo            | all               |         5 |
|          70 |         16 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          70 |         15 | random               | dijkstra         | random          | all               |         5 |
|          61 |         15 | most_recently_added  | bfs              | random          | all               |         5 |
|          61 |          6 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          60 |          9 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          58 |         14 | random               | bfs              | random          | all               |         5 |
|          54 |         10 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          50 |          6 | most_recently_used   | random           | random          | all               |         5 |
|          46 |         34 | most_recently_used   | random           | lru             | all               |         5 |
|          45 |         14 | most_frequently_used | random           | random          | all               |         5 |
|          44 |         13 | random               | random           | fifo            | all               |         5 |
|          42 |         21 | most_frequently_used | random           | lru             | all               |         5 |
|          41 |         20 | random               | random           | lru             | all               |         5 |
|          40 |         19 | most_recently_added  | random           | fifo            | all               |         5 |
|          39 |          6 | random               | random           | random          | all               |         5 |
|          38 |          5 | most_recently_added  | random           | random          | all               |         5 |
|          37 |         19 | most_recently_used   | random           | fifo            | all               |         5 |
|          36 |         21 | most_recently_added  | random           | lru             | all               |         5 |
|          35 |         19 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 16

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         362 |         92 | random               | bfs              | lfu             | all               |         5 |
|         354 |        116 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         351 |         45 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         338 |         62 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         332 |         35 | random               | dijkstra         | lru             | all               |         5 |
|         328 |        129 | random               | dijkstra         | lfu             | all               |         5 |
|         310 |         43 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         301 |         76 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         295 |         30 | most_recently_added  | bfs              | lru             | all               |         5 |
|         284 |        116 | most_frequently_used | random           | lfu             | all               |         5 |
|         281 |         53 | random               | bfs              | lru             | all               |         5 |
|         271 |         52 | most_frequently_used | bfs              | lru             | all               |         5 |
|         262 |         28 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         255 |        158 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         254 |         76 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         246 |         35 | most_recently_used   | bfs              | lru             | all               |         5 |
|         197 |         56 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         159 |         55 | most_recently_added  | random           | lfu             | all               |         5 |
|         158 |         98 | random               | random           | lfu             | all               |         5 |
|         143 |         60 | most_recently_used   | random           | lfu             | all               |         5 |
|         126 |          8 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         125 |          8 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         123 |         10 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         123 |         10 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         116 |         15 | random               | dijkstra         | random          | all               |         5 |
|         115 |         10 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         114 |         11 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         114 |         74 | most_frequently_used | random           | fifo            | all               |         5 |
|         110 |         23 | random               | dijkstra         | fifo            | all               |         5 |
|         108 |         21 | random               | bfs              | fifo            | all               |         5 |
|         108 |         28 | random               | bfs              | random          | all               |         5 |
|         105 |         65 | most_recently_added  | random           | lru             | all               |         5 |
|         104 |         71 | most_recently_used   | random           | lru             | all               |         5 |
|         101 |         11 | most_recently_added  | bfs              | random          | all               |         5 |
|          95 |         16 | most_frequently_used | bfs              | random          | all               |         5 |
|          95 |         45 | random               | random           | lru             | all               |         5 |
|          94 |         16 | most_recently_used   | bfs              | random          | all               |         5 |
|          90 |         20 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          90 |         33 | most_frequently_used | random           | lru             | all               |         5 |
|          88 |         27 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          68 |         23 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          66 |          5 | most_recently_used   | random           | random          | all               |         5 |
|          66 |         26 | most_recently_added  | random           | fifo            | all               |         5 |
|          64 |         14 | random               | random           | fifo            | all               |         5 |
|          63 |         24 | most_recently_used   | random           | fifo            | all               |         5 |
|          61 |         25 | most_frequently_used | random           | random          | all               |         5 |
|          52 |         13 | most_recently_added  | random           | random          | all               |         5 |
|          47 |         15 | random               | random           | random          | all               |         5 |

## Memory Size 32

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         529 |         29 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         512 |         57 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         490 |         53 | random               | bfs              | lfu             | all               |         5 |
|         485 |         21 | most_recently_used   | bfs              | lru             | all               |         5 |
|         483 |         42 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         479 |         63 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         467 |         20 | most_recently_added  | bfs              | lru             | all               |         5 |
|         447 |         38 | random               | bfs              | lru             | all               |         5 |
|         445 |         18 | most_frequently_used | bfs              | lru             | all               |         5 |
|         428 |         70 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         427 |         58 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         419 |         51 | random               | dijkstra         | lru             | all               |         5 |
|         412 |        148 | random               | dijkstra         | lfu             | all               |         5 |
|         396 |         88 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         394 |         93 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         351 |         72 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         246 |         25 | most_recently_added  | random           | lfu             | all               |         5 |
|         211 |         27 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         207 |         25 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         204 |         84 | most_frequently_used | random           | lru             | all               |         5 |
|         203 |         20 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         200 |         51 | most_recently_added  | random           | lru             | all               |         5 |
|         200 |         27 | most_recently_added  | bfs              | random          | all               |         5 |
|         199 |         23 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         198 |         21 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         195 |         31 | random               | dijkstra         | fifo            | all               |         5 |
|         190 |         19 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         187 |         76 | most_frequently_used | random           | lfu             | all               |         5 |
|         179 |         25 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         178 |         18 | random               | bfs              | fifo            | all               |         5 |
|         170 |         17 | random               | dijkstra         | random          | all               |         5 |
|         169 |         28 | most_frequently_used | bfs              | random          | all               |         5 |
|         169 |         65 | random               | random           | lru             | all               |         5 |
|         165 |         20 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         165 |         33 | most_recently_used   | bfs              | random          | all               |         5 |
|         159 |         30 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         158 |         23 | random               | bfs              | random          | all               |         5 |
|         137 |         64 | random               | random           | lfu             | all               |         5 |
|         124 |         36 | most_recently_used   | random           | lfu             | all               |         5 |
|         123 |         64 | most_recently_used   | random           | lru             | all               |         5 |
|         122 |         33 | most_frequently_used | random           | random          | all               |         5 |
|          96 |         25 | most_frequently_used | random           | fifo            | all               |         5 |
|          88 |         20 | random               | random           | random          | all               |         5 |
|          82 |         17 | most_recently_added  | random           | fifo            | all               |         5 |
|          78 |         21 | most_recently_added  | random           | random          | all               |         5 |
|          77 |         25 | most_recently_used   | random           | fifo            | all               |         5 |
|          57 |         16 | random               | random           | fifo            | all               |         5 |
|          51 |         29 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 64

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         624 |         46 | most_recently_used   | bfs              | lru             | all               |         5 |
|         614 |         51 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         608 |         49 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         598 |         26 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         594 |         33 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         587 |         46 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         583 |         46 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         568 |         27 | most_recently_added  | bfs              | lru             | all               |         5 |
|         567 |         25 | random               | bfs              | lfu             | all               |         5 |
|         555 |         44 | random               | dijkstra         | lfu             | all               |         5 |
|         550 |         90 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         549 |         53 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         539 |         48 | random               | dijkstra         | lru             | all               |         5 |
|         536 |         48 | most_frequently_used | bfs              | lru             | all               |         5 |
|         527 |         53 | random               | bfs              | lru             | all               |         5 |
|         524 |         89 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         338 |         24 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         337 |         33 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         326 |         48 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         325 |         24 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         324 |         42 | random               | dijkstra         | fifo            | all               |         5 |
|         323 |         21 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         309 |         31 | random               | bfs              | fifo            | all               |         5 |
|         306 |         24 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         304 |         40 | most_frequently_used | bfs              | random          | all               |         5 |
|         297 |         23 | most_recently_added  | bfs              | random          | all               |         5 |
|         291 |         24 | most_recently_used   | bfs              | random          | all               |         5 |
|         276 |         43 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         273 |         12 | random               | dijkstra         | random          | all               |         5 |
|         267 |         21 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         260 |         34 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         250 |         24 | random               | bfs              | random          | all               |         5 |
|         218 |         42 | most_frequently_used | random           | lfu             | all               |         5 |
|         188 |         83 | most_recently_added  | random           | lfu             | all               |         5 |
|         180 |         79 | most_frequently_used | random           | lru             | all               |         5 |
|         175 |         78 | most_recently_used   | random           | lru             | all               |         5 |
|         134 |         58 | random               | random           | lfu             | all               |         5 |
|         129 |        108 | most_recently_added  | random           | lru             | all               |         5 |
|         127 |         52 | random               | random           | lru             | all               |         5 |
|         123 |         50 | most_frequently_used | random           | random          | all               |         5 |
|         113 |         69 | most_recently_used   | random           | lfu             | all               |         5 |
|         111 |         40 | most_frequently_used | random           | fifo            | all               |         5 |
|         107 |         59 | most_recently_used   | random           | random          | all               |         5 |
|         105 |         35 | random               | random           | fifo            | all               |         5 |
|         102 |         48 | most_recently_added  | random           | random          | all               |         5 |
|          91 |         39 | most_recently_used   | random           | fifo            | all               |         5 |
|          88 |         24 | random               | random           | random          | all               |         5 |
|          87 |         25 | most_recently_added  | random           | fifo            | all               |         5 |

## Memory Size 128

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         642 |         66 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         634 |         44 | most_recently_added  | bfs              | lru             | all               |         5 |
|         631 |         61 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         630 |         44 | most_recently_used   | bfs              | lru             | all               |         5 |
|         607 |         58 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         603 |         61 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         597 |         56 | random               | bfs              | lfu             | all               |         5 |
|         589 |         44 | random               | bfs              | lru             | all               |         5 |
|         586 |         39 | random               | dijkstra         | lru             | all               |         5 |
|         584 |         72 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         579 |         60 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         575 |         33 | random               | dijkstra         | lfu             | all               |         5 |
|         562 |         62 | most_frequently_used | bfs              | lru             | all               |         5 |
|         542 |        100 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         534 |         48 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         531 |         41 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         507 |         32 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         498 |         35 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         482 |         53 | random               | bfs              | fifo            | all               |         5 |
|         467 |         24 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         464 |         29 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         463 |         51 | random               | dijkstra         | fifo            | all               |         5 |
|         455 |         18 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         448 |         46 | random               | bfs              | random          | all               |         5 |
|         448 |         26 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         429 |         34 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         416 |         27 | most_recently_used   | bfs              | random          | all               |         5 |
|         408 |         29 | random               | dijkstra         | random          | all               |         5 |
|         405 |         52 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         405 |         23 | most_recently_added  | bfs              | random          | all               |         5 |
|         403 |         48 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         399 |         50 | most_frequently_used | bfs              | random          | all               |         5 |
|         271 |         74 | most_recently_added  | random           | lfu             | all               |         5 |
|         252 |        107 | random               | random           | lfu             | all               |         5 |
|         228 |         96 | random               | random           | lru             | all               |         5 |
|         216 |         95 | most_recently_added  | random           | lru             | all               |         5 |
|         205 |         91 | random               | random           | random          | all               |         5 |
|         203 |         26 | most_recently_added  | random           | random          | all               |         5 |
|         195 |         72 | most_recently_added  | random           | fifo            | all               |         5 |
|         187 |         71 | most_frequently_used | random           | lfu             | all               |         5 |
|         172 |         48 | most_frequently_used | random           | lru             | all               |         5 |
|         170 |         90 | most_recently_used   | random           | lru             | all               |         5 |
|         168 |         49 | most_frequently_used | random           | random          | all               |         5 |
|         165 |         42 | most_frequently_used | random           | fifo            | all               |         5 |
|         164 |         65 | random               | random           | fifo            | all               |         5 |
|         145 |         25 | most_recently_used   | random           | fifo            | all               |         5 |
|         126 |         63 | most_recently_used   | random           | lfu             | all               |         5 |
|          98 |         40 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 256

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         650 |         23 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         650 |         35 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         649 |         39 | most_recently_added  | bfs              | lru             | all               |         5 |
|         633 |         30 | random               | bfs              | lru             | all               |         5 |
|         628 |         34 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         623 |         33 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         619 |         42 | random               | dijkstra         | lfu             | all               |         5 |
|         616 |         48 | most_recently_added  | bfs              | random          | all               |         5 |
|         612 |         31 | random               | bfs              | lfu             | all               |         5 |
|         610 |         40 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         606 |         39 | random               | dijkstra         | lru             | all               |         5 |
|         606 |         33 | random               | bfs              | fifo            | all               |         5 |
|         604 |         46 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         602 |         33 | random               | dijkstra         | fifo            | all               |         5 |
|         602 |         30 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         601 |         33 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         597 |         37 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         592 |         29 | most_recently_used   | bfs              | lru             | all               |         5 |
|         592 |         29 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         583 |         89 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         578 |         36 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         578 |         71 | random               | dijkstra         | random          | all               |         5 |
|         570 |         24 | random               | bfs              | random          | all               |         5 |
|         570 |         36 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         546 |         17 | most_frequently_used | bfs              | lru             | all               |         5 |
|         545 |         27 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         543 |         67 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         539 |         51 | most_recently_used   | bfs              | random          | all               |         5 |
|         539 |         21 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         536 |         14 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         529 |         63 | most_frequently_used | bfs              | random          | all               |         5 |
|         526 |         31 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         219 |         95 | random               | random           | lfu             | all               |         5 |
|         215 |        103 | random               | random           | random          | all               |         5 |
|         213 |         98 | random               | random           | lru             | all               |         5 |
|         213 |         42 | most_frequently_used | random           | lfu             | all               |         5 |
|         212 |         41 | most_frequently_used | random           | lru             | all               |         5 |
|         203 |         54 | most_recently_added  | random           | random          | all               |         5 |
|         199 |         48 | random               | random           | fifo            | all               |         5 |
|         187 |         62 | most_frequently_used | random           | random          | all               |         5 |
|         184 |         51 | most_recently_used   | random           | lfu             | all               |         5 |
|         174 |         75 | most_recently_added  | random           | lru             | all               |         5 |
|         174 |         61 | most_recently_used   | random           | lru             | all               |         5 |
|         173 |         90 | most_recently_added  | random           | lfu             | all               |         5 |
|         167 |         53 | most_recently_added  | random           | fifo            | all               |         5 |
|         165 |         54 | most_frequently_used | random           | fifo            | all               |         5 |
|         146 |         73 | most_recently_used   | random           | random          | all               |         5 |
|         140 |         46 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 512

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         642 |         27 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         641 |         28 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         641 |         28 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         640 |         26 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         638 |         21 | most_recently_added  | bfs              | random          | all               |         5 |
|         636 |         22 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         633 |         20 | most_recently_added  | bfs              | lru             | all               |         5 |
|         633 |         20 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         611 |         48 | most_recently_used   | bfs              | random          | all               |         5 |
|         611 |         50 | most_recently_used   | bfs              | lru             | all               |         5 |
|         610 |         50 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         609 |         49 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         607 |         46 | random               | dijkstra         | lru             | all               |         5 |
|         607 |         47 | random               | dijkstra         | lfu             | all               |         5 |
|         603 |         37 | random               | dijkstra         | random          | all               |         5 |
|         603 |         41 | random               | dijkstra         | fifo            | all               |         5 |
|         595 |         40 | random               | bfs              | fifo            | all               |         5 |
|         595 |         41 | random               | bfs              | random          | all               |         5 |
|         594 |         42 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         594 |         33 | random               | bfs              | lfu             | all               |         5 |
|         593 |         35 | random               | bfs              | lru             | all               |         5 |
|         591 |         43 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         591 |         43 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         590 |         51 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         584 |         34 | most_frequently_used | bfs              | random          | all               |         5 |
|         580 |         29 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         577 |         29 | most_frequently_used | bfs              | lru             | all               |         5 |
|         577 |         29 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         566 |         41 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         563 |         39 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         558 |         43 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         558 |         43 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         233 |        105 | random               | random           | random          | all               |         5 |
|         230 |        101 | random               | random           | lfu             | all               |         5 |
|         230 |        101 | random               | random           | lru             | all               |         5 |
|         228 |         99 | random               | random           | fifo            | all               |         5 |
|         215 |         57 | most_frequently_used | random           | random          | all               |         5 |
|         213 |         59 | most_frequently_used | random           | lfu             | all               |         5 |
|         213 |         59 | most_frequently_used | random           | lru             | all               |         5 |
|         210 |         55 | most_frequently_used | random           | fifo            | all               |         5 |
|         202 |         72 | most_recently_added  | random           | fifo            | all               |         5 |
|         201 |         72 | most_recently_added  | random           | random          | all               |         5 |
|         201 |         70 | most_recently_added  | random           | lfu             | all               |         5 |
|         201 |         70 | most_recently_added  | random           | lru             | all               |         5 |
|         129 |         42 | most_recently_used   | random           | random          | all               |         5 |
|         128 |         42 | most_recently_used   | random           | lfu             | all               |         5 |
|         127 |         43 | most_recently_used   | random           | lru             | all               |         5 |
|         126 |         40 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 1024

Total configurations: 48

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         644 |         31 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         644 |         31 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         639 |         23 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         639 |         23 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         639 |         23 | most_recently_added  | bfs              | lru             | all               |         5 |
|         639 |         23 | most_recently_added  | bfs              | random          | all               |         5 |
|         614 |         50 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         614 |         50 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         614 |         50 | most_recently_used   | bfs              | lru             | all               |         5 |
|         614 |         50 | most_recently_used   | bfs              | random          | all               |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         602 |         41 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         599 |         43 | random               | dijkstra         | fifo            | all               |         5 |
|         599 |         43 | random               | dijkstra         | lfu             | all               |         5 |
|         599 |         43 | random               | dijkstra         | lru             | all               |         5 |
|         599 |         43 | random               | dijkstra         | random          | all               |         5 |
|         595 |         36 | random               | bfs              | random          | all               |         5 |
|         595 |         36 | random               | bfs              | lru             | all               |         5 |
|         595 |         36 | random               | bfs              | lfu             | all               |         5 |
|         595 |         36 | random               | bfs              | fifo            | all               |         5 |
|         575 |         28 | most_frequently_used | bfs              | random          | all               |         5 |
|         575 |         28 | most_frequently_used | bfs              | lru             | all               |         5 |
|         575 |         28 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         575 |         28 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         559 |         40 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         232 |        103 | random               | random           | fifo            | all               |         5 |
|         232 |        103 | random               | random           | lfu             | all               |         5 |
|         232 |        103 | random               | random           | lru             | all               |         5 |
|         232 |        103 | random               | random           | random          | all               |         5 |
|         218 |         61 | most_frequently_used | random           | fifo            | all               |         5 |
|         218 |         61 | most_frequently_used | random           | lfu             | all               |         5 |
|         218 |         61 | most_frequently_used | random           | lru             | all               |         5 |
|         218 |         61 | most_frequently_used | random           | random          | all               |         5 |
|         213 |         79 | most_recently_added  | random           | fifo            | all               |         5 |
|         213 |         79 | most_recently_added  | random           | lfu             | all               |         5 |
|         213 |         79 | most_recently_added  | random           | lru             | all               |         5 |
|         213 |         79 | most_recently_added  | random           | random          | all               |         5 |
|         125 |         38 | most_recently_used   | random           | fifo            | all               |         5 |
|         125 |         38 | most_recently_used   | random           | lfu             | all               |         5 |
|         125 |         38 | most_recently_used   | random           | lru             | all               |         5 |
|         125 |         38 | most_recently_used   | random           | random          | all               |         5 |

