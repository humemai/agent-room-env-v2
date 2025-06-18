# Results for xxl-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|     450.7500 |     54.5774 | most_recently_used   | bfs              | lru             | all               |           512 |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | fifo            | all               |          1024 |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | lfu             | all               |          1024 |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | random          | all               |          1024 |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | lru             | all               |          1024 |         4 |
|     449.5000 |     55.2336 | most_recently_used   | bfs              | lfu             | all               |           512 |         4 |
|     444.5000 |     52.6427 | most_recently_used   | bfs              | random          | all               |           512 |         4 |
|     440.0000 |     52.3211 | most_recently_used   | bfs              | fifo            | all               |           512 |         4 |
|     438.7500 |     62.2590 | most_recently_used   | bfs              | lfu             | all               |           256 |         4 |
|     437.5000 |     43.8264 | most_recently_used   | bfs              | lru             | all               |           256 |         4 |
|     422.7500 |     53.0206 | most_frequently_used | bfs              | lru             | all               |           512 |         4 |
|     420.7500 |     54.5728 | most_frequently_used | bfs              | lfu             | all               |           512 |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | lru             | all               |          1024 |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | random          | all               |          1024 |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | lfu             | all               |          1024 |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | fifo            | all               |          1024 |         4 |
|     418.5000 |     51.9447 | most_frequently_used | bfs              | random          | all               |           512 |         4 |
|     415.7500 |     54.6689 | most_frequently_used | bfs              | fifo            | all               |           512 |         4 |
|     403.2500 |     36.4649 | most_recently_used   | bfs              | lru             | all               |           128 |         4 |
|     401.0000 |     82.3681 | most_frequently_used | bfs              | lfu             | all               |           256 |         4 |
|     396.0000 |     73.4132 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         4 |
|     396.0000 |     73.4132 | most_recently_added  | dijkstra         | random          | all               |          1024 |         4 |
|     396.0000 |     73.4132 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         4 |
|     394.2500 |    101.3765 | most_recently_used   | dijkstra         | random          | all               |          1024 |         4 |
|     394.2500 |    101.3765 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         4 |
|     394.0000 |     72.3015 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         4 |
|     394.0000 |     59.2340 | most_recently_added  | bfs              | lfu             | all               |          1024 |         3 |
|     394.0000 |     71.8123 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         4 |
|     393.0000 |     59.6210 | most_recently_added  | bfs              | lfu             | all               |           512 |         3 |
|     390.0000 |     53.2870 | most_recently_added  | bfs              | random          | all               |           512 |         4 |
|     388.5000 |     73.0804 | most_recently_added  | bfs              | lru             | all               |           256 |         4 |
|     388.0000 |     67.7237 | most_recently_added  | dijkstra         | random          | all               |           512 |         4 |
|     387.5000 |    100.1636 | most_recently_used   | dijkstra         | random          | all               |           512 |         4 |
|     387.2500 |     52.6136 | most_recently_added  | bfs              | fifo            | all               |          1024 |         4 |
|     387.2500 |     52.6136 | most_recently_added  | bfs              | lru             | all               |          1024 |         4 |
|     387.2500 |     52.6136 | most_recently_added  | bfs              | random          | all               |          1024 |         4 |
|     386.5000 |     80.9336 | most_frequently_used | bfs              | lru             | all               |           256 |         4 |
|     385.7500 |     55.7107 | most_recently_added  | bfs              | fifo            | all               |           512 |         4 |
|     385.7500 |     53.1384 | most_recently_added  | bfs              | lru             | all               |           512 |         4 |
|     385.5000 |    100.4652 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         4 |
|     382.0000 |     52.3323 | most_recently_added  | bfs              | lfu             | all               |           256 |         3 |
|     376.6667 |     75.4380 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         3 |
|     373.0000 |     71.6147 | most_recently_added  | dijkstra         | lru             | all               |           512 |         3 |
|     371.5000 |     71.8836 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         4 |
|     371.5000 |     71.8836 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         4 |
|     368.0000 |     71.4108 | most_frequently_used | dijkstra         | lru             | all               |           512 |         4 |
|     366.5000 |     68.0790 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         4 |
|     366.2500 |     35.6467 | most_recently_used   | bfs              | random          | all               |           256 |         4 |
|     363.7500 |    122.0172 | most_recently_added  | bfs              | lfu             | all               |           128 |         4 |
|     360.7500 |     51.9345 | most_frequently_used | bfs              | fifo            | all               |           256 |         4 |
|     356.7500 |     42.0974 | most_recently_used   | bfs              | lfu             | all               |           128 |         4 |
|     354.7500 |     73.3361 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         4 |
|     353.3333 |     26.4113 | most_recently_used   | dijkstra         | lru             | all               |           128 |         3 |
|     349.5000 |     11.8427 | most_recently_used   | bfs              | fifo            | all               |           256 |         4 |
|     343.5000 |     85.8443 | most_frequently_used | bfs              | lru             | all               |           128 |         4 |
|     341.5000 |     44.0539 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         4 |
|     340.0000 |    107.8819 | most_frequently_used | bfs              | lfu             | all               |           128 |         4 |
|     339.0000 |     51.6204 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         3 |
|     339.0000 |     51.6204 | most_frequently_used | dijkstra         | random          | all               |          1024 |         3 |
|     338.6667 |     49.7750 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         3 |
|     336.0000 |     11.4310 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         3 |
|     336.0000 |     11.4310 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         3 |
|     335.7500 |    102.9038 | most_recently_added  | bfs              | lru             | all               |           128 |         4 |
|     333.0000 |     70.7001 | most_frequently_used | bfs              | random          | all               |           256 |         4 |
|     331.6667 |     11.7284 | most_recently_used   | dijkstra         | lru             | all               |           512 |         3 |
|     331.0000 |     12.5698 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         3 |
|     330.7500 |     40.2267 | most_recently_added  | bfs              | fifo            | all               |           256 |         4 |
|     329.0000 |     48.8330 | most_frequently_used | dijkstra         | random          | all               |           512 |         3 |
|     327.6667 |     99.1206 | most_recently_added  | dijkstra         | lru             | all               |           256 |         3 |
|     326.5000 |     84.4349 | most_frequently_used | dijkstra         | lru             | all               |           256 |         4 |
|     322.3333 |     64.5618 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         3 |
|     320.7500 |     60.4044 | most_recently_added  | bfs              | lfu             | all               |            64 |         4 |
|     318.5000 |     47.4368 | most_recently_added  | bfs              | random          | all               |           256 |         4 |
|     318.2500 |     89.6755 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         4 |
|     312.0000 |     75.7331 | most_frequently_used | dijkstra         | random          | all               |           256 |         4 |
|     310.0000 |     94.9289 | most_frequently_used | dijkstra         | lru             | all               |           128 |         4 |
|     308.0000 |     48.6672 | most_recently_added  | dijkstra         | random          | all               |           256 |         4 |
|     305.6667 |      9.8432 | most_recently_used   | dijkstra         | lru             | all               |           256 |         3 |
|     304.3333 |      7.5865 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         3 |
|     300.7500 |     53.2183 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         4 |
|     298.7500 |     70.3611 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         4 |
|     298.5000 |     52.9221 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         4 |
|     298.2500 |     61.3244 | most_recently_used   | dijkstra         | random          | all               |           256 |         4 |
|     293.5000 |     40.8993 | most_recently_used   | bfs              | lfu             | all               |            64 |         4 |
|     292.7500 |     56.1711 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         4 |
|     279.3333 |      6.5490 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         3 |
|     272.2500 |     40.6040 | most_recently_added  | bfs              | lru             | all               |            64 |         4 |
|     270.0000 |     66.6146 | most_frequently_used | bfs              | lfu             | all               |            64 |         4 |
|     268.2500 |     94.5790 | most_recently_added  | dijkstra         | lru             | all               |           128 |         4 |
|     267.5000 |     89.7455 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         4 |
|     259.6667 |     33.4797 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         3 |
|     257.0000 |     35.2420 | most_recently_added  | dijkstra         | lru             | all               |            64 |         4 |
|     247.7500 |     37.8178 | most_frequently_used | dijkstra         | lru             | all               |            64 |         4 |
|     233.2500 |     73.4894 | most_frequently_used | bfs              | lru             | all               |            64 |         4 |
|     232.6667 |     43.3154 | most_recently_used   | dijkstra         | lru             | all               |            64 |         3 |
|     231.0000 |     35.1923 | most_recently_used   | bfs              | lru             | all               |            64 |         4 |
|     224.5000 |     32.1908 | most_recently_used   | bfs              | fifo            | all               |           128 |         4 |
|     223.2500 |     28.4726 | most_frequently_used | bfs              | fifo            | all               |           128 |         4 |
|     222.2500 |     28.2168 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         4 |
|     214.0000 |     14.4453 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         3 |
|     209.5000 |     48.2157 | most_frequently_used | bfs              | random          | all               |           128 |         4 |
|     208.7500 |     51.2902 | most_recently_added  | dijkstra         | random          | all               |           128 |         4 |
|     204.2500 |     36.7789 | most_frequently_used | bfs              | lfu             | all               |            32 |         4 |
|     201.2500 |     43.6656 | most_recently_added  | bfs              | fifo            | all               |           128 |         4 |
|     200.5000 |     65.3816 | most_recently_used   | bfs              | lfu             | all               |            32 |         4 |
|     199.2500 |     44.1439 | most_recently_used   | bfs              | random          | all               |           128 |         4 |
|     199.0000 |     46.6744 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         4 |
|     192.0000 |     55.4076 | most_recently_added  | bfs              | random          | all               |           128 |         4 |
|     185.7500 |     39.3915 | most_recently_added  | bfs              | lfu             | all               |            32 |         4 |
|     182.5000 |     47.0346 | most_frequently_used | dijkstra         | random          | all               |           128 |         4 |
|     176.2500 |     41.5955 | most_recently_used   | dijkstra         | random          | all               |           128 |         4 |
|     176.0000 |     27.7969 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         3 |
|     176.0000 |     30.1579 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         4 |
|     172.5000 |     40.5247 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         4 |
|     146.2500 |     25.9362 | most_recently_used   | bfs              | lru             | all               |            32 |         4 |
|     143.0000 |     16.7183 | most_recently_added  | dijkstra         | lru             | all               |            32 |         4 |
|     141.0000 |     37.5433 | most_recently_added  | bfs              | lru             | all               |            32 |         4 |
|     139.5000 |     24.5917 | most_recently_added  | bfs              | fifo            | all               |            64 |         4 |
|     134.2500 |     31.2360 | most_frequently_used | bfs              | lfu             | all               |            16 |         4 |
|     132.7500 |     37.2986 | most_recently_used   | bfs              | fifo            | all               |            64 |         4 |
|     130.3333 |     26.1958 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         3 |
|     127.2500 |     20.1789 | most_frequently_used | bfs              | lru             | all               |            32 |         4 |
|     124.5000 |     16.1012 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         4 |
|     123.0000 |     24.3413 | most_frequently_used | dijkstra         | lru             | all               |            32 |         4 |
|     122.3333 |     16.1107 | most_recently_used   | dijkstra         | lru             | all               |            32 |         3 |
|     121.7500 |     26.3569 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         4 |
|     121.3333 |     20.8859 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         3 |
|     120.5000 |     31.3169 | most_recently_used   | bfs              | random          | all               |            64 |         4 |
|     118.7500 |     39.8332 | most_recently_added  | dijkstra         | random          | all               |            64 |         4 |
|     117.2500 |     28.7609 | most_frequently_used | bfs              | random          | all               |            64 |         4 |
|     116.7500 |     16.7984 | most_frequently_used | bfs              | fifo            | all               |            64 |         4 |
|     114.2500 |     57.1724 | most_recently_used   | bfs              | lfu             | all               |            16 |         4 |
|     112.0000 |     22.7486 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         4 |
|     111.0000 |     30.4549 | most_recently_added  | bfs              | random          | all               |            64 |         4 |
|     110.2500 |     27.2615 | most_recently_added  | bfs              | lfu             | all               |            16 |         4 |
|     108.2500 |     34.9025 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         4 |
|     104.5000 |     18.7150 | most_frequently_used | dijkstra         | random          | all               |            64 |         4 |
|     104.5000 |     44.2860 | most_recently_used   | random           | lfu             | all               |            64 |         4 |
|     101.3333 |     28.8020 | most_frequently_used | random           | lru             | all               |           256 |         3 |
|     101.3333 |     28.8020 | most_frequently_used | random           | lfu             | all               |           256 |         3 |
|      99.2500 |     38.9832 | most_recently_used   | random           | lru             | all               |           128 |         4 |
|      96.2500 |     24.6513 | most_frequently_used | random           | random          | all               |          1024 |         4 |
|      96.2500 |     24.6513 | most_frequently_used | random           | fifo            | all               |          1024 |         4 |
|      96.0000 |     23.8432 | most_frequently_used | random           | random          | all               |           512 |         4 |
|      95.0000 |     39.5053 | most_frequently_used | random           | lru             | all               |           128 |         3 |
|      94.0000 |     15.7321 | most_recently_added  | random           | lfu             | all               |            64 |         4 |
|      94.0000 |     32.7719 | most_recently_used   | dijkstra         | random          | all               |            64 |         4 |
|      93.5000 |     23.2648 | most_frequently_used | random           | random          | all               |           256 |         4 |
|      92.2500 |     18.7667 | most_recently_used   | bfs              | fifo            | all               |            32 |         4 |
|      92.0000 |     25.9615 | most_frequently_used | random           | fifo            | all               |           512 |         3 |
|      91.3333 |     25.9015 | most_frequently_used | random           | lru             | all               |           512 |         3 |
|      91.3333 |     25.9015 | most_frequently_used | random           | lfu             | all               |           512 |         3 |
|      90.7500 |     14.4114 | most_recently_added  | random           | lru             | all               |           256 |         4 |
|      90.3333 |     28.1109 | most_frequently_used | random           | lfu             | all               |           128 |         3 |
|      89.0000 |     20.8327 | most_recently_used   | random           | fifo            | all               |           256 |         3 |
|      88.6667 |     24.0878 | most_frequently_used | random           | lfu             | all               |          1024 |         3 |
|      88.6667 |     24.0878 | most_frequently_used | random           | lru             | all               |          1024 |         3 |
|      87.5000 |     14.3962 | most_recently_added  | random           | fifo            | all               |           512 |         4 |
|      85.0000 |     23.1625 | most_recently_used   | random           | lru             | all               |           256 |         4 |
|      84.7500 |     11.6485 | most_recently_added  | random           | lfu             | all               |           512 |         4 |
|      83.2500 |      9.2026 | most_recently_added  | random           | lru             | all               |           512 |         4 |
|      83.0000 |     20.6074 | most_recently_used   | random           | lru             | all               |          1024 |         3 |
|      83.0000 |     20.6074 | most_recently_used   | random           | fifo            | all               |          1024 |         3 |
|      82.5000 |     13.6107 | most_frequently_used | bfs              | fifo            | all               |            32 |         4 |
|      82.5000 |     37.3464 | most_recently_added  | random           | lru             | all               |           128 |         4 |
|      81.7500 |      8.2576 | most_recently_added  | random           | lfu             | all               |          1024 |         4 |
|      81.7500 |      8.2576 | most_recently_added  | random           | lru             | all               |          1024 |         4 |
|      81.7500 |      8.2576 | most_recently_added  | random           | fifo            | all               |          1024 |         4 |
|      81.5000 |     14.6714 | most_recently_added  | random           | lfu             | all               |           256 |         4 |
|      81.5000 |     11.5217 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         4 |
|      81.3333 |     13.4247 | most_frequently_used | random           | fifo            | all               |           256 |         3 |
|      81.0000 |      9.3541 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         4 |
|      81.0000 |      8.2865 | most_recently_added  | random           | random          | all               |           512 |         3 |
|      79.7500 |     21.6838 | most_frequently_used | bfs              | lfu             | all               |             8 |         4 |
|      79.6667 |     22.6912 | most_recently_used   | bfs              | lfu             | all               |             8 |         3 |
|      79.6667 |     15.9652 | most_recently_used   | random           | lru             | all               |           512 |         3 |
|      79.3333 |      8.2192 | most_recently_added  | random           | random          | all               |          1024 |         3 |
|      79.0000 |     24.6678 | most_recently_used   | random           | lfu             | all               |            32 |         4 |
|      77.7500 |     20.3270 | most_recently_used   | random           | lfu             | all               |           128 |         4 |
|      77.0000 |     14.2361 | most_recently_added  | random           | random          | all               |           256 |         3 |
|      76.5000 |     19.0853 | most_frequently_used | bfs              | lru             | all               |            16 |         4 |
|      75.7500 |     21.8217 | most_recently_used   | random           | lfu             | all               |          1024 |         4 |
|      75.7500 |     21.8217 | most_recently_used   | random           | random          | all               |          1024 |         4 |
|      75.7500 |     14.5667 | most_frequently_used | dijkstra         | lru             | all               |            16 |         4 |
|      74.0000 |     13.1403 | most_recently_used   | random           | fifo            | all               |           512 |         3 |
|      73.0000 |     16.0312 | most_recently_used   | random           | lfu             | all               |           512 |         4 |
|      72.7500 |     13.8992 | most_recently_used   | random           | lru             | all               |            64 |         4 |
|      72.5000 |     17.3566 | most_recently_used   | random           | random          | all               |           512 |         4 |
|      72.0000 |      6.0415 | most_recently_added  | bfs              | random          | all               |            32 |         4 |
|      72.0000 |     11.1131 | most_recently_used   | random           | lfu             | all               |           256 |         4 |
|      71.7500 |     21.9360 | most_recently_used   | bfs              | lru             | all               |            16 |         4 |
|      71.6667 |     25.6168 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         3 |
|      70.5000 |      7.0887 | most_frequently_used | random           | random          | all               |           128 |         4 |
|      70.3333 |     35.7243 | most_frequently_used | random           | lfu             | all               |            64 |         3 |
|      70.0000 |     14.5144 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         3 |
|      70.0000 |     21.0832 | most_recently_added  | random           | lfu             | all               |            32 |         4 |
|      69.2500 |      5.8041 | most_recently_used   | random           | random          | all               |           256 |         4 |
|      69.2500 |     23.8681 | most_recently_added  | random           | lfu             | all               |             8 |         4 |
|      68.0000 |     11.2916 | most_recently_added  | random           | fifo            | all               |           256 |         4 |
|      67.7500 |     30.3016 | most_recently_added  | random           | lfu             | all               |           128 |         4 |
|      67.2500 |     16.5435 | most_recently_added  | random           | lru             | all               |            64 |         4 |
|      66.7500 |     18.9522 | most_recently_added  | random           | lfu             | all               |            16 |         4 |
|      66.6667 |     14.2906 | most_recently_added  | random           | random          | all               |           128 |         3 |
|      66.2500 |     15.7698 | most_recently_used   | random           | lru             | all               |            32 |         4 |
|      65.2500 |     21.9929 | most_recently_added  | random           | fifo            | all               |           128 |         4 |
|      64.6667 |      7.1336 | most_recently_used   | dijkstra         | lru             | all               |            16 |         3 |
|      64.2500 |      9.2837 | most_recently_added  | bfs              | lru             | all               |            16 |         4 |
|      63.7500 |     14.2017 | most_recently_added  | random           | random          | all               |            64 |         4 |
|      63.0000 |      9.4340 | most_frequently_used | dijkstra         | random          | all               |            32 |         4 |
|      63.0000 |      7.4498 | most_frequently_used | bfs              | random          | all               |            32 |         4 |
|      62.6667 |     16.7796 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         3 |
|      62.5000 |     27.6812 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         4 |
|      62.0000 |      6.2048 | most_recently_added  | bfs              | fifo            | all               |            32 |         4 |
|      61.7500 |     11.7978 | most_recently_added  | dijkstra         | lru             | all               |            16 |         4 |
|      61.2500 |     23.2634 | most_recently_used   | random           | lfu             | all               |             8 |         4 |
|      61.0000 |     12.6293 | most_recently_used   | bfs              | random          | all               |            32 |         4 |
|      60.6667 |      3.0912 | most_recently_used   | random           | random          | all               |            64 |         3 |
|      60.5000 |      4.1533 | most_recently_added  | bfs              | lfu             | all               |             8 |         4 |
|      59.6667 |     16.4992 | most_frequently_used | random           | lfu             | all               |            32 |         3 |
|      59.5000 |      6.3443 | most_frequently_used | random           | random          | all               |            64 |         4 |
|      58.7500 |     18.2808 | most_recently_used   | random           | random          | all               |           128 |         4 |
|      57.6667 |     14.5220 | most_frequently_used | random           | lfu             | all               |             8 |         3 |
|      56.0000 |      5.2440 | most_recently_used   | dijkstra         | random          | all               |            32 |         4 |
|      55.3333 |     15.9652 | most_recently_used   | random           | fifo            | all               |           128 |         3 |
|      54.6667 |     19.6016 | most_frequently_used | random           | fifo            | all               |           128 |         3 |
|      53.2500 |     14.3592 | most_recently_added  | random           | lru             | all               |            32 |         4 |
|      53.0000 |      9.4163 | most_frequently_used | random           | lru             | all               |            64 |         3 |
|      52.6667 |     16.7398 | most_frequently_used | random           | fifo            | all               |            64 |         3 |
|      52.2500 |     14.5151 | most_recently_added  | dijkstra         | random          | all               |            32 |         4 |
|      51.7500 |      8.5550 | most_recently_added  | random           | fifo            | all               |            64 |         4 |
|      51.5000 |     10.5000 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         4 |
|      50.7500 |     20.6079 | most_recently_used   | random           | lfu             | all               |            16 |         4 |
|      50.0000 |     26.9444 | most_frequently_used | random           | lfu             | all               |            16 |         3 |
|      49.7500 |      9.4439 | most_recently_added  | bfs              | fifo            | all               |            16 |         4 |
|      49.5000 |     13.0480 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         4 |
|      48.5000 |     16.8597 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         4 |
|      47.3333 |      2.3570 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         3 |
|      47.2500 |     13.9530 | most_frequently_used | bfs              | random          | all               |            16 |         4 |
|      47.0000 |      6.9642 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         4 |
|      46.6667 |      9.7411 | most_recently_used   | random           | random          | all               |            32 |         3 |
|      45.5000 |     22.2879 | most_recently_added  | bfs              | lfu             | all               |             4 |         4 |
|      45.2500 |     17.4123 | most_recently_used   | bfs              | random          | all               |            16 |         4 |
|      43.7500 |     13.3112 | most_frequently_used | bfs              | lru             | all               |             8 |         4 |
|      43.7500 |     12.8525 | most_frequently_used | bfs              | fifo            | all               |            16 |         4 |
|      43.7500 |     13.3112 | most_recently_used   | bfs              | lru             | all               |             8 |         4 |
|      43.0000 |     10.6145 | most_recently_used   | random           | fifo            | all               |            32 |         3 |
|      43.0000 |      8.8600 | most_recently_added  | bfs              | random          | all               |            16 |         4 |
|      42.5000 |     12.5399 | most_recently_used   | bfs              | fifo            | all               |            16 |         4 |
|      41.7500 |     14.6693 | most_frequently_used | dijkstra         | lru             | all               |             8 |         4 |
|      40.7500 |     26.1474 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         4 |
|      40.3333 |     12.2837 | most_recently_used   | dijkstra         | lru             | all               |             8 |         3 |
|      40.0000 |      9.0921 | most_frequently_used | random           | lfu             | all               |             4 |         3 |
|      39.5000 |      8.5294 | most_recently_used   | random           | lfu             | all               |             4 |         4 |
|      39.0000 |      4.5277 | most_recently_added  | random           | random          | all               |            32 |         4 |
|      39.0000 |     14.1244 | most_recently_added  | dijkstra         | random          | all               |            16 |         4 |
|      38.0000 |     10.4163 | most_recently_added  | random           | fifo            | all               |            32 |         4 |
|      38.0000 |     15.6045 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         4 |
|      37.7500 |      3.7666 | most_recently_used   | dijkstra         | random          | all               |            16 |         4 |
|      37.5000 |     20.1680 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         4 |
|      37.2500 |      9.7308 | most_recently_added  | bfs              | lru             | all               |             8 |         4 |
|      36.7500 |      5.4486 | most_frequently_used | dijkstra         | random          | all               |            16 |         4 |
|      36.6667 |      0.9428 | most_frequently_used | random           | lru             | all               |            32 |         3 |
|      36.5000 |      4.7170 | most_recently_used   | random           | lru             | all               |            16 |         4 |
|      36.0000 |      6.5955 | most_recently_added  | dijkstra         | lru             | all               |             8 |         4 |
|      34.2500 |      6.1796 | most_recently_added  | random           | lfu             | all               |             4 |         4 |
|      34.0000 |      3.6742 | most_recently_added  | bfs              | fifo            | all               |             4 |         4 |
|      33.5000 |     18.0901 | most_frequently_used | bfs              | lfu             | all               |             2 |         4 |
|      33.0000 |     16.3095 | most_recently_added  | random           | lru             | all               |            16 |         4 |
|      32.0000 |      5.3385 | most_recently_added  | random           | random          | all               |            16 |         4 |
|      31.7500 |      7.5622 | most_recently_added  | random           | lru             | all               |             8 |         4 |
|      31.3333 |     11.1156 | most_recently_used   | bfs              | lfu             | all               |             4 |         3 |
|      30.7500 |      9.6792 | most_frequently_used | bfs              | lfu             | all               |             4 |         4 |
|      30.0000 |     11.5542 | most_frequently_used | random           | random          | all               |            32 |         4 |
|      29.5000 |      9.5263 | most_frequently_used | random           | random          | all               |            16 |         4 |
|      29.0000 |      9.1378 | most_frequently_used | dijkstra         | random          | all               |             8 |         4 |
|      29.0000 |      6.8191 | most_recently_added  | random           | fifo            | all               |            16 |         4 |
|      28.2500 |     14.9562 | most_recently_added  | bfs              | lfu             | all               |             2 |         4 |
|      28.0000 |      3.5355 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         4 |
|      28.0000 |      3.5355 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         4 |
|      28.0000 |      4.5461 | most_recently_used   | random           | random          | all               |            16 |         3 |
|      27.5000 |      9.5525 | most_frequently_used | bfs              | random          | all               |             8 |         4 |
|      27.3333 |     13.3000 | most_recently_used   | random           | fifo            | all               |            64 |         3 |
|      27.3333 |      9.4281 | most_frequently_used | random           | fifo            | all               |            16 |         3 |
|      27.2500 |      4.7104 | most_recently_added  | bfs              | fifo            | all               |             8 |         4 |
|      27.0000 |      2.8284 | most_frequently_used | random           | lru             | all               |            16 |         3 |
|      27.0000 |     11.4018 | most_recently_used   | dijkstra         | random          | all               |             8 |         4 |
|      26.7500 |      9.1207 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         4 |
|      26.7500 |      9.1207 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         4 |
|      26.6667 |     15.7973 | most_recently_used   | bfs              | lfu             | all               |             2 |         3 |
|      26.0000 |      4.9497 | most_recently_added  | random           | fifo            | all               |             8 |         4 |
|      25.3333 |     18.9268 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         3 |
|      25.2500 |      2.9475 | most_recently_used   | random           | lru             | all               |             8 |         4 |
|      24.7500 |      5.6734 | most_recently_used   | bfs              | fifo            | all               |             8 |         4 |
|      24.7500 |      5.6734 | most_frequently_used | bfs              | fifo            | all               |             8 |         4 |
|      24.6667 |      5.7927 | most_frequently_used | random           | fifo            | all               |            32 |         3 |
|      24.6667 |      8.5765 | most_frequently_used | random           | lfu             | all               |             0 |         3 |
|      24.6667 |      8.5765 | most_frequently_used | random           | lru             | all               |             0 |         3 |
|      24.5000 |     11.4127 | most_frequently_used | random           | random          | all               |             8 |         4 |
|      24.3333 |      4.4969 | most_frequently_used | random           | lru             | all               |             8 |         3 |
|      24.0000 |      6.7454 | most_recently_used   | bfs              | lru             | all               |             4 |         4 |
|      24.0000 |      6.7454 | most_frequently_used | bfs              | lru             | all               |             4 |         4 |
|      23.3333 |      5.2493 | most_recently_used   | random           | random          | all               |             4 |         3 |
|      23.2500 |      4.7104 | most_recently_added  | dijkstra         | random          | all               |             8 |         4 |
|      23.2500 |      1.9203 | most_recently_added  | bfs              | lru             | all               |             4 |         4 |
|      23.0000 |      1.8708 | most_recently_added  | dijkstra         | lru             | all               |             4 |         4 |
|      22.6667 |      3.0912 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         3 |
|      22.6667 |      6.5997 | most_recently_used   | dijkstra         | lru             | all               |             4 |         3 |
|      22.6667 |      6.5997 | most_frequently_used | dijkstra         | lru             | all               |             4 |         3 |
|      22.5000 |      6.0208 | most_frequently_used | random           | random          | all               |             4 |         4 |
|      22.2500 |     11.5190 | most_recently_added  | bfs              | random          | all               |             8 |         4 |
|      22.2500 |      8.4076 | most_recently_added  | random           | random          | all               |             8 |         4 |
|      21.7500 |      5.5396 | most_recently_added  | bfs              | random          | all               |             4 |         4 |
|      21.6667 |      7.0396 | most_recently_used   | random           | fifo            | all               |            16 |         3 |
|      21.6667 |      8.7305 | most_recently_used   | random           | fifo            | all               |             8 |         3 |
|      21.5000 |      6.8007 | most_recently_added  | random           | lru             | all               |             4 |         4 |
|      21.2500 |      9.4967 | most_recently_used   | random           | lfu             | all               |             0 |         4 |
|      21.2500 |      9.4967 | most_recently_added  | random           | lfu             | all               |             0 |         4 |
|      21.2500 |      9.4967 | most_recently_added  | random           | lru             | all               |             0 |         4 |
|      21.2500 |      9.4967 | most_recently_used   | random           | lru             | all               |             0 |         4 |
|      20.5000 |      8.5586 | most_recently_used   | random           | lru             | all               |             4 |         4 |
|      20.3333 |      5.2493 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         3 |
|      20.3333 |      2.0548 | most_recently_used   | dijkstra         | lru             | all               |             2 |         3 |
|      20.3333 |      2.0548 | most_frequently_used | dijkstra         | lru             | all               |             2 |         3 |
|      20.2500 |      7.9804 | most_frequently_used | bfs              | fifo            | all               |             4 |         4 |
|      20.2500 |      7.9804 | most_recently_used   | bfs              | fifo            | all               |             4 |         4 |
|      20.0000 |      8.6023 | most_frequently_used | random           | fifo            | all               |             8 |         3 |
|      19.7500 |      2.4875 | most_recently_used   | bfs              | random          | all               |             8 |         4 |
|      19.5000 |      3.9051 | most_recently_added  | bfs              | fifo            | all               |             2 |         4 |
|      19.0000 |      4.0825 | most_recently_used   | random           | fifo            | all               |             4 |         3 |
|      19.0000 |      4.0825 | most_frequently_used | random           | fifo            | all               |             4 |         3 |
|      18.5000 |      5.6789 | most_recently_added  | bfs              | lru             | all               |             2 |         4 |
|      18.2500 |      2.5860 | most_recently_added  | dijkstra         | random          | all               |             4 |         4 |
|      18.2500 |      5.5396 | most_recently_added  | dijkstra         | random          | all               |             2 |         4 |
|      18.2500 |      5.5846 | most_frequently_used | random           | random          | all               |             2 |         4 |
|      18.0000 |      3.0000 | most_recently_added  | random           | fifo            | all               |             4 |         4 |
|      18.0000 |     14.0535 | most_recently_used   | random           | lfu             | all               |             2 |         4 |
|      18.0000 |      8.6410 | most_recently_used   | random           | random          | all               |             8 |         3 |
|      17.7500 |      8.8424 | most_recently_added  | random           | random          | all               |             2 |         4 |
|      17.6667 |      2.8674 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         3 |
|      17.5000 |      4.3875 | most_frequently_used | bfs              | random          | all               |             4 |         4 |
|      17.5000 |      4.3875 | most_recently_used   | bfs              | random          | all               |             4 |         4 |
|      17.2500 |      6.1390 | most_recently_added  | dijkstra         | lru             | all               |             2 |         4 |
|      16.6667 |      9.8432 | most_recently_used   | random           | fifo            | all               |             2 |         3 |
|      16.6667 |      9.8432 | most_frequently_used | random           | fifo            | all               |             2 |         3 |
|      16.6667 |      6.2361 | most_frequently_used | random           | lru             | all               |             4 |         3 |
|      16.5000 |      5.1720 | most_frequently_used | bfs              | fifo            | all               |             2 |         4 |
|      16.5000 |      5.1720 | most_recently_used   | bfs              | fifo            | all               |             2 |         4 |
|      16.2500 |      3.5620 | most_recently_used   | bfs              | random          | all               |             2 |         4 |
|      16.2500 |      4.3229 | most_recently_added  | random           | random          | all               |             4 |         4 |
|      16.2500 |      3.5620 | most_frequently_used | bfs              | random          | all               |             2 |         4 |
|      16.0000 |      5.8878 | most_recently_used   | dijkstra         | lru             | all               |             0 |         3 |
|      16.0000 |      5.8878 | most_recently_added  | bfs              | lru             | all               |             0 |         3 |
|      16.0000 |      5.8878 | most_recently_used   | bfs              | lfu             | all               |             0 |         3 |
|      16.0000 |      5.8878 | most_frequently_used | dijkstra         | lru             | all               |             0 |         3 |
|      15.6667 |      3.8586 | most_recently_used   | random           | random          | all               |             2 |         3 |
|      15.5000 |      2.8723 | most_frequently_used | bfs              | lru             | all               |             2 |         4 |
|      15.5000 |      2.8723 | most_recently_used   | bfs              | lru             | all               |             2 |         4 |
|      15.3333 |     15.3261 | most_frequently_used | random           | lfu             | all               |             2 |         3 |
|      15.2500 |      9.2837 | most_recently_used   | dijkstra         | random          | all               |             2 |         4 |
|      15.2500 |      9.2837 | most_frequently_used | dijkstra         | random          | all               |             2 |         4 |
|      15.0000 |      4.9497 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         4 |
|      15.0000 |      4.9497 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         4 |
|      14.5000 |      2.2913 | most_recently_used   | dijkstra         | random          | all               |             4 |         4 |
|      14.5000 |      2.2913 | most_frequently_used | dijkstra         | random          | all               |             4 |         4 |
|      13.7500 |      6.4177 | most_frequently_used | bfs              | lfu             | all               |             0 |         4 |
|      13.7500 |      6.4177 | most_recently_added  | dijkstra         | lru             | all               |             0 |         4 |
|      13.7500 |      6.4177 | most_recently_used   | bfs              | lru             | all               |             0 |         4 |
|      13.7500 |      6.4177 | most_recently_added  | bfs              | lfu             | all               |             0 |         4 |
|      13.7500 |      6.4177 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         4 |
|      13.7500 |      1.7854 | most_recently_added  | bfs              | random          | all               |             2 |         4 |
|      13.7500 |      6.4177 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         4 |
|      13.7500 |      6.4177 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         4 |
|      13.7500 |      6.4177 | most_frequently_used | bfs              | lru             | all               |             0 |         4 |
|      12.0000 |      0.8165 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         3 |
|      11.7500 |      0.8292 | most_frequently_used | dijkstra         | random          | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_used   | bfs              | random          | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_used   | dijkstra         | random          | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_frequently_used | bfs              | random          | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_added  | dijkstra         | random          | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_added  | bfs              | random          | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_added  | bfs              | fifo            | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_recently_used   | bfs              | fifo            | all               |             0 |         4 |
|      11.7500 |      0.8292 | most_frequently_used | bfs              | fifo            | all               |             0 |         4 |
|      11.2500 |      2.9475 | most_recently_added  | random           | fifo            | all               |             2 |         4 |
|       9.0000 |      4.8477 | most_recently_added  | random           | lfu             | all               |             2 |         4 |
|       8.7500 |      4.3229 | most_recently_added  | random           | lru             | all               |             2 |         4 |
|       8.2500 |      3.0311 | most_recently_added  | random           | fifo            | all               |             0 |         4 |
|       8.2500 |      3.0311 | most_recently_added  | random           | random          | all               |             0 |         4 |
|       8.2500 |      3.0311 | most_frequently_used | random           | random          | all               |             0 |         4 |
|       8.0000 |      3.6742 | most_recently_used   | random           | lru             | all               |             2 |         4 |
|       7.6667 |      3.2998 | most_recently_used   | random           | fifo            | all               |             0 |         3 |
|       7.6667 |      3.2998 | most_frequently_used | random           | fifo            | all               |             0 |         3 |
|       7.6667 |      3.2998 | most_recently_used   | random           | random          | all               |             0 |         3 |
|       7.3333 |      4.0277 | most_frequently_used | random           | lru             | all               |             2 |         3 |

