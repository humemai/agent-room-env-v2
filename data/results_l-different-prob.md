# Results for l-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|     751.6667 |     30.1809 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         3 |
|     749.7500 |     52.4518 | most_recently_used   | bfs              | lru             | all               |           512 |         4 |
|     749.0000 |     51.3274 | most_recently_used   | bfs              | lfu             | all               |           512 |         4 |
|     748.7500 |     57.2249 | most_recently_added  | bfs              | random          | all               |           512 |         4 |
|     748.5000 |     55.9218 | most_recently_used   | bfs              | random          | all               |           512 |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | lfu             | all               |          1024 |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | fifo            | all               |          1024 |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | random          | all               |          1024 |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | lru             | all               |          1024 |         4 |
|     747.0000 |     47.8592 | most_recently_used   | bfs              | fifo            | all               |           512 |         4 |
|     746.7500 |     48.7564 | most_recently_added  | bfs              | fifo            | all               |           512 |         4 |
|     745.2500 |     47.6832 | most_recently_added  | bfs              | lru             | all               |           128 |         4 |
|     743.2500 |     46.9275 | most_recently_added  | bfs              | lru             | all               |           512 |         4 |
|     742.0000 |     47.9740 | most_recently_added  | bfs              | lfu             | all               |           512 |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | lru             | all               |          1024 |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | lfu             | all               |          1024 |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | random          | all               |          1024 |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | fifo            | all               |          1024 |         4 |
|     738.0000 |     54.4488 | most_recently_added  | dijkstra         | random          | all               |           512 |         3 |
|     737.2500 |     55.0744 | most_recently_added  | bfs              | lru             | all               |           256 |         4 |
|     733.7500 |     55.5535 | most_recently_added  | bfs              | lfu             | all               |           256 |         4 |
|     732.6667 |      9.5685 | most_recently_used   | dijkstra         | random          | all               |           512 |         3 |
|     732.3333 |      9.5685 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         3 |
|     732.3333 |      9.5685 | most_recently_used   | dijkstra         | random          | all               |          1024 |         3 |
|     732.3333 |      9.5685 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         3 |
|     730.7500 |     56.7775 | most_recently_used   | bfs              | lfu             | all               |           256 |         4 |
|     729.2500 |     37.7649 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         4 |
|     728.7500 |     73.3191 | most_recently_used   | bfs              | lru             | all               |           256 |         4 |
|     728.5000 |     73.0223 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         4 |
|     728.3333 |      9.6724 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         3 |
|     728.3333 |     61.7216 | most_recently_added  | dijkstra         | random          | all               |          1024 |         3 |
|     726.7500 |     42.1152 | most_recently_used   | dijkstra         | lru             | all               |           256 |         4 |
|     726.2500 |     38.4927 | most_recently_used   | bfs              | lru             | all               |           128 |         4 |
|     722.6667 |     22.8959 | most_recently_used   | dijkstra         | random          | all               |           256 |         3 |
|     721.5000 |     55.6799 | most_recently_added  | dijkstra         | lru             | all               |           128 |         4 |
|     721.0000 |     45.3707 | most_recently_added  | bfs              | lru             | all               |            64 |         4 |
|     720.0000 |     22.9129 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         4 |
|     719.5000 |     41.6803 | most_recently_used   | bfs              | lfu             | all               |           128 |         4 |
|     718.5000 |     59.2178 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         4 |
|     718.0000 |     45.9946 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         4 |
|     718.0000 |     25.6418 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         4 |
|     717.2500 |     54.3524 | most_recently_added  | dijkstra         | lru             | all               |           512 |         4 |
|     716.7500 |     47.2989 | most_recently_used   | bfs              | random          | all               |           256 |         4 |
|     715.5000 |     52.2135 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         4 |
|     714.2500 |     23.7105 | most_recently_used   | dijkstra         | lru             | all               |           512 |         4 |
|     714.2500 |     47.2090 | most_recently_added  | bfs              | fifo            | all               |           256 |         4 |
|     714.0000 |     58.9364 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         4 |
|     714.0000 |     58.9364 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         4 |
|     714.0000 |     58.9364 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         4 |
|     713.2500 |     48.9713 | most_recently_used   | bfs              | fifo            | all               |           256 |         4 |
|     712.7500 |     57.8765 | most_recently_used   | dijkstra         | lru             | all               |           128 |         4 |
|     711.7500 |     38.5641 | most_recently_added  | bfs              | random          | all               |           256 |         4 |
|     710.2500 |     41.4872 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         4 |
|     707.2500 |     43.6427 | most_recently_added  | dijkstra         | lru             | all               |            64 |         4 |
|     702.5000 |     54.9067 | most_recently_added  | dijkstra         | lru             | all               |            32 |         4 |
|     700.3333 |     31.9409 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         3 |
|     698.5000 |     55.4549 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         4 |
|     694.7500 |     63.9037 | most_recently_added  | bfs              | lfu             | all               |            64 |         4 |
|     692.0000 |     54.3093 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         4 |
|     690.5000 |     43.0726 | most_recently_added  | bfs              | lfu             | all               |           128 |         4 |
|     686.2500 |     37.8575 | most_recently_used   | bfs              | lfu             | all               |            64 |         4 |
|     685.2500 |     33.2519 | most_recently_used   | dijkstra         | lru             | all               |            64 |         4 |
|     684.5000 |     74.8883 | most_recently_added  | dijkstra         | lru             | all               |           256 |         4 |
|     681.0000 |     62.2937 | most_recently_used   | bfs              | lru             | all               |            32 |         4 |
|     678.5000 |     42.1337 | most_recently_used   | bfs              | fifo            | all               |           128 |         4 |
|     675.7500 |     75.9091 | most_recently_added  | bfs              | lru             | all               |            32 |         4 |
|     667.8000 |     75.7744 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|     662.5000 |     15.2561 | most_recently_used   | bfs              | lru             | all               |            64 |         4 |
|     658.5000 |     44.4382 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         4 |
|     656.0000 |     62.6578 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         3 |
|     654.5000 |     63.3739 | most_frequently_used | bfs              | fifo            | all               |           128 |         4 |
|     651.0000 |     60.2163 | most_frequently_used | dijkstra         | lru             | all               |           128 |         3 |
|     645.3333 |     90.2749 | most_recently_added  | dijkstra         | random          | all               |           256 |         3 |
|     645.0000 |     62.3110 | most_frequently_used | bfs              | lru             | all               |           128 |         3 |
|     643.2500 |     70.0620 | most_frequently_used | bfs              | lfu             | all               |           128 |         4 |
|     639.2500 |     44.5498 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         4 |
|     638.7500 |    127.1679 | most_recently_used   | bfs              | lfu             | all               |            32 |         4 |
|     637.7500 |     28.9687 | most_frequently_used | bfs              | fifo            | all               |           256 |         4 |
|     637.2500 |     61.8643 | most_recently_added  | bfs              | fifo            | all               |           128 |         4 |
|     635.0000 |     36.1202 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         3 |
|     633.0000 |     55.9151 | most_frequently_used | bfs              | lru             | all               |            32 |         4 |
|     626.5000 |     68.1634 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         4 |
|     625.2500 |    100.8027 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         4 |
|     624.5000 |     80.2013 | most_recently_used   | dijkstra         | lru             | all               |            32 |         4 |
|     617.7500 |     40.6471 | most_frequently_used | bfs              | lfu             | all               |            64 |         4 |
|     617.2500 |     63.6450 | most_frequently_used | bfs              | lfu             | all               |            16 |         4 |
|     616.0000 |     48.8740 | most_recently_used   | dijkstra         | random          | all               |           128 |         3 |
|     612.5000 |     67.7809 | most_frequently_used | bfs              | lfu             | all               |           256 |         4 |
|     610.7500 |     26.9293 | most_frequently_used | dijkstra         | lru             | all               |            32 |         4 |
|     605.0000 |     58.4466 | most_frequently_used | dijkstra         | lru             | all               |           256 |         3 |
|     605.0000 |     59.4362 | most_frequently_used | bfs              | lru             | all               |           256 |         3 |
|     599.5000 |     74.2108 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         4 |
|     598.0000 |     24.5255 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         4 |
|     595.0000 |     29.5296 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         3 |
|     594.7500 |     26.2333 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         4 |
|     594.3333 |     29.3182 | most_frequently_used | dijkstra         | lru             | all               |           512 |         3 |
|     592.0000 |     90.4682 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         4 |
|     592.0000 |     31.9139 | most_frequently_used | dijkstra         | random          | all               |           256 |         4 |
|     588.5000 |     27.5454 | most_frequently_used | dijkstra         | lru             | all               |            64 |         4 |
|     588.0000 |     29.4194 | most_frequently_used | dijkstra         | random          | all               |           512 |         4 |
|     586.7500 |     29.2948 | most_frequently_used | bfs              | fifo            | all               |           512 |         4 |
|     585.0000 |     33.0252 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         3 |
|     585.0000 |     33.0252 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         3 |
|     583.7500 |     33.5513 | most_frequently_used | bfs              | lfu             | all               |           512 |         4 |
|     583.6667 |    100.9433 | most_recently_added  | dijkstra         | random          | all               |           128 |         3 |
|     583.5000 |     28.7185 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         4 |
|     583.5000 |     28.7185 | most_frequently_used | dijkstra         | random          | all               |          1024 |         4 |
|     582.2500 |     34.0689 | most_frequently_used | bfs              | lru             | all               |           512 |         4 |
|     581.2500 |     34.6654 | most_frequently_used | bfs              | random          | all               |           512 |         4 |
|     581.0000 |     28.1869 | most_frequently_used | bfs              | lru             | all               |            64 |         4 |
|     580.7500 |     24.8131 | most_frequently_used | bfs              | random          | all               |           256 |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | lfu             | all               |          1024 |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | lru             | all               |          1024 |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | random          | all               |          1024 |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | fifo            | all               |          1024 |         4 |
|     572.2500 |    137.5125 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         4 |
|     567.2500 |     83.2237 | most_recently_added  | bfs              | random          | all               |           128 |         4 |
|     563.7500 |    146.1359 | most_frequently_used | bfs              | lfu             | all               |            32 |         4 |
|     559.0000 |     27.0463 | most_recently_used   | bfs              | lfu             | all               |            16 |         4 |
|     542.7500 |     84.1973 | most_recently_used   | bfs              | random          | all               |           128 |         4 |
|     531.8000 |     60.9964 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|     529.0000 |     47.9270 | most_frequently_used | dijkstra         | random          | all               |           128 |         4 |
|     528.0000 |     66.5545 | most_recently_used   | dijkstra         | lru             | all               |            16 |         4 |
|     526.0000 |     94.4272 | most_recently_added  | dijkstra         | lru             | all               |            16 |         4 |
|     517.0000 |     87.9631 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         4 |
|     516.2500 |     27.7252 | most_frequently_used | bfs              | lru             | all               |            16 |         4 |
|     512.7500 |     35.3297 | most_recently_added  | bfs              | lru             | all               |            16 |         4 |
|     508.0000 |     36.6879 | most_recently_added  | random           | lfu             | all               |           256 |         3 |
|     505.0000 |     63.9375 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         3 |
|     502.5000 |     17.1537 | most_frequently_used | bfs              | random          | all               |           128 |         4 |
|     497.5000 |     57.6910 | most_frequently_used | dijkstra         | lru             | all               |            16 |         4 |
|     494.7500 |     26.2809 | most_recently_used   | bfs              | fifo            | all               |            64 |         4 |
|     485.6667 |     29.4882 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         3 |
|     482.5000 |     63.8338 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         4 |
|     482.0000 |     41.8629 | most_recently_added  | bfs              | fifo            | all               |            64 |         4 |
|     478.0000 |     56.7274 | most_recently_added  | random           | lfu             | all               |           512 |         3 |
|     475.5000 |     80.1888 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         4 |
|     472.2500 |     40.2888 | most_frequently_used | bfs              | fifo            | all               |            64 |         4 |
|     466.0000 |     42.0238 | most_recently_used   | bfs              | lru             | all               |            16 |         4 |
|     453.2500 |     75.0712 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         4 |
|     444.2500 |     61.7510 | most_frequently_used | bfs              | lfu             | all               |             8 |         4 |
|     443.2500 |    111.8914 | most_recently_added  | random           | lru             | all               |           256 |         4 |
|     440.3333 |    114.9647 | most_recently_added  | random           | lfu             | all               |            16 |         3 |
|     437.5000 |     17.0367 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         4 |
|     421.2500 |     25.3513 | most_frequently_used | dijkstra         | random          | all               |            64 |         4 |
|     420.0000 |     53.9583 | most_recently_used   | random           | lfu             | all               |             8 |         4 |
|     420.0000 |     23.8642 | most_frequently_used | random           | lfu             | all               |            32 |         4 |
|     411.2500 |     80.6082 | most_recently_used   | random           | lru             | all               |            32 |         4 |
|     405.7500 |      5.6292 | most_recently_used   | bfs              | random          | all               |            64 |         4 |
|     405.0000 |     31.7569 | most_recently_added  | dijkstra         | random          | all               |            64 |         4 |
|     404.7500 |    148.8613 | most_recently_used   | random           | lru             | all               |            64 |         4 |
|     404.2500 |     58.2253 | most_frequently_used | random           | lru             | all               |           256 |         4 |
|     404.2500 |     58.2253 | most_frequently_used | random           | lfu             | all               |           256 |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | lru             | all               |          1024 |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | lfu             | all               |          1024 |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | random          | all               |          1024 |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | fifo            | all               |          1024 |         4 |
|     397.2500 |    148.2403 | most_recently_added  | random           | lru             | all               |           512 |         4 |
|     395.7500 |    145.1592 | most_recently_added  | random           | fifo            | all               |           512 |         4 |
|     393.5000 |     57.7819 | most_recently_added  | random           | fifo            | all               |           256 |         4 |
|     390.0000 |    140.4778 | most_recently_added  | random           | random          | all               |           512 |         4 |
|     389.2500 |     48.0488 | most_frequently_used | random           | fifo            | all               |           256 |         4 |
|     387.2500 |     32.2442 | most_frequently_used | random           | lfu             | all               |             8 |         4 |
|     383.2500 |    100.9762 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         4 |
|     379.0000 |     44.6430 | most_recently_added  | bfs              | random          | all               |            64 |         4 |
|     378.0000 |     54.5023 | most_recently_used   | random           | random          | all               |           512 |         4 |
|     377.0000 |     37.3564 | most_frequently_used | bfs              | random          | all               |            64 |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | random          | all               |          1024 |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | lfu             | all               |          1024 |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | fifo            | all               |          1024 |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | lru             | all               |          1024 |         4 |
|     374.7500 |     62.6314 | most_recently_used   | random           | lfu             | all               |           512 |         4 |
|     374.7500 |     62.6314 | most_recently_used   | random           | lru             | all               |           512 |         4 |
|     374.5000 |     63.1368 | most_recently_used   | random           | fifo            | all               |           512 |         4 |
|     374.5000 |     34.3329 | most_frequently_used | random           | random          | all               |           256 |         4 |
|     374.0000 |     51.5315 | most_recently_used   | random           | lfu             | all               |           256 |         4 |
|     371.2500 |     63.6568 | most_frequently_used | random           | fifo            | all               |           512 |         4 |
|     371.0000 |     41.1947 | most_frequently_used | random           | lfu             | all               |           128 |         4 |
|     370.6667 |     52.9297 | most_recently_added  | random           | lfu             | all               |            64 |         3 |
|     368.5000 |     40.6848 | most_frequently_used | random           | lru             | all               |           128 |         4 |
|     366.7500 |     73.1689 | most_frequently_used | random           | random          | all               |           512 |         4 |
|     363.2500 |     68.7473 | most_frequently_used | random           | lru             | all               |           512 |         4 |
|     363.2500 |     68.7473 | most_frequently_used | random           | lfu             | all               |           512 |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | lfu             | all               |          1024 |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | fifo            | all               |          1024 |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | lru             | all               |          1024 |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | random          | all               |          1024 |         4 |
|     360.7500 |    123.6414 | most_recently_used   | random           | lfu             | all               |            16 |         4 |
|     359.0000 |     99.3428 | most_recently_used   | random           | lfu             | all               |           128 |         4 |
|     358.7500 |     72.6993 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         4 |
|     358.0000 |     40.7370 | most_recently_used   | random           | random          | all               |           256 |         4 |
|     357.3333 |     37.9678 | most_recently_added  | random           | lfu             | all               |            32 |         3 |
|     357.2500 |     64.2471 | most_recently_used   | random           | lru             | all               |           128 |         4 |
|     352.6000 |     60.5858 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|     347.5000 |     55.5765 | most_recently_used   | random           | lru             | all               |           256 |         4 |
|     347.4000 |    109.8628 | most_recently_added  | random           | random          | all               |           128 |         5 |
|     346.7500 |     37.4057 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         4 |
|     346.7500 |     37.4057 | most_recently_added  | bfs              | fifo            | all               |            32 |         4 |
|     345.3333 |     56.0079 | most_recently_added  | random           | lfu             | all               |           128 |         3 |
|     345.2500 |     73.8660 | most_recently_added  | random           | lru             | all               |           128 |         4 |
|     343.7500 |     74.5197 | most_recently_used   | bfs              | lfu             | all               |             8 |         4 |
|     343.3333 |     99.6070 | most_recently_used   | dijkstra         | random          | all               |            64 |         3 |
|     338.7500 |    111.7058 | most_recently_added  | random           | lru             | all               |            32 |         4 |
|     338.5000 |     53.0731 | most_frequently_used | random           | lru             | all               |            32 |         4 |
|     337.5000 |     40.9542 | most_recently_used   | random           | fifo            | all               |           256 |         4 |
|     336.2500 |     49.8867 | most_recently_used   | random           | lfu             | all               |            32 |         4 |
|     332.5000 |     64.6471 | most_frequently_used | random           | random          | all               |           128 |         4 |
|     330.0000 |     75.5811 | most_frequently_used | random           | lfu             | all               |            64 |         4 |
|     323.7500 |    111.3741 | most_recently_added  | random           | random          | all               |           256 |         4 |
|     322.2500 |     68.8998 | most_frequently_used | bfs              | lfu             | all               |             4 |         4 |
|     319.7500 |    105.1579 | most_recently_used   | random           | lfu             | all               |            64 |         4 |
|     317.5000 |     96.2562 | most_recently_added  | random           | lru             | all               |            64 |         4 |
|     311.5000 |      4.9749 | most_recently_added  | bfs              | lru             | all               |             8 |         4 |
|     311.5000 |     29.3044 | most_recently_used   | bfs              | random          | all               |            32 |         4 |
|     305.5000 |      6.8007 | most_frequently_used | bfs              | fifo            | all               |            32 |         4 |
|     305.0000 |      7.7889 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         3 |
|     301.7500 |     59.4112 | most_frequently_used | random           | lru             | all               |            16 |         4 |
|     301.2500 |     72.7783 | most_frequently_used | random           | lru             | all               |            64 |         4 |
|     300.0000 |     14.7139 | most_recently_used   | bfs              | lru             | all               |             8 |         4 |
|     299.4000 |     77.8989 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|     297.7500 |     86.0592 | most_recently_used   | bfs              | lfu             | all               |             4 |         4 |
|     295.7500 |     38.5770 | most_frequently_used | bfs              | random          | all               |            32 |         4 |
|     286.3333 |     72.8530 | most_recently_used   | dijkstra         | random          | all               |            32 |         3 |
|     286.2500 |     17.5553 | most_recently_used   | dijkstra         | lru             | all               |             8 |         4 |
|     285.7500 |     21.9360 | most_frequently_used | dijkstra         | lru             | all               |             8 |         4 |
|     285.0000 |     14.7817 | most_frequently_used | bfs              | lru             | all               |             8 |         4 |
|     283.7500 |     46.7567 | most_recently_added  | dijkstra         | lru             | all               |             8 |         4 |
|     283.5000 |     24.1299 | most_recently_used   | random           | random          | all               |            64 |         4 |
|     282.0000 |     30.7652 | most_recently_used   | bfs              | fifo            | all               |            32 |         4 |
|     273.7500 |     73.5540 | most_recently_added  | random           | lru             | all               |            16 |         4 |
|     273.6667 |     31.3723 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         3 |
|     272.5000 |    115.0532 | most_recently_used   | random           | random          | all               |           128 |         4 |
|     268.7500 |     51.5819 | most_frequently_used | dijkstra         | random          | all               |            32 |         4 |
|     267.2500 |     63.1838 | most_frequently_used | random           | random          | all               |            64 |         4 |
|     266.5000 |     56.1004 | most_recently_added  | random           | fifo            | all               |           128 |         4 |
|     264.0000 |     55.8077 | most_recently_added  | bfs              | random          | all               |            32 |         4 |
|     263.6667 |     76.2860 | most_recently_added  | random           | lfu             | all               |             8 |         3 |
|     261.2500 |     71.2017 | most_recently_added  | dijkstra         | random          | all               |            32 |         4 |
|     260.0000 |     33.9706 | most_frequently_used | random           | lfu             | all               |            16 |         4 |
|     259.7500 |     48.8435 | most_recently_used   | random           | lru             | all               |            16 |         4 |
|     252.2500 |     66.8931 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         4 |
|     248.7500 |     44.6731 | most_recently_used   | random           | fifo            | all               |           128 |         4 |
|     246.0000 |     63.2811 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         4 |
|     243.2500 |     65.5224 | most_recently_added  | random           | lru             | all               |             8 |         4 |
|     230.6667 |     36.8088 | most_recently_used   | dijkstra         | random          | all               |            16 |         3 |
|     230.2500 |    126.8865 | most_frequently_used | random           | lfu             | all               |             4 |         4 |
|     223.6667 |     26.6625 | most_recently_added  | random           | lfu             | all               |             2 |         3 |
|     222.0000 |     63.6113 | most_recently_added  | random           | random          | all               |            64 |         5 |
|     219.2500 |     37.4591 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         4 |
|     215.5000 |     55.8816 | most_recently_added  | bfs              | random          | all               |            16 |         4 |
|     211.5000 |     18.0208 | most_frequently_used | random           | fifo            | all               |            64 |         4 |
|     211.2500 |     20.1168 | most_recently_added  | bfs              | fifo            | all               |            16 |         4 |
|     207.2500 |     13.9530 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         4 |
|     202.3333 |      8.8066 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         3 |
|     201.0000 |     11.6404 | most_frequently_used | bfs              | fifo            | all               |            16 |         4 |
|     194.6667 |     19.3620 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         3 |
|     194.2500 |     24.6006 | most_frequently_used | random           | lru             | all               |             8 |         4 |
|     194.0000 |     16.8077 | most_recently_used   | bfs              | fifo            | all               |            16 |         4 |
|     188.2500 |     34.3684 | most_recently_used   | random           | lru             | all               |             8 |         4 |
|     188.2500 |    106.1611 | most_frequently_used | random           | fifo            | all               |           128 |         4 |
|     182.5000 |     90.6766 | most_recently_used   | random           | lfu             | all               |             4 |         4 |
|     179.5000 |     29.8789 | most_frequently_used | bfs              | random          | all               |            16 |         4 |
|     178.0000 |     63.6121 | most_recently_used   | random           | fifo            | all               |            64 |         4 |
|     177.2500 |     54.1589 | most_recently_added  | random           | fifo            | all               |            64 |         4 |
|     176.2500 |     67.1244 | most_recently_used   | bfs              | lfu             | all               |             2 |         4 |
|     176.2500 |     67.1244 | most_frequently_used | bfs              | lfu             | all               |             2 |         4 |
|     174.2500 |     59.9265 | most_recently_added  | dijkstra         | random          | all               |            16 |         4 |
|     174.0000 |     22.3271 | most_recently_used   | bfs              | random          | all               |            16 |         4 |
|     173.6667 |     25.7725 | most_frequently_used | dijkstra         | random          | all               |            16 |         3 |
|     168.2500 |     33.9660 | most_recently_used   | random           | random          | all               |            32 |         4 |
|     166.7500 |     70.9872 | most_recently_added  | bfs              | lfu             | all               |             2 |         4 |
|     166.5000 |     55.6889 | most_frequently_used | random           | random          | all               |            32 |         4 |
|     161.7500 |     44.1156 | most_recently_used   | bfs              | lru             | all               |             4 |         4 |
|     161.7500 |     44.1156 | most_frequently_used | bfs              | lru             | all               |             4 |         4 |
|     161.7500 |     48.7513 | most_frequently_used | bfs              | random          | all               |             8 |         4 |
|     159.5000 |     31.9257 | most_recently_used   | random           | fifo            | all               |            32 |         4 |
|     158.0000 |     38.3406 | most_frequently_used | random           | lfu             | all               |             2 |         4 |
|     157.0000 |     18.1842 | most_recently_used   | dijkstra         | random          | all               |             8 |         3 |
|     150.3333 |      5.7927 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         3 |
|     150.3333 |      5.7927 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         3 |
|     149.7500 |     33.0407 | most_frequently_used | random           | fifo            | all               |             8 |         4 |
|     148.6667 |     40.1442 | most_recently_used   | random           | lfu             | all               |             2 |         3 |
|     148.0000 |     41.2698 | most_recently_added  | random           | random          | all               |            32 |         5 |
|     146.7500 |     27.0497 | most_recently_used   | random           | random          | all               |            16 |         4 |
|     146.0000 |     34.5615 | most_recently_added  | bfs              | lru             | all               |             4 |         4 |
|     146.0000 |     11.4310 | most_frequently_used | dijkstra         | random          | all               |             8 |         3 |
|     144.5000 |     29.5846 | most_frequently_used | random           | random          | all               |            16 |         4 |
|     144.0000 |     26.1343 | most_recently_used   | bfs              | fifo            | all               |             8 |         4 |
|     144.0000 |     26.1343 | most_frequently_used | bfs              | fifo            | all               |             8 |         4 |
|     141.2500 |     15.3032 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         4 |
|     140.0000 |     55.1785 | most_recently_added  | random           | lfu             | all               |             4 |         3 |
|     139.5000 |     55.5630 | most_recently_added  | random           | fifo            | all               |            32 |         4 |
|     136.8000 |     30.4657 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|     136.0000 |     27.2855 | most_recently_used   | bfs              | random          | all               |             8 |         4 |
|     135.0000 |     33.8231 | most_frequently_used | dijkstra         | lru             | all               |             4 |         4 |
|     134.7500 |     24.3143 | most_frequently_used | random           | fifo            | all               |            16 |         4 |
|     134.5000 |     37.5267 | most_frequently_used | random           | fifo            | all               |            32 |         4 |
|     133.2500 |     11.2333 | most_recently_added  | bfs              | fifo            | all               |             8 |         4 |
|     131.2500 |     19.3051 | most_recently_added  | dijkstra         | lru             | all               |             4 |         4 |
|     130.2500 |     22.4207 | most_recently_added  | dijkstra         | random          | all               |             8 |         4 |
|     130.0000 |     34.9380 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         3 |
|     130.0000 |     34.9380 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         3 |
|     129.0000 |     43.9716 | most_recently_added  | random           | fifo            | all               |            16 |         4 |
|     128.5000 |     18.8481 | most_recently_added  | bfs              | random          | all               |             8 |         4 |
|     128.0000 |     51.3566 | most_recently_added  | random           | random          | all               |            16 |         4 |
|     126.0000 |     43.8577 | most_recently_used   | random           | fifo            | all               |            16 |         4 |
|     125.3333 |     38.5256 | most_frequently_used | dijkstra         | random          | all               |             4 |         3 |
|     125.3333 |     38.5256 | most_recently_used   | dijkstra         | random          | all               |             4 |         3 |
|     118.5000 |     45.2023 | most_recently_used   | random           | lru             | all               |             2 |         4 |
|     118.5000 |     45.2023 | most_frequently_used | random           | lru             | all               |             2 |         4 |
|     116.6667 |     18.0801 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         3 |
|     116.6667 |     18.0801 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         3 |
|     114.0000 |     24.4643 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         4 |
|     112.7500 |     23.8472 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         4 |
|     111.0000 |     28.2931 | most_recently_added  | bfs              | lru             | all               |             2 |         4 |
|     108.2500 |     21.6838 | most_recently_added  | dijkstra         | random          | all               |             4 |         4 |
|     107.2500 |     15.6744 | most_recently_added  | bfs              | random          | all               |             4 |         4 |
|     105.0000 |     22.9020 | most_frequently_used | bfs              | lru             | all               |             2 |         4 |
|     105.0000 |     22.9020 | most_recently_used   | bfs              | lru             | all               |             2 |         4 |
|     104.0000 |     29.4024 | most_recently_added  | dijkstra         | lru             | all               |             2 |         4 |
|     103.2500 |     39.9773 | most_frequently_used | dijkstra         | lru             | all               |             2 |         4 |
|     103.2500 |     15.5624 | most_recently_added  | random           | random          | all               |             8 |         4 |
|     102.2500 |     21.1704 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         4 |
|     101.5000 |     14.6714 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         4 |
|     100.5000 |     30.1206 | most_recently_used   | random           | random          | all               |             4 |         4 |
|      99.5000 |     26.6880 | most_recently_added  | random           | random          | all               |             2 |         4 |
|      99.2500 |     15.5141 | most_frequently_used | bfs              | fifo            | all               |             2 |         4 |
|      99.2500 |     15.5141 | most_recently_used   | bfs              | fifo            | all               |             2 |         4 |
|      98.2500 |     25.4104 | most_frequently_used | bfs              | random          | all               |             4 |         4 |
|      97.7500 |     12.6763 | most_recently_added  | bfs              | fifo            | all               |             2 |         4 |
|      97.5000 |     34.2673 | most_frequently_used | random           | random          | all               |             8 |         4 |
|      96.7500 |     31.1157 | most_frequently_used | random           | random          | all               |             4 |         4 |
|      94.0000 |     12.3491 | most_recently_added  | bfs              | fifo            | all               |             4 |         4 |
|      92.4000 |     41.8263 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|      92.0000 |     14.2478 | most_recently_used   | bfs              | fifo            | all               |             4 |         4 |
|      92.0000 |     14.2478 | most_frequently_used | bfs              | fifo            | all               |             4 |         4 |
|      88.5000 |     35.8922 | most_recently_added  | random           | lru             | all               |             4 |         4 |
|      87.5000 |     10.7819 | most_recently_used   | bfs              | random          | all               |             4 |         4 |
|      85.7500 |     27.2798 | most_recently_added  | random           | lru             | all               |             2 |         4 |
|      84.2500 |     14.4460 | most_recently_added  | random           | fifo            | all               |             4 |         4 |
|      84.0000 |     39.4525 | most_recently_added  | random           | fifo            | all               |             2 |         4 |
|      82.2500 |     45.4773 | most_recently_added  | dijkstra         | random          | all               |             2 |         4 |
|      80.0000 |     24.6475 | most_frequently_used | random           | random          | all               |             2 |         4 |
|      80.0000 |     24.6475 | most_recently_used   | random           | random          | all               |             2 |         4 |
|      78.5000 |     23.4787 | most_recently_used   | random           | fifo            | all               |             8 |         4 |
|      77.7500 |     38.6806 | most_recently_added  | random           | fifo            | all               |             8 |         4 |
|      76.5000 |     18.6346 | most_recently_added  | random           | random          | all               |             4 |         4 |
|      73.3333 |     17.1723 | most_recently_used   | dijkstra         | random          | all               |             2 |         3 |
|      73.3333 |     17.1723 | most_frequently_used | dijkstra         | random          | all               |             2 |         3 |
|      73.2500 |     34.8667 | most_recently_used   | random           | fifo            | all               |             4 |         4 |
|      73.2500 |     34.8667 | most_frequently_used | random           | fifo            | all               |             4 |         4 |
|      72.2500 |     38.9511 | most_recently_used   | random           | random          | all               |             8 |         4 |
|      72.0000 |     22.1923 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         4 |
|      70.2500 |     17.5410 | most_recently_used   | random           | lru             | all               |             0 |         4 |
|      70.2500 |     17.5410 | most_recently_added  | random           | lru             | all               |             0 |         4 |
|      70.2500 |     17.5410 | most_frequently_used | random           | lfu             | all               |             0 |         4 |
|      70.2500 |     17.5410 | most_frequently_used | random           | lru             | all               |             0 |         4 |
|      69.0000 |     20.3142 | most_recently_used   | dijkstra         | random          | all               |             0 |         3 |
|      69.0000 |     20.3142 | most_frequently_used | dijkstra         | random          | all               |             0 |         3 |
|      69.0000 |     20.3142 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         3 |
|      69.0000 |     20.3142 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         3 |
|      68.2500 |     18.4713 | most_frequently_used | bfs              | random          | all               |             2 |         4 |
|      68.2500 |     18.4713 | most_recently_used   | bfs              | random          | all               |             2 |         4 |
|      66.2500 |      4.9687 | most_frequently_used | bfs              | lru             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_frequently_used | bfs              | lfu             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_used   | bfs              | lru             | all               |             0 |         4 |
|      66.2500 |     19.1882 | most_frequently_used | random           | lru             | all               |             4 |         4 |
|      66.2500 |      4.9687 | most_recently_added  | bfs              | lru             | all               |             0 |         4 |
|      66.2500 |     19.1882 | most_recently_used   | random           | lru             | all               |             4 |         4 |
|      66.2500 |      4.9687 | most_frequently_used | dijkstra         | lru             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_used   | dijkstra         | lru             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_added  | bfs              | lfu             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_added  | dijkstra         | lru             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         4 |
|      66.2500 |      4.9687 | most_recently_used   | bfs              | lfu             | all               |             0 |         4 |
|      66.0000 |     18.3848 | most_recently_added  | random           | lfu             | all               |             0 |         3 |
|      66.0000 |     18.3848 | most_recently_used   | random           | lfu             | all               |             0 |         3 |
|      65.5000 |     24.8847 | most_recently_added  | bfs              | random          | all               |             2 |         4 |
|      65.0000 |     29.6057 | most_frequently_used | random           | fifo            | all               |             2 |         4 |
|      65.0000 |     29.6057 | most_recently_used   | random           | fifo            | all               |             2 |         4 |
|      58.0000 |     25.9326 | most_frequently_used | bfs              | random          | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_recently_used   | bfs              | random          | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_recently_used   | bfs              | fifo            | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_recently_added  | dijkstra         | random          | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_recently_added  | bfs              | random          | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_recently_added  | bfs              | fifo            | all               |             0 |         4 |
|      58.0000 |     25.9326 | most_frequently_used | bfs              | fifo            | all               |             0 |         4 |
|      50.7500 |     19.4984 | most_frequently_used | random           | fifo            | all               |             0 |         4 |
|      50.7500 |     19.4984 | most_recently_added  | random           | fifo            | all               |             0 |         4 |
|      50.7500 |     19.4984 | most_frequently_used | random           | random          | all               |             0 |         4 |
|      50.7500 |     19.4984 | most_recently_used   | random           | fifo            | all               |             0 |         4 |
|      50.7500 |     19.4984 | most_recently_added  | random           | random          | all               |             0 |         4 |
|      50.7500 |     19.4984 | most_recently_used   | random           | random          | all               |             0 |         4 |

