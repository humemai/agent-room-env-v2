# Results for xxl-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|         433 |         61 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|         432 |         61 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|         431 |         59 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|         431 |         59 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|         431 |         59 | most_recently_used   | bfs              | random          | all               |          1024 |         5 |
|         431 |         59 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|         427 |         59 | most_recently_used   | bfs              | random          | all               |           512 |         5 |
|         422 |         59 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|         415 |         73 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|         415 |         60 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | random          | all               |          1024 |         5 |
|         398 |         69 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|         398 |         65 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|         398 |         65 | most_frequently_used | bfs              | random          | all               |          1024 |         5 |
|         398 |         65 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|         398 |         65 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|         397 |         35 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|         396 |         69 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|         395 |         67 | most_frequently_used | bfs              | random          | all               |           512 |         5 |
|         394 |         92 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|         394 |         93 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|         392 |         68 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|         391 |         90 | most_recently_used   | dijkstra         | random          | all               |           512 |         5 |
|         391 |         91 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | random          | all               |          1024 |         5 |
|         383 |         68 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|         383 |         68 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|         382 |         69 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|         378 |         64 | most_recently_added  | dijkstra         | random          | all               |           512 |         5 |
|         375 |         45 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|         370 |         59 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|         370 |         59 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|         370 |         59 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|         370 |         59 | most_recently_added  | bfs              | random          | all               |          1024 |         5 |
|         368 |         65 | most_recently_added  | bfs              | random          | all               |           512 |         5 |
|         367 |         61 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|         367 |         61 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|         366 |         63 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|         365 |         81 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|         364 |         77 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|         363 |         78 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|         361 |         48 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|         359 |        111 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | random          | all               |          1024 |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|         354 |         38 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|         352 |        101 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|         351 |         74 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|         349 |         74 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|         349 |         70 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|         347 |        114 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|         347 |         73 | most_frequently_used | dijkstra         | random          | all               |           512 |         5 |
|         343 |         57 | most_recently_used   | bfs              | random          | all               |           256 |         5 |
|         340 |         22 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|         340 |         63 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|         339 |         72 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|         331 |         81 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|         331 |         95 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|         330 |         84 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|         324 |        102 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|         323 |         54 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|         318 |         77 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|         315 |        101 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|         314 |         73 | most_frequently_used | bfs              | random          | all               |           256 |         5 |
|         312 |         57 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|         311 |         78 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|         311 |         54 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|         309 |         68 | most_frequently_used | dijkstra         | random          | all               |           256 |         5 |
|         307 |         50 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|         306 |         50 | most_recently_added  | bfs              | random          | all               |           256 |         5 |
|         305 |         56 | most_recently_used   | dijkstra         | random          | all               |           256 |         5 |
|         298 |         48 | most_recently_added  | dijkstra         | random          | all               |           256 |         5 |
|         297 |         75 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|         293 |         91 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|         285 |         52 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|         277 |         67 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|         271 |         85 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|         271 |         36 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|         270 |         85 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|         266 |         65 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|         258 |         87 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|         254 |         85 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|         253 |         69 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|         242 |         44 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|         238 |         34 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|         237 |         66 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|         233 |         45 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|         232 |         26 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|         227 |         29 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|         222 |         26 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|         219 |         26 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|         218 |         38 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|         206 |         53 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|         204 |         45 | most_frequently_used | bfs              | random          | all               |           128 |         5 |
|         198 |         40 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|         194 |         43 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|         193 |         56 | most_recently_added  | dijkstra         | random          | all               |           128 |         5 |
|         191 |         50 | most_recently_added  | bfs              | random          | all               |           128 |         5 |
|         188 |         63 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|         185 |         51 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|         183 |         52 | most_recently_used   | bfs              | random          | all               |           128 |         5 |
|         171 |         48 | most_frequently_used | dijkstra         | random          | all               |           128 |         5 |
|         165 |         39 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|         165 |         44 | most_recently_used   | dijkstra         | random          | all               |           128 |         5 |
|         164 |         37 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|         157 |         36 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|         139 |         28 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|         139 |         22 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|         137 |         22 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|         136 |         35 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|         134 |         23 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|         130 |         18 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|         127 |         23 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|         126 |         36 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|         124 |         19 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|         123 |         24 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|         122 |         37 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|         121 |         17 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|         120 |         17 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|         113 |         25 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|         112 |         20 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|         111 |         34 | most_recently_used   | bfs              | random          | all               |            64 |         5 |
|         111 |         27 | most_recently_added  | bfs              | random          | all               |            64 |         5 |
|         110 |         41 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|         110 |         40 | most_recently_added  | dijkstra         | random          | all               |            64 |         5 |
|         109 |         30 | most_frequently_used | bfs              | random          | all               |            64 |         5 |
|         105 |         54 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|         104 |         17 | most_frequently_used | dijkstra         | random          | all               |            64 |         5 |
|         100 |         35 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|          98 |         52 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|          97 |         23 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|          97 |         35 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|          96 |         39 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|          95 |         29 | most_recently_used   | dijkstra         | random          | all               |            64 |         5 |
|          95 |         36 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|          93 |         25 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|          92 |         25 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|          91 |         13 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|          91 |         32 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|          91 |         32 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|          90 |         30 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|          89 |         17 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|          89 |         18 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|          87 |         29 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|          87 |         29 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|          87 |         29 | most_frequently_used | random           | random          | all               |          1024 |         5 |
|          87 |         29 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|          87 |         28 | most_frequently_used | random           | random          | all               |           512 |         5 |
|          87 |         34 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|          87 |         13 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|          84 |         14 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|          84 |         34 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|          84 |         11 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|          84 |         29 | most_frequently_used | random           | random          | all               |           256 |         5 |
|          83 |          9 | most_recently_added  | random           | random          | all               |           512 |         5 |
|          83 |         20 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|          83 |         45 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|          82 |         18 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|          82 |         24 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|          82 |          9 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|          82 |         30 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|          81 |         13 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|          80 |         19 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|          80 |         20 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|          80 |          8 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|          80 |          8 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|          80 |          8 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|          80 |          8 | most_recently_added  | random           | random          | all               |          1024 |         5 |
|          80 |         16 | most_recently_added  | random           | random          | all               |           256 |         5 |
|          78 |         13 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|          78 |         20 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|          78 |         20 | most_recently_used   | random           | random          | all               |          1024 |         5 |
|          78 |         20 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|          78 |         20 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|          78 |         11 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|          77 |         38 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|          77 |         22 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|          77 |         33 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|          77 |         15 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|          76 |         15 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|          76 |         22 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|          76 |         23 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|          75 |         15 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|          75 |         16 | most_recently_used   | random           | random          | all               |           512 |         5 |
|          75 |         13 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|          74 |         18 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|          73 |          8 | most_frequently_used | random           | random          | all               |           128 |         5 |
|          72 |         12 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|          71 |         15 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|          70 |          6 | most_recently_used   | random           | random          | all               |           256 |         5 |
|          70 |         11 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|          70 |         29 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|          70 |         20 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|          69 |          8 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|          68 |         20 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|          68 |         10 | most_recently_added  | bfs              | random          | all               |            32 |         5 |
|          68 |         28 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|          65 |         12 | most_recently_added  | random           | random          | all               |           128 |         5 |
|          64 |         21 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|          63 |         23 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|          63 |         16 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|          62 |          6 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|          62 |         20 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|          61 |          8 | most_frequently_used | bfs              | random          | all               |            32 |         5 |
|          60 |         11 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|          60 |         10 | most_recently_used   | dijkstra         | random          | all               |            32 |         5 |
|          60 |         14 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|          60 |         26 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|          59 |         11 | most_frequently_used | dijkstra         | random          | all               |            32 |         5 |
|          59 |          6 | most_frequently_used | random           | random          | all               |            64 |         5 |
|          58 |         12 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|          58 |         24 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|          58 |         13 | most_recently_used   | bfs              | random          | all               |            32 |         5 |
|          58 |         18 | most_recently_added  | random           | random          | all               |            64 |         5 |
|          57 |         33 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|          56 |          7 | most_recently_used   | random           | random          | all               |            64 |         5 |
|          56 |         22 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|          55 |         18 | most_recently_used   | random           | random          | all               |           128 |         5 |
|          55 |         20 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|          52 |         28 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|          52 |         16 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|          52 |         24 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|          52 |         16 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|          51 |         18 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|          51 |         13 | most_recently_added  | dijkstra         | random          | all               |            32 |         5 |
|          50 |          8 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|          49 |          8 | most_recently_used   | random           | random          | all               |            32 |         5 |
|          49 |          8 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|          48 |         11 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|          48 |          9 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|          48 |         14 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|          48 |          3 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|          47 |         17 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|          47 |         13 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|          46 |         13 | most_frequently_used | bfs              | random          | all               |            16 |         5 |
|          45 |         13 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|          45 |         12 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|          45 |         25 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|          44 |          9 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|          44 |         16 | most_recently_used   | bfs              | random          | all               |            16 |         5 |
|          43 |          8 | most_recently_added  | bfs              | random          | all               |            16 |         5 |
|          42 |         13 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|          42 |         13 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|          41 |         14 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|          41 |         15 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|          41 |          9 | most_frequently_used | dijkstra         | random          | all               |            16 |         5 |
|          40 |         13 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|          40 |          5 | most_recently_used   | dijkstra         | random          | all               |            16 |         5 |
|          39 |         10 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|          38 |         17 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|          38 |         10 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|          37 |         13 | most_recently_added  | dijkstra         | random          | all               |            16 |         5 |
|          37 |          6 | most_recently_added  | random           | random          | all               |            32 |         5 |
|          37 |         18 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|          36 |          6 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|          35 |         12 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|          35 |         15 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|          34 |         13 | most_frequently_used | random           | random          | all               |            32 |         5 |
|          33 |         14 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|          32 |         15 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|          32 |          7 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|          31 |          6 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|          31 |         12 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|          31 |         13 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|          30 |          5 | most_recently_used   | random           | random          | all               |            16 |         5 |
|          30 |          8 | most_frequently_used | dijkstra         | random          | all               |             8 |         5 |
|          29 |          9 | most_frequently_used | bfs              | random          | all               |             8 |         5 |
|          29 |         11 | most_recently_used   | dijkstra         | random          | all               |             8 |         5 |
|          29 |          8 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|          29 |         19 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|          29 |         19 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|          29 |          8 | most_recently_added  | random           | random          | all               |            16 |         5 |
|          28 |          8 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|          28 |          9 | most_frequently_used | random           | random          | all               |            16 |         5 |
|          27 |          9 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|          27 |          9 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|          27 |         11 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|          27 |          7 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|          27 |          7 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|          27 |         13 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|          27 |          4 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|          27 |          8 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|          27 |          8 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|          26 |          8 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|          26 |          5 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|          26 |         15 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|          26 |          5 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|          25 |         12 | most_recently_added  | bfs              | random          | all               |             8 |         5 |
|          25 |          5 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|          25 |         15 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|          25 |         19 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|          25 |         19 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|          24 |          3 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|          24 |          6 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|          24 |          9 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|          24 |          6 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|          23 |          7 | most_recently_used   | bfs              | random          | all               |             8 |         5 |
|          23 |          9 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|          23 |          7 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|          23 |          7 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|          22 |          2 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|          22 |          6 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|          22 |          6 | most_frequently_used | random           | random          | all               |             4 |         5 |
|          22 |          6 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|          22 |          8 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|          22 |          8 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|          21 |         12 | most_frequently_used | random           | random          | all               |             8 |         5 |
|          21 |          5 | most_recently_used   | random           | random          | all               |             4 |         5 |
|          21 |          6 | most_recently_added  | dijkstra         | random          | all               |             8 |         5 |
|          21 |          4 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|          20 |          4 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|          20 |          6 | most_recently_added  | bfs              | random          | all               |             4 |         5 |
|          20 |          5 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|          20 |          5 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|          19 |          7 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|          19 |          3 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|          19 |          3 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|          18 |         11 | most_recently_added  | random           | random          | all               |             8 |         5 |
|          18 |          5 | most_recently_used   | random           | random          | all               |             2 |         5 |
|          18 |          5 | most_frequently_used | random           | random          | all               |             2 |         5 |
|          18 |          9 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|          18 |         10 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|          18 |         10 | most_frequently_used | random           | lfu             | all               |             0 |         5 |
|          18 |         10 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|          18 |         10 | most_recently_added  | random           | lru             | all               |             0 |         5 |
|          18 |         10 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|          18 |         10 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|          18 |          9 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|          18 |          4 | most_recently_used   | bfs              | random          | all               |             4 |         5 |
|          18 |          4 | most_frequently_used | bfs              | random          | all               |             4 |         5 |
|          18 |          2 | most_recently_added  | dijkstra         | random          | all               |             4 |         5 |
|          17 |          6 | most_frequently_used | dijkstra         | random          | all               |             4 |         5 |
|          17 |          6 | most_recently_used   | dijkstra         | random          | all               |             4 |         5 |
|          17 |          6 | most_recently_added  | dijkstra         | random          | all               |             2 |         5 |
|          17 |          6 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|          16 |          5 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|          16 |          5 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|          16 |          4 | most_recently_added  | random           | random          | all               |             4 |         5 |
|          16 |          9 | most_recently_added  | random           | random          | all               |             2 |         5 |
|          16 |          8 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|          16 |          8 | most_recently_used   | random           | random          | all               |             8 |         5 |
|          16 |          8 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|          16 |          3 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|          16 |          3 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|          16 |          5 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|          15 |          8 | most_recently_used   | dijkstra         | random          | all               |             2 |         5 |
|          15 |          8 | most_frequently_used | dijkstra         | random          | all               |             2 |         5 |
|          15 |          7 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|          15 |          4 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|          15 |          4 | most_recently_used   | bfs              | random          | all               |             2 |         5 |
|          15 |          4 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|          15 |          4 | most_frequently_used | bfs              | random          | all               |             2 |         5 |
|          15 |          2 | most_recently_added  | bfs              | random          | all               |             2 |         5 |
|          14 |          5 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|          13 |          6 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|          13 |          6 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|          13 |          6 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|          13 |          6 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|          13 |          6 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|          13 |          6 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|          13 |          6 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|          13 |          6 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|          13 |          6 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|          13 |          6 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|          13 |          6 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|          13 |          6 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|          11 |          1 | most_recently_used   | bfs              | random          | all               |             0 |         5 |
|          11 |          1 | most_recently_added  | dijkstra         | random          | all               |             0 |         5 |
|          11 |          1 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|          11 |          1 | most_recently_used   | dijkstra         | random          | all               |             0 |         5 |
|          11 |          1 | most_frequently_used | dijkstra         | random          | all               |             0 |         5 |
|          11 |          1 | most_frequently_used | bfs              | random          | all               |             0 |         5 |
|          11 |          1 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|          11 |          1 | most_recently_added  | bfs              | random          | all               |             0 |         5 |
|          11 |          1 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|          11 |          1 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|          11 |          1 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|          11 |          1 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|           9 |          4 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|           9 |          4 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|           9 |          3 | most_recently_used   | random           | random          | all               |             0 |         5 |
|           9 |          3 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|           9 |          4 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|           9 |          3 | most_recently_added  | random           | random          | all               |             0 |         5 |
|           9 |          4 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|           9 |          3 | most_frequently_used | random           | random          | all               |             0 |         5 |
|           9 |          3 | most_recently_added  | random           | fifo            | all               |             0 |         5 |
|           9 |          3 | most_recently_used   | random           | fifo            | all               |             0 |         5 |