## Memory Size 0

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|      24.6667 |      8.5765 | most_frequently_used | random           | lfu             | all               |         3 |
|      24.6667 |      8.5765 | most_frequently_used | random           | lru             | all               |         3 |
|      21.2500 |      9.4967 | most_recently_added  | random           | lfu             | all               |         4 |
|      21.2500 |      9.4967 | most_recently_added  | random           | lru             | all               |         4 |
|      21.2500 |      9.4967 | most_recently_used   | random           | lru             | all               |         4 |
|      21.2500 |      9.4967 | most_recently_used   | random           | lfu             | all               |         4 |
|      16.0000 |      5.8878 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|      16.0000 |      5.8878 | most_recently_added  | bfs              | lru             | all               |         3 |
|      16.0000 |      5.8878 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|      16.0000 |      5.8878 | most_recently_used   | bfs              | lfu             | all               |         3 |
|      13.7500 |      6.4177 | most_frequently_used | bfs              | lru             | all               |         4 |
|      13.7500 |      6.4177 | most_frequently_used | bfs              | lfu             | all               |         4 |
|      13.7500 |      6.4177 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|      13.7500 |      6.4177 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|      13.7500 |      6.4177 | most_recently_used   | bfs              | lru             | all               |         4 |
|      13.7500 |      6.4177 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|      13.7500 |      6.4177 | most_recently_added  | bfs              | lfu             | all               |         4 |
|      13.7500 |      6.4177 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|      12.0000 |      0.8165 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|      11.7500 |      0.8292 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      11.7500 |      0.8292 | most_frequently_used | bfs              | random          | all               |         4 |
|      11.7500 |      0.8292 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      11.7500 |      0.8292 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      11.7500 |      0.8292 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|      11.7500 |      0.8292 | most_frequently_used | dijkstra         | random          | all               |         4 |
|      11.7500 |      0.8292 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|      11.7500 |      0.8292 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      11.7500 |      0.8292 | most_recently_added  | bfs              | random          | all               |         4 |
|      11.7500 |      0.8292 | most_recently_used   | bfs              | random          | all               |         4 |
|      11.7500 |      0.8292 | most_recently_used   | bfs              | fifo            | all               |         4 |
|       8.2500 |      3.0311 | most_recently_added  | random           | fifo            | all               |         4 |
|       8.2500 |      3.0311 | most_frequently_used | random           | random          | all               |         4 |
|       8.2500 |      3.0311 | most_recently_added  | random           | random          | all               |         4 |
|       7.6667 |      3.2998 | most_frequently_used | random           | fifo            | all               |         3 |
|       7.6667 |      3.2998 | most_recently_used   | random           | fifo            | all               |         3 |
|       7.6667 |      3.2998 | most_recently_used   | random           | random          | all               |         3 |