## Memory Size 0

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|      70.2500 |     17.5410 | most_recently_added  | random           | lru             | all               |         4 |
|      70.2500 |     17.5410 | most_recently_used   | random           | lru             | all               |         4 |
|      70.2500 |     17.5410 | most_frequently_used | random           | lfu             | all               |         4 |
|      70.2500 |     17.5410 | most_frequently_used | random           | lru             | all               |         4 |
|      69.0000 |     20.3142 | most_recently_used   | dijkstra         | random          | all               |         3 |
|      69.0000 |     20.3142 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|      69.0000 |     20.3142 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|      69.0000 |     20.3142 | most_frequently_used | dijkstra         | random          | all               |         3 |
|      66.2500 |      4.9687 | most_recently_used   | bfs              | lru             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|      66.2500 |      4.9687 | most_frequently_used | bfs              | lru             | all               |         4 |
|      66.2500 |      4.9687 | most_frequently_used | bfs              | lfu             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_used   | bfs              | lfu             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|      66.2500 |      4.9687 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|      66.2500 |      4.9687 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_added  | bfs              | lru             | all               |         4 |
|      66.2500 |      4.9687 | most_recently_added  | bfs              | lfu             | all               |         4 |
|      66.0000 |     18.3848 | most_recently_added  | random           | lfu             | all               |         3 |
|      66.0000 |     18.3848 | most_recently_used   | random           | lfu             | all               |         3 |
|      58.0000 |     25.9326 | most_frequently_used | bfs              | random          | all               |         4 |
|      58.0000 |     25.9326 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      58.0000 |     25.9326 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      58.0000 |     25.9326 | most_recently_added  | bfs              | random          | all               |         4 |
|      58.0000 |     25.9326 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      58.0000 |     25.9326 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|      58.0000 |     25.9326 | most_recently_used   | bfs              | random          | all               |         4 |
|      58.0000 |     25.9326 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      50.7500 |     19.4984 | most_frequently_used | random           | fifo            | all               |         4 |
|      50.7500 |     19.4984 | most_frequently_used | random           | random          | all               |         4 |
|      50.7500 |     19.4984 | most_recently_added  | random           | fifo            | all               |         4 |
|      50.7500 |     19.4984 | most_recently_added  | random           | random          | all               |         4 |
|      50.7500 |     19.4984 | most_recently_used   | random           | fifo            | all               |         4 |
|      50.7500 |     19.4984 | most_recently_used   | random           | random          | all               |         4 |