## Memory Size 0

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          18 |         10 | most_recently_added  | random           | lfu             | all               |         5 |
|          18 |         10 | most_recently_added  | random           | lru             | all               |         5 |
|          18 |         10 | most_frequently_used | random           | lfu             | all               |         5 |
|          18 |         10 | most_frequently_used | random           | lru             | all               |         5 |
|          18 |         10 | most_recently_used   | random           | lru             | all               |         5 |
|          18 |         10 | most_recently_used   | random           | lfu             | all               |         5 |
|          13 |          6 | most_frequently_used | bfs              | lru             | all               |         5 |
|          13 |          6 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          13 |          6 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          13 |          6 | most_recently_used   | bfs              | lru             | all               |         5 |
|          13 |          6 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          13 |          6 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          13 |          6 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          13 |          6 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          13 |          6 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          13 |          6 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          13 |          6 | most_recently_added  | bfs              | lru             | all               |         5 |
|          13 |          6 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          11 |          1 | most_frequently_used | bfs              | random          | all               |         5 |
|          11 |          1 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          11 |          1 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          11 |          1 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          11 |          1 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          11 |          1 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          11 |          1 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          11 |          1 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          11 |          1 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          11 |          1 | most_recently_added  | bfs              | random          | all               |         5 |
|          11 |          1 | most_recently_used   | bfs              | random          | all               |         5 |
|          11 |          1 | most_recently_used   | bfs              | fifo            | all               |         5 |
|           9 |          3 | most_frequently_used | random           | fifo            | all               |         5 |
|           9 |          3 | most_frequently_used | random           | random          | all               |         5 |
|           9 |          3 | most_recently_added  | random           | fifo            | all               |         5 |
|           9 |          3 | most_recently_added  | random           | random          | all               |         5 |
|           9 |          3 | most_recently_used   | random           | fifo            | all               |         5 |
|           9 |          3 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 2

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          41 |         15 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          37 |         18 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          29 |         19 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          29 |         19 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          26 |         15 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          25 |         15 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          25 |         19 | most_frequently_used | random           | lfu             | all               |         5 |
|          25 |         19 | most_recently_used   | random           | lfu             | all               |         5 |
|          21 |          4 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          20 |          4 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          19 |          3 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          19 |          3 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          18 |          5 | most_frequently_used | random           | random          | all               |         5 |
|          18 |          5 | most_recently_used   | random           | random          | all               |         5 |
|          17 |          6 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          17 |          6 | most_recently_added  | bfs              | lru             | all               |         5 |
|          16 |          5 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          16 |          5 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          16 |          9 | most_recently_added  | random           | random          | all               |         5 |
|          16 |          8 | most_frequently_used | random           | fifo            | all               |         5 |
|          16 |          8 | most_recently_used   | random           | fifo            | all               |         5 |
|          16 |          3 | most_frequently_used | bfs              | lru             | all               |         5 |
|          16 |          3 | most_recently_used   | bfs              | lru             | all               |         5 |
|          15 |          8 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          15 |          8 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          15 |          4 | most_frequently_used | bfs              | random          | all               |         5 |
|          15 |          4 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          15 |          7 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          15 |          4 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          15 |          4 | most_recently_used   | bfs              | random          | all               |         5 |
|          15 |          2 | most_recently_added  | bfs              | random          | all               |         5 |
|          14 |          5 | most_recently_added  | random           | fifo            | all               |         5 |
|           9 |          4 | most_recently_added  | random           | lfu             | all               |         5 |
|           9 |          4 | most_frequently_used | random           | lru             | all               |         5 |
|           9 |          4 | most_recently_added  | random           | lru             | all               |         5 |
|           9 |          4 | most_recently_used   | random           | lru             | all               |         5 |

