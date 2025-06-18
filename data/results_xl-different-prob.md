# Results for xl-different-prob

Total configurations: 528
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|     650.2000 |     22.5335 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|     649.6000 |     34.9949 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|     648.8000 |     38.6544 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | random          | all               |          1024 |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|     641.8000 |     65.5726 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|     641.8000 |     27.0658 | most_recently_added  | dijkstra         | random          | all               |           512 |         5 |
|     641.4000 |     27.6810 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|     640.6000 |     27.5942 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|     639.8000 |     26.2480 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | random          | all               |          1024 |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|     637.6000 |     21.2283 | most_recently_added  | bfs              | random          | all               |           512 |         5 |
|     635.8000 |     21.5258 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|     633.8000 |     43.9017 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|     633.4000 |     29.8436 | random               | bfs              | lru             | all               |           256 |         5 |
|     633.2000 |     19.7525 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|     632.8000 |     20.1336 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|     631.2000 |     60.9373 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|     630.0000 |     43.6119 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|     628.2000 |     33.7010 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|     623.8000 |     46.0973 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|     622.8000 |     33.3311 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|     618.8000 |     42.2724 | random               | dijkstra         | lfu             | all               |           256 |         5 |
|     615.6000 |     47.7100 | most_recently_added  | bfs              | random          | all               |           256 |         5 |
|     614.4000 |     51.2273 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | random          | all               |          1024 |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|     612.0000 |     31.1833 | random               | bfs              | lfu             | all               |           256 |         5 |
|     611.0000 |     48.0541 | most_recently_used   | bfs              | random          | all               |           512 |         5 |
|     610.8000 |     49.7811 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|     610.4000 |     50.0424 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|     609.8000 |     40.2313 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|     609.2000 |     49.0037 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|     608.4000 |     49.2203 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|     607.2000 |     57.5757 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|     606.8000 |     46.4086 | random               | dijkstra         | lru             | all               |           512 |         5 |
|     606.8000 |     46.8419 | random               | dijkstra         | lfu             | all               |           512 |         5 |
|     606.0000 |     39.4107 | random               | dijkstra         | lru             | all               |           256 |         5 |
|     605.8000 |     33.1083 | random               | bfs              | fifo            | all               |           256 |         5 |
|     603.8000 |     46.4603 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|     603.4000 |     60.7441 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|     603.2000 |     37.2312 | random               | dijkstra         | random          | all               |           512 |         5 |
|     602.6000 |     41.3212 | random               | dijkstra         | fifo            | all               |           512 |         5 |
|     602.2000 |     32.8232 | random               | dijkstra         | fifo            | all               |           256 |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | random          | all               |          1024 |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|     601.8000 |     30.1224 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|     601.4000 |     33.1940 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | lfu             | all               |          1024 |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | fifo            | all               |          1024 |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | lru             | all               |          1024 |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | random          | all               |          1024 |         5 |
|     598.4000 |     26.4167 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|     597.2000 |     37.2043 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|     596.6000 |     56.4220 | random               | bfs              | lfu             | all               |           128 |         5 |
|     595.2000 |     40.3009 | random               | bfs              | fifo            | all               |           512 |         5 |
|     594.8000 |     36.1851 | random               | bfs              | lru             | all               |          1024 |         5 |
|     594.8000 |     36.1851 | random               | bfs              | lfu             | all               |          1024 |         5 |
|     594.8000 |     36.1851 | random               | bfs              | random          | all               |          1024 |         5 |
|     594.8000 |     40.6468 | random               | bfs              | random          | all               |           512 |         5 |
|     594.8000 |     36.1851 | random               | bfs              | fifo            | all               |          1024 |         5 |
|     594.4000 |     42.2308 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|     594.4000 |     33.4102 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|     593.8000 |     33.1988 | random               | bfs              | lfu             | all               |           512 |         5 |
|     592.6000 |     35.3418 | random               | bfs              | lru             | all               |           512 |         5 |
|     592.4000 |     29.2889 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|     592.0000 |     28.9897 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|     591.4000 |     42.9027 | most_recently_used   | dijkstra         | random          | all               |           512 |         5 |
|     591.0000 |     42.7972 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|     589.6000 |     50.6067 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|     588.6000 |     44.4999 | random               | bfs              | lru             | all               |           128 |         5 |
|     586.6000 |     45.8327 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|     586.0000 |     38.8999 | random               | dijkstra         | lru             | all               |           128 |         5 |
|     584.4000 |     34.1151 | most_frequently_used | bfs              | random          | all               |           512 |         5 |
|     584.2000 |     72.4276 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|     583.4000 |     46.3448 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|     583.2000 |     88.9301 | most_recently_added  | dijkstra         | random          | all               |           256 |         5 |
|     580.0000 |     29.2780 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|     579.4000 |     60.2847 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|     578.2000 |     35.9299 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|     578.0000 |     71.0324 | random               | dijkstra         | random          | all               |           256 |         5 |
|     577.0000 |     29.1822 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|     576.6000 |     29.2342 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | random          | all               |          1024 |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|     575.2000 |     32.9327 | random               | dijkstra         | lfu             | all               |           128 |         5 |
|     570.4000 |     24.3195 | random               | bfs              | random          | all               |           256 |         5 |
|     570.0000 |     36.1386 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|     568.4000 |     27.0599 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|     566.6000 |     25.0488 | random               | bfs              | lfu             | all               |            64 |         5 |
|     565.8000 |     41.1990 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|     562.8000 |     39.4837 | most_frequently_used | dijkstra         | random          | all               |           512 |         5 |
|     562.0000 |     61.9032 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | random          | all               |          1024 |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|     558.0000 |     42.6474 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|     557.8000 |     42.6774 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|     555.4000 |     43.6147 | random               | dijkstra         | lfu             | all               |            64 |         5 |
|     549.6000 |     90.2942 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|     549.4000 |     53.0494 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|     546.4000 |     17.2812 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|     544.6000 |     26.7103 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|     542.8000 |     66.8054 | most_frequently_used | dijkstra         | random          | all               |           256 |         5 |
|     542.4000 |     99.6245 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|     539.0000 |     21.3073 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|     539.0000 |     50.9235 | most_recently_used   | bfs              | random          | all               |           256 |         5 |
|     538.6000 |     48.3760 | random               | dijkstra         | lru             | all               |            64 |         5 |
|     536.2000 |     14.4693 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|     535.6000 |     47.9608 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|     534.4000 |     48.3967 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|     531.0000 |     40.9243 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|     528.8000 |     28.9786 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|     528.8000 |     62.5888 | most_frequently_used | bfs              | random          | all               |           256 |         5 |
|     527.4000 |     52.5913 | random               | bfs              | lru             | all               |            64 |         5 |
|     525.6000 |     30.5326 | most_recently_used   | dijkstra         | random          | all               |           256 |         5 |
|     523.6000 |     88.8788 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|     512.2000 |     56.9189 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|     506.8000 |     31.9086 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|     498.0000 |     34.7448 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|     490.0000 |     52.8432 | random               | bfs              | lfu             | all               |            32 |         5 |
|     485.4000 |     21.0580 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|     482.6000 |     41.7833 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|     482.0000 |     52.8923 | random               | bfs              | fifo            | all               |           128 |         5 |
|     478.8000 |     63.3574 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|     467.4000 |     20.2840 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|     467.4000 |     23.7200 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|     463.6000 |     28.5139 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|     463.4000 |     51.0866 | random               | dijkstra         | fifo            | all               |           128 |         5 |
|     455.2000 |     18.1813 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|     448.4000 |     45.9069 | random               | bfs              | random          | all               |           128 |         5 |
|     447.8000 |     26.1641 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|     446.8000 |     38.1125 | random               | bfs              | lru             | all               |            32 |         5 |
|     444.6000 |     18.1505 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|     428.6000 |     33.5595 | most_recently_added  | dijkstra         | random          | all               |           128 |         5 |
|     428.0000 |     70.3420 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|     427.0000 |     58.1446 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|     418.8000 |     51.4564 | random               | dijkstra         | lru             | all               |            32 |         5 |
|     415.6000 |     26.8820 | most_recently_used   | bfs              | random          | all               |           128 |         5 |
|     411.6000 |    148.0278 | random               | dijkstra         | lfu             | all               |            32 |         5 |
|     408.0000 |     28.5797 | random               | dijkstra         | random          | all               |           128 |         5 |
|     405.4000 |     51.8482 | most_recently_used   | dijkstra         | random          | all               |           128 |         5 |
|     404.8000 |     22.7982 | most_recently_added  | bfs              | random          | all               |           128 |         5 |
|     402.6000 |     48.4628 | most_frequently_used | dijkstra         | random          | all               |           128 |         5 |
|     399.0000 |     50.4063 | most_frequently_used | bfs              | random          | all               |           128 |         5 |
|     396.4000 |     87.9718 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|     393.8000 |     92.8556 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|     362.2000 |     92.0595 | random               | bfs              | lfu             | all               |            16 |         5 |
|     353.6000 |    115.6868 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|     351.2000 |     71.8983 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|     350.6000 |     45.4031 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|     337.6000 |     24.1876 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|     337.6000 |     61.5097 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|     337.4000 |     32.7329 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|     332.0000 |     34.6006 | random               | dijkstra         | lru             | all               |            16 |         5 |
|     328.4000 |    128.9443 | random               | dijkstra         | lfu             | all               |            16 |         5 |
|     325.6000 |     48.0566 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|     325.0000 |     24.0167 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|     324.0000 |     41.5596 | random               | dijkstra         | fifo            | all               |            64 |         5 |
|     322.8000 |     20.6243 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|     311.4000 |     42.6033 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|     310.4000 |     42.7486 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|     308.6000 |     31.1551 | random               | bfs              | fifo            | all               |            64 |         5 |
|     305.8000 |     23.9115 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|     303.8000 |     40.1069 | most_frequently_used | bfs              | random          | all               |            64 |         5 |
|     301.2000 |     75.7559 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|     296.8000 |     23.4896 | most_recently_added  | bfs              | random          | all               |            64 |         5 |
|     295.2000 |     29.6877 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|     295.0000 |     69.7746 | random               | bfs              | lfu             | all               |             8 |         4 |
|     291.2000 |     24.4082 | most_recently_used   | bfs              | random          | all               |            64 |         5 |
|     283.6000 |    116.2439 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|     280.6000 |     53.1962 | random               | bfs              | lru             | all               |            16 |         5 |
|     277.8000 |     84.1793 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|     276.4000 |     32.6411 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|     275.8000 |     43.3931 | most_recently_added  | dijkstra         | random          | all               |            64 |         5 |
|     273.0000 |     12.4579 | random               | dijkstra         | random          | all               |            64 |         5 |
|     271.4000 |     51.7092 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|     271.4000 |     68.3479 | random               | dijkstra         | lfu             | all               |             8 |         5 |
|     271.2000 |     73.7113 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|     266.6000 |     21.3972 | most_recently_used   | dijkstra         | random          | all               |            64 |         5 |
|     262.0000 |     28.3337 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|     259.6000 |     34.3430 | most_frequently_used | dijkstra         | random          | all               |            64 |         5 |
|     254.8000 |    158.1865 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|     253.8000 |     76.0878 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|     252.4000 |    106.8618 | random               | random           | lfu             | all               |           128 |         5 |
|     251.2000 |     74.3650 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|     249.8000 |     24.0782 | random               | bfs              | random          | all               |            64 |         5 |
|     245.8000 |     34.5798 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|     245.8000 |     25.4275 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|     240.2000 |     74.9250 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|     233.0000 |    105.4438 | random               | random           | random          | all               |           512 |         5 |
|     232.0000 |    102.7716 | random               | random           | random          | all               |          1024 |         5 |
|     232.0000 |    102.7716 | random               | random           | fifo            | all               |          1024 |         5 |
|     232.0000 |    102.7716 | random               | random           | lru             | all               |          1024 |         5 |
|     232.0000 |    102.7716 | random               | random           | lfu             | all               |          1024 |         5 |
|     229.8000 |    101.0810 | random               | random           | lru             | all               |           512 |         5 |
|     229.8000 |    101.0810 | random               | random           | lfu             | all               |           512 |         5 |
|     228.2000 |     96.4622 | random               | random           | lru             | all               |           128 |         5 |
|     227.8000 |     99.1028 | random               | random           | fifo            | all               |           512 |         5 |
|     218.8000 |     94.7574 | random               | random           | lfu             | all               |           256 |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | random          | all               |          1024 |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|     217.6000 |     42.4009 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|     216.4000 |     95.3113 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|     214.8000 |     56.5240 | most_frequently_used | random           | random          | all               |           512 |         5 |
|     214.6000 |    102.9050 | random               | random           | random          | all               |           256 |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | random          | all               |          1024 |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|     213.0000 |     58.7026 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|     213.0000 |     58.7026 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|     212.6000 |     97.7049 | random               | random           | lru             | all               |           256 |         5 |
|     212.6000 |     41.8167 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|     212.0000 |     41.1485 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|     211.0000 |     26.8626 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|     210.4000 |     54.7671 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|     206.6000 |     24.8322 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|     204.8000 |     90.6143 | random               | random           | random          | all               |           128 |         5 |
|     203.6000 |     84.2700 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|     203.0000 |     20.1494 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|     202.8000 |     53.9385 | most_recently_added  | random           | random          | all               |           256 |         5 |
|     202.8000 |     25.6780 | most_recently_added  | random           | random          | all               |           128 |         5 |
|     201.6000 |     71.6369 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|     201.4000 |     71.8237 | most_recently_added  | random           | random          | all               |           512 |         5 |
|     201.2000 |     70.0725 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|     201.2000 |     70.0725 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|     200.2000 |     51.4680 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|     200.2000 |     27.2206 | most_recently_added  | bfs              | random          | all               |            32 |         5 |
|     199.2000 |     22.5690 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|     198.6000 |     48.2270 | random               | random           | fifo            | all               |           256 |         5 |
|     197.6000 |     20.9724 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|     197.4000 |     56.2089 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|     195.2000 |     30.7402 | random               | dijkstra         | fifo            | all               |            32 |         5 |
|     195.2000 |     71.8899 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|     189.8000 |     19.3948 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|     188.4000 |     82.8362 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|     187.4000 |     61.7239 | most_frequently_used | random           | random          | all               |           256 |         5 |
|     187.0000 |     75.8630 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|     186.6000 |     71.1241 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|     184.4000 |     50.6896 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|     180.4000 |     63.3296 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|     180.4000 |     79.2202 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|     178.6000 |     24.5487 | most_recently_added  | dijkstra         | random          | all               |            32 |         5 |
|     178.0000 |     18.1439 | random               | bfs              | fifo            | all               |            32 |         5 |
|     174.6000 |     77.6314 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|     174.4000 |     74.6072 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|     174.4000 |     60.8460 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|     173.4000 |     90.1545 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|     171.8000 |     47.7259 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|     170.2000 |     89.5732 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|     170.0000 |     17.2627 | random               | dijkstra         | random          | all               |            32 |         5 |
|     168.8000 |     28.3789 | most_frequently_used | bfs              | random          | all               |            32 |         5 |
|     168.6000 |     65.1540 | random               | random           | lru             | all               |            32 |         5 |
|     168.4000 |     16.3291 | random               | dijkstra         | lru             | all               |             8 |         5 |
|     167.6000 |     49.4312 | most_frequently_used | random           | random          | all               |           128 |         5 |
|     166.6000 |     53.3464 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|     165.8000 |     36.7663 | random               | bfs              | lru             | all               |             8 |         5 |
|     165.2000 |     20.4685 | most_recently_used   | dijkstra         | random          | all               |            32 |         5 |
|     165.2000 |     42.2724 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|     165.0000 |     54.2181 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|     164.8000 |     32.6766 | most_recently_used   | bfs              | random          | all               |            32 |         5 |
|     164.2000 |     65.0612 | random               | random           | fifo            | all               |           128 |         5 |
|     162.0000 |     67.7761 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|     160.6000 |     68.8581 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|     159.2000 |     55.3006 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|     159.0000 |     29.5905 | most_frequently_used | dijkstra         | random          | all               |            32 |         5 |
|     158.6000 |     65.1110 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|     157.8000 |     22.7543 | random               | bfs              | random          | all               |            32 |         5 |
|     157.6000 |     98.4532 | random               | random           | lfu             | all               |            16 |         5 |
|     157.6000 |     27.9757 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|     149.4000 |     21.2471 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|     148.8000 |     20.1336 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|     147.6000 |     14.5685 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|     147.6000 |     14.5685 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|     145.8000 |     73.0737 | most_recently_used   | random           | random          | all               |           256 |         5 |
|     144.6000 |     24.6868 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|     143.0000 |     59.8231 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|     142.0000 |     11.4368 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|     140.2000 |     46.1363 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|     136.8000 |     63.5371 | random               | random           | lfu             | all               |            32 |         5 |
|     134.2000 |     58.1495 | random               | random           | lfu             | all               |            64 |         5 |
|     134.0000 |     40.3534 | random               | bfs              | lfu             | all               |             4 |         5 |
|     129.0000 |     41.9905 | most_recently_used   | random           | random          | all               |           512 |         5 |
|     128.8000 |    107.6762 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|     127.6000 |     42.1027 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|     127.4000 |     52.2287 | random               | random           | lru             | all               |            64 |         5 |
|     126.8000 |     43.2823 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|     126.0000 |     39.7240 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|     126.0000 |     62.8299 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|     126.0000 |      7.6942 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | random          | all               |          1024 |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|     125.2000 |      7.9095 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|     124.0000 |     36.3703 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|     123.4000 |     64.4875 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|     123.0000 |     49.6306 | most_frequently_used | random           | random          | all               |            64 |         5 |
|     122.8000 |     10.0280 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|     122.6000 |     10.4038 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|     122.0000 |     33.3287 | most_frequently_used | random           | random          | all               |            32 |         5 |
|     118.2000 |     54.9996 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|     116.0000 |     14.9265 | random               | dijkstra         | random          | all               |            16 |         5 |
|     115.6000 |     69.7900 | random               | random           | lfu             | all               |             8 |         5 |
|     115.0000 |     10.4115 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|     114.4000 |     11.0743 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|     114.0000 |     73.6695 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|     113.4000 |     68.9916 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|     111.0000 |     39.7341 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|     110.2000 |     22.5956 | random               | dijkstra         | fifo            | all               |            16 |         5 |
|     108.4000 |     21.3410 | random               | bfs              | fifo            | all               |            16 |         5 |
|     107.8000 |     27.7662 | random               | bfs              | random          | all               |            16 |         5 |
|     106.8000 |     58.6495 | most_recently_used   | random           | random          | all               |            64 |         5 |
|     106.8000 |     31.8207 | random               | bfs              | lfu             | all               |             2 |         5 |
|     106.6000 |     61.8566 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|     105.0000 |     35.4570 | random               | random           | fifo            | all               |            64 |         5 |
|     104.6000 |     65.3195 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|     104.0000 |     70.7842 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|     102.0000 |     47.8163 | most_recently_added  | random           | random          | all               |            64 |         5 |
|     101.4000 |     10.6132 | most_recently_added  | bfs              | random          | all               |            16 |         5 |
|      99.0000 |     40.9732 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|      98.4000 |     40.1577 | most_recently_used   | random           | random          | all               |           128 |         5 |
|      98.0000 |     39.1357 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|      98.0000 |     48.6004 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|      98.0000 |     39.1357 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|      95.8000 |     24.8709 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|      94.8000 |     16.4730 | most_frequently_used | bfs              | random          | all               |            16 |         5 |
|      94.6000 |     44.7464 | random               | random           | lru             | all               |            16 |         5 |
|      94.2000 |     57.1258 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|      94.2000 |     16.4609 | most_recently_used   | bfs              | random          | all               |            16 |         5 |
|      90.6000 |     39.1438 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|      90.0000 |     20.2287 | most_recently_used   | dijkstra         | random          | all               |            16 |         5 |
|      89.8000 |     32.6582 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|      88.4000 |     11.2889 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|      88.2000 |     24.0366 | random               | random           | random          | all               |            64 |         5 |
|      88.0000 |     27.0851 | most_frequently_used | dijkstra         | random          | all               |            16 |         5 |
|      87.6000 |     20.4216 | random               | random           | random          | all               |            32 |         5 |
|      87.4000 |     50.2896 | random               | dijkstra         | lfu             | all               |             4 |         5 |
|      87.4000 |     19.2208 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|      87.0000 |     25.3850 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|      85.0000 |     33.7580 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|      84.6000 |     12.3709 | most_frequently_used | bfs              | random          | all               |             8 |         5 |
|      83.4000 |     14.2352 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|      83.4000 |     15.3441 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|      81.6000 |     16.5602 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|      81.0000 |     34.5427 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|      79.0000 |      8.2946 | most_recently_used   | bfs              | random          | all               |             8 |         5 |
|      77.8000 |     20.9705 | most_recently_added  | random           | random          | all               |            32 |         5 |
|      76.6000 |     25.3346 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|      75.6000 |     11.0562 | random               | bfs              | fifo            | all               |             8 |         5 |
|      75.4000 |     30.7024 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|      72.2000 |     15.2892 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|      71.6000 |     15.0280 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|      71.4000 |     17.2928 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|      71.2000 |     13.6733 | random               | bfs              | lru             | all               |             4 |         5 |
|      70.2000 |      9.9076 | random               | dijkstra         | fifo            | all               |             8 |         5 |
|      70.0000 |     16.4803 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|      70.0000 |     50.9313 | random               | dijkstra         | lfu             | all               |             2 |         5 |
|      69.8000 |     15.3023 | random               | dijkstra         | random          | all               |             8 |         5 |
|      68.6000 |     15.7048 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|      68.6000 |     15.7048 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|      68.0000 |     21.6241 | random               | random           | lfu             | all               |             4 |         5 |
|      68.0000 |     23.1689 | most_recently_added  | dijkstra         | random          | all               |            16 |         5 |
|      66.4000 |      5.0040 | most_recently_used   | random           | random          | all               |            16 |         5 |
|      66.0000 |     26.0845 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|      65.0000 |     23.8747 | random               | dijkstra         | lru             | all               |             4 |         5 |
|      64.2000 |     19.5694 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|      64.0000 |     14.3805 | random               | random           | fifo            | all               |            16 |         5 |
|      62.8000 |      5.2688 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|      62.8000 |     23.8109 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|      61.2000 |     15.4842 | most_recently_added  | bfs              | random          | all               |             8 |         5 |
|      61.2000 |     24.5959 | most_frequently_used | random           | random          | all               |            16 |         5 |
|      61.0000 |      6.1968 | most_recently_used   | dijkstra         | random          | all               |             8 |         5 |
|      60.8000 |     20.5173 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|      60.8000 |     20.5173 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|      59.8000 |      2.9257 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|      59.6000 |      8.6163 | most_frequently_used | dijkstra         | random          | all               |             8 |         5 |
|      58.8000 |      8.8182 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|      58.4000 |     32.8244 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|      58.0000 |     13.7113 | most_frequently_used | bfs              | random          | all               |             4 |         5 |
|      58.0000 |     13.7113 | most_recently_used   | bfs              | random          | all               |             4 |         5 |
|      57.8000 |     34.4465 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|      57.6000 |     14.4582 | random               | bfs              | random          | all               |             8 |         5 |
|      56.6000 |     15.6282 | random               | random           | fifo            | all               |            32 |         5 |
|      55.8000 |     11.8220 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|      55.8000 |     11.8220 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|      54.8000 |     16.7021 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|      54.8000 |     16.7021 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|      54.0000 |     10.3730 | most_recently_added  | dijkstra         | random          | all               |             8 |         5 |
|      53.8000 |     13.7026 | random               | dijkstra         | fifo            | all               |             4 |         5 |
|      53.6000 |      7.1162 | random               | bfs              | fifo            | all               |             4 |         5 |
|      53.6000 |     33.3143 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|      52.6000 |     22.0145 | random               | dijkstra         | random          | all               |             4 |         5 |
|      52.0000 |     19.0263 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|      52.0000 |     19.0263 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|      51.6000 |     12.6111 | most_recently_added  | random           | random          | all               |            16 |         5 |
|      51.4000 |     28.7722 | most_recently_used   | random           | random          | all               |            32 |         5 |
|      51.4000 |     15.4221 | random               | bfs              | lru             | all               |             2 |         5 |
|      50.2000 |      6.4000 | most_recently_used   | random           | random          | all               |             8 |         5 |
|      48.2000 |     17.1511 | most_recently_added  | bfs              | random          | all               |             4 |         5 |
|      47.4000 |     15.0280 | random               | random           | random          | all               |            16 |         5 |
|      47.4000 |      7.6315 | random               | bfs              | random          | all               |             4 |         5 |
|      47.4000 |     23.4145 | most_recently_added  | dijkstra         | random          | all               |             4 |         5 |
|      46.4000 |     33.6012 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|      45.0000 |     14.1563 | most_frequently_used | random           | random          | all               |             8 |         5 |
|      44.6000 |     26.9414 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|      44.6000 |     26.9414 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|      44.0000 |     12.9923 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|      43.6000 |     13.0015 | random               | random           | fifo            | all               |             8 |         5 |
|      43.2000 |     21.0181 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|      43.0000 |     20.1693 | random               | random           | lru             | all               |             4 |         5 |
|      42.0000 |     14.6287 | random               | dijkstra         | lru             | all               |             2 |         5 |
|      41.8000 |     21.4886 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|      41.4000 |     20.3627 | random               | random           | lru             | all               |             8 |         5 |
|      40.8000 |     19.0515 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|      40.4000 |     18.5753 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|      40.2000 |     12.9831 | random               | bfs              | random          | all               |             2 |         5 |
|      40.2000 |     13.6147 | random               | random           | lfu             | all               |             2 |         5 |
|      39.6000 |     23.5423 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|      39.6000 |     23.5423 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|      38.8000 |     11.7541 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|      38.8000 |     11.7541 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|      38.8000 |      9.7447 | most_recently_added  | bfs              | random          | all               |             2 |         5 |
|      38.6000 |      6.2801 | random               | random           | random          | all               |             8 |         5 |
|      38.0000 |      4.6043 | most_recently_added  | random           | random          | all               |             8 |         5 |
|      37.6000 |     12.6586 | most_recently_added  | random           | random          | all               |             2 |         5 |
|      37.0000 |      9.9398 | random               | bfs              | fifo            | all               |             2 |         5 |
|      36.8000 |     19.2603 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|      36.2000 |     16.5336 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|      36.0000 |     21.4196 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|      35.2000 |     18.9251 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|      34.6000 |     17.5111 | random               | random           | random          | all               |             4 |         5 |
|      34.4000 |     13.7346 | most_frequently_used | dijkstra         | random          | all               |             4 |         5 |
|      34.4000 |     13.7346 | most_recently_used   | dijkstra         | random          | all               |             4 |         5 |
|      34.2000 |      8.6579 | most_recently_added  | dijkstra         | random          | all               |             2 |         5 |
|      33.8000 |     19.5591 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|      33.8000 |     19.5591 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|      33.6000 |      8.8000 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|      33.0000 |      8.4143 | most_recently_used   | dijkstra         | random          | all               |             2 |         5 |
|      33.0000 |      8.4143 | most_frequently_used | dijkstra         | random          | all               |             2 |         5 |
|      32.8000 |     14.7838 | most_recently_used   | bfs              | random          | all               |             2 |         5 |
|      32.8000 |     14.7838 | most_frequently_used | bfs              | random          | all               |             2 |         5 |
|      32.8000 |     13.6733 | random               | random           | fifo            | all               |             2 |         5 |
|      32.8000 |      7.7045 | random               | dijkstra         | random          | all               |             2 |         5 |
|      32.6000 |     10.9654 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|      32.6000 |      7.9145 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|      32.6000 |     10.9654 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|      32.6000 |     10.9654 | random               | bfs              | lru             | all               |             0 |         5 |
|      32.6000 |     10.9654 | random               | dijkstra         | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | random               | dijkstra         | lru             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|      32.6000 |     10.9654 | random               | bfs              | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|      32.6000 |     10.9654 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|      32.6000 |     15.3571 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|      32.6000 |     10.9654 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|      31.2000 |      8.5417 | most_frequently_used | random           | random          | all               |             2 |         5 |
|      31.2000 |      8.5417 | most_recently_used   | random           | random          | all               |             2 |         5 |
|      30.2000 |      6.6151 | random               | random           | random          | all               |             2 |         5 |
|      29.4000 |      8.4758 | most_recently_added  | random           | random          | all               |             4 |         5 |
|      29.0000 |     10.7145 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|      29.0000 |     10.7145 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|      28.6000 |      7.4993 | random               | random           | lru             | all               |             2 |         5 |
|      28.4000 |     12.0266 | most_frequently_used | random           | random          | all               |             4 |         5 |
|      28.0000 |      9.9398 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|      27.4000 |      9.0907 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|      27.4000 |      6.1514 | random               | dijkstra         | fifo            | all               |             2 |         5 |
|      26.8000 |      7.9599 | random               | random           | fifo            | all               |             4 |         5 |
|      26.2000 |      4.1665 | most_recently_added  | random           | random          | all               |             0 |         5 |
|      26.2000 |      4.1665 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|      26.2000 |      4.1665 | most_recently_added  | random           | fifo            | all               |             0 |         5 |
|      26.2000 |      4.1665 | most_frequently_used | random           | random          | all               |             0 |         5 |
|      26.2000 |      4.1665 | most_recently_used   | random           | random          | all               |             0 |         5 |
|      26.2000 |      4.1665 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|      26.2000 |      4.1665 | random               | random           | fifo            | all               |             0 |         5 |
|      26.2000 |      4.1665 | random               | random           | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_frequently_used | dijkstra         | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | random               | dijkstra         | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | random               | bfs              | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_used   | dijkstra         | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_used   | bfs              | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | random               | bfs              | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | random               | dijkstra         | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_frequently_used | bfs              | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_added  | dijkstra         | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_added  | bfs              | random          | all               |             0 |         5 |
|      24.6000 |     11.1821 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|      24.4000 |      8.3331 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|      24.4000 |      8.3331 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|      24.2000 |      9.2390 | most_recently_used   | random           | random          | all               |             4 |         5 |
|      23.2000 |      5.1536 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|      23.2000 |      5.1536 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|      21.2000 |      5.9464 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|      21.2000 |      5.9464 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|      17.8000 |      5.2688 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|      17.8000 |      5.2688 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|      17.8000 |      5.2688 | most_frequently_used | random           | lfu             | all               |             0 |         5 |
|      17.8000 |      5.2688 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|      17.8000 |      5.2688 | random               | random           | lfu             | all               |             0 |         5 |
|      17.8000 |      5.2688 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|      17.8000 |      5.2688 | random               | random           | lru             | all               |             0 |         5 |
|      17.8000 |      5.2688 | most_recently_added  | random           | lru             | all               |             0 |         5 |