## Memory Size 2

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|      38.0000 |     15.6045 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|      37.5000 |     20.1680 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|      33.5000 |     18.0901 | most_frequently_used | bfs              | lfu             | all               |         4 |
|      28.2500 |     14.9562 | most_recently_added  | bfs              | lfu             | all               |         4 |
|      26.6667 |     15.7973 | most_recently_used   | bfs              | lfu             | all               |         3 |
|      25.3333 |     18.9268 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|      20.3333 |      2.0548 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|      20.3333 |      2.0548 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|      19.5000 |      3.9051 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      18.5000 |      5.6789 | most_recently_added  | bfs              | lru             | all               |         4 |
|      18.2500 |      5.5396 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      18.2500 |      5.5846 | most_frequently_used | random           | random          | all               |         4 |
|      18.0000 |     14.0535 | most_recently_used   | random           | lfu             | all               |         4 |
|      17.7500 |      8.8424 | most_recently_added  | random           | random          | all               |         4 |
|      17.6667 |      2.8674 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|      17.2500 |      6.1390 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|      16.6667 |      9.8432 | most_recently_used   | random           | fifo            | all               |         3 |
|      16.6667 |      9.8432 | most_frequently_used | random           | fifo            | all               |         3 |
|      16.5000 |      5.1720 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      16.5000 |      5.1720 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      16.2500 |      3.5620 | most_recently_used   | bfs              | random          | all               |         4 |
|      16.2500 |      3.5620 | most_frequently_used | bfs              | random          | all               |         4 |
|      15.6667 |      3.8586 | most_recently_used   | random           | random          | all               |         3 |
|      15.5000 |      2.8723 | most_frequently_used | bfs              | lru             | all               |         4 |
|      15.5000 |      2.8723 | most_recently_used   | bfs              | lru             | all               |         4 |
|      15.3333 |     15.3261 | most_frequently_used | random           | lfu             | all               |         3 |
|      15.2500 |      9.2837 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      15.2500 |      9.2837 | most_frequently_used | dijkstra         | random          | all               |         4 |
|      15.0000 |      4.9497 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|      15.0000 |      4.9497 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|      13.7500 |      1.7854 | most_recently_added  | bfs              | random          | all               |         4 |
|      11.2500 |      2.9475 | most_recently_added  | random           | fifo            | all               |         4 |
|       9.0000 |      4.8477 | most_recently_added  | random           | lfu             | all               |         4 |
|       8.7500 |      4.3229 | most_recently_added  | random           | lru             | all               |         4 |
|       8.0000 |      3.6742 | most_recently_used   | random           | lru             | all               |         4 |
|       7.3333 |      4.0277 | most_frequently_used | random           | lru             | all               |         3 |