## Memory Size 2

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     223.6667 |     26.6625 | most_recently_added  | random           | lfu             | all               |         3 |
|     176.2500 |     67.1244 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     176.2500 |     67.1244 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     166.7500 |     70.9872 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     158.0000 |     38.3406 | most_frequently_used | random           | lfu             | all               |         4 |
|     148.6667 |     40.1442 | most_recently_used   | random           | lfu             | all               |         3 |
|     130.0000 |     34.9380 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     130.0000 |     34.9380 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     118.5000 |     45.2023 | most_recently_used   | random           | lru             | all               |         4 |
|     118.5000 |     45.2023 | most_frequently_used | random           | lru             | all               |         4 |
|     114.0000 |     24.4643 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     111.0000 |     28.2931 | most_recently_added  | bfs              | lru             | all               |         4 |
|     105.0000 |     22.9020 | most_frequently_used | bfs              | lru             | all               |         4 |
|     105.0000 |     22.9020 | most_recently_used   | bfs              | lru             | all               |         4 |
|     104.0000 |     29.4024 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     103.2500 |     39.9773 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     102.2500 |     21.1704 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     101.5000 |     14.6714 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|      99.5000 |     26.6880 | most_recently_added  | random           | random          | all               |         4 |
|      99.2500 |     15.5141 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      99.2500 |     15.5141 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      97.7500 |     12.6763 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      92.4000 |     41.8263 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|      85.7500 |     27.2798 | most_recently_added  | random           | lru             | all               |         4 |
|      84.0000 |     39.4525 | most_recently_added  | random           | fifo            | all               |         4 |
|      82.2500 |     45.4773 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      80.0000 |     24.6475 | most_recently_used   | random           | random          | all               |         4 |
|      80.0000 |     24.6475 | most_frequently_used | random           | random          | all               |         4 |
|      73.3333 |     17.1723 | most_frequently_used | dijkstra         | random          | all               |         3 |
|      73.3333 |     17.1723 | most_recently_used   | dijkstra         | random          | all               |         3 |
|      72.0000 |     22.1923 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|      68.2500 |     18.4713 | most_frequently_used | bfs              | random          | all               |         4 |
|      68.2500 |     18.4713 | most_recently_used   | bfs              | random          | all               |         4 |
|      65.5000 |     24.8847 | most_recently_added  | bfs              | random          | all               |         4 |
|      65.0000 |     29.6057 | most_frequently_used | random           | fifo            | all               |         4 |
|      65.0000 |     29.6057 | most_recently_used   | random           | fifo            | all               |         4 |

