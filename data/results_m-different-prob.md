# Results for m-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|         839 |         74 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|         839 |         74 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|         834 |         32 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|         834 |         32 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|         832 |         40 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|         832 |         40 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|         830 |         60 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|         830 |         60 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|         827 |         31 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|         827 |         31 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|         826 |         55 | most_recently_added  | bfs              | random          | all               |           256 |         5 |
|         826 |         55 | most_recently_added  | dijkstra         | random          | all               |           256 |         5 |
|         822 |         97 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|         822 |         97 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|         822 |         85 | most_recently_added  | bfs              | random          | all               |           512 |         5 |
|         822 |         85 | most_recently_added  | dijkstra         | random          | all               |           512 |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | random          | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | bfs              | random          | all               |          1024 |         5 |
|         821 |         97 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|         820 |         91 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|         820 |         91 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|         819 |         52 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|         819 |        100 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|         819 |        100 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|         819 |         52 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|         816 |         47 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|         814 |        102 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|         814 |        102 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|         814 |         75 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|         814 |         75 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|         813 |         52 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|         811 |         64 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|         811 |         64 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|         806 |         39 | most_recently_added  | dijkstra         | random          | all               |           128 |         5 |
|         800 |         64 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|         800 |         64 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|         799 |         91 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|         799 |         91 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|         798 |         51 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|         798 |         51 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|         798 |         27 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|         798 |         27 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|         794 |        112 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|         793 |         71 | most_recently_used   | bfs              | random          | all               |           512 |         5 |
|         793 |         71 | most_recently_used   | dijkstra         | random          | all               |           512 |         5 |
|         792 |         38 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|         792 |         38 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|         791 |         31 | most_recently_added  | bfs              | random          | all               |           128 |         5 |
|         790 |         62 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | random          | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | bfs              | random          | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|         790 |         62 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|         787 |        106 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|         786 |         36 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|         782 |         83 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|         782 |         41 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|         782 |         83 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|         782 |         41 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|         780 |         83 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|         780 |         83 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|         776 |         80 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|         776 |         80 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|         770 |         21 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|         770 |         21 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|         769 |         23 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|         765 |         84 | most_recently_used   | dijkstra         | random          | all               |           256 |         5 |
|         765 |         84 | most_recently_used   | bfs              | random          | all               |           256 |         5 |
|         756 |        116 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|         746 |         48 | most_recently_used   | dijkstra         | random          | all               |           128 |         5 |
|         746 |         48 | most_recently_used   | bfs              | random          | all               |           128 |         5 |
|         739 |         37 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|         739 |         37 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|         739 |         37 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|         733 |         85 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|         733 |         85 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|         727 |         33 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|         722 |         39 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|         722 |         39 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|         720 |         75 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|         707 |         65 | most_recently_used   | bfs              | random          | all               |            64 |         5 |
|         700 |         64 | most_recently_used   | dijkstra         | random          | all               |            64 |         5 |
|         700 |         93 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|         688 |        142 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|         678 |         92 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|         668 |         54 | most_frequently_used | dijkstra         | random          | all               |           128 |         5 |
|         665 |         82 | most_frequently_used | bfs              | random          | all               |            64 |         5 |
|         663 |         46 | most_frequently_used | bfs              | random          | all               |           128 |         5 |
|         654 |        116 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|         649 |        110 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|         639 |         76 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|         631 |         60 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|         629 |         42 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|         629 |         42 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|         629 |        114 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|         628 |         77 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|         626 |         58 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|         626 |         58 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|         619 |         47 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|         619 |         47 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|         616 |        100 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|         615 |         64 | most_frequently_used | bfs              | random          | all               |           256 |         5 |
|         615 |         64 | most_frequently_used | dijkstra         | random          | all               |           256 |         5 |
|         610 |         44 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|         610 |         44 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|         609 |         26 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|         609 |         26 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|         609 |         41 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|         609 |         41 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | random          | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | bfs              | random          | all               |          1024 |         5 |
|         608 |         46 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|         606 |         40 | most_frequently_used | dijkstra         | random          | all               |           512 |         5 |
|         606 |         40 | most_frequently_used | bfs              | random          | all               |           512 |         5 |
|         601 |         40 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|         601 |         48 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|         601 |         48 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|         596 |         93 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|         596 |         93 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|         595 |         78 | most_frequently_used | dijkstra         | random          | all               |            64 |         5 |
|         594 |         69 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|         587 |         62 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|         587 |         35 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|         587 |         35 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|         583 |         79 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|         583 |         79 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|         583 |         96 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|         581 |         71 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|         581 |         52 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|         581 |         52 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|         578 |         17 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|         578 |         17 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|         568 |        163 | most_recently_added  | bfs              | random          | all               |            64 |         5 |
|         562 |         82 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|         557 |         47 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|         557 |        173 | most_recently_added  | dijkstra         | random          | all               |            64 |         5 |
|         554 |         42 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|         552 |         48 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|         552 |         56 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|         551 |        132 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|         547 |         47 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|         539 |         51 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|         538 |        140 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|         537 |         44 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|         534 |         10 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|         532 |        119 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|         530 |         90 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|         524 |        122 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|         505 |        104 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|         494 |         91 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|         493 |         43 | most_frequently_used | bfs              | random          | all               |            32 |         5 |
|         489 |         73 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|         485 |         89 | most_frequently_used | dijkstra         | random          | all               |            32 |         5 |
|         484 |         60 | most_recently_added  | dijkstra         | random          | all               |            32 |         5 |
|         482 |         70 | most_recently_used   | bfs              | random          | all               |            32 |         5 |
|         480 |         72 | most_recently_added  | bfs              | random          | all               |            32 |         5 |
|         470 |        122 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|         461 |        197 | most_recently_added  | random           | random          | all               |           512 |         5 |
|         459 |        203 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|         459 |        203 | most_recently_added  | random           | random          | all               |          1024 |         5 |
|         459 |        203 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|         459 |        203 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|         456 |        191 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|         455 |         26 | most_recently_used   | dijkstra         | random          | all               |            32 |         5 |
|         454 |        191 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|         452 |        191 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|         445 |        140 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|         437 |        200 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|         435 |        207 | most_recently_added  | random           | random          | all               |           256 |         5 |
|         429 |        236 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|         424 |        220 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|         414 |        180 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|         407 |         22 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|         407 |         22 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|         405 |         18 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|         405 |         18 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|         401 |        171 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|         401 |        182 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|         400 |        151 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|         399 |        223 | most_recently_added  | random           | random          | all               |           128 |         5 |
|         398 |        154 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|         397 |        165 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|         394 |         19 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|         394 |         19 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|         391 |        127 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|         390 |         88 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|         390 |        176 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|         387 |         63 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|         387 |         94 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|         386 |        107 | most_recently_added  | dijkstra         | random          | all               |            16 |         5 |
|         382 |         40 | most_frequently_used | dijkstra         | random          | all               |            16 |         5 |
|         381 |        136 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|         380 |        126 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|         379 |         75 | most_recently_used   | dijkstra         | random          | all               |            16 |         5 |
|         378 |        188 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|         376 |         52 | most_recently_used   | bfs              | random          | all               |            16 |         5 |
|         375 |         20 | most_recently_added  | bfs              | random          | all               |            16 |         5 |
|         374 |         67 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|         371 |        183 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|         369 |        147 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|         368 |         33 | most_frequently_used | bfs              | random          | all               |            16 |         5 |
|         361 |         61 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|         358 |        237 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|         351 |        176 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|         350 |         81 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|         349 |         64 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|         349 |        146 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|         349 |         93 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|         348 |        171 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|         342 |        102 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|         338 |        225 | most_recently_used   | random           | random          | all               |           512 |         5 |
|         337 |        224 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|         337 |        224 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|         337 |        224 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|         337 |        224 | most_recently_used   | random           | random          | all               |          1024 |         5 |
|         337 |        224 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|         335 |        235 | most_recently_used   | random           | random          | all               |            64 |         5 |
|         335 |        222 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|         333 |        219 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|         332 |        183 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|         329 |        185 | most_frequently_used | random           | random          | all               |           512 |         5 |
|         325 |        180 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|         324 |         70 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|         324 |         70 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|         322 |         15 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|         322 |         15 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|         322 |        153 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|         322 |        182 | most_frequently_used | random           | random          | all               |          1024 |         5 |
|         322 |        182 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|         322 |        182 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|         322 |        182 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|         319 |         98 | most_frequently_used | random           | random          | all               |           256 |         5 |
|         318 |        177 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|         318 |        177 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|         311 |         15 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|         310 |         47 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|         308 |         19 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|         304 |        111 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|         300 |         50 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|         299 |        137 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|         295 |        227 | most_recently_used   | random           | random          | all               |           256 |         5 |
|         295 |        114 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|         294 |         77 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|         292 |         29 | most_recently_added  | dijkstra         | random          | all               |             8 |         5 |
|         292 |         15 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|         292 |         15 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|         289 |         51 | most_recently_added  | random           | random          | all               |            16 |         5 |
|         285 |         47 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|         284 |         16 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|         284 |         16 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|         284 |        165 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|         284 |        165 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|         283 |        174 | most_frequently_used | random           | random          | all               |            32 |         5 |
|         283 |        172 | most_recently_used   | random           | random          | all               |            32 |         5 |
|         282 |        156 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|         272 |        139 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|         271 |         26 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|         267 |         45 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|         266 |        204 | most_recently_added  | random           | random          | all               |            64 |         5 |
|         266 |        109 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|         260 |        186 | most_frequently_used | random           | random          | all               |            64 |         5 |
|         259 |        117 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|         258 |         15 | most_frequently_used | bfs              | random          | all               |             8 |         5 |
|         257 |         34 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|         251 |         16 | most_recently_used   | bfs              | random          | all               |             8 |         5 |
|         248 |        168 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|         248 |        120 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|         245 |         47 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|         245 |         47 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|         241 |        218 | most_frequently_used | random           | random          | all               |           128 |         5 |
|         239 |        156 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|         239 |        171 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|         239 |        171 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|         237 |         48 | most_recently_added  | bfs              | random          | all               |             8 |         5 |
|         237 |        158 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|         235 |         58 | most_recently_added  | random           | random          | all               |            32 |         5 |
|         232 |         55 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|         232 |         55 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|         232 |         23 | most_frequently_used | dijkstra         | random          | all               |             4 |         5 |
|         230 |         68 | most_recently_used   | dijkstra         | random          | all               |             8 |         5 |
|         229 |         25 | most_recently_used   | dijkstra         | random          | all               |             4 |         5 |
|         226 |         63 | most_frequently_used | dijkstra         | random          | all               |             8 |         5 |
|         226 |        105 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|         223 |        217 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|         223 |         34 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|         223 |        126 | most_frequently_used | random           | random          | all               |            16 |         5 |
|         222 |         51 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|         222 |         51 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|         220 |        125 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|         214 |         34 | most_recently_added  | bfs              | random          | all               |             4 |         5 |
|         208 |         20 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|         208 |         20 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|         203 |         69 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|         203 |         69 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|         203 |         40 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|         202 |         40 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|         200 |         98 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|         198 |        260 | most_recently_used   | random           | random          | all               |           128 |         5 |
|         194 |        116 | most_recently_used   | random           | random          | all               |            16 |         5 |
|         189 |        127 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|         185 |         63 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|         182 |         29 | most_recently_used   | dijkstra         | random          | all               |             2 |         5 |
|         182 |         29 | most_frequently_used | dijkstra         | random          | all               |             2 |         5 |
|         180 |         85 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|         180 |         85 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|         180 |         32 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|         180 |         32 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|         175 |         20 | most_frequently_used | bfs              | random          | all               |             4 |         5 |
|         175 |         20 | most_recently_used   | bfs              | random          | all               |             4 |         5 |
|         173 |         75 | most_recently_added  | dijkstra         | random          | all               |             4 |         5 |
|         168 |        102 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|         165 |         10 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|         160 |         38 | most_recently_added  | dijkstra         | random          | all               |             2 |         5 |
|         157 |        102 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|         154 |        114 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|         151 |        107 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|         148 |         81 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|         148 |         61 | most_recently_added  | random           | random          | all               |             8 |         5 |
|         146 |         70 | most_recently_used   | random           | random          | all               |             8 |         5 |
|         145 |         50 | most_recently_added  | random           | random          | all               |             4 |         5 |
|         145 |         51 | most_frequently_used | random           | random          | all               |             4 |         5 |
|         143 |         62 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|         143 |         57 | most_recently_used   | random           | random          | all               |             4 |         5 |
|         140 |         56 | most_recently_added  | random           | random          | all               |             2 |         5 |
|         136 |         63 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|         136 |         63 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|         135 |         57 | most_frequently_used | bfs              | random          | all               |             2 |         5 |
|         135 |         57 | most_recently_used   | bfs              | random          | all               |             2 |         5 |
|         133 |         59 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|         132 |         45 | most_recently_added  | bfs              | random          | all               |             2 |         5 |
|         131 |         15 | most_recently_used   | dijkstra         | random          | all               |             0 |         5 |
|         131 |         15 | most_frequently_used | bfs              | random          | all               |             0 |         5 |
|         131 |         15 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|         131 |         15 | most_frequently_used | dijkstra         | random          | all               |             0 |         5 |
|         131 |         15 | most_recently_added  | dijkstra         | random          | all               |             0 |         5 |
|         131 |         15 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|         131 |         15 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|         131 |         15 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|         131 |         15 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|         131 |         15 | most_recently_used   | bfs              | random          | all               |             0 |         5 |
|         131 |         15 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|         131 |         15 | most_recently_added  | bfs              | random          | all               |             0 |         5 |
|         129 |         79 | most_recently_used   | random           | random          | all               |             2 |         5 |
|         129 |         79 | most_frequently_used | random           | random          | all               |             2 |         5 |
|         128 |        124 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|         125 |         90 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|         124 |         45 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|         124 |         45 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|         122 |         55 | most_frequently_used | random           | random          | all               |             8 |         5 |
|         118 |         55 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|         118 |         55 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|         118 |         55 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|         118 |         55 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|         118 |         55 | most_frequently_used | random           | lfu             | all               |             0 |         5 |
|         118 |         55 | most_recently_added  | random           | lru             | all               |             0 |         5 |
|         114 |         86 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|         109 |         41 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|         109 |         41 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|         109 |         41 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|         109 |         41 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|         109 |         41 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|         109 |         41 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|         109 |         41 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|         109 |         41 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|         109 |         41 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|         109 |         41 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|         109 |         41 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|         109 |         41 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|         106 |         51 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|         106 |         51 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|         101 |         44 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|          98 |         46 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|          96 |         85 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|          96 |         85 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|          94 |         67 | most_recently_used   | random           | random          | all               |             0 |         5 |
|          94 |         67 | most_frequently_used | random           | random          | all               |             0 |         5 |
|          94 |         67 | most_recently_added  | random           | random          | all               |             0 |         5 |
|          94 |         67 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|          94 |         67 | most_recently_added  | random           | fifo            | all               |             0 |         5 |
|          94 |         67 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|          92 |         39 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|          86 |         53 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|          69 |         36 | most_frequently_used | random           | fifo            | all               |            16 |         5 |