## Memory Size 4

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|      62.6667 |     16.7796 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|      47.0000 |      6.9642 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|      45.5000 |     22.2879 | most_recently_added  | bfs              | lfu             | all               |         4 |
|      40.7500 |     26.1474 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|      40.0000 |      9.0921 | most_frequently_used | random           | lfu             | all               |         3 |
|      39.5000 |      8.5294 | most_recently_used   | random           | lfu             | all               |         4 |
|      34.2500 |      6.1796 | most_recently_added  | random           | lfu             | all               |         4 |
|      34.0000 |      3.6742 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      31.3333 |     11.1156 | most_recently_used   | bfs              | lfu             | all               |         3 |
|      30.7500 |      9.6792 | most_frequently_used | bfs              | lfu             | all               |         4 |
|      26.7500 |      9.1207 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|      26.7500 |      9.1207 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|      24.0000 |      6.7454 | most_frequently_used | bfs              | lru             | all               |         4 |
|      24.0000 |      6.7454 | most_recently_used   | bfs              | lru             | all               |         4 |
|      23.3333 |      5.2493 | most_recently_used   | random           | random          | all               |         3 |
|      23.2500 |      1.9203 | most_recently_added  | bfs              | lru             | all               |         4 |
|      23.0000 |      1.8708 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|      22.6667 |      6.5997 | most_frequently_used | dijkstra         | lru             | all               |         3 |
|      22.6667 |      6.5997 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|      22.5000 |      6.0208 | most_frequently_used | random           | random          | all               |         4 |
|      21.7500 |      5.5396 | most_recently_added  | bfs              | random          | all               |         4 |
|      21.5000 |      6.8007 | most_recently_added  | random           | lru             | all               |         4 |
|      20.5000 |      8.5586 | most_recently_used   | random           | lru             | all               |         4 |
|      20.3333 |      5.2493 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|      20.2500 |      7.9804 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      20.2500 |      7.9804 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      19.0000 |      4.0825 | most_recently_used   | random           | fifo            | all               |         3 |
|      19.0000 |      4.0825 | most_frequently_used | random           | fifo            | all               |         3 |
|      18.2500 |      2.5860 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      18.0000 |      3.0000 | most_recently_added  | random           | fifo            | all               |         4 |
|      17.5000 |      4.3875 | most_frequently_used | bfs              | random          | all               |         4 |
|      17.5000 |      4.3875 | most_recently_used   | bfs              | random          | all               |         4 |
|      16.6667 |      6.2361 | most_frequently_used | random           | lru             | all               |         3 |
|      16.2500 |      4.3229 | most_recently_added  | random           | random          | all               |         4 |
|      14.5000 |      2.2913 | most_frequently_used | dijkstra         | random          | all               |         4 |
|      14.5000 |      2.2913 | most_recently_used   | dijkstra         | random          | all               |         4 |

