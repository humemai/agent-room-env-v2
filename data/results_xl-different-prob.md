# Results for xl-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|         667 |         34 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|         659 |         33 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|         658 |         21 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|         652 |         30 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|         642 |         66 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|         640 |         38 | most_recently_used   | bfs              | random          | all               |           512 |         5 |
|         639 |         25 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|         639 |         25 | most_recently_added  | bfs              | random          | all               |          1024 |         5 |
|         639 |         25 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|         639 |         25 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|         638 |         42 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|         638 |         42 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|         638 |         42 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|         638 |         42 | most_recently_used   | bfs              | random          | all               |          1024 |         5 |
|         637 |         46 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|         637 |         47 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|         636 |         36 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|         635 |         25 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|         634 |         44 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|         633 |         24 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|         631 |         61 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | random          | all               |          1024 |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|         631 |         28 | most_recently_added  | bfs              | random          | all               |           512 |         5 |
|         630 |         44 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|         629 |         26 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|         628 |          5 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|         624 |         46 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|         623 |         26 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|         623 |         25 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|         621 |         25 | most_recently_added  | dijkstra         | random          | all               |           512 |         5 |
|         617 |         25 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|         614 |         51 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|         609 |         39 | most_recently_added  | bfs              | random          | all               |           256 |         5 |
|         608 |         49 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|         607 |         58 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|         605 |         50 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|         604 |         30 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|         603 |         61 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|         601 |         33 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|         600 |         35 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | random          | all               |          1024 |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|         598 |         26 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|         598 |         44 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|         597 |         48 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|         597 |         47 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|         596 |         47 | most_recently_used   | dijkstra         | random          | all               |           512 |         5 |
|         594 |         29 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|         594 |         33 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|         593 |         33 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|         592 |         23 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|         591 |         47 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|         587 |         46 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|         586 |         34 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|         584 |         72 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|         583 |         46 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|         581 |         34 | most_frequently_used | bfs              | random          | all               |           512 |         5 |
|         579 |         60 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|         578 |         38 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|         578 |         36 | most_frequently_used | bfs              | random          | all               |          1024 |         5 |
|         578 |         36 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|         578 |         36 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|         578 |         36 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|         578 |         37 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|         577 |         38 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|         568 |         27 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|         562 |         62 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|         557 |         47 | most_recently_added  | dijkstra         | random          | all               |           256 |         5 |
|         552 |         47 | most_frequently_used | dijkstra         | random          | all               |           512 |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | random          | all               |          1024 |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|         550 |         10 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|         550 |         90 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|         549 |         53 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|         544 |         17 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|         543 |         40 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|         542 |        100 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|         542 |         45 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|         542 |         41 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|         542 |         16 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|         539 |         59 | most_frequently_used | bfs              | random          | all               |           256 |         5 |
|         536 |         48 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|         534 |         48 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|         534 |         53 | most_recently_used   | bfs              | random          | all               |           256 |         5 |
|         533 |         23 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|         533 |         38 | most_recently_used   | dijkstra         | random          | all               |           256 |         5 |
|         531 |         47 | most_frequently_used | dijkstra         | random          | all               |           256 |         5 |
|         531 |         41 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|         529 |         29 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|         524 |         89 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|         523 |         51 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|         507 |         32 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|         498 |         35 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|         494 |         32 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|         483 |         41 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|         479 |         63 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|         467 |         24 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|         467 |         20 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|         464 |         29 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|         455 |         18 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|         450 |         24 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|         448 |         26 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|         431 |         34 | most_recently_added  | dijkstra         | random          | all               |           128 |         5 |
|         428 |         70 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|         427 |         58 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|         414 |         60 | most_frequently_used | bfs              | random          | all               |           128 |         5 |
|         411 |         24 | most_recently_used   | bfs              | random          | all               |           128 |         5 |
|         409 |         48 | most_frequently_used | dijkstra         | random          | all               |           128 |         5 |
|         401 |         25 | most_recently_added  | bfs              | random          | all               |           128 |         5 |
|         396 |         88 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|         396 |         45 | most_recently_used   | dijkstra         | random          | all               |           128 |         5 |
|         394 |         93 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|         354 |        116 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|         351 |         72 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|         351 |         45 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|         338 |         24 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|         338 |         62 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|         337 |         33 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|         326 |         48 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|         325 |         24 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|         323 |         21 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|         311 |         43 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|         310 |         43 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|         306 |         24 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|         304 |         21 | most_recently_added  | bfs              | random          | all               |            64 |         5 |
|         303 |         40 | most_frequently_used | bfs              | random          | all               |            64 |         5 |
|         301 |         76 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|         295 |         30 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|         289 |         22 | most_recently_used   | bfs              | random          | all               |            64 |         5 |
|         284 |        116 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|         278 |         84 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|         276 |         33 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|         276 |         43 | most_recently_added  | dijkstra         | random          | all               |            64 |         5 |
|         271 |         52 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|         271 |         74 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|         262 |         28 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|         261 |         36 | most_frequently_used | dijkstra         | random          | all               |            64 |         5 |
|         255 |        158 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|         254 |         76 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|         251 |         74 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|         249 |         43 | most_recently_used   | dijkstra         | random          | all               |            64 |         5 |
|         246 |         25 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|         246 |         35 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|         240 |         75 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|         218 |         61 | most_frequently_used | random           | random          | all               |          1024 |         5 |
|         218 |         61 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|         218 |         61 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|         218 |         61 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|         218 |         42 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|         216 |         95 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|         215 |         57 | most_frequently_used | random           | random          | all               |           512 |         5 |
|         213 |         79 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|         213 |         79 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|         213 |         79 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|         213 |         79 | most_recently_added  | random           | random          | all               |          1024 |         5 |
|         213 |         59 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|         213 |         59 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|         213 |         42 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|         212 |         41 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|         211 |         27 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|         210 |         55 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|         207 |         25 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|         204 |         84 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|         203 |         20 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|         203 |         26 | most_recently_added  | random           | random          | all               |           128 |         5 |
|         203 |         54 | most_recently_added  | random           | random          | all               |           256 |         5 |
|         202 |         72 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|         201 |         72 | most_recently_added  | random           | random          | all               |           512 |         5 |
|         201 |         70 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|         201 |         70 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|         200 |         51 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|         199 |         23 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|         198 |         21 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|         197 |         56 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|         195 |         72 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|         190 |         19 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|         188 |         83 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|         187 |         62 | most_frequently_used | random           | random          | all               |           256 |         5 |
|         187 |         76 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|         187 |         71 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|         184 |         51 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|         180 |         79 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|         180 |         63 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|         178 |         21 | most_frequently_used | bfs              | random          | all               |            32 |         5 |
|         175 |         11 | most_recently_added  | bfs              | random          | all               |            32 |         5 |
|         175 |         78 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|         174 |         75 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|         174 |         61 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|         173 |         90 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|         173 |         20 | most_recently_added  | dijkstra         | random          | all               |            32 |         5 |
|         172 |         48 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|         170 |         90 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|         169 |         27 | most_recently_used   | bfs              | random          | all               |            32 |         5 |
|         168 |         49 | most_frequently_used | random           | random          | all               |           128 |         5 |
|         167 |         53 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|         165 |         42 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|         165 |         54 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|         164 |         14 | most_recently_used   | dijkstra         | random          | all               |            32 |         5 |
|         162 |         68 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|         161 |         69 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|         159 |         55 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|         159 |         65 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|         158 |         28 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|         154 |         35 | most_frequently_used | dijkstra         | random          | all               |            32 |         5 |
|         149 |         21 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|         149 |         20 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|         148 |         15 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|         148 |         15 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|         146 |         73 | most_recently_used   | random           | random          | all               |           256 |         5 |
|         145 |         25 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|         143 |         60 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|         142 |         11 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|         140 |         46 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|         129 |         42 | most_recently_used   | random           | random          | all               |           512 |         5 |
|         129 |        108 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|         128 |         42 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|         127 |         43 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|         126 |         63 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|         126 |          8 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|         126 |         40 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|         125 |         38 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|         125 |          8 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|         125 |         38 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|         125 |         38 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|         125 |         38 | most_recently_used   | random           | random          | all               |          1024 |         5 |
|         124 |         36 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|         123 |         64 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|         123 |         50 | most_frequently_used | random           | random          | all               |            64 |         5 |
|         123 |         10 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|         123 |         10 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|         122 |         33 | most_frequently_used | random           | random          | all               |            32 |         5 |
|         118 |         55 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|         115 |         10 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|         114 |         11 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|         113 |         69 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|         111 |         40 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|         107 |         59 | most_recently_used   | random           | random          | all               |            64 |         5 |
|         107 |         62 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|         106 |         13 | most_frequently_used | bfs              | random          | all               |            16 |         5 |
|         105 |          5 | most_recently_added  | bfs              | random          | all               |            16 |         5 |
|         105 |         65 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|         104 |         71 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|         102 |         48 | most_recently_added  | random           | random          | all               |            64 |         5 |
|         100 |         15 | most_recently_used   | bfs              | random          | all               |            16 |         5 |
|          99 |         41 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|          98 |         40 | most_recently_used   | random           | random          | all               |           128 |         5 |
|          98 |         39 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|          98 |         39 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|          98 |         49 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|          96 |         25 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|          94 |         57 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|          93 |         33 | most_frequently_used | dijkstra         | random          | all               |            16 |         5 |
|          91 |         30 | most_recently_used   | dijkstra         | random          | all               |            16 |         5 |
|          91 |         39 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|          90 |         33 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|          88 |         11 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|          87 |         19 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|          87 |         25 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|          85 |         34 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|          83 |         15 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|          83 |         14 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|          83 |         13 | most_frequently_used | bfs              | random          | all               |             8 |         5 |
|          82 |         17 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|          81 |         35 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|          81 |         25 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|          78 |         21 | most_recently_added  | random           | random          | all               |            32 |         5 |
|          77 |          8 | most_recently_used   | bfs              | random          | all               |             8 |         5 |
|          77 |         25 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|          75 |         31 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|          72 |         15 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|          72 |         15 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|          71 |         17 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|          70 |         16 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|          69 |         16 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|          69 |         16 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|          68 |         23 | most_recently_added  | dijkstra         | random          | all               |            16 |         5 |
|          66 |          5 | most_recently_used   | random           | random          | all               |            16 |         5 |
|          66 |         26 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|          64 |         20 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|          63 |          5 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|          63 |         24 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|          63 |         16 | most_recently_added  | bfs              | random          | all               |             8 |         5 |
|          61 |         25 | most_frequently_used | random           | random          | all               |            16 |         5 |
|          61 |         21 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|          61 |         21 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|          60 |          3 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|          59 |          9 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|          58 |         33 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|          58 |         14 | most_recently_used   | bfs              | random          | all               |             4 |         5 |
|          58 |         14 | most_frequently_used | bfs              | random          | all               |             4 |         5 |
|          58 |         34 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|          57 |          7 | most_recently_used   | dijkstra         | random          | all               |             8 |         5 |
|          56 |         12 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|          56 |          9 | most_frequently_used | dijkstra         | random          | all               |             8 |         5 |
|          56 |         12 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|          55 |         17 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|          55 |         17 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|          54 |         33 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|          52 |         19 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|          52 |         19 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|          52 |         13 | most_recently_added  | random           | random          | all               |            16 |         5 |
|          51 |         29 | most_recently_used   | random           | random          | all               |            32 |         5 |
|          50 |          6 | most_recently_used   | random           | random          | all               |             8 |         5 |
|          50 |         11 | most_recently_added  | dijkstra         | random          | all               |             8 |         5 |
|          48 |         17 | most_recently_added  | bfs              | random          | all               |             4 |         5 |
|          47 |         23 | most_recently_added  | dijkstra         | random          | all               |             4 |         5 |
|          46 |         34 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|          45 |         14 | most_frequently_used | random           | random          | all               |             8 |         5 |
|          45 |         27 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|          45 |         27 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|          44 |         13 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|          43 |         21 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|          42 |         21 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|          41 |         19 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|          40 |         19 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|          40 |         24 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|          40 |         24 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|          39 |         10 | most_recently_added  | bfs              | random          | all               |             2 |         5 |
|          39 |         12 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|          39 |         12 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|          38 |          5 | most_recently_added  | random           | random          | all               |             8 |         5 |
|          38 |         13 | most_recently_added  | random           | random          | all               |             2 |         5 |
|          37 |         19 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|          36 |         17 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|          36 |         21 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|          35 |         19 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|          34 |          9 | most_recently_added  | dijkstra         | random          | all               |             2 |         5 |
|          34 |         13 | most_frequently_used | dijkstra         | random          | all               |             4 |         5 |
|          34 |         13 | most_recently_used   | dijkstra         | random          | all               |             4 |         5 |
|          34 |         20 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|          34 |         20 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|          34 |          9 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|          33 |          8 | most_frequently_used | dijkstra         | random          | all               |             2 |         5 |
|          33 |          8 | most_recently_used   | dijkstra         | random          | all               |             2 |         5 |
|          33 |         15 | most_frequently_used | bfs              | random          | all               |             2 |         5 |
|          33 |         15 | most_recently_used   | bfs              | random          | all               |             2 |         5 |
|          33 |         11 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|          33 |          8 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|          33 |         11 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|          33 |         15 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|          33 |         11 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|          31 |          9 | most_frequently_used | random           | random          | all               |             2 |         5 |
|          31 |          9 | most_recently_used   | random           | random          | all               |             2 |         5 |
|          29 |          8 | most_recently_added  | random           | random          | all               |             4 |         5 |
|          29 |         11 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|          29 |         11 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|          28 |         12 | most_frequently_used | random           | random          | all               |             4 |         5 |
|          28 |         10 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|          27 |          9 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|          26 |          4 | most_recently_used   | random           | random          | all               |             0 |         5 |
|          26 |          4 | most_recently_added  | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | most_recently_added  | random           | random          | all               |             0 |         5 |
|          26 |          4 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|          26 |          4 | most_frequently_used | random           | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | random          | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | bfs              | random          | all               |             0 |         5 |
|          25 |         11 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | random          | all               |             0 |         5 |
|          24 |          8 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|          24 |          8 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|          24 |          9 | most_recently_used   | random           | random          | all               |             4 |         5 |
|          23 |          5 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|          23 |          5 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|          21 |          6 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|          21 |          6 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|          18 |          5 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|          18 |          5 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|          18 |          5 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|          18 |          5 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|          18 |          5 | most_recently_added  | random           | lru             | all               |             0 |         5 |
|          18 |          5 | most_frequently_used | random           | lfu             | all               |             0 |         5 |