## Memory Size 0

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         131 |         15 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         131 |         15 | most_frequently_used | bfs              | random          | all               |         5 |
|         131 |         15 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         131 |         15 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         131 |         15 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         131 |         15 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         131 |         15 | most_recently_added  | bfs              | random          | all               |         5 |
|         131 |         15 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         131 |         15 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         131 |         15 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         131 |         15 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         131 |         15 | most_recently_used   | bfs              | random          | all               |         5 |
|         118 |         55 | most_recently_added  | random           | lru             | all               |         5 |
|         118 |         55 | most_recently_added  | random           | lfu             | all               |         5 |
|         118 |         55 | most_recently_used   | random           | lru             | all               |         5 |
|         118 |         55 | most_recently_used   | random           | lfu             | all               |         5 |
|         118 |         55 | most_frequently_used | random           | lru             | all               |         5 |
|         118 |         55 | most_frequently_used | random           | lfu             | all               |         5 |
|         109 |         41 | most_frequently_used | bfs              | lru             | all               |         5 |
|         109 |         41 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         109 |         41 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         109 |         41 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         109 |         41 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         109 |         41 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         109 |         41 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         109 |         41 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         109 |         41 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         109 |         41 | most_recently_added  | bfs              | lru             | all               |         5 |
|         109 |         41 | most_recently_used   | bfs              | lru             | all               |         5 |
|         109 |         41 | most_recently_used   | bfs              | lfu             | all               |         5 |
|          94 |         67 | most_frequently_used | random           | fifo            | all               |         5 |
|          94 |         67 | most_frequently_used | random           | random          | all               |         5 |
|          94 |         67 | most_recently_added  | random           | fifo            | all               |         5 |
|          94 |         67 | most_recently_added  | random           | random          | all               |         5 |
|          94 |         67 | most_recently_used   | random           | fifo            | all               |         5 |
|          94 |         67 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 2

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         387 |         63 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         361 |         61 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         349 |         93 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         257 |         34 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         232 |         55 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         232 |         55 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         222 |         51 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         222 |         51 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         220 |        125 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         203 |         69 | most_recently_used   | bfs              | lru             | all               |         5 |
|         203 |         69 | most_frequently_used | bfs              | lru             | all               |         5 |
|         203 |         40 | most_recently_added  | bfs              | lru             | all               |         5 |
|         202 |         40 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         200 |         98 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         182 |         29 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         182 |         29 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         180 |         85 | most_frequently_used | random           | lru             | all               |         5 |
|         180 |         85 | most_recently_used   | random           | lru             | all               |         5 |
|         180 |         32 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         180 |         32 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         165 |         10 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         160 |         38 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         154 |        114 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         143 |         62 | most_recently_added  | random           | lfu             | all               |         5 |
|         140 |         56 | most_recently_added  | random           | random          | all               |         5 |
|         136 |         63 | most_recently_used   | random           | lfu             | all               |         5 |
|         136 |         63 | most_frequently_used | random           | lfu             | all               |         5 |
|         135 |         57 | most_frequently_used | bfs              | random          | all               |         5 |
|         135 |         57 | most_recently_used   | bfs              | random          | all               |         5 |
|         133 |         59 | most_recently_added  | random           | fifo            | all               |         5 |
|         132 |         45 | most_recently_added  | bfs              | random          | all               |         5 |
|         129 |         79 | most_frequently_used | random           | random          | all               |         5 |
|         129 |         79 | most_recently_used   | random           | random          | all               |         5 |
|         106 |         51 | most_frequently_used | random           | fifo            | all               |         5 |
|         106 |         51 | most_recently_used   | random           | fifo            | all               |         5 |
|          86 |         53 | most_recently_added  | random           | lru             | all               |         5 |