## Memory Size 4

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          64 |         21 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          52 |         24 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          49 |          8 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          48 |         14 | most_frequently_used | random           | lfu             | all               |         5 |
|          47 |         17 | most_recently_used   | random           | lfu             | all               |         5 |
|          45 |         25 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          38 |         17 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          35 |         12 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          32 |          7 | most_recently_added  | random           | lfu             | all               |         5 |
|          31 |          6 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          27 |          9 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          27 |          9 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          27 |          8 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          27 |          8 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          24 |          3 | most_recently_added  | bfs              | lru             | all               |         5 |
|          24 |          6 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          23 |          7 | most_frequently_used | bfs              | lru             | all               |         5 |
|          23 |          7 | most_recently_used   | bfs              | lru             | all               |         5 |
|          22 |          2 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          22 |          6 | most_frequently_used | random           | random          | all               |         5 |
|          22 |          8 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          22 |          8 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          22 |          6 | most_recently_added  | random           | lru             | all               |         5 |
|          21 |          5 | most_recently_used   | random           | random          | all               |         5 |
|          20 |          5 | most_recently_used   | random           | fifo            | all               |         5 |
|          20 |          5 | most_frequently_used | random           | fifo            | all               |         5 |
|          20 |          6 | most_recently_added  | bfs              | random          | all               |         5 |
|          18 |          9 | most_frequently_used | random           | lru             | all               |         5 |
|          18 |          9 | most_recently_used   | random           | lru             | all               |         5 |
|          18 |          4 | most_frequently_used | bfs              | random          | all               |         5 |
|          18 |          4 | most_recently_used   | bfs              | random          | all               |         5 |
|          18 |          2 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          17 |          6 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          17 |          6 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          16 |          4 | most_recently_added  | random           | random          | all               |         5 |
|          16 |          5 | most_recently_added  | random           | fifo            | all               |         5 |