## Memory Size 0

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|      32.6000 |     10.9654 | most_frequently_used | bfs              | lfu             | all               |         5 |
|      32.6000 |     10.9654 | most_frequently_used | bfs              | lru             | all               |         5 |
|      32.6000 |     10.9654 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|      32.6000 |     10.9654 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_added  | bfs              | lfu             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_added  | bfs              | lru             | all               |         5 |
|      32.6000 |     10.9654 | random               | dijkstra         | lru             | all               |         5 |
|      32.6000 |     10.9654 | random               | dijkstra         | lfu             | all               |         5 |
|      32.6000 |     10.9654 | random               | bfs              | lru             | all               |         5 |
|      32.6000 |     10.9654 | random               | bfs              | lfu             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_used   | bfs              | lfu             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_used   | bfs              | lru             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|      32.6000 |     10.9654 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|      26.2000 |      4.1665 | most_frequently_used | random           | fifo            | all               |         5 |
|      26.2000 |      4.1665 | most_frequently_used | random           | random          | all               |         5 |
|      26.2000 |      4.1665 | random               | random           | random          | all               |         5 |
|      26.2000 |      4.1665 | random               | random           | fifo            | all               |         5 |
|      26.2000 |      4.1665 | most_recently_used   | random           | random          | all               |         5 |
|      26.2000 |      4.1665 | most_recently_used   | random           | fifo            | all               |         5 |
|      26.2000 |      4.1665 | most_recently_added  | random           | random          | all               |         5 |
|      26.2000 |      4.1665 | most_recently_added  | random           | fifo            | all               |         5 |
|      24.6000 |     11.1821 | random               | dijkstra         | random          | all               |         5 |
|      24.6000 |     11.1821 | random               | dijkstra         | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_recently_added  | bfs              | random          | all               |         5 |
|      24.6000 |     11.1821 | most_recently_added  | bfs              | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_frequently_used | bfs              | random          | all               |         5 |
|      24.6000 |     11.1821 | most_frequently_used | bfs              | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_frequently_used | dijkstra         | random          | all               |         5 |
|      24.6000 |     11.1821 | random               | bfs              | random          | all               |         5 |
|      24.6000 |     11.1821 | random               | bfs              | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_recently_used   | dijkstra         | random          | all               |         5 |
|      24.6000 |     11.1821 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_recently_added  | dijkstra         | random          | all               |         5 |
|      24.6000 |     11.1821 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_recently_used   | bfs              | fifo            | all               |         5 |
|      24.6000 |     11.1821 | most_recently_used   | bfs              | random          | all               |         5 |
|      17.8000 |      5.2688 | most_frequently_used | random           | lfu             | all               |         5 |
|      17.8000 |      5.2688 | most_frequently_used | random           | lru             | all               |         5 |
|      17.8000 |      5.2688 | most_recently_added  | random           | lfu             | all               |         5 |
|      17.8000 |      5.2688 | most_recently_added  | random           | lru             | all               |         5 |
|      17.8000 |      5.2688 | most_recently_used   | random           | lfu             | all               |         5 |
|      17.8000 |      5.2688 | most_recently_used   | random           | lru             | all               |         5 |
|      17.8000 |      5.2688 | random               | random           | lfu             | all               |         5 |
|      17.8000 |      5.2688 | random               | random           | lru             | all               |         5 |