## Memory Size 4

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         374 |         67 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         350 |         81 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         349 |         64 | most_recently_added  | bfs              | lru             | all               |         5 |
|         324 |         70 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         324 |         70 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         322 |         15 | most_recently_used   | bfs              | lru             | all               |         5 |
|         322 |         15 | most_frequently_used | bfs              | lru             | all               |         5 |
|         300 |         50 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         294 |         77 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         285 |         47 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         271 |         26 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         259 |        117 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         248 |        120 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         245 |         47 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         245 |         47 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         232 |         23 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         229 |         25 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         223 |         34 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         214 |         34 | most_recently_added  | bfs              | random          | all               |         5 |
|         208 |         20 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         208 |         20 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         175 |         20 | most_frequently_used | bfs              | random          | all               |         5 |
|         175 |         20 | most_recently_used   | bfs              | random          | all               |         5 |
|         173 |         75 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         151 |        107 | most_recently_added  | random           | lfu             | all               |         5 |
|         145 |         50 | most_recently_added  | random           | random          | all               |         5 |
|         145 |         51 | most_frequently_used | random           | random          | all               |         5 |
|         143 |         57 | most_recently_used   | random           | random          | all               |         5 |
|         125 |         90 | most_recently_added  | random           | lru             | all               |         5 |
|         124 |         45 | most_recently_used   | random           | fifo            | all               |         5 |
|         124 |         45 | most_frequently_used | random           | fifo            | all               |         5 |
|         101 |         44 | most_recently_used   | random           | lfu             | all               |         5 |
|          98 |         46 | most_recently_added  | random           | fifo            | all               |         5 |
|          96 |         85 | most_frequently_used | random           | lru             | all               |         5 |
|          96 |         85 | most_recently_used   | random           | lru             | all               |         5 |
|          92 |         39 | most_frequently_used | random           | lfu             | all               |         5 |