## Memory Size 4

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     322.2500 |     68.8998 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     299.4000 |     77.8989 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     297.7500 |     86.0592 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     252.2500 |     66.8931 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     246.0000 |     63.2811 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     230.2500 |    126.8865 | most_frequently_used | random           | lfu             | all               |         4 |
|     219.2500 |     37.4591 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     182.5000 |     90.6766 | most_recently_used   | random           | lfu             | all               |         4 |
|     161.7500 |     44.1156 | most_frequently_used | bfs              | lru             | all               |         4 |
|     161.7500 |     44.1156 | most_recently_used   | bfs              | lru             | all               |         4 |
|     146.0000 |     34.5615 | most_recently_added  | bfs              | lru             | all               |         4 |
|     140.0000 |     55.1785 | most_recently_added  | random           | lfu             | all               |         3 |
|     136.8000 |     30.4657 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     135.0000 |     33.8231 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     131.2500 |     19.3051 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     125.3333 |     38.5256 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     125.3333 |     38.5256 | most_frequently_used | dijkstra         | random          | all               |         3 |
|     116.6667 |     18.0801 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     116.6667 |     18.0801 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     112.7500 |     23.8472 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     108.2500 |     21.6838 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     107.2500 |     15.6744 | most_recently_added  | bfs              | random          | all               |         4 |
|     100.5000 |     30.1206 | most_recently_used   | random           | random          | all               |         4 |
|      98.2500 |     25.4104 | most_frequently_used | bfs              | random          | all               |         4 |
|      96.7500 |     31.1157 | most_frequently_used | random           | random          | all               |         4 |
|      94.0000 |     12.3491 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      92.0000 |     14.2478 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      92.0000 |     14.2478 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      88.5000 |     35.8922 | most_recently_added  | random           | lru             | all               |         4 |
|      87.5000 |     10.7819 | most_recently_used   | bfs              | random          | all               |         4 |
|      84.2500 |     14.4460 | most_recently_added  | random           | fifo            | all               |         4 |
|      76.5000 |     18.6346 | most_recently_added  | random           | random          | all               |         4 |
|      73.2500 |     34.8667 | most_recently_used   | random           | fifo            | all               |         4 |
|      73.2500 |     34.8667 | most_frequently_used | random           | fifo            | all               |         4 |
|      66.2500 |     19.1882 | most_frequently_used | random           | lru             | all               |         4 |
|      66.2500 |     19.1882 | most_recently_used   | random           | lru             | all               |         4 |