## Memory Size 8

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|          95 |         36 | most_frequently_used | bfs              | lfu             | all               |         5 |
|          83 |         45 | most_recently_added  | bfs              | lfu             | all               |         5 |
|          76 |         22 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          70 |         29 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          68 |         28 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          57 |         33 | most_recently_added  | random           | lfu             | all               |         5 |
|          55 |         20 | most_frequently_used | random           | lfu             | all               |         5 |
|          52 |         28 | most_recently_used   | random           | lfu             | all               |         5 |
|          52 |         16 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|          42 |         13 | most_recently_used   | bfs              | lru             | all               |         5 |
|          42 |         13 | most_frequently_used | bfs              | lru             | all               |         5 |
|          40 |         13 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          39 |         10 | most_recently_added  | bfs              | lru             | all               |         5 |
|          38 |         10 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          36 |          6 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          30 |          8 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          29 |         11 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          29 |          9 | most_frequently_used | bfs              | random          | all               |         5 |
|          28 |          8 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          27 |         11 | most_recently_added  | random           | lru             | all               |         5 |
|          27 |          7 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          27 |          7 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          27 |          4 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          26 |          5 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          26 |          5 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          25 |         12 | most_recently_added  | bfs              | random          | all               |         5 |
|          25 |          5 | most_recently_added  | random           | fifo            | all               |         5 |
|          24 |          9 | most_recently_used   | random           | fifo            | all               |         5 |
|          23 |          7 | most_recently_used   | bfs              | random          | all               |         5 |
|          23 |          9 | most_frequently_used | random           | fifo            | all               |         5 |
|          22 |          6 | most_recently_used   | random           | lru             | all               |         5 |
|          21 |         12 | most_frequently_used | random           | random          | all               |         5 |
|          21 |          6 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          19 |          7 | most_frequently_used | random           | lru             | all               |         5 |
|          18 |         11 | most_recently_added  | random           | random          | all               |         5 |
|          16 |          8 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 16

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         122 |         37 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         113 |         25 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         112 |         20 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         105 |         54 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         100 |         35 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|          96 |         39 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|          75 |         13 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|          74 |         18 | most_frequently_used | bfs              | lru             | all               |         5 |
|          70 |         20 | most_recently_used   | bfs              | lru             | all               |         5 |
|          69 |          8 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|          60 |         11 | most_recently_added  | bfs              | lru             | all               |         5 |
|          58 |         12 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|          58 |         24 | most_recently_added  | random           | lfu             | all               |         5 |
|          56 |         22 | most_frequently_used | random           | lfu             | all               |         5 |
|          51 |         18 | most_recently_used   | random           | lfu             | all               |         5 |
|          48 |         11 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          48 |          9 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          48 |          3 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          47 |         13 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          46 |         13 | most_frequently_used | bfs              | random          | all               |         5 |
|          45 |         13 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          45 |         12 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          44 |         16 | most_recently_used   | bfs              | random          | all               |         5 |
|          43 |          8 | most_recently_added  | bfs              | random          | all               |         5 |
|          41 |          9 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          40 |          5 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          37 |         13 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          32 |         15 | most_recently_added  | random           | lru             | all               |         5 |
|          31 |         13 | most_recently_used   | random           | lru             | all               |         5 |
|          30 |          5 | most_recently_used   | random           | random          | all               |         5 |
|          29 |          8 | most_frequently_used | random           | fifo            | all               |         5 |
|          29 |          8 | most_recently_added  | random           | random          | all               |         5 |
|          28 |          9 | most_frequently_used | random           | random          | all               |         5 |
|          27 |         13 | most_frequently_used | random           | lru             | all               |         5 |
|          26 |          8 | most_recently_added  | random           | fifo            | all               |         5 |
|          24 |          6 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 32

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         206 |         53 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         188 |         63 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         185 |         51 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         165 |         39 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         164 |         37 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         157 |         36 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         139 |         28 | most_recently_used   | bfs              | lru             | all               |         5 |
|         136 |         35 | most_recently_added  | bfs              | lru             | all               |         5 |
|         134 |         23 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         130 |         18 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         127 |         23 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         124 |         19 | most_frequently_used | bfs              | lru             | all               |         5 |
|          98 |         52 | most_frequently_used | random           | lfu             | all               |         5 |
|          89 |         18 | most_recently_used   | bfs              | fifo            | all               |         5 |
|          82 |         30 | most_recently_added  | random           | lfu             | all               |         5 |
|          81 |         13 | most_frequently_used | bfs              | fifo            | all               |         5 |
|          78 |         13 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|          78 |         11 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          77 |         22 | most_recently_used   | random           | lfu             | all               |         5 |
|          72 |         12 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|          68 |         10 | most_recently_added  | bfs              | random          | all               |         5 |
|          63 |         23 | most_recently_added  | random           | lru             | all               |         5 |
|          63 |         16 | most_recently_used   | random           | lru             | all               |         5 |
|          62 |          6 | most_recently_added  | bfs              | fifo            | all               |         5 |
|          61 |          8 | most_frequently_used | bfs              | random          | all               |         5 |
|          60 |         10 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          59 |         11 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          58 |         13 | most_recently_used   | bfs              | random          | all               |         5 |
|          51 |         13 | most_recently_added  | dijkstra         | random          | all               |         5 |
|          49 |          8 | most_recently_used   | random           | random          | all               |         5 |
|          44 |          9 | most_recently_used   | random           | fifo            | all               |         5 |
|          41 |         14 | most_frequently_used | random           | lru             | all               |         5 |
|          37 |          6 | most_recently_added  | random           | random          | all               |         5 |
|          34 |         13 | most_frequently_used | random           | random          | all               |         5 |
|          33 |         14 | most_recently_added  | random           | fifo            | all               |         5 |
|          31 |         12 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 64

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         312 |         57 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         277 |         67 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         271 |         85 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         271 |         36 | most_recently_added  | bfs              | lru             | all               |         5 |
|         270 |         85 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         266 |         65 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         253 |         69 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         242 |         44 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         238 |         34 | most_recently_used   | bfs              | lru             | all               |         5 |
|         237 |         66 | most_frequently_used | bfs              | lru             | all               |         5 |
|         233 |         45 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         218 |         38 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         139 |         22 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         137 |         22 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         126 |         36 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         123 |         24 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         121 |         17 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         120 |         17 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         111 |         34 | most_recently_used   | bfs              | random          | all               |         5 |
|         111 |         27 | most_recently_added  | bfs              | random          | all               |         5 |
|         110 |         41 | most_recently_used   | random           | lfu             | all               |         5 |
|         110 |         40 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         109 |         30 | most_frequently_used | bfs              | random          | all               |         5 |
|         104 |         17 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          95 |         29 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          89 |         17 | most_recently_added  | random           | lfu             | all               |         5 |
|          77 |         38 | most_frequently_used | random           | lfu             | all               |         5 |
|          77 |         15 | most_recently_used   | random           | lru             | all               |         5 |
|          76 |         23 | most_recently_added  | random           | lru             | all               |         5 |
|          62 |         20 | most_frequently_used | random           | lru             | all               |         5 |
|          59 |          6 | most_frequently_used | random           | random          | all               |         5 |
|          58 |         18 | most_recently_added  | random           | random          | all               |         5 |
|          56 |          7 | most_recently_used   | random           | random          | all               |         5 |
|          52 |         16 | most_frequently_used | random           | fifo            | all               |         5 |
|          50 |          8 | most_recently_added  | random           | fifo            | all               |         5 |
|          35 |         15 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 128

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         397 |         35 | most_recently_used   | bfs              | lru             | all               |         5 |
|         375 |         45 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         354 |         38 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         347 |        114 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         331 |         81 | most_frequently_used | bfs              | lru             | all               |         5 |
|         330 |         84 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         324 |        102 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         315 |        101 | most_recently_added  | bfs              | lru             | all               |         5 |
|         297 |         75 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         293 |         91 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         258 |         87 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         254 |         85 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         232 |         26 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         227 |         29 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         222 |         26 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         219 |         26 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         204 |         45 | most_frequently_used | bfs              | random          | all               |         5 |
|         198 |         40 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         194 |         43 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         193 |         56 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         191 |         50 | most_recently_added  | bfs              | random          | all               |         5 |
|         183 |         52 | most_recently_used   | bfs              | random          | all               |         5 |
|         171 |         48 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         165 |         44 | most_recently_used   | dijkstra         | random          | all               |         5 |
|          97 |         35 | most_recently_used   | random           | lru             | all               |         5 |
|          87 |         34 | most_recently_added  | random           | lru             | all               |         5 |
|          84 |         34 | most_frequently_used | random           | lru             | all               |         5 |
|          82 |         24 | most_frequently_used | random           | lfu             | all               |         5 |
|          80 |         19 | most_recently_used   | random           | lfu             | all               |         5 |
|          77 |         33 | most_recently_added  | random           | lfu             | all               |         5 |
|          73 |          8 | most_frequently_used | random           | random          | all               |         5 |
|          68 |         20 | most_recently_added  | random           | fifo            | all               |         5 |
|          65 |         12 | most_recently_added  | random           | random          | all               |         5 |
|          60 |         14 | most_recently_used   | random           | fifo            | all               |         5 |
|          60 |         26 | most_frequently_used | random           | fifo            | all               |         5 |
|          55 |         18 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 256

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         415 |         73 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         415 |         60 | most_recently_used   | bfs              | lru             | all               |         5 |
|         365 |         81 | most_recently_added  | bfs              | lru             | all               |         5 |
|         364 |         77 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         363 |         78 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         361 |         48 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         359 |        111 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         352 |        101 | most_frequently_used | bfs              | lru             | all               |         5 |
|         343 |         57 | most_recently_used   | bfs              | random          | all               |         5 |
|         340 |         63 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         340 |         22 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         339 |         72 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         331 |         95 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         323 |         54 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         318 |         77 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         314 |         73 | most_frequently_used | bfs              | random          | all               |         5 |
|         311 |         78 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         311 |         54 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         309 |         68 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         307 |         50 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         306 |         50 | most_recently_added  | bfs              | random          | all               |         5 |
|         305 |         56 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         298 |         48 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         285 |         52 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|          97 |         23 | most_frequently_used | random           | lfu             | all               |         5 |
|          93 |         25 | most_frequently_used | random           | lru             | all               |         5 |
|          92 |         25 | most_recently_used   | random           | lru             | all               |         5 |
|          91 |         13 | most_recently_added  | random           | lru             | all               |         5 |
|          84 |         14 | most_recently_added  | random           | lfu             | all               |         5 |
|          84 |         29 | most_frequently_used | random           | random          | all               |         5 |
|          83 |         20 | most_frequently_used | random           | fifo            | all               |         5 |
|          82 |         18 | most_recently_used   | random           | fifo            | all               |         5 |
|          80 |         20 | most_recently_used   | random           | lfu             | all               |         5 |
|          80 |         16 | most_recently_added  | random           | random          | all               |         5 |
|          70 |          6 | most_recently_used   | random           | random          | all               |         5 |
|          70 |         11 | most_recently_added  | random           | fifo            | all               |         5 |