## Memory Size 8

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         594 |         69 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         557 |         47 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         554 |         42 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         552 |         48 | most_recently_used   | bfs              | lru             | all               |         5 |
|         552 |         56 | most_frequently_used | bfs              | lru             | all               |         5 |
|         551 |        132 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         539 |         51 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         534 |         10 | most_recently_added  | bfs              | lru             | all               |         5 |
|         524 |        122 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         505 |        104 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         494 |         91 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         489 |         73 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         424 |        220 | most_recently_used   | random           | lfu             | all               |         5 |
|         358 |        237 | most_frequently_used | random           | lfu             | all               |         5 |
|         311 |         15 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         310 |         47 | most_recently_added  | random           | lfu             | all               |         5 |
|         308 |         19 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         292 |         29 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         292 |         15 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         292 |         15 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         284 |         16 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         284 |         16 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         282 |        156 | most_recently_used   | random           | lru             | all               |         5 |
|         272 |        139 | most_frequently_used | random           | lru             | all               |         5 |
|         267 |         45 | most_recently_added  | random           | lru             | all               |         5 |
|         258 |         15 | most_frequently_used | bfs              | random          | all               |         5 |
|         251 |         16 | most_recently_used   | bfs              | random          | all               |         5 |
|         237 |         48 | most_recently_added  | bfs              | random          | all               |         5 |
|         230 |         68 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         226 |         63 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         185 |         63 | most_recently_added  | random           | fifo            | all               |         5 |
|         168 |        102 | most_recently_used   | random           | fifo            | all               |         5 |
|         157 |        102 | most_frequently_used | random           | fifo            | all               |         5 |
|         148 |         61 | most_recently_added  | random           | random          | all               |         5 |
|         146 |         70 | most_recently_used   | random           | random          | all               |         5 |
|         122 |         55 | most_frequently_used | random           | random          | all               |         5 |