## Memory Size 8

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     444.2500 |     61.7510 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     437.5000 |     17.0367 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     420.0000 |     53.9583 | most_recently_used   | random           | lfu             | all               |         4 |
|     387.2500 |     32.2442 | most_frequently_used | random           | lfu             | all               |         4 |
|     383.2500 |    100.9762 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     358.7500 |     72.6993 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     352.6000 |     60.5858 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     343.7500 |     74.5197 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     311.5000 |      4.9749 | most_recently_added  | bfs              | lru             | all               |         4 |
|     300.0000 |     14.7139 | most_recently_used   | bfs              | lru             | all               |         4 |
|     286.2500 |     17.5553 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     285.7500 |     21.9360 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     285.0000 |     14.7817 | most_frequently_used | bfs              | lru             | all               |         4 |
|     283.7500 |     46.7567 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     263.6667 |     76.2860 | most_recently_added  | random           | lfu             | all               |         3 |
|     243.2500 |     65.5224 | most_recently_added  | random           | lru             | all               |         4 |
|     194.2500 |     24.6006 | most_frequently_used | random           | lru             | all               |         4 |
|     188.2500 |     34.3684 | most_recently_used   | random           | lru             | all               |         4 |
|     161.7500 |     48.7513 | most_frequently_used | bfs              | random          | all               |         4 |
|     157.0000 |     18.1842 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     150.3333 |      5.7927 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     150.3333 |      5.7927 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     149.7500 |     33.0407 | most_frequently_used | random           | fifo            | all               |         4 |
|     146.0000 |     11.4310 | most_frequently_used | dijkstra         | random          | all               |         3 |
|     144.0000 |     26.1343 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     144.0000 |     26.1343 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     141.2500 |     15.3032 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     136.0000 |     27.2855 | most_recently_used   | bfs              | random          | all               |         4 |
|     133.2500 |     11.2333 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     130.2500 |     22.4207 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     128.5000 |     18.8481 | most_recently_added  | bfs              | random          | all               |         4 |
|     103.2500 |     15.5624 | most_recently_added  | random           | random          | all               |         4 |
|      97.5000 |     34.2673 | most_frequently_used | random           | random          | all               |         4 |
|      78.5000 |     23.4787 | most_recently_used   | random           | fifo            | all               |         4 |
|      77.7500 |     38.6806 | most_recently_added  | random           | fifo            | all               |         4 |
|      72.2500 |     38.9511 | most_recently_used   | random           | random          | all               |         4 |