## Memory Size 2

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     106.8000 |     31.8207 | random               | bfs              | lfu             | all               |         5 |
|      98.0000 |     39.1357 | most_frequently_used | bfs              | lfu             | all               |         5 |
|      98.0000 |     39.1357 | most_recently_used   | bfs              | lfu             | all               |         5 |
|      75.4000 |     30.7024 | most_recently_added  | bfs              | lfu             | all               |         5 |
|      70.0000 |     50.9313 | random               | dijkstra         | lfu             | all               |         5 |
|      58.4000 |     32.8244 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|      57.8000 |     34.4465 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|      53.6000 |     33.3143 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|      52.0000 |     19.0263 | most_recently_used   | bfs              | lru             | all               |         5 |
|      52.0000 |     19.0263 | most_frequently_used | bfs              | lru             | all               |         5 |
|      51.4000 |     15.4221 | random               | bfs              | lru             | all               |         5 |
|      44.0000 |     12.9923 | most_recently_added  | bfs              | lru             | all               |         5 |
|      42.0000 |     14.6287 | random               | dijkstra         | lru             | all               |         5 |
|      40.8000 |     19.0515 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|      40.2000 |     12.9831 | random               | bfs              | random          | all               |         5 |
|      40.2000 |     13.6147 | random               | random           | lfu             | all               |         5 |
|      39.6000 |     23.5423 | most_frequently_used | random           | lfu             | all               |         5 |
|      39.6000 |     23.5423 | most_recently_used   | random           | lfu             | all               |         5 |
|      38.8000 |     11.7541 | most_frequently_used | bfs              | fifo            | all               |         5 |
|      38.8000 |      9.7447 | most_recently_added  | bfs              | random          | all               |         5 |
|      38.8000 |     11.7541 | most_recently_used   | bfs              | fifo            | all               |         5 |
|      37.6000 |     12.6586 | most_recently_added  | random           | random          | all               |         5 |
|      37.0000 |      9.9398 | random               | bfs              | fifo            | all               |         5 |
|      36.2000 |     16.5336 | most_recently_added  | random           | lfu             | all               |         5 |
|      34.2000 |      8.6579 | most_recently_added  | dijkstra         | random          | all               |         5 |
|      33.8000 |     19.5591 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|      33.8000 |     19.5591 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|      33.6000 |      8.8000 | most_recently_added  | bfs              | fifo            | all               |         5 |
|      33.0000 |      8.4143 | most_recently_used   | dijkstra         | random          | all               |         5 |
|      33.0000 |      8.4143 | most_frequently_used | dijkstra         | random          | all               |         5 |
|      32.8000 |     14.7838 | most_frequently_used | bfs              | random          | all               |         5 |
|      32.8000 |     13.6733 | random               | random           | fifo            | all               |         5 |
|      32.8000 |     14.7838 | most_recently_used   | bfs              | random          | all               |         5 |
|      32.8000 |      7.7045 | random               | dijkstra         | random          | all               |         5 |
|      32.6000 |      7.9145 | most_recently_added  | random           | lru             | all               |         5 |
|      32.6000 |     15.3571 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|      31.2000 |      8.5417 | most_recently_used   | random           | random          | all               |         5 |
|      31.2000 |      8.5417 | most_frequently_used | random           | random          | all               |         5 |
|      30.2000 |      6.6151 | random               | random           | random          | all               |         5 |
|      29.0000 |     10.7145 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|      29.0000 |     10.7145 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|      28.6000 |      7.4993 | random               | random           | lru             | all               |         5 |
|      27.4000 |      9.0907 | most_recently_added  | random           | fifo            | all               |         5 |
|      27.4000 |      6.1514 | random               | dijkstra         | fifo            | all               |         5 |
|      23.2000 |      5.1536 | most_recently_used   | random           | lru             | all               |         5 |
|      23.2000 |      5.1536 | most_frequently_used | random           | lru             | all               |         5 |
|      21.2000 |      5.9464 | most_frequently_used | random           | fifo            | all               |         5 |
|      21.2000 |      5.9464 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 4

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     162.0000 |     67.7761 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     160.6000 |     68.8581 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     158.6000 |     65.1110 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     134.0000 |     40.3534 | random               | bfs              | lfu             | all               |         5 |
|      99.0000 |     40.9732 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|      94.2000 |     57.1258 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|      87.4000 |     19.2208 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|      87.4000 |     50.2896 | random               | dijkstra         | lfu             | all               |         5 |
|      85.0000 |     33.7580 | most_frequently_used | random           | lfu             | all               |         5 |
|      83.4000 |     14.2352 | most_recently_added  | random           | lfu             | all               |         5 |
|      81.0000 |     34.5427 | most_recently_used   | random           | lfu             | all               |         5 |
|      71.2000 |     13.6733 | random               | bfs              | lru             | all               |         5 |
|      68.6000 |     15.7048 | most_frequently_used | bfs              | lru             | all               |         5 |
|      68.6000 |     15.7048 | most_recently_used   | bfs              | lru             | all               |         5 |
|      68.0000 |     21.6241 | random               | random           | lfu             | all               |         5 |
|      65.0000 |     23.8747 | random               | dijkstra         | lru             | all               |         5 |
|      64.2000 |     19.5694 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|      62.8000 |      5.2688 | most_recently_added  | bfs              | lru             | all               |         5 |
|      60.8000 |     20.5173 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|      60.8000 |     20.5173 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|      59.8000 |      2.9257 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|      58.8000 |      8.8182 | most_recently_added  | bfs              | fifo            | all               |         5 |
|      58.0000 |     13.7113 | most_recently_used   | bfs              | random          | all               |         5 |
|      58.0000 |     13.7113 | most_frequently_used | bfs              | random          | all               |         5 |
|      55.8000 |     11.8220 | most_frequently_used | bfs              | fifo            | all               |         5 |
|      55.8000 |     11.8220 | most_recently_used   | bfs              | fifo            | all               |         5 |
|      54.8000 |     16.7021 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|      54.8000 |     16.7021 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|      53.8000 |     13.7026 | random               | dijkstra         | fifo            | all               |         5 |
|      53.6000 |      7.1162 | random               | bfs              | fifo            | all               |         5 |
|      52.6000 |     22.0145 | random               | dijkstra         | random          | all               |         5 |
|      48.2000 |     17.1511 | most_recently_added  | bfs              | random          | all               |         5 |
|      47.4000 |     23.4145 | most_recently_added  | dijkstra         | random          | all               |         5 |
|      47.4000 |      7.6315 | random               | bfs              | random          | all               |         5 |
|      44.6000 |     26.9414 | most_recently_used   | random           | lru             | all               |         5 |
|      44.6000 |     26.9414 | most_frequently_used | random           | lru             | all               |         5 |
|      43.2000 |     21.0181 | most_recently_added  | random           | lru             | all               |         5 |
|      43.0000 |     20.1693 | random               | random           | lru             | all               |         5 |
|      34.6000 |     17.5111 | random               | random           | random          | all               |         5 |
|      34.4000 |     13.7346 | most_frequently_used | dijkstra         | random          | all               |         5 |
|      34.4000 |     13.7346 | most_recently_used   | dijkstra         | random          | all               |         5 |
|      29.4000 |      8.4758 | most_recently_added  | random           | random          | all               |         5 |
|      28.4000 |     12.0266 | most_frequently_used | random           | random          | all               |         5 |
|      28.0000 |      9.9398 | most_recently_added  | random           | fifo            | all               |         5 |
|      26.8000 |      7.9599 | random               | random           | fifo            | all               |         5 |
|      24.4000 |      8.3331 | most_frequently_used | random           | fifo            | all               |         5 |
|      24.4000 |      8.3331 | most_recently_used   | random           | fifo            | all               |         5 |
|      24.2000 |      9.2390 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 8

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     311.4000 |     42.6033 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     295.0000 |     69.7746 | random               | bfs              | lfu             | all               |         4 |
|     277.8000 |     84.1793 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     276.4000 |     32.6411 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     271.4000 |     68.3479 | random               | dijkstra         | lfu             | all               |         5 |
|     251.2000 |     74.3650 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     240.2000 |     74.9250 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     180.4000 |     63.3296 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     168.4000 |     16.3291 | random               | dijkstra         | lru             | all               |         5 |
|     165.8000 |     36.7663 | random               | bfs              | lru             | all               |         5 |
|     157.6000 |     27.9757 | most_recently_added  | bfs              | lru             | all               |         5 |
|     149.4000 |     21.2471 | most_frequently_used | bfs              | lru             | all               |         5 |
|     148.8000 |     20.1336 | most_recently_used   | bfs              | lru             | all               |         5 |
|     147.6000 |     14.5685 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     147.6000 |     14.5685 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     142.0000 |     11.4368 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     118.2000 |     54.9996 | most_recently_added  | random           | lfu             | all               |         5 |
|     115.6000 |     69.7900 | random               | random           | lfu             | all               |         5 |
|     106.6000 |     61.8566 | most_frequently_used | random           | lfu             | all               |         5 |
|      98.0000 |     48.6004 | most_recently_used   | random           | lfu             | all               |         5 |
|      88.4000 |     11.2889 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|      84.6000 |     12.3709 | most_frequently_used | bfs              | random          | all               |         5 |
|      83.4000 |     15.3441 | most_recently_added  | bfs              | fifo            | all               |         5 |
|      79.0000 |      8.2946 | most_recently_used   | bfs              | random          | all               |         5 |
|      75.6000 |     11.0562 | random               | bfs              | fifo            | all               |         5 |
|      72.2000 |     15.2892 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|      71.6000 |     15.0280 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|      71.4000 |     17.2928 | most_frequently_used | bfs              | fifo            | all               |         5 |
|      70.2000 |      9.9076 | random               | dijkstra         | fifo            | all               |         5 |
|      70.0000 |     16.4803 | most_recently_used   | bfs              | fifo            | all               |         5 |
|      69.8000 |     15.3023 | random               | dijkstra         | random          | all               |         5 |
|      61.2000 |     15.4842 | most_recently_added  | bfs              | random          | all               |         5 |
|      61.0000 |      6.1968 | most_recently_used   | dijkstra         | random          | all               |         5 |
|      59.6000 |      8.6163 | most_frequently_used | dijkstra         | random          | all               |         5 |
|      57.6000 |     14.4582 | random               | bfs              | random          | all               |         5 |
|      54.0000 |     10.3730 | most_recently_added  | dijkstra         | random          | all               |         5 |
|      50.2000 |      6.4000 | most_recently_used   | random           | random          | all               |         5 |
|      46.4000 |     33.6012 | most_recently_used   | random           | lru             | all               |         5 |
|      45.0000 |     14.1563 | most_frequently_used | random           | random          | all               |         5 |
|      43.6000 |     13.0015 | random               | random           | fifo            | all               |         5 |
|      41.8000 |     21.4886 | most_frequently_used | random           | lru             | all               |         5 |
|      41.4000 |     20.3627 | random               | random           | lru             | all               |         5 |
|      40.4000 |     18.5753 | most_recently_added  | random           | fifo            | all               |         5 |
|      38.6000 |      6.2801 | random               | random           | random          | all               |         5 |
|      38.0000 |      4.6043 | most_recently_added  | random           | random          | all               |         5 |
|      36.8000 |     19.2603 | most_recently_used   | random           | fifo            | all               |         5 |
|      36.0000 |     21.4196 | most_recently_added  | random           | lru             | all               |         5 |
|      35.2000 |     18.9251 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 16

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     362.2000 |     92.0595 | random               | bfs              | lfu             | all               |         5 |
|     353.6000 |    115.6868 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     350.6000 |     45.4031 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     337.6000 |     61.5097 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     332.0000 |     34.6006 | random               | dijkstra         | lru             | all               |         5 |
|     328.4000 |    128.9443 | random               | dijkstra         | lfu             | all               |         5 |
|     310.4000 |     42.7486 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     301.2000 |     75.7559 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     295.2000 |     29.6877 | most_recently_added  | bfs              | lru             | all               |         5 |
|     283.6000 |    116.2439 | most_frequently_used | random           | lfu             | all               |         5 |
|     280.6000 |     53.1962 | random               | bfs              | lru             | all               |         5 |
|     271.4000 |     51.7092 | most_frequently_used | bfs              | lru             | all               |         5 |
|     262.0000 |     28.3337 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     254.8000 |    158.1865 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     253.8000 |     76.0878 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     245.8000 |     34.5798 | most_recently_used   | bfs              | lru             | all               |         5 |
|     197.4000 |     56.2089 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     159.2000 |     55.3006 | most_recently_added  | random           | lfu             | all               |         5 |
|     157.6000 |     98.4532 | random               | random           | lfu             | all               |         5 |
|     143.0000 |     59.8231 | most_recently_used   | random           | lfu             | all               |         5 |
|     126.0000 |      7.6942 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     125.2000 |      7.9095 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     122.8000 |     10.0280 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     122.6000 |     10.4038 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     116.0000 |     14.9265 | random               | dijkstra         | random          | all               |         5 |
|     115.0000 |     10.4115 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     114.4000 |     11.0743 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     114.0000 |     73.6695 | most_frequently_used | random           | fifo            | all               |         5 |
|     110.2000 |     22.5956 | random               | dijkstra         | fifo            | all               |         5 |
|     108.4000 |     21.3410 | random               | bfs              | fifo            | all               |         5 |
|     107.8000 |     27.7662 | random               | bfs              | random          | all               |         5 |
|     104.6000 |     65.3195 | most_recently_added  | random           | lru             | all               |         5 |
|     104.0000 |     70.7842 | most_recently_used   | random           | lru             | all               |         5 |
|     101.4000 |     10.6132 | most_recently_added  | bfs              | random          | all               |         5 |
|      94.8000 |     16.4730 | most_frequently_used | bfs              | random          | all               |         5 |
|      94.6000 |     44.7464 | random               | random           | lru             | all               |         5 |
|      94.2000 |     16.4609 | most_recently_used   | bfs              | random          | all               |         5 |
|      90.0000 |     20.2287 | most_recently_used   | dijkstra         | random          | all               |         5 |
|      89.8000 |     32.6582 | most_frequently_used | random           | lru             | all               |         5 |
|      88.0000 |     27.0851 | most_frequently_used | dijkstra         | random          | all               |         5 |
|      68.0000 |     23.1689 | most_recently_added  | dijkstra         | random          | all               |         5 |
|      66.4000 |      5.0040 | most_recently_used   | random           | random          | all               |         5 |
|      66.0000 |     26.0845 | most_recently_added  | random           | fifo            | all               |         5 |
|      64.0000 |     14.3805 | random               | random           | fifo            | all               |         5 |
|      62.8000 |     23.8109 | most_recently_used   | random           | fifo            | all               |         5 |
|      61.2000 |     24.5959 | most_frequently_used | random           | random          | all               |         5 |
|      51.6000 |     12.6111 | most_recently_added  | random           | random          | all               |         5 |
|      47.4000 |     15.0280 | random               | random           | random          | all               |         5 |