## Memory Size 16

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         786 |         36 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         769 |         23 | most_recently_added  | bfs              | lru             | all               |         5 |
|         739 |         37 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         727 |         33 | most_recently_used   | bfs              | lru             | all               |         5 |
|         678 |         92 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         629 |        114 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         601 |         40 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         587 |         62 | most_frequently_used | bfs              | lru             | all               |         5 |
|         583 |         96 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         581 |         71 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         562 |         82 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         530 |         90 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         407 |         22 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         407 |         22 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         405 |         18 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         405 |         18 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         398 |        154 | most_recently_added  | random           | lfu             | all               |         5 |
|         394 |         19 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         394 |         19 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         386 |        107 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         382 |         40 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         379 |         75 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         376 |         52 | most_recently_used   | bfs              | random          | all               |         5 |
|         375 |         20 | most_recently_added  | bfs              | random          | all               |         5 |
|         368 |         33 | most_frequently_used | bfs              | random          | all               |         5 |
|         348 |        171 | most_recently_used   | random           | lru             | all               |         5 |
|         342 |        102 | most_recently_added  | random           | lru             | all               |         5 |
|         299 |        137 | most_recently_used   | random           | lfu             | all               |         5 |
|         289 |         51 | most_recently_added  | random           | random          | all               |         5 |
|         248 |        168 | most_frequently_used | random           | lru             | all               |         5 |
|         226 |        105 | most_frequently_used | random           | lfu             | all               |         5 |
|         223 |        126 | most_frequently_used | random           | random          | all               |         5 |
|         194 |        116 | most_recently_used   | random           | random          | all               |         5 |
|         148 |         81 | most_recently_used   | random           | fifo            | all               |         5 |
|         114 |         86 | most_recently_added  | random           | fifo            | all               |         5 |
|          69 |         36 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 32

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         798 |         51 | most_recently_used   | bfs              | lru             | all               |         5 |
|         798 |         51 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         798 |         27 | most_recently_added  | bfs              | lru             | all               |         5 |
|         798 |         27 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         700 |         93 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         688 |        142 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         649 |        110 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         639 |         76 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         631 |         60 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         616 |        100 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         609 |         26 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         609 |         26 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         587 |         35 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         587 |         35 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         581 |         52 | most_frequently_used | bfs              | lru             | all               |         5 |
|         581 |         52 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         578 |         17 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         578 |         17 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         538 |        140 | most_recently_added  | random           | lfu             | all               |         5 |
|         493 |         43 | most_frequently_used | bfs              | random          | all               |         5 |
|         485 |         89 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         484 |         60 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         482 |         70 | most_recently_used   | bfs              | random          | all               |         5 |
|         480 |         72 | most_recently_added  | bfs              | random          | all               |         5 |
|         470 |        122 | most_recently_added  | random           | lru             | all               |         5 |
|         455 |         26 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         401 |        171 | most_recently_used   | random           | lfu             | all               |         5 |
|         391 |        127 | most_frequently_used | random           | lru             | all               |         5 |
|         390 |         88 | most_frequently_used | random           | lfu             | all               |         5 |
|         371 |        183 | most_recently_used   | random           | lru             | all               |         5 |
|         283 |        174 | most_frequently_used | random           | random          | all               |         5 |
|         283 |        172 | most_recently_used   | random           | random          | all               |         5 |
|         237 |        158 | most_frequently_used | random           | fifo            | all               |         5 |
|         235 |         58 | most_recently_added  | random           | random          | all               |         5 |
|         189 |        127 | most_recently_added  | random           | fifo            | all               |         5 |
|         128 |        124 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 64

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         827 |         31 | most_recently_added  | bfs              | lru             | all               |         5 |
|         827 |         31 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         792 |         38 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         792 |         38 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         782 |         41 | most_recently_used   | bfs              | lru             | all               |         5 |
|         782 |         41 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         770 |         21 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         770 |         21 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         756 |        116 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         739 |         37 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         739 |         37 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         720 |         75 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         707 |         65 | most_recently_used   | bfs              | random          | all               |         5 |
|         700 |         64 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         665 |         82 | most_frequently_used | bfs              | random          | all               |         5 |
|         654 |        116 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         628 |         77 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         595 |         78 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         583 |         79 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         583 |         79 | most_frequently_used | bfs              | lru             | all               |         5 |
|         568 |        163 | most_recently_added  | bfs              | random          | all               |         5 |
|         557 |        173 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         547 |         47 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         537 |         44 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         532 |        119 | most_recently_added  | random           | lfu             | all               |         5 |
|         401 |        182 | most_recently_added  | random           | lru             | all               |         5 |
|         400 |        151 | most_recently_used   | random           | lru             | all               |         5 |
|         397 |        165 | most_recently_used   | random           | lfu             | all               |         5 |
|         381 |        136 | most_frequently_used | random           | lru             | all               |         5 |
|         380 |        126 | most_frequently_used | random           | lfu             | all               |         5 |
|         369 |        147 | most_recently_added  | random           | fifo            | all               |         5 |
|         351 |        176 | most_frequently_used | random           | fifo            | all               |         5 |
|         335 |        235 | most_recently_used   | random           | random          | all               |         5 |
|         304 |        111 | most_recently_used   | random           | fifo            | all               |         5 |
|         266 |        204 | most_recently_added  | random           | random          | all               |         5 |
|         260 |        186 | most_frequently_used | random           | random          | all               |         5 |