## Memory Size 8

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|      79.7500 |     21.6838 | most_frequently_used | bfs              | lfu             | all               |         4 |
|      79.6667 |     22.6912 | most_recently_used   | bfs              | lfu             | all               |         3 |
|      71.6667 |     25.6168 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|      69.2500 |     23.8681 | most_recently_added  | random           | lfu             | all               |         4 |
|      62.5000 |     27.6812 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|      61.2500 |     23.2634 | most_recently_used   | random           | lfu             | all               |         4 |
|      60.5000 |      4.1533 | most_recently_added  | bfs              | lfu             | all               |         4 |
|      57.6667 |     14.5220 | most_frequently_used | random           | lfu             | all               |         3 |
|      48.5000 |     16.8597 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|      43.7500 |     13.3112 | most_recently_used   | bfs              | lru             | all               |         4 |
|      43.7500 |     13.3112 | most_frequently_used | bfs              | lru             | all               |         4 |
|      41.7500 |     14.6693 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|      40.3333 |     12.2837 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|      37.2500 |      9.7308 | most_recently_added  | bfs              | lru             | all               |         4 |
|      36.0000 |      6.5955 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|      31.7500 |      7.5622 | most_recently_added  | random           | lru             | all               |         4 |
|      29.0000 |      9.1378 | most_frequently_used | dijkstra         | random          | all               |         4 |
|      28.0000 |      3.5355 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|      28.0000 |      3.5355 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|      27.5000 |      9.5525 | most_frequently_used | bfs              | random          | all               |         4 |
|      27.2500 |      4.7104 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      27.0000 |     11.4018 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      26.0000 |      4.9497 | most_recently_added  | random           | fifo            | all               |         4 |
|      25.2500 |      2.9475 | most_recently_used   | random           | lru             | all               |         4 |
|      24.7500 |      5.6734 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      24.7500 |      5.6734 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      24.5000 |     11.4127 | most_frequently_used | random           | random          | all               |         4 |
|      24.3333 |      4.4969 | most_frequently_used | random           | lru             | all               |         3 |
|      23.2500 |      4.7104 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      22.6667 |      3.0912 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|      22.2500 |      8.4076 | most_recently_added  | random           | random          | all               |         4 |
|      22.2500 |     11.5190 | most_recently_added  | bfs              | random          | all               |         4 |
|      21.6667 |      8.7305 | most_recently_used   | random           | fifo            | all               |         3 |
|      20.0000 |      8.6023 | most_frequently_used | random           | fifo            | all               |         3 |
|      19.7500 |      2.4875 | most_recently_used   | bfs              | random          | all               |         4 |
|      18.0000 |      8.6410 | most_recently_used   | random           | random          | all               |         3 |