## Memory Size 16

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     617.2500 |     63.6450 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     559.0000 |     27.0463 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     531.8000 |     60.9964 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     528.0000 |     66.5545 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     526.0000 |     94.4272 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     517.0000 |     87.9631 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     516.2500 |     27.7252 | most_frequently_used | bfs              | lru             | all               |         4 |
|     512.7500 |     35.3297 | most_recently_added  | bfs              | lru             | all               |         4 |
|     497.5000 |     57.6910 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     482.5000 |     63.8338 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     475.5000 |     80.1888 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     466.0000 |     42.0238 | most_recently_used   | bfs              | lru             | all               |         4 |
|     440.3333 |    114.9647 | most_recently_added  | random           | lfu             | all               |         3 |
|     360.7500 |    123.6414 | most_recently_used   | random           | lfu             | all               |         4 |
|     301.7500 |     59.4112 | most_frequently_used | random           | lru             | all               |         4 |
|     273.7500 |     73.5540 | most_recently_added  | random           | lru             | all               |         4 |
|     260.0000 |     33.9706 | most_frequently_used | random           | lfu             | all               |         4 |
|     259.7500 |     48.8435 | most_recently_used   | random           | lru             | all               |         4 |
|     230.6667 |     36.8088 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     215.5000 |     55.8816 | most_recently_added  | bfs              | random          | all               |         4 |
|     211.2500 |     20.1168 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     207.2500 |     13.9530 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     202.3333 |      8.8066 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     201.0000 |     11.6404 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     194.6667 |     19.3620 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     194.0000 |     16.8077 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     179.5000 |     29.8789 | most_frequently_used | bfs              | random          | all               |         4 |
|     174.2500 |     59.9265 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     174.0000 |     22.3271 | most_recently_used   | bfs              | random          | all               |         4 |
|     173.6667 |     25.7725 | most_frequently_used | dijkstra         | random          | all               |         3 |
|     146.7500 |     27.0497 | most_recently_used   | random           | random          | all               |         4 |
|     144.5000 |     29.5846 | most_frequently_used | random           | random          | all               |         4 |
|     134.7500 |     24.3143 | most_frequently_used | random           | fifo            | all               |         4 |
|     129.0000 |     43.9716 | most_recently_added  | random           | fifo            | all               |         4 |
|     128.0000 |     51.3566 | most_recently_added  | random           | random          | all               |         4 |
|     126.0000 |     43.8577 | most_recently_used   | random           | fifo            | all               |         4 |