## Memory Size 128

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         834 |         32 | most_recently_used   | bfs              | lru             | all               |         5 |
|         834 |         32 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         830 |         60 | most_recently_added  | bfs              | lru             | all               |         5 |
|         830 |         60 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         816 |         47 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         814 |         75 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         814 |         75 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         813 |         52 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         806 |         39 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         794 |        112 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         791 |         31 | most_recently_added  | bfs              | random          | all               |         5 |
|         787 |        106 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         780 |         83 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         780 |         83 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         746 |         48 | most_recently_used   | bfs              | random          | all               |         5 |
|         746 |         48 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         722 |         39 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         722 |         39 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         668 |         54 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         663 |         46 | most_frequently_used | bfs              | random          | all               |         5 |
|         619 |         47 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         619 |         47 | most_frequently_used | bfs              | lru             | all               |         5 |
|         596 |         93 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         596 |         93 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         429 |        236 | most_recently_added  | random           | lru             | all               |         5 |
|         399 |        223 | most_recently_added  | random           | random          | all               |         5 |
|         387 |         94 | most_recently_added  | random           | fifo            | all               |         5 |
|         378 |        188 | most_recently_added  | random           | lfu             | all               |         5 |
|         322 |        153 | most_recently_used   | random           | fifo            | all               |         5 |
|         295 |        114 | most_frequently_used | random           | fifo            | all               |         5 |
|         241 |        218 | most_frequently_used | random           | random          | all               |         5 |
|         239 |        156 | most_recently_used   | random           | lru             | all               |         5 |
|         239 |        171 | most_frequently_used | random           | lfu             | all               |         5 |
|         239 |        171 | most_frequently_used | random           | lru             | all               |         5 |
|         223 |        217 | most_recently_used   | random           | lfu             | all               |         5 |
|         198 |        260 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 256

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         839 |         74 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         839 |         74 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         832 |         40 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         832 |         40 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         826 |         55 | most_recently_added  | bfs              | random          | all               |         5 |
|         826 |         55 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         820 |         91 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         820 |         91 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         819 |         52 | most_recently_used   | bfs              | lru             | all               |         5 |
|         819 |         52 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         811 |         64 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         811 |         64 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         799 |         91 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         799 |         91 | most_recently_added  | bfs              | lru             | all               |         5 |
|         765 |         84 | most_recently_used   | bfs              | random          | all               |         5 |
|         765 |         84 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         733 |         85 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         733 |         85 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         626 |         58 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         626 |         58 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         615 |         64 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         615 |         64 | most_frequently_used | bfs              | random          | all               |         5 |
|         601 |         48 | most_frequently_used | bfs              | lru             | all               |         5 |
|         601 |         48 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         445 |        140 | most_recently_added  | random           | fifo            | all               |         5 |
|         437 |        200 | most_recently_added  | random           | lfu             | all               |         5 |
|         435 |        207 | most_recently_added  | random           | random          | all               |         5 |
|         414 |        180 | most_recently_added  | random           | lru             | all               |         5 |
|         390 |        176 | most_recently_used   | random           | lru             | all               |         5 |
|         349 |        146 | most_recently_used   | random           | lfu             | all               |         5 |
|         332 |        183 | most_recently_used   | random           | fifo            | all               |         5 |
|         319 |         98 | most_frequently_used | random           | random          | all               |         5 |
|         295 |        227 | most_recently_used   | random           | random          | all               |         5 |
|         284 |        165 | most_frequently_used | random           | lfu             | all               |         5 |
|         284 |        165 | most_frequently_used | random           | lru             | all               |         5 |
|         266 |        109 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 512

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         822 |         97 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         822 |         97 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         822 |         85 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         822 |         85 | most_recently_added  | bfs              | random          | all               |         5 |
|         819 |        100 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         819 |        100 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         814 |        102 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         814 |        102 | most_recently_added  | bfs              | lru             | all               |         5 |
|         800 |         64 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         800 |         64 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         793 |         71 | most_recently_used   | bfs              | random          | all               |         5 |
|         793 |         71 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         782 |         83 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         782 |         83 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         776 |         80 | most_recently_used   | bfs              | lru             | all               |         5 |
|         776 |         80 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         629 |         42 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         629 |         42 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         610 |         44 | most_frequently_used | bfs              | lru             | all               |         5 |
|         610 |         44 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         609 |         41 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         609 |         41 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         606 |         40 | most_frequently_used | bfs              | random          | all               |         5 |
|         606 |         40 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         461 |        197 | most_recently_added  | random           | random          | all               |         5 |
|         456 |        191 | most_recently_added  | random           | lru             | all               |         5 |
|         454 |        191 | most_recently_added  | random           | lfu             | all               |         5 |
|         452 |        191 | most_recently_added  | random           | fifo            | all               |         5 |
|         338 |        225 | most_recently_used   | random           | random          | all               |         5 |
|         337 |        224 | most_recently_used   | random           | lfu             | all               |         5 |
|         335 |        222 | most_recently_used   | random           | lru             | all               |         5 |
|         333 |        219 | most_recently_used   | random           | fifo            | all               |         5 |
|         329 |        185 | most_frequently_used | random           | random          | all               |         5 |
|         325 |        180 | most_frequently_used | random           | fifo            | all               |         5 |
|         318 |        177 | most_frequently_used | random           | lfu             | all               |         5 |
|         318 |        177 | most_frequently_used | random           | lru             | all               |         5 |