## Memory Size 0

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          33 |         11 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_frequently_used | bfs              | lru             | all               |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          33 |         11 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          33 |         11 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          33 |         11 | most_recently_added  | bfs              | lru             | all               |         5 |
|          33 |         11 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          33 |         11 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          33 |         11 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          33 |         11 | most_recently_used   | bfs              | lru             | all               |         5 |
|          26 |          4 | most_recently_added  | random           | random          | all               |         5 |
|          26 |          4 | most_recently_added  | random           | fifo            | all               |         5 |
|          26 |          4 | most_recently_used   | random           | random          | all               |         5 |
|          26 |          4 | most_recently_used   | random           | fifo            | all               |         5 |
|          26 |          4 | most_frequently_used | random           | random          | all               |         5 |
|          26 |          4 | most_frequently_used | random           | fifo            | all               |         5 |
|          25 |         11 | most_frequently_used | bfs              | random          | all               |         5 |
|          25 |         11 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          25 |         11 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          25 |         11 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          25 |         11 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          25 |         11 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          25 |         11 | most_recently_added  | bfs              | random          | all               |         5 |
|          25 |         11 | most_recently_used   | bfs              | random          | all               |         5 |
|          25 |         11 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          18 |          5 | most_frequently_used | random           | lfu             | all               |         5 |
|          18 |          5 | most_frequently_used | random           | lru             | all               |         5 |
|          18 |          5 | most_recently_added  | random           | lfu             | all               |         5 |
|          18 |          5 | most_recently_added  | random           | lru             | all               |         5 |
|          18 |          5 | most_recently_used   | random           | lfu             | all               |         5 |
|          18 |          5 | most_recently_used   | random           | lru             | all               |         5 |