## Memory Size 512

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         433 |         61 | most_recently_used   | bfs              | lru             | all               |         5 |
|         432 |         61 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         427 |         59 | most_recently_used   | bfs              | random          | all               |         5 |
|         422 |         59 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         398 |         69 | most_frequently_used | bfs              | lru             | all               |         5 |
|         396 |         69 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         395 |         67 | most_frequently_used | bfs              | random          | all               |         5 |
|         394 |         92 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         394 |         93 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         392 |         68 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         391 |         90 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         391 |         91 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         383 |         68 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         383 |         68 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         382 |         69 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         378 |         64 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         368 |         65 | most_recently_added  | bfs              | random          | all               |         5 |
|         367 |         61 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         367 |         61 | most_recently_added  | bfs              | lru             | all               |         5 |
|         366 |         63 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         351 |         74 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         349 |         74 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         349 |         70 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         347 |         73 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          91 |         32 | most_frequently_used | random           | lfu             | all               |         5 |
|          91 |         32 | most_frequently_used | random           | lru             | all               |         5 |
|          90 |         30 | most_frequently_used | random           | fifo            | all               |         5 |
|          87 |         28 | most_frequently_used | random           | random          | all               |         5 |
|          87 |         13 | most_recently_added  | random           | fifo            | all               |         5 |
|          84 |         11 | most_recently_added  | random           | lfu             | all               |         5 |
|          83 |          9 | most_recently_added  | random           | random          | all               |         5 |
|          82 |          9 | most_recently_added  | random           | lru             | all               |         5 |
|          76 |         15 | most_recently_used   | random           | lru             | all               |         5 |
|          75 |         15 | most_recently_used   | random           | lfu             | all               |         5 |
|          75 |         16 | most_recently_used   | random           | random          | all               |         5 |
|          71 |         15 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 1024

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         431 |         59 | most_recently_used   | bfs              | random          | all               |         5 |
|         431 |         59 | most_recently_used   | bfs              | lru             | all               |         5 |
|         431 |         59 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         431 |         59 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         399 |         91 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         398 |         65 | most_frequently_used | bfs              | random          | all               |         5 |
|         398 |         65 | most_frequently_used | bfs              | lru             | all               |         5 |
|         398 |         65 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         398 |         65 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         384 |         70 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         370 |         59 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         370 |         59 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         370 |         59 | most_recently_added  | bfs              | lru             | all               |         5 |
|         370 |         59 | most_recently_added  | bfs              | random          | all               |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         355 |         72 | most_frequently_used | dijkstra         | random          | all               |         5 |
|          87 |         29 | most_frequently_used | random           | fifo            | all               |         5 |
|          87 |         29 | most_frequently_used | random           | lfu             | all               |         5 |
|          87 |         29 | most_frequently_used | random           | lru             | all               |         5 |
|          87 |         29 | most_frequently_used | random           | random          | all               |         5 |
|          80 |          8 | most_recently_added  | random           | fifo            | all               |         5 |
|          80 |          8 | most_recently_added  | random           | lfu             | all               |         5 |
|          80 |          8 | most_recently_added  | random           | lru             | all               |         5 |
|          80 |          8 | most_recently_added  | random           | random          | all               |         5 |
|          78 |         20 | most_recently_used   | random           | fifo            | all               |         5 |
|          78 |         20 | most_recently_used   | random           | lfu             | all               |         5 |
|          78 |         20 | most_recently_used   | random           | lru             | all               |         5 |
|          78 |         20 | most_recently_used   | random           | random          | all               |         5 |