## Memory Size 32

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     528.8000 |     28.9786 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     512.2000 |     56.9189 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     490.0000 |     52.8432 | random               | bfs              | lfu             | all               |         5 |
|     485.4000 |     21.0580 | most_recently_used   | bfs              | lru             | all               |         5 |
|     482.6000 |     41.7833 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     478.8000 |     63.3574 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     467.4000 |     20.2840 | most_recently_added  | bfs              | lru             | all               |         5 |
|     446.8000 |     38.1125 | random               | bfs              | lru             | all               |         5 |
|     444.6000 |     18.1505 | most_frequently_used | bfs              | lru             | all               |         5 |
|     428.0000 |     70.3420 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     427.0000 |     58.1446 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     418.8000 |     51.4564 | random               | dijkstra         | lru             | all               |         5 |
|     411.6000 |    148.0278 | random               | dijkstra         | lfu             | all               |         5 |
|     396.4000 |     87.9718 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     393.8000 |     92.8556 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     351.2000 |     71.8983 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     245.8000 |     25.4275 | most_recently_added  | random           | lfu             | all               |         5 |
|     211.0000 |     26.8626 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     206.6000 |     24.8322 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     203.6000 |     84.2700 | most_frequently_used | random           | lru             | all               |         5 |
|     203.0000 |     20.1494 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     200.2000 |     51.4680 | most_recently_added  | random           | lru             | all               |         5 |
|     200.2000 |     27.2206 | most_recently_added  | bfs              | random          | all               |         5 |
|     199.2000 |     22.5690 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     197.6000 |     20.9724 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     195.2000 |     30.7402 | random               | dijkstra         | fifo            | all               |         5 |
|     189.8000 |     19.3948 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     187.0000 |     75.8630 | most_frequently_used | random           | lfu             | all               |         5 |
|     178.6000 |     24.5487 | most_recently_added  | dijkstra         | random          | all               |         5 |
|     178.0000 |     18.1439 | random               | bfs              | fifo            | all               |         5 |
|     170.0000 |     17.2627 | random               | dijkstra         | random          | all               |         5 |
|     168.8000 |     28.3789 | most_frequently_used | bfs              | random          | all               |         5 |
|     168.6000 |     65.1540 | random               | random           | lru             | all               |         5 |
|     165.2000 |     20.4685 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     164.8000 |     32.6766 | most_recently_used   | bfs              | random          | all               |         5 |
|     159.0000 |     29.5905 | most_frequently_used | dijkstra         | random          | all               |         5 |
|     157.8000 |     22.7543 | random               | bfs              | random          | all               |         5 |
|     136.8000 |     63.5371 | random               | random           | lfu             | all               |         5 |
|     124.0000 |     36.3703 | most_recently_used   | random           | lfu             | all               |         5 |
|     123.4000 |     64.4875 | most_recently_used   | random           | lru             | all               |         5 |
|     122.0000 |     33.3287 | most_frequently_used | random           | random          | all               |         5 |
|      95.8000 |     24.8709 | most_frequently_used | random           | fifo            | all               |         5 |
|      87.6000 |     20.4216 | random               | random           | random          | all               |         5 |
|      81.6000 |     16.5602 | most_recently_added  | random           | fifo            | all               |         5 |
|      77.8000 |     20.9705 | most_recently_added  | random           | random          | all               |         5 |
|      76.6000 |     25.3346 | most_recently_used   | random           | fifo            | all               |         5 |
|      56.6000 |     15.6282 | random               | random           | fifo            | all               |         5 |
|      51.4000 |     28.7722 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 64

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     623.8000 |     46.0973 | most_recently_used   | bfs              | lru             | all               |         5 |
|     614.4000 |     51.2273 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     608.4000 |     49.2203 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     598.4000 |     26.4167 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     594.4000 |     33.4102 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     586.6000 |     45.8327 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     583.4000 |     46.3448 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     568.4000 |     27.0599 | most_recently_added  | bfs              | lru             | all               |         5 |
|     566.6000 |     25.0488 | random               | bfs              | lfu             | all               |         5 |
|     555.4000 |     43.6147 | random               | dijkstra         | lfu             | all               |         5 |
|     549.6000 |     90.2942 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     549.4000 |     53.0494 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     538.6000 |     48.3760 | random               | dijkstra         | lru             | all               |         5 |
|     535.6000 |     47.9608 | most_frequently_used | bfs              | lru             | all               |         5 |
|     527.4000 |     52.5913 | random               | bfs              | lru             | all               |         5 |
|     523.6000 |     88.8788 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     337.6000 |     24.1876 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     337.4000 |     32.7329 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     325.6000 |     48.0566 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     325.0000 |     24.0167 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     324.0000 |     41.5596 | random               | dijkstra         | fifo            | all               |         5 |
|     322.8000 |     20.6243 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     308.6000 |     31.1551 | random               | bfs              | fifo            | all               |         5 |
|     305.8000 |     23.9115 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     303.8000 |     40.1069 | most_frequently_used | bfs              | random          | all               |         5 |
|     296.8000 |     23.4896 | most_recently_added  | bfs              | random          | all               |         5 |
|     291.2000 |     24.4082 | most_recently_used   | bfs              | random          | all               |         5 |
|     275.8000 |     43.3931 | most_recently_added  | dijkstra         | random          | all               |         5 |
|     273.0000 |     12.4579 | random               | dijkstra         | random          | all               |         5 |
|     266.6000 |     21.3972 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     259.6000 |     34.3430 | most_frequently_used | dijkstra         | random          | all               |         5 |
|     249.8000 |     24.0782 | random               | bfs              | random          | all               |         5 |
|     217.6000 |     42.4009 | most_frequently_used | random           | lfu             | all               |         5 |
|     188.4000 |     82.8362 | most_recently_added  | random           | lfu             | all               |         5 |
|     180.4000 |     79.2202 | most_frequently_used | random           | lru             | all               |         5 |
|     174.6000 |     77.6314 | most_recently_used   | random           | lru             | all               |         5 |
|     134.2000 |     58.1495 | random               | random           | lfu             | all               |         5 |
|     128.8000 |    107.6762 | most_recently_added  | random           | lru             | all               |         5 |
|     127.4000 |     52.2287 | random               | random           | lru             | all               |         5 |
|     123.0000 |     49.6306 | most_frequently_used | random           | random          | all               |         5 |
|     113.4000 |     68.9916 | most_recently_used   | random           | lfu             | all               |         5 |
|     111.0000 |     39.7341 | most_frequently_used | random           | fifo            | all               |         5 |
|     106.8000 |     58.6495 | most_recently_used   | random           | random          | all               |         5 |
|     105.0000 |     35.4570 | random               | random           | fifo            | all               |         5 |
|     102.0000 |     47.8163 | most_recently_added  | random           | random          | all               |         5 |
|      90.6000 |     39.1438 | most_recently_used   | random           | fifo            | all               |         5 |
|      88.2000 |     24.0366 | random               | random           | random          | all               |         5 |
|      87.0000 |     25.3850 | most_recently_added  | random           | fifo            | all               |         5 |