## Memory Size 16

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     134.2500 |     31.2360 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     121.3333 |     20.8859 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     114.2500 |     57.1724 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     112.0000 |     22.7486 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     110.2500 |     27.2615 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     108.2500 |     34.9025 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|      76.5000 |     19.0853 | most_frequently_used | bfs              | lru             | all               |         4 |
|      75.7500 |     14.5667 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|      71.7500 |     21.9360 | most_recently_used   | bfs              | lru             | all               |         4 |
|      66.7500 |     18.9522 | most_recently_added  | random           | lfu             | all               |         4 |
|      64.6667 |      7.1336 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|      64.2500 |      9.2837 | most_recently_added  | bfs              | lru             | all               |         4 |
|      61.7500 |     11.7978 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|      51.5000 |     10.5000 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|      50.7500 |     20.6079 | most_recently_used   | random           | lfu             | all               |         4 |
|      50.0000 |     26.9444 | most_frequently_used | random           | lfu             | all               |         3 |
|      49.7500 |      9.4439 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      49.5000 |     13.0480 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|      47.3333 |      2.3570 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|      47.2500 |     13.9530 | most_frequently_used | bfs              | random          | all               |         4 |
|      45.2500 |     17.4123 | most_recently_used   | bfs              | random          | all               |         4 |
|      43.7500 |     12.8525 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      43.0000 |      8.8600 | most_recently_added  | bfs              | random          | all               |         4 |
|      42.5000 |     12.5399 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      39.0000 |     14.1244 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      37.7500 |      3.7666 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      36.7500 |      5.4486 | most_frequently_used | dijkstra         | random          | all               |         4 |
|      36.5000 |      4.7170 | most_recently_used   | random           | lru             | all               |         4 |
|      33.0000 |     16.3095 | most_recently_added  | random           | lru             | all               |         4 |
|      32.0000 |      5.3385 | most_recently_added  | random           | random          | all               |         4 |
|      29.5000 |      9.5263 | most_frequently_used | random           | random          | all               |         4 |
|      29.0000 |      6.8191 | most_recently_added  | random           | fifo            | all               |         4 |
|      28.0000 |      4.5461 | most_recently_used   | random           | random          | all               |         3 |
|      27.3333 |      9.4281 | most_frequently_used | random           | fifo            | all               |         3 |
|      27.0000 |      2.8284 | most_frequently_used | random           | lru             | all               |         3 |
|      21.6667 |      7.0396 | most_recently_used   | random           | fifo            | all               |         3 |