## Memory Size 32

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     702.5000 |     54.9067 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     681.0000 |     62.2937 | most_recently_used   | bfs              | lru             | all               |         4 |
|     675.7500 |     75.9091 | most_recently_added  | bfs              | lru             | all               |         4 |
|     667.8000 |     75.7744 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     638.7500 |    127.1679 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     633.0000 |     55.9151 | most_frequently_used | bfs              | lru             | all               |         4 |
|     625.2500 |    100.8027 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     624.5000 |     80.2013 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     610.7500 |     26.9293 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     592.0000 |     90.4682 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     572.2500 |    137.5125 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     563.7500 |    146.1359 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     420.0000 |     23.8642 | most_frequently_used | random           | lfu             | all               |         4 |
|     411.2500 |     80.6082 | most_recently_used   | random           | lru             | all               |         4 |
|     357.3333 |     37.9678 | most_recently_added  | random           | lfu             | all               |         3 |
|     346.7500 |     37.4057 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     346.7500 |     37.4057 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     338.7500 |    111.7058 | most_recently_added  | random           | lru             | all               |         4 |
|     338.5000 |     53.0731 | most_frequently_used | random           | lru             | all               |         4 |
|     336.2500 |     49.8867 | most_recently_used   | random           | lfu             | all               |         4 |
|     311.5000 |     29.3044 | most_recently_used   | bfs              | random          | all               |         4 |
|     305.5000 |      6.8007 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     305.0000 |      7.7889 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     295.7500 |     38.5770 | most_frequently_used | bfs              | random          | all               |         4 |
|     286.3333 |     72.8530 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     282.0000 |     30.7652 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     273.6667 |     31.3723 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     268.7500 |     51.5819 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     264.0000 |     55.8077 | most_recently_added  | bfs              | random          | all               |         4 |
|     261.2500 |     71.2017 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     168.2500 |     33.9660 | most_recently_used   | random           | random          | all               |         4 |
|     166.5000 |     55.6889 | most_frequently_used | random           | random          | all               |         4 |
|     159.5000 |     31.9257 | most_recently_used   | random           | fifo            | all               |         4 |
|     148.0000 |     41.2698 | most_recently_added  | random           | random          | all               |         5 |
|     139.5000 |     55.5630 | most_recently_added  | random           | fifo            | all               |         4 |
|     134.5000 |     37.5267 | most_frequently_used | random           | fifo            | all               |         4 |

## Memory Size 64

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     721.0000 |     45.3707 | most_recently_added  | bfs              | lru             | all               |         4 |
|     710.2500 |     41.4872 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     707.2500 |     43.6427 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     694.7500 |     63.9037 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     686.2500 |     37.8575 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     685.2500 |     33.2519 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     662.5000 |     15.2561 | most_recently_used   | bfs              | lru             | all               |         4 |
|     658.5000 |     44.4382 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     617.7500 |     40.6471 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     598.0000 |     24.5255 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     588.5000 |     27.5454 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     581.0000 |     28.1869 | most_frequently_used | bfs              | lru             | all               |         4 |
|     505.0000 |     63.9375 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     494.7500 |     26.2809 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     485.6667 |     29.4882 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     482.0000 |     41.8629 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     472.2500 |     40.2888 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     453.2500 |     75.0712 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     421.2500 |     25.3513 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     405.7500 |      5.6292 | most_recently_used   | bfs              | random          | all               |         4 |
|     405.0000 |     31.7569 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     404.7500 |    148.8613 | most_recently_used   | random           | lru             | all               |         4 |
|     379.0000 |     44.6430 | most_recently_added  | bfs              | random          | all               |         4 |
|     377.0000 |     37.3564 | most_frequently_used | bfs              | random          | all               |         4 |
|     370.6667 |     52.9297 | most_recently_added  | random           | lfu             | all               |         3 |
|     343.3333 |     99.6070 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     330.0000 |     75.5811 | most_frequently_used | random           | lfu             | all               |         4 |
|     319.7500 |    105.1579 | most_recently_used   | random           | lfu             | all               |         4 |
|     317.5000 |     96.2562 | most_recently_added  | random           | lru             | all               |         4 |
|     301.2500 |     72.7783 | most_frequently_used | random           | lru             | all               |         4 |
|     283.5000 |     24.1299 | most_recently_used   | random           | random          | all               |         4 |
|     267.2500 |     63.1838 | most_frequently_used | random           | random          | all               |         4 |
|     222.0000 |     63.6113 | most_recently_added  | random           | random          | all               |         5 |
|     211.5000 |     18.0208 | most_frequently_used | random           | fifo            | all               |         4 |
|     178.0000 |     63.6121 | most_recently_used   | random           | fifo            | all               |         4 |
|     177.2500 |     54.1589 | most_recently_added  | random           | fifo            | all               |         4 |