## Memory Size 2

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          98 |         39 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          98 |         39 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          75 |         31 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          58 |         33 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          58 |         34 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          54 |         33 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          52 |         19 | most_frequently_used | bfs              | lru             | all               |         5 |
|          52 |         19 | most_recently_used   | bfs              | lru             | all               |         5 |
|          44 |         13 | most_recently_added  | bfs              | lru             | all               |         5 |
|          41 |         19 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          40 |         24 | most_recently_used   | random           | lfu             | all               |         5 |
|          40 |         24 | most_frequently_used | random           | lfu             | all               |         5 |
|          39 |         10 | most_recently_added  | bfs              | random          | all               |         5 |
|          39 |         12 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          39 |         12 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          38 |         13 | most_recently_added  | random           | random          | all               |         5 |
|          36 |         17 | most_recently_added  | random           | lfu             | all               |         5 |
|          34 |          9 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          34 |         20 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          34 |         20 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          34 |          9 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          33 |          8 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          33 |          8 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          33 |         15 | most_frequently_used | bfs              | random          | all               |         5 |
|          33 |         15 | most_recently_used   | bfs              | random          | all               |         5 |
|          33 |         15 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          33 |          8 | most_recently_added  | random           | lru             | all               |         5 |
|          31 |          9 | most_frequently_used | random           | random          | all               |         5 |
|          31 |          9 | most_recently_used   | random           | random          | all               |         5 |
|          29 |         11 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          29 |         11 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          27 |          9 | most_recently_added  | random           | fifo            | all               |         5 |
|          23 |          5 | most_recently_used   | random           | lru             | all               |         5 |
|          23 |          5 | most_frequently_used | random           | lru             | all               |         5 |
|          21 |          6 | most_frequently_used | random           | fifo            | all               |         5 |
|          21 |          6 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 4

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         162 |         68 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         161 |         69 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         159 |         65 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          99 |         41 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          94 |         57 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          87 |         19 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          85 |         34 | most_frequently_used | random           | lfu             | all               |         5 |
|          83 |         14 | most_recently_added  | random           | lfu             | all               |         5 |
|          81 |         35 | most_recently_used   | random           | lfu             | all               |         5 |
|          69 |         16 | most_recently_used   | bfs              | lru             | all               |         5 |
|          69 |         16 | most_frequently_used | bfs              | lru             | all               |         5 |
|          64 |         20 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          63 |          5 | most_recently_added  | bfs              | lru             | all               |         5 |
|          61 |         21 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          61 |         21 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          60 |          3 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          59 |          9 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          58 |         14 | most_frequently_used | bfs              | random          | all               |         5 |
|          58 |         14 | most_recently_used   | bfs              | random          | all               |         5 |
|          56 |         12 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          56 |         12 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          55 |         17 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          55 |         17 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          48 |         17 | most_recently_added  | bfs              | random          | all               |         5 |
|          47 |         23 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          45 |         27 | most_recently_used   | random           | lru             | all               |         5 |
|          45 |         27 | most_frequently_used | random           | lru             | all               |         5 |
|          43 |         21 | most_recently_added  | random           | lru             | all               |         5 |
|          34 |         13 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          34 |         13 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          29 |          8 | most_recently_added  | random           | random          | all               |         5 |
|          28 |         12 | most_frequently_used | random           | random          | all               |         5 |
|          28 |         10 | most_recently_added  | random           | fifo            | all               |         5 |
|          24 |          8 | most_frequently_used | random           | fifo            | all               |         5 |
|          24 |          8 | most_recently_used   | random           | fifo            | all               |         5 |
|          24 |          9 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 8

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         311 |         43 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         278 |         84 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         276 |         33 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         251 |         74 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         240 |         75 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         180 |         63 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         158 |         28 | most_recently_added  | bfs              | lru             | all               |         5 |
|         149 |         21 | most_frequently_used | bfs              | lru             | all               |         5 |
|         149 |         20 | most_recently_used   | bfs              | lru             | all               |         5 |
|         148 |         15 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         148 |         15 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         142 |         11 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         118 |         55 | most_recently_added  | random           | lfu             | all               |         5 |
|         107 |         62 | most_frequently_used | random           | lfu             | all               |         5 |
|          98 |         49 | most_recently_used   | random           | lfu             | all               |         5 |
|          88 |         11 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          83 |         15 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          83 |         13 | most_frequently_used | bfs              | random          | all               |         5 |
|          77 |          8 | most_recently_used   | bfs              | random          | all               |         5 |
|          72 |         15 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          72 |         15 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          71 |         17 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          70 |         16 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          63 |         16 | most_recently_added  | bfs              | random          | all               |         5 |
|          57 |          7 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          56 |          9 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          50 |          6 | most_recently_used   | random           | random          | all               |         5 |
|          50 |         11 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          46 |         34 | most_recently_used   | random           | lru             | all               |         5 |
|          45 |         14 | most_frequently_used | random           | random          | all               |         5 |
|          42 |         21 | most_frequently_used | random           | lru             | all               |         5 |
|          40 |         19 | most_recently_added  | random           | fifo            | all               |         5 |
|          38 |          5 | most_recently_added  | random           | random          | all               |         5 |
|          37 |         19 | most_recently_used   | random           | fifo            | all               |         5 |
|          36 |         21 | most_recently_added  | random           | lru             | all               |         5 |
|          35 |         19 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 16

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         354 |        116 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         351 |         45 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         338 |         62 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         310 |         43 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         301 |         76 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         295 |         30 | most_recently_added  | bfs              | lru             | all               |         5 |
|         284 |        116 | most_frequently_used | random           | lfu             | all               |         5 |
|         271 |         52 | most_frequently_used | bfs              | lru             | all               |         5 |
|         262 |         28 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         255 |        158 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         254 |         76 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         246 |         35 | most_recently_used   | bfs              | lru             | all               |         5 |
|         197 |         56 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         159 |         55 | most_recently_added  | random           | lfu             | all               |         5 |
|         143 |         60 | most_recently_used   | random           | lfu             | all               |         5 |
|         126 |          8 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         125 |          8 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         123 |         10 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         123 |         10 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         115 |         10 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         114 |         11 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         106 |         13 | most_frequently_used | bfs              | random          | all               |         5 |
|         105 |          5 | most_recently_added  | bfs              | random          | all               |         5 |
|         105 |         65 | most_recently_added  | random           | lru             | all               |         5 |
|         104 |         71 | most_recently_used   | random           | lru             | all               |         5 |
|         100 |         15 | most_recently_used   | bfs              | random          | all               |         5 |
|          93 |         33 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          91 |         30 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          90 |         33 | most_frequently_used | random           | lru             | all               |         5 |
|          81 |         25 | most_frequently_used | random           | fifo            | all               |         5 |
|          68 |         23 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          66 |          5 | most_recently_used   | random           | random          | all               |         5 |
|          66 |         26 | most_recently_added  | random           | fifo            | all               |         5 |
|          63 |         24 | most_recently_used   | random           | fifo            | all               |         5 |
|          61 |         25 | most_frequently_used | random           | random          | all               |         5 |
|          52 |         13 | most_recently_added  | random           | random          | all               |         5 |