## Memory Size 128

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     641.8000 |     65.5726 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     633.8000 |     43.9017 | most_recently_added  | bfs              | lru             | all               |         5 |
|     631.2000 |     60.9373 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     630.0000 |     43.6119 | most_recently_used   | bfs              | lru             | all               |         5 |
|     607.2000 |     57.5757 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     603.4000 |     60.7441 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     596.6000 |     56.4220 | random               | bfs              | lfu             | all               |         5 |
|     588.6000 |     44.4999 | random               | bfs              | lru             | all               |         5 |
|     586.0000 |     38.8999 | random               | dijkstra         | lru             | all               |         5 |
|     584.2000 |     72.4276 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     579.4000 |     60.2847 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     575.2000 |     32.9327 | random               | dijkstra         | lfu             | all               |         5 |
|     562.0000 |     61.9032 | most_frequently_used | bfs              | lru             | all               |         5 |
|     542.4000 |     99.6245 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     534.4000 |     48.3967 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     531.0000 |     40.9243 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     506.8000 |     31.9086 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     498.0000 |     34.7448 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     482.0000 |     52.8923 | random               | bfs              | fifo            | all               |         5 |
|     467.4000 |     23.7200 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     463.6000 |     28.5139 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     463.4000 |     51.0866 | random               | dijkstra         | fifo            | all               |         5 |
|     455.2000 |     18.1813 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     448.4000 |     45.9069 | random               | bfs              | random          | all               |         5 |
|     447.8000 |     26.1641 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     428.6000 |     33.5595 | most_recently_added  | dijkstra         | random          | all               |         5 |
|     415.6000 |     26.8820 | most_recently_used   | bfs              | random          | all               |         5 |
|     408.0000 |     28.5797 | random               | dijkstra         | random          | all               |         5 |
|     405.4000 |     51.8482 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     404.8000 |     22.7982 | most_recently_added  | bfs              | random          | all               |         5 |
|     402.6000 |     48.4628 | most_frequently_used | dijkstra         | random          | all               |         5 |
|     399.0000 |     50.4063 | most_frequently_used | bfs              | random          | all               |         5 |
|     271.2000 |     73.7113 | most_recently_added  | random           | lfu             | all               |         5 |
|     252.4000 |    106.8618 | random               | random           | lfu             | all               |         5 |
|     228.2000 |     96.4622 | random               | random           | lru             | all               |         5 |
|     216.4000 |     95.3113 | most_recently_added  | random           | lru             | all               |         5 |
|     204.8000 |     90.6143 | random               | random           | random          | all               |         5 |
|     202.8000 |     25.6780 | most_recently_added  | random           | random          | all               |         5 |
|     195.2000 |     71.8899 | most_recently_added  | random           | fifo            | all               |         5 |
|     186.6000 |     71.1241 | most_frequently_used | random           | lfu             | all               |         5 |
|     171.8000 |     47.7259 | most_frequently_used | random           | lru             | all               |         5 |
|     170.2000 |     89.5732 | most_recently_used   | random           | lru             | all               |         5 |
|     167.6000 |     49.4312 | most_frequently_used | random           | random          | all               |         5 |
|     165.2000 |     42.2724 | most_frequently_used | random           | fifo            | all               |         5 |
|     164.2000 |     65.0612 | random               | random           | fifo            | all               |         5 |
|     144.6000 |     24.6868 | most_recently_used   | random           | fifo            | all               |         5 |
|     126.0000 |     62.8299 | most_recently_used   | random           | lfu             | all               |         5 |
|      98.4000 |     40.1577 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 256

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     650.2000 |     22.5335 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     649.6000 |     34.9949 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     648.8000 |     38.6544 | most_recently_added  | bfs              | lru             | all               |         5 |
|     633.4000 |     29.8436 | random               | bfs              | lru             | all               |         5 |
|     628.2000 |     33.7010 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     622.8000 |     33.3311 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     618.8000 |     42.2724 | random               | dijkstra         | lfu             | all               |         5 |
|     615.6000 |     47.7100 | most_recently_added  | bfs              | random          | all               |         5 |
|     612.0000 |     31.1833 | random               | bfs              | lfu             | all               |         5 |
|     609.8000 |     40.2313 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     606.0000 |     39.4107 | random               | dijkstra         | lru             | all               |         5 |
|     605.8000 |     33.1083 | random               | bfs              | fifo            | all               |         5 |
|     603.8000 |     46.4603 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     602.2000 |     32.8232 | random               | dijkstra         | fifo            | all               |         5 |
|     601.8000 |     30.1224 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     601.4000 |     33.1940 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     597.2000 |     37.2043 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     592.4000 |     29.2889 | most_recently_used   | bfs              | lru             | all               |         5 |
|     592.0000 |     28.9897 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     583.2000 |     88.9301 | most_recently_added  | dijkstra         | random          | all               |         5 |
|     578.2000 |     35.9299 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     578.0000 |     71.0324 | random               | dijkstra         | random          | all               |         5 |
|     570.4000 |     24.3195 | random               | bfs              | random          | all               |         5 |
|     570.0000 |     36.1386 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     546.4000 |     17.2812 | most_frequently_used | bfs              | lru             | all               |         5 |
|     544.6000 |     26.7103 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     542.8000 |     66.8054 | most_frequently_used | dijkstra         | random          | all               |         5 |
|     539.0000 |     50.9235 | most_recently_used   | bfs              | random          | all               |         5 |
|     539.0000 |     21.3073 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     536.2000 |     14.4693 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     528.8000 |     62.5888 | most_frequently_used | bfs              | random          | all               |         5 |
|     525.6000 |     30.5326 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     218.8000 |     94.7574 | random               | random           | lfu             | all               |         5 |
|     214.6000 |    102.9050 | random               | random           | random          | all               |         5 |
|     212.6000 |     97.7049 | random               | random           | lru             | all               |         5 |
|     212.6000 |     41.8167 | most_frequently_used | random           | lfu             | all               |         5 |
|     212.0000 |     41.1485 | most_frequently_used | random           | lru             | all               |         5 |
|     202.8000 |     53.9385 | most_recently_added  | random           | random          | all               |         5 |
|     198.6000 |     48.2270 | random               | random           | fifo            | all               |         5 |
|     187.4000 |     61.7239 | most_frequently_used | random           | random          | all               |         5 |
|     184.4000 |     50.6896 | most_recently_used   | random           | lfu             | all               |         5 |
|     174.4000 |     74.6072 | most_recently_added  | random           | lru             | all               |         5 |
|     174.4000 |     60.8460 | most_recently_used   | random           | lru             | all               |         5 |
|     173.4000 |     90.1545 | most_recently_added  | random           | lfu             | all               |         5 |
|     166.6000 |     53.3464 | most_recently_added  | random           | fifo            | all               |         5 |
|     165.0000 |     54.2181 | most_frequently_used | random           | fifo            | all               |         5 |
|     145.8000 |     73.0737 | most_recently_used   | random           | random          | all               |         5 |
|     140.2000 |     46.1363 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 512

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     641.8000 |     27.0658 | most_recently_added  | dijkstra         | random          | all               |         5 |
|     641.4000 |     27.6810 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     640.6000 |     27.5942 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     639.8000 |     26.2480 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     637.6000 |     21.2283 | most_recently_added  | bfs              | random          | all               |         5 |
|     635.8000 |     21.5258 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     633.2000 |     19.7525 | most_recently_added  | bfs              | lru             | all               |         5 |
|     632.8000 |     20.1336 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     611.0000 |     48.0541 | most_recently_used   | bfs              | random          | all               |         5 |
|     610.8000 |     49.7811 | most_recently_used   | bfs              | lru             | all               |         5 |
|     610.4000 |     50.0424 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     609.2000 |     49.0037 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     606.8000 |     46.4086 | random               | dijkstra         | lru             | all               |         5 |
|     606.8000 |     46.8419 | random               | dijkstra         | lfu             | all               |         5 |
|     603.2000 |     37.2312 | random               | dijkstra         | random          | all               |         5 |
|     602.6000 |     41.3212 | random               | dijkstra         | fifo            | all               |         5 |
|     595.2000 |     40.3009 | random               | bfs              | fifo            | all               |         5 |
|     594.8000 |     40.6468 | random               | bfs              | random          | all               |         5 |
|     594.4000 |     42.2308 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     593.8000 |     33.1988 | random               | bfs              | lfu             | all               |         5 |
|     592.6000 |     35.3418 | random               | bfs              | lru             | all               |         5 |
|     591.4000 |     42.9027 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     591.0000 |     42.7972 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     589.6000 |     50.6067 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     584.4000 |     34.1151 | most_frequently_used | bfs              | random          | all               |         5 |
|     580.0000 |     29.2780 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     577.0000 |     29.1822 | most_frequently_used | bfs              | lru             | all               |         5 |
|     576.6000 |     29.2342 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     565.8000 |     41.1990 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     562.8000 |     39.4837 | most_frequently_used | dijkstra         | random          | all               |         5 |
|     558.0000 |     42.6474 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     557.8000 |     42.6774 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     233.0000 |    105.4438 | random               | random           | random          | all               |         5 |
|     229.8000 |    101.0810 | random               | random           | lfu             | all               |         5 |
|     229.8000 |    101.0810 | random               | random           | lru             | all               |         5 |
|     227.8000 |     99.1028 | random               | random           | fifo            | all               |         5 |
|     214.8000 |     56.5240 | most_frequently_used | random           | random          | all               |         5 |
|     213.0000 |     58.7026 | most_frequently_used | random           | lfu             | all               |         5 |
|     213.0000 |     58.7026 | most_frequently_used | random           | lru             | all               |         5 |
|     210.4000 |     54.7671 | most_frequently_used | random           | fifo            | all               |         5 |
|     201.6000 |     71.6369 | most_recently_added  | random           | fifo            | all               |         5 |
|     201.4000 |     71.8237 | most_recently_added  | random           | random          | all               |         5 |
|     201.2000 |     70.0725 | most_recently_added  | random           | lfu             | all               |         5 |
|     201.2000 |     70.0725 | most_recently_added  | random           | lru             | all               |         5 |
|     129.0000 |     41.9905 | most_recently_used   | random           | random          | all               |         5 |
|     127.6000 |     42.1027 | most_recently_used   | random           | lfu             | all               |         5 |
|     126.8000 |     43.2823 | most_recently_used   | random           | lru             | all               |         5 |
|     126.0000 |     39.7240 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 1024