## Memory Size 128

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     745.2500 |     47.6832 | most_recently_added  | bfs              | lru             | all               |         4 |
|     728.5000 |     73.0223 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     726.2500 |     38.4927 | most_recently_used   | bfs              | lru             | all               |         4 |
|     721.5000 |     55.6799 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     719.5000 |     41.6803 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     712.7500 |     57.8765 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     700.3333 |     31.9409 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     692.0000 |     54.3093 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     690.5000 |     43.0726 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     678.5000 |     42.1337 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     656.0000 |     62.6578 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     654.5000 |     63.3739 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     651.0000 |     60.2163 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|     645.0000 |     62.3110 | most_frequently_used | bfs              | lru             | all               |         3 |
|     643.2500 |     70.0620 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     639.2500 |     44.5498 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     637.2500 |     61.8643 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     626.5000 |     68.1634 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     616.0000 |     48.8740 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     583.6667 |    100.9433 | most_recently_added  | dijkstra         | random          | all               |         3 |
|     567.2500 |     83.2237 | most_recently_added  | bfs              | random          | all               |         4 |
|     542.7500 |     84.1973 | most_recently_used   | bfs              | random          | all               |         4 |
|     529.0000 |     47.9270 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     502.5000 |     17.1537 | most_frequently_used | bfs              | random          | all               |         4 |
|     371.0000 |     41.1947 | most_frequently_used | random           | lfu             | all               |         4 |
|     368.5000 |     40.6848 | most_frequently_used | random           | lru             | all               |         4 |
|     359.0000 |     99.3428 | most_recently_used   | random           | lfu             | all               |         4 |
|     357.2500 |     64.2471 | most_recently_used   | random           | lru             | all               |         4 |
|     347.4000 |    109.8628 | most_recently_added  | random           | random          | all               |         5 |
|     345.3333 |     56.0079 | most_recently_added  | random           | lfu             | all               |         3 |
|     345.2500 |     73.8660 | most_recently_added  | random           | lru             | all               |         4 |
|     332.5000 |     64.6471 | most_frequently_used | random           | random          | all               |         4 |
|     272.5000 |    115.0532 | most_recently_used   | random           | random          | all               |         4 |
|     266.5000 |     56.1004 | most_recently_added  | random           | fifo            | all               |         4 |
|     248.7500 |     44.6731 | most_recently_used   | random           | fifo            | all               |         4 |
|     188.2500 |    106.1611 | most_frequently_used | random           | fifo            | all               |         4 |

## Memory Size 256

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     751.6667 |     30.1809 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     737.2500 |     55.0744 | most_recently_added  | bfs              | lru             | all               |         4 |
|     733.7500 |     55.5535 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     730.7500 |     56.7775 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     729.2500 |     37.7649 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     728.7500 |     73.3191 | most_recently_used   | bfs              | lru             | all               |         4 |
|     726.7500 |     42.1152 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     722.6667 |     22.8959 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     716.7500 |     47.2989 | most_recently_used   | bfs              | random          | all               |         4 |
|     715.5000 |     52.2135 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     714.2500 |     47.2090 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     713.2500 |     48.9713 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     711.7500 |     38.5641 | most_recently_added  | bfs              | random          | all               |         4 |
|     698.5000 |     55.4549 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     684.5000 |     74.8883 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     645.3333 |     90.2749 | most_recently_added  | dijkstra         | random          | all               |         3 |
|     637.7500 |     28.9687 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     635.0000 |     36.1202 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     612.5000 |     67.7809 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     605.0000 |     59.4362 | most_frequently_used | bfs              | lru             | all               |         3 |
|     605.0000 |     58.4466 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|     599.5000 |     74.2108 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     592.0000 |     31.9139 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     580.7500 |     24.8131 | most_frequently_used | bfs              | random          | all               |         4 |
|     508.0000 |     36.6879 | most_recently_added  | random           | lfu             | all               |         3 |
|     443.2500 |    111.8914 | most_recently_added  | random           | lru             | all               |         4 |
|     404.2500 |     58.2253 | most_frequently_used | random           | lfu             | all               |         4 |
|     404.2500 |     58.2253 | most_frequently_used | random           | lru             | all               |         4 |
|     393.5000 |     57.7819 | most_recently_added  | random           | fifo            | all               |         4 |
|     389.2500 |     48.0488 | most_frequently_used | random           | fifo            | all               |         4 |
|     374.5000 |     34.3329 | most_frequently_used | random           | random          | all               |         4 |
|     374.0000 |     51.5315 | most_recently_used   | random           | lfu             | all               |         4 |
|     358.0000 |     40.7370 | most_recently_used   | random           | random          | all               |         4 |
|     347.5000 |     55.5765 | most_recently_used   | random           | lru             | all               |         4 |
|     337.5000 |     40.9542 | most_recently_used   | random           | fifo            | all               |         4 |
|     323.7500 |    111.3741 | most_recently_added  | random           | random          | all               |         4 |

## Memory Size 512

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     749.7500 |     52.4518 | most_recently_used   | bfs              | lru             | all               |         4 |
|     749.0000 |     51.3274 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     748.7500 |     57.2249 | most_recently_added  | bfs              | random          | all               |         4 |
|     748.5000 |     55.9218 | most_recently_used   | bfs              | random          | all               |         4 |
|     747.0000 |     47.8592 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     746.7500 |     48.7564 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     743.2500 |     46.9275 | most_recently_added  | bfs              | lru             | all               |         4 |
|     742.0000 |     47.9740 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     738.0000 |     54.4488 | most_recently_added  | dijkstra         | random          | all               |         3 |
|     732.6667 |      9.5685 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     728.3333 |      9.6724 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     718.5000 |     59.2178 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     718.0000 |     45.9946 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     718.0000 |     25.6418 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     717.2500 |     54.3524 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     714.2500 |     23.7105 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     595.0000 |     29.5296 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     594.7500 |     26.2333 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     594.3333 |     29.3182 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|     588.0000 |     29.4194 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     586.7500 |     29.2948 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     583.7500 |     33.5513 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     582.2500 |     34.0689 | most_frequently_used | bfs              | lru             | all               |         4 |
|     581.2500 |     34.6654 | most_frequently_used | bfs              | random          | all               |         4 |
|     478.0000 |     56.7274 | most_recently_added  | random           | lfu             | all               |         3 |
|     397.2500 |    148.2403 | most_recently_added  | random           | lru             | all               |         4 |
|     395.7500 |    145.1592 | most_recently_added  | random           | fifo            | all               |         4 |
|     390.0000 |    140.4778 | most_recently_added  | random           | random          | all               |         4 |
|     378.0000 |     54.5023 | most_recently_used   | random           | random          | all               |         4 |
|     374.7500 |     62.6314 | most_recently_used   | random           | lfu             | all               |         4 |
|     374.7500 |     62.6314 | most_recently_used   | random           | lru             | all               |         4 |
|     374.5000 |     63.1368 | most_recently_used   | random           | fifo            | all               |         4 |
|     371.2500 |     63.6568 | most_frequently_used | random           | fifo            | all               |         4 |
|     366.7500 |     73.1689 | most_frequently_used | random           | random          | all               |         4 |
|     363.2500 |     68.7473 | most_frequently_used | random           | lfu             | all               |         4 |
|     363.2500 |     68.7473 | most_frequently_used | random           | lru             | all               |         4 |

## Memory Size 1024

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     748.2500 |     61.0343 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | lru             | all               |         4 |
|     748.2500 |     61.0343 | most_recently_added  | bfs              | random          | all               |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | lru             | all               |         4 |
|     739.0000 |     52.9717 | most_recently_used   | bfs              | random          | all               |         4 |
|     732.3333 |      9.5685 | most_recently_used   | dijkstra         | random          | all               |         3 |
|     732.3333 |      9.5685 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     732.3333 |      9.5685 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|     728.3333 |     61.7216 | most_recently_added  | dijkstra         | random          | all               |         3 |
|     720.0000 |     22.9129 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     714.0000 |     58.9364 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     714.0000 |     58.9364 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     714.0000 |     58.9364 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     585.0000 |     33.0252 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     585.0000 |     33.0252 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|     583.5000 |     28.7185 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     583.5000 |     28.7185 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | random          | all               |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | lru             | all               |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     578.0000 |     34.1687 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | fifo            | all               |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | lfu             | all               |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | lru             | all               |         4 |
|     402.0000 |    155.9054 | most_recently_added  | random           | random          | all               |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | fifo            | all               |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | lfu             | all               |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | lru             | all               |         4 |
|     376.2500 |     64.3326 | most_recently_used   | random           | random          | all               |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | fifo            | all               |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | lfu             | all               |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | lru             | all               |         4 |
|     361.2500 |     77.6800 | most_frequently_used | random           | random          | all               |         4 |