## Memory Size 32

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         529 |         29 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         523 |         51 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         494 |         32 | most_recently_used   | bfs              | lru             | all               |         5 |
|         483 |         41 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         479 |         63 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         467 |         20 | most_recently_added  | bfs              | lru             | all               |         5 |
|         450 |         24 | most_frequently_used | bfs              | lru             | all               |         5 |
|         428 |         70 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         427 |         58 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         396 |         88 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         394 |         93 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         351 |         72 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         246 |         25 | most_recently_added  | random           | lfu             | all               |         5 |
|         211 |         27 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         207 |         25 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         204 |         84 | most_frequently_used | random           | lru             | all               |         5 |
|         203 |         20 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         200 |         51 | most_recently_added  | random           | lru             | all               |         5 |
|         199 |         23 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         198 |         21 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         190 |         19 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         187 |         76 | most_frequently_used | random           | lfu             | all               |         5 |
|         178 |         21 | most_frequently_used | bfs              | random          | all               |         5 |
|         175 |         11 | most_recently_added  | bfs              | random          | all               |         5 |
|         173 |         20 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         169 |         27 | most_recently_used   | bfs              | random          | all               |         5 |
|         164 |         14 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         154 |         35 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         124 |         36 | most_recently_used   | random           | lfu             | all               |         5 |
|         123 |         64 | most_recently_used   | random           | lru             | all               |         5 |
|         122 |         33 | most_frequently_used | random           | random          | all               |         5 |
|          96 |         25 | most_frequently_used | random           | fifo            | all               |         5 |
|          82 |         17 | most_recently_added  | random           | fifo            | all               |         5 |
|          78 |         21 | most_recently_added  | random           | random          | all               |         5 |
|          77 |         25 | most_recently_used   | random           | fifo            | all               |         5 |
|          51 |         29 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 64