Total configurations: 48

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | random          | all               |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     644.2000 |     31.4795 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | lru             | all               |         5 |
|     638.8000 |     22.5690 | most_recently_added  | bfs              | random          | all               |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | lru             | all               |         5 |
|     614.0000 |     49.6548 | most_recently_used   | bfs              | random          | all               |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     602.0000 |     41.3376 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | fifo            | all               |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | lfu             | all               |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | lru             | all               |         5 |
|     599.2000 |     42.7757 | random               | dijkstra         | random          | all               |         5 |
|     594.8000 |     36.1851 | random               | bfs              | random          | all               |         5 |
|     594.8000 |     36.1851 | random               | bfs              | lru             | all               |         5 |
|     594.8000 |     36.1851 | random               | bfs              | lfu             | all               |         5 |
|     594.8000 |     36.1851 | random               | bfs              | fifo            | all               |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | random          | all               |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | lru             | all               |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     575.4000 |     27.9185 | most_frequently_used | bfs              | fifo            | all               |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|     559.2000 |     40.0120 | most_frequently_used | dijkstra         | random          | all               |         5 |
|     232.0000 |    102.7716 | random               | random           | fifo            | all               |         5 |
|     232.0000 |    102.7716 | random               | random           | lfu             | all               |         5 |
|     232.0000 |    102.7716 | random               | random           | lru             | all               |         5 |
|     232.0000 |    102.7716 | random               | random           | random          | all               |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | fifo            | all               |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | lfu             | all               |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | lru             | all               |         5 |
|     218.4000 |     61.3436 | most_frequently_used | random           | random          | all               |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | fifo            | all               |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | lfu             | all               |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | lru             | all               |         5 |
|     213.2000 |     79.0605 | most_recently_added  | random           | random          | all               |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | fifo            | all               |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | lfu             | all               |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | lru             | all               |         5 |
|     125.2000 |     37.9758 | most_recently_used   | random           | random          | all               |         5 |