## Memory Size 1024

Total configurations: 36

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         821 |         97 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         821 |         97 | most_recently_added  | dijkstra         | random          | all               |         5 |
|         821 |         97 | most_recently_added  | bfs              | random          | all               |         5 |
|         821 |         97 | most_recently_added  | bfs              | lru             | all               |         5 |
|         821 |         97 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         821 |         97 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         790 |         62 | most_recently_used   | dijkstra         | random          | all               |         5 |
|         790 |         62 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         790 |         62 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         790 |         62 | most_recently_used   | bfs              | lru             | all               |         5 |
|         790 |         62 | most_recently_used   | bfs              | random          | all               |         5 |
|         608 |         46 | most_frequently_used | bfs              | random          | all               |         5 |
|         608 |         46 | most_frequently_used | bfs              | lru             | all               |         5 |
|         608 |         46 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         608 |         46 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         608 |         46 | most_frequently_used | dijkstra         | random          | all               |         5 |
|         459 |        203 | most_recently_added  | random           | fifo            | all               |         5 |
|         459 |        203 | most_recently_added  | random           | lfu             | all               |         5 |
|         459 |        203 | most_recently_added  | random           | lru             | all               |         5 |
|         459 |        203 | most_recently_added  | random           | random          | all               |         5 |
|         337 |        224 | most_recently_used   | random           | fifo            | all               |         5 |
|         337 |        224 | most_recently_used   | random           | lfu             | all               |         5 |
|         337 |        224 | most_recently_used   | random           | lru             | all               |         5 |
|         337 |        224 | most_recently_used   | random           | random          | all               |         5 |
|         322 |        182 | most_frequently_used | random           | fifo            | all               |         5 |
|         322 |        182 | most_frequently_used | random           | lfu             | all               |         5 |
|         322 |        182 | most_frequently_used | random           | lru             | all               |         5 |
|         322 |        182 | most_frequently_used | random           | random          | all               |         5 |