Total configurations: 36

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
|         550 |         90 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         549 |         53 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         536 |         48 | most_frequently_used | bfs              | lru             | all               |         5 |
|         524 |         89 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         338 |         24 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         337 |         33 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         326 |         48 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         325 |         24 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         323 |         21 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         306 |         24 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         304 |         21 | most_recently_added  | bfs              | random          | all               |         5 |
|         303 |         40 | most_frequently_used | bfs              | random          | all               |         5 |
|         289 |         22 | most_recently_used   | bfs              | random          | all               |         5 |
|         276 |         43 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         261 |         36 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         249 |         43 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         218 |         42 | most_frequently_used | random           | lfu             | all               |         5 |
|         188 |         83 | most_recently_added  | random           | lfu             | all               |         5 |
|         180 |         79 | most_frequently_used | random           | lru             | all               |         5 |
|         175 |         78 | most_recently_used   | random           | lru             | all               |         5 |
|         129 |        108 | most_recently_added  | random           | lru             | all               |         5 |
|         123 |         50 | most_frequently_used | random           | random          | all               |         5 |
|         113 |         69 | most_recently_used   | random           | lfu             | all               |         5 |
|         111 |         40 | most_frequently_used | random           | fifo            | all               |         5 |
|         107 |         59 | most_recently_used   | random           | random          | all               |         5 |
|         102 |         48 | most_recently_added  | random           | random          | all               |         5 |
|          91 |         39 | most_recently_used   | random           | fifo            | all               |         5 |
|          87 |         25 | most_recently_added  | random           | fifo            | all               |         5 |