## Memory Size 32

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     204.2500 |     36.7789 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     200.5000 |     65.3816 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     185.7500 |     39.3915 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     176.0000 |     30.1579 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     176.0000 |     27.7969 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     172.5000 |     40.5247 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     146.2500 |     25.9362 | most_recently_used   | bfs              | lru             | all               |         4 |
|     143.0000 |     16.7183 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     141.0000 |     37.5433 | most_recently_added  | bfs              | lru             | all               |         4 |
|     127.2500 |     20.1789 | most_frequently_used | bfs              | lru             | all               |         4 |
|     123.0000 |     24.3413 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     122.3333 |     16.1107 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|      92.2500 |     18.7667 | most_recently_used   | bfs              | fifo            | all               |         4 |
|      82.5000 |     13.6107 | most_frequently_used | bfs              | fifo            | all               |         4 |
|      81.5000 |     11.5217 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|      81.0000 |      9.3541 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|      79.0000 |     24.6678 | most_recently_used   | random           | lfu             | all               |         4 |
|      72.0000 |      6.0415 | most_recently_added  | bfs              | random          | all               |         4 |
|      70.0000 |     21.0832 | most_recently_added  | random           | lfu             | all               |         4 |
|      70.0000 |     14.5144 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|      66.2500 |     15.7698 | most_recently_used   | random           | lru             | all               |         4 |
|      63.0000 |      7.4498 | most_frequently_used | bfs              | random          | all               |         4 |
|      63.0000 |      9.4340 | most_frequently_used | dijkstra         | random          | all               |         4 |
|      62.0000 |      6.2048 | most_recently_added  | bfs              | fifo            | all               |         4 |
|      61.0000 |     12.6293 | most_recently_used   | bfs              | random          | all               |         4 |
|      59.6667 |     16.4992 | most_frequently_used | random           | lfu             | all               |         3 |
|      56.0000 |      5.2440 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      53.2500 |     14.3592 | most_recently_added  | random           | lru             | all               |         4 |
|      52.2500 |     14.5151 | most_recently_added  | dijkstra         | random          | all               |         4 |
|      46.6667 |      9.7411 | most_recently_used   | random           | random          | all               |         3 |
|      43.0000 |     10.6145 | most_recently_used   | random           | fifo            | all               |         3 |
|      39.0000 |      4.5277 | most_recently_added  | random           | random          | all               |         4 |
|      38.0000 |     10.4163 | most_recently_added  | random           | fifo            | all               |         4 |
|      36.6667 |      0.9428 | most_frequently_used | random           | lru             | all               |         3 |
|      30.0000 |     11.5542 | most_frequently_used | random           | random          | all               |         4 |
|      24.6667 |      5.7927 | most_frequently_used | random           | fifo            | all               |         3 |

## Memory Size 64

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     322.3333 |     64.5618 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     320.7500 |     60.4044 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     300.7500 |     53.2183 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     298.7500 |     70.3611 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     293.5000 |     40.8993 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     272.2500 |     40.6040 | most_recently_added  | bfs              | lru             | all               |         4 |
|     270.0000 |     66.6146 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     257.0000 |     35.2420 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     247.7500 |     37.8178 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     233.2500 |     73.4894 | most_frequently_used | bfs              | lru             | all               |         4 |
|     232.6667 |     43.3154 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|     231.0000 |     35.1923 | most_recently_used   | bfs              | lru             | all               |         4 |
|     139.5000 |     24.5917 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     132.7500 |     37.2986 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     130.3333 |     26.1958 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|     124.5000 |     16.1012 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     121.7500 |     26.3569 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     120.5000 |     31.3169 | most_recently_used   | bfs              | random          | all               |         4 |
|     118.7500 |     39.8332 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     117.2500 |     28.7609 | most_frequently_used | bfs              | random          | all               |         4 |
|     116.7500 |     16.7984 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     111.0000 |     30.4549 | most_recently_added  | bfs              | random          | all               |         4 |
|     104.5000 |     18.7150 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     104.5000 |     44.2860 | most_recently_used   | random           | lfu             | all               |         4 |
|      94.0000 |     32.7719 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      94.0000 |     15.7321 | most_recently_added  | random           | lfu             | all               |         4 |
|      72.7500 |     13.8992 | most_recently_used   | random           | lru             | all               |         4 |
|      70.3333 |     35.7243 | most_frequently_used | random           | lfu             | all               |         3 |
|      67.2500 |     16.5435 | most_recently_added  | random           | lru             | all               |         4 |
|      63.7500 |     14.2017 | most_recently_added  | random           | random          | all               |         4 |
|      60.6667 |      3.0912 | most_recently_used   | random           | random          | all               |         3 |
|      59.5000 |      6.3443 | most_frequently_used | random           | random          | all               |         4 |
|      53.0000 |      9.4163 | most_frequently_used | random           | lru             | all               |         3 |
|      52.6667 |     16.7398 | most_frequently_used | random           | fifo            | all               |         3 |
|      51.7500 |      8.5550 | most_recently_added  | random           | fifo            | all               |         4 |
|      27.3333 |     13.3000 | most_recently_used   | random           | fifo            | all               |         3 |

## Memory Size 128

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     403.2500 |     36.4649 | most_recently_used   | bfs              | lru             | all               |         4 |
|     363.7500 |    122.0172 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     356.7500 |     42.0974 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     353.3333 |     26.4113 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|     343.5000 |     85.8443 | most_frequently_used | bfs              | lru             | all               |         4 |
|     340.0000 |    107.8819 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     335.7500 |    102.9038 | most_recently_added  | bfs              | lru             | all               |         4 |
|     318.2500 |     89.6755 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     310.0000 |     94.9289 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     268.2500 |     94.5790 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     267.5000 |     89.7455 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     259.6667 |     33.4797 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     224.5000 |     32.1908 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     223.2500 |     28.4726 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     222.2500 |     28.2168 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     214.0000 |     14.4453 | most_recently_added  | dijkstra         | fifo            | all               |         3 |
|     209.5000 |     48.2157 | most_frequently_used | bfs              | random          | all               |         4 |
|     208.7500 |     51.2902 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     201.2500 |     43.6656 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     199.2500 |     44.1439 | most_recently_used   | bfs              | random          | all               |         4 |
|     199.0000 |     46.6744 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     192.0000 |     55.4076 | most_recently_added  | bfs              | random          | all               |         4 |
|     182.5000 |     47.0346 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     176.2500 |     41.5955 | most_recently_used   | dijkstra         | random          | all               |         4 |
|      99.2500 |     38.9832 | most_recently_used   | random           | lru             | all               |         4 |
|      95.0000 |     39.5053 | most_frequently_used | random           | lru             | all               |         3 |
|      90.3333 |     28.1109 | most_frequently_used | random           | lfu             | all               |         3 |
|      82.5000 |     37.3464 | most_recently_added  | random           | lru             | all               |         4 |
|      77.7500 |     20.3270 | most_recently_used   | random           | lfu             | all               |         4 |
|      70.5000 |      7.0887 | most_frequently_used | random           | random          | all               |         4 |
|      67.7500 |     30.3016 | most_recently_added  | random           | lfu             | all               |         4 |
|      66.6667 |     14.2906 | most_recently_added  | random           | random          | all               |         3 |
|      65.2500 |     21.9929 | most_recently_added  | random           | fifo            | all               |         4 |
|      58.7500 |     18.2808 | most_recently_used   | random           | random          | all               |         4 |
|      55.3333 |     15.9652 | most_recently_used   | random           | fifo            | all               |         3 |
|      54.6667 |     19.6016 | most_frequently_used | random           | fifo            | all               |         3 |