## Memory Size 128

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         642 |         66 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         634 |         44 | most_recently_added  | bfs              | lru             | all               |         5 |
|         631 |         61 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         630 |         44 | most_recently_used   | bfs              | lru             | all               |         5 |
|         607 |         58 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         603 |         61 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         584 |         72 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         579 |         60 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         562 |         62 | most_frequently_used | bfs              | lru             | all               |         5 |
|         542 |        100 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         534 |         48 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         531 |         41 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         507 |         32 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         498 |         35 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         467 |         24 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         464 |         29 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         455 |         18 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         448 |         26 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         431 |         34 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         414 |         60 | most_frequently_used | bfs              | random          | all               |         5 |
|         411 |         24 | most_recently_used   | bfs              | random          | all               |         5 |
|         409 |         48 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         401 |         25 | most_recently_added  | bfs              | random          | all               |         5 |
|         396 |         45 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         271 |         74 | most_recently_added  | random           | lfu             | all               |         5 |
|         216 |         95 | most_recently_added  | random           | lru             | all               |         5 |
|         203 |         26 | most_recently_added  | random           | random          | all               |         5 |
|         195 |         72 | most_recently_added  | random           | fifo            | all               |         5 |
|         187 |         71 | most_frequently_used | random           | lfu             | all               |         5 |
|         172 |         48 | most_frequently_used | random           | lru             | all               |         5 |
|         170 |         90 | most_recently_used   | random           | lru             | all               |         5 |
|         168 |         49 | most_frequently_used | random           | random          | all               |         5 |
|         165 |         42 | most_frequently_used | random           | fifo            | all               |         5 |
|         145 |         25 | most_recently_used   | random           | fifo            | all               |         5 |
|         126 |         63 | most_recently_used   | random           | lfu             | all               |         5 |
|          98 |         40 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 256

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         667 |         34 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         659 |         33 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         658 |         21 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         652 |         30 | most_recently_added  | bfs              | lru             | all               |         5 |
|         628 |          5 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         609 |         39 | most_recently_added  | bfs              | random          | all               |         5 |
|         605 |         50 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         604 |         30 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         601 |         33 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         600 |         35 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         598 |         44 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         594 |         29 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         593 |         33 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         592 |         23 | most_recently_used   | bfs              | lru             | all               |         5 |
|         586 |         34 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         557 |         47 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         550 |         10 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         544 |         17 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         542 |         16 | most_frequently_used | bfs              | lru             | all               |         5 |
|         539 |         59 | most_frequently_used | bfs              | random          | all               |         5 |
|         534 |         53 | most_recently_used   | bfs              | random          | all               |         5 |
|         533 |         23 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         533 |         38 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         531 |         47 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         213 |         42 | most_frequently_used | random           | lfu             | all               |         5 |
|         212 |         41 | most_frequently_used | random           | lru             | all               |         5 |
|         203 |         54 | most_recently_added  | random           | random          | all               |         5 |
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

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         640 |         38 | most_recently_used   | bfs              | random          | all               |         5 |
|         637 |         46 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         637 |         47 | most_recently_used   | bfs              | lru             | all               |         5 |
|         636 |         36 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         635 |         25 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         633 |         24 | most_recently_added  | bfs              | lru             | all               |         5 |
|         631 |         28 | most_recently_added  | bfs              | random          | all               |         5 |
|         629 |         26 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         623 |         26 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         623 |         25 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         621 |         25 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         617 |         25 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         597 |         48 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         597 |         47 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         596 |         47 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         591 |         47 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         581 |         34 | most_frequently_used | bfs              | random          | all               |         5 |
|         578 |         38 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         578 |         37 | most_frequently_used | bfs              | lru             | all               |         5 |
|         577 |         38 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         552 |         47 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         543 |         40 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         542 |         45 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         542 |         41 | most_frequently_used | dijkstra         | lru             | all               |         5 |
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

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         639 |         25 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         639 |         25 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         639 |         25 | most_recently_added  | bfs              | lru             | all               |         5 |
|         639 |         25 | most_recently_added  | bfs              | random          | all               |         5 |
|         638 |         42 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         638 |         42 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         638 |         42 | most_recently_used   | bfs              | lru             | all               |         5 |
|         638 |         42 | most_recently_used   | bfs              | random          | all               |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         631 |         25 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         599 |         44 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         578 |         36 | most_frequently_used | bfs              | random          | all               |         5 |
|         578 |         36 | most_frequently_used | bfs              | lru             | all               |         5 |
|         578 |         36 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         578 |         36 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         551 |         49 | most_frequently_used | dijkstra         | random          | all               |         5 |
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