## Memory Size 256

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     438.7500 |     62.2590 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     437.5000 |     43.8264 | most_recently_used   | bfs              | lru             | all               |         4 |
|     401.0000 |     82.3681 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     388.5000 |     73.0804 | most_recently_added  | bfs              | lru             | all               |         4 |
|     386.5000 |     80.9336 | most_frequently_used | bfs              | lru             | all               |         4 |
|     382.0000 |     52.3323 | most_recently_added  | bfs              | lfu             | all               |         3 |
|     366.2500 |     35.6467 | most_recently_used   | bfs              | random          | all               |         4 |
|     360.7500 |     51.9345 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     354.7500 |     73.3361 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     349.5000 |     11.8427 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     341.5000 |     44.0539 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     333.0000 |     70.7001 | most_frequently_used | bfs              | random          | all               |         4 |
|     330.7500 |     40.2267 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     327.6667 |     99.1206 | most_recently_added  | dijkstra         | lru             | all               |         3 |
|     326.5000 |     84.4349 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     318.5000 |     47.4368 | most_recently_added  | bfs              | random          | all               |         4 |
|     312.0000 |     75.7331 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     308.0000 |     48.6672 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     305.6667 |      9.8432 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|     304.3333 |      7.5865 | most_recently_used   | dijkstra         | lfu             | all               |         3 |
|     298.5000 |     52.9221 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     298.2500 |     61.3244 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     292.7500 |     56.1711 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     279.3333 |      6.5490 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     101.3333 |     28.8020 | most_frequently_used | random           | lfu             | all               |         3 |
|     101.3333 |     28.8020 | most_frequently_used | random           | lru             | all               |         3 |
|      93.5000 |     23.2648 | most_frequently_used | random           | random          | all               |         4 |
|      90.7500 |     14.4114 | most_recently_added  | random           | lru             | all               |         4 |
|      89.0000 |     20.8327 | most_recently_used   | random           | fifo            | all               |         3 |
|      85.0000 |     23.1625 | most_recently_used   | random           | lru             | all               |         4 |
|      81.5000 |     14.6714 | most_recently_added  | random           | lfu             | all               |         4 |
|      81.3333 |     13.4247 | most_frequently_used | random           | fifo            | all               |         3 |
|      77.0000 |     14.2361 | most_recently_added  | random           | random          | all               |         3 |
|      72.0000 |     11.1131 | most_recently_used   | random           | lfu             | all               |         4 |
|      69.2500 |      5.8041 | most_recently_used   | random           | random          | all               |         4 |
|      68.0000 |     11.2916 | most_recently_added  | random           | fifo            | all               |         4 |

## Memory Size 512

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     450.7500 |     54.5774 | most_recently_used   | bfs              | lru             | all               |         4 |
|     449.5000 |     55.2336 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     444.5000 |     52.6427 | most_recently_used   | bfs              | random          | all               |         4 |
|     440.0000 |     52.3211 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     422.7500 |     53.0206 | most_frequently_used | bfs              | lru             | all               |         4 |
|     420.7500 |     54.5728 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     418.5000 |     51.9447 | most_frequently_used | bfs              | random          | all               |         4 |
|     415.7500 |     54.6689 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     394.0000 |     71.8123 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     394.0000 |     72.3015 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     393.0000 |     59.6210 | most_recently_added  | bfs              | lfu             | all               |         3 |
|     390.0000 |     53.2870 | most_recently_added  | bfs              | random          | all               |         4 |
|     388.0000 |     67.7237 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     387.5000 |    100.1636 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     385.7500 |     53.1384 | most_recently_added  | bfs              | lru             | all               |         4 |
|     385.7500 |     55.7107 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     385.5000 |    100.4652 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     373.0000 |     71.6147 | most_recently_added  | dijkstra         | lru             | all               |         3 |
|     368.0000 |     71.4108 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     366.5000 |     68.0790 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     338.6667 |     49.7750 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     331.6667 |     11.7284 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|     331.0000 |     12.5698 | most_recently_used   | dijkstra         | lfu             | all               |         3 |
|     329.0000 |     48.8330 | most_frequently_used | dijkstra         | random          | all               |         3 |
|      96.0000 |     23.8432 | most_frequently_used | random           | random          | all               |         4 |
|      92.0000 |     25.9615 | most_frequently_used | random           | fifo            | all               |         3 |
|      91.3333 |     25.9015 | most_frequently_used | random           | lfu             | all               |         3 |
|      91.3333 |     25.9015 | most_frequently_used | random           | lru             | all               |         3 |
|      87.5000 |     14.3962 | most_recently_added  | random           | fifo            | all               |         4 |
|      84.7500 |     11.6485 | most_recently_added  | random           | lfu             | all               |         4 |
|      83.2500 |      9.2026 | most_recently_added  | random           | lru             | all               |         4 |
|      81.0000 |      8.2865 | most_recently_added  | random           | random          | all               |         3 |
|      79.6667 |     15.9652 | most_recently_used   | random           | lru             | all               |         3 |
|      74.0000 |     13.1403 | most_recently_used   | random           | fifo            | all               |         3 |
|      73.0000 |     16.0312 | most_recently_used   | random           | lfu             | all               |         4 |
|      72.5000 |     17.3566 | most_recently_used   | random           | random          | all               |         4 |

## Memory Size 1024

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     449.7500 |     52.3038 | most_recently_used   | bfs              | random          | all               |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | lru             | all               |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     449.7500 |     52.3038 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | random          | all               |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | lru             | all               |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     419.7500 |     52.8459 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     396.0000 |     73.4132 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     396.0000 |     73.4132 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     396.0000 |     73.4132 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     394.2500 |    101.3765 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     394.2500 |    101.3765 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     394.0000 |     59.2340 | most_recently_added  | bfs              | lfu             | all               |         3 |
|     387.2500 |     52.6136 | most_recently_added  | bfs              | lru             | all               |         4 |
|     387.2500 |     52.6136 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     387.2500 |     52.6136 | most_recently_added  | bfs              | random          | all               |         4 |
|     376.6667 |     75.4380 | most_recently_added  | dijkstra         | lru             | all               |         3 |
|     371.5000 |     71.8836 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     371.5000 |     71.8836 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     339.0000 |     51.6204 | most_frequently_used | dijkstra         | lfu             | all               |         3 |
|     339.0000 |     51.6204 | most_frequently_used | dijkstra         | random          | all               |         3 |
|     336.0000 |     11.4310 | most_recently_used   | dijkstra         | lru             | all               |         3 |
|     336.0000 |     11.4310 | most_recently_used   | dijkstra         | lfu             | all               |         3 |
|      96.2500 |     24.6513 | most_frequently_used | random           | fifo            | all               |         4 |
|      96.2500 |     24.6513 | most_frequently_used | random           | random          | all               |         4 |
|      88.6667 |     24.0878 | most_frequently_used | random           | lfu             | all               |         3 |
|      88.6667 |     24.0878 | most_frequently_used | random           | lru             | all               |         3 |
|      83.0000 |     20.6074 | most_recently_used   | random           | fifo            | all               |         3 |
|      83.0000 |     20.6074 | most_recently_used   | random           | lru             | all               |         3 |
|      81.7500 |      8.2576 | most_recently_added  | random           | lru             | all               |         4 |
|      81.7500 |      8.2576 | most_recently_added  | random           | lfu             | all               |         4 |
|      81.7500 |      8.2576 | most_recently_added  | random           | fifo            | all               |         4 |
|      79.3333 |      8.2192 | most_recently_added  | random           | random          | all               |         3 |
|      75.7500 |     21.8217 | most_recently_used   | random           | lfu             | all               |         4 |
|      75.7500 |     21.8217 | most_recently_used   | random           | random          | all               |         4 |

