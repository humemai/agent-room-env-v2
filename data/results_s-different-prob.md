# Results for s-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|     924.8000 |     24.4491 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|     924.8000 |     24.4491 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|     917.4000 |     12.1754 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|     917.4000 |     12.1754 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|     913.2500 |     35.1879 | most_recently_added  | bfs              | fifo            | all               |           256 |         4 |
|     913.2500 |     35.1879 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         4 |
|     910.0000 |     42.7036 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|     906.2500 |      5.3092 | most_recently_added  | bfs              | fifo            | all               |           512 |         4 |
|     906.2500 |      5.3092 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         4 |
|     903.7500 |      1.7854 | most_recently_added  | bfs              | random          | all               |          1024 |         4 |
|     903.7500 |      1.7854 | most_recently_added  | dijkstra         | random          | all               |          1024 |         4 |
|     903.7500 |      1.7854 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         4 |
|     903.7500 |      1.7854 | most_recently_added  | bfs              | fifo            | all               |          1024 |         4 |
|     903.0000 |      1.7321 | most_recently_added  | bfs              | random          | all               |           512 |         4 |
|     903.0000 |      1.7321 | most_recently_added  | dijkstra         | random          | all               |           512 |         4 |
|     902.4000 |     29.8704 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|     902.0000 |     53.5574 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|     902.0000 |     53.5574 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|     900.4000 |     41.5047 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|     899.7500 |     41.8830 | most_recently_used   | bfs              | lru             | all               |            32 |         4 |
|     899.2000 |     18.2910 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|     897.8000 |     20.5563 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|     897.8000 |     20.5563 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|     897.6000 |     23.8713 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|     897.6000 |     23.8713 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|     893.6000 |     20.3627 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|     893.6000 |     20.3627 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|     893.6000 |     20.3627 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|     893.6000 |     20.3627 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|     893.0000 |     39.9650 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|     890.0000 |     44.7158 | most_recently_used   | bfs              | fifo            | all               |           256 |         4 |
|     890.0000 |     44.7158 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         4 |
|     889.2000 |     55.9836 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|     889.2000 |     55.9836 | most_recently_used   | bfs              | random          | all               |          1024 |         5 |
|     889.2000 |     55.9836 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|     885.2500 |     25.4693 | most_recently_used   | bfs              | lru             | all               |            16 |         4 |
|     884.2500 |     54.0619 | most_recently_used   | bfs              | lru             | all               |           256 |         4 |
|     884.2500 |     54.0619 | most_recently_used   | dijkstra         | lru             | all               |           256 |         4 |
|     883.8000 |     62.6431 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|     883.8000 |     62.6431 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|     881.5000 |     60.1768 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         4 |
|     881.5000 |     60.1768 | most_recently_used   | dijkstra         | random          | all               |          1024 |         4 |
|     881.5000 |     60.1768 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         4 |
|     881.5000 |     60.1768 | most_recently_used   | bfs              | lru             | all               |          1024 |         4 |
|     881.5000 |     60.1768 | most_recently_used   | bfs              | fifo            | all               |          1024 |         4 |
|     881.0000 |     35.3610 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|     880.4000 |     33.5476 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|     880.2000 |     47.6294 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|     880.2000 |     47.6294 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|     879.8000 |     59.4454 | most_recently_used   | bfs              | random          | all               |           512 |         5 |
|     879.5000 |     50.3115 | most_recently_added  | dijkstra         | random          | all               |           256 |         4 |
|     879.5000 |     50.3115 | most_recently_added  | bfs              | random          | all               |           256 |         4 |
|     875.6000 |     36.6911 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|     875.0000 |     53.3713 | most_recently_used   | dijkstra         | lru             | all               |           128 |         4 |
|     875.0000 |     53.3713 | most_recently_used   | bfs              | lru             | all               |           128 |         4 |
|     873.7500 |     49.2310 | most_recently_used   | bfs              | fifo            | all               |           512 |         4 |
|     872.7500 |     48.7051 | most_recently_used   | dijkstra         | lru             | all               |           512 |         4 |
|     872.7500 |     48.7051 | most_recently_used   | bfs              | lru             | all               |           512 |         4 |
|     872.6000 |     44.2656 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|     871.2000 |     62.9425 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|     869.4000 |     42.0837 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|     869.4000 |     42.0837 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|     867.2500 |     60.2469 | most_recently_used   | dijkstra         | random          | all               |           512 |         4 |
|     866.4000 |     50.8157 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|     866.4000 |     50.8157 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|     865.6000 |     27.6810 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|     863.8000 |     66.9878 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|     861.4000 |     37.0600 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|     861.2000 |     60.0646 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|     860.7500 |     35.6467 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         4 |
|     860.7500 |     35.6467 | most_recently_used   | bfs              | fifo            | all               |           128 |         4 |
|     854.6667 |     42.1294 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         3 |
|     853.4000 |     61.2359 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|     853.2000 |     58.3863 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|     850.2500 |     46.7353 | most_recently_added  | bfs              | fifo            | all               |           128 |         4 |
|     850.2500 |     46.7353 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         4 |
|     843.0000 |     12.0167 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|     841.2500 |     12.8525 | most_recently_used   | bfs              | lru             | all               |            64 |         4 |
|     840.5000 |     54.6877 | most_recently_used   | dijkstra         | random          | all               |           128 |         4 |
|     840.5000 |     54.6877 | most_recently_used   | bfs              | random          | all               |           128 |         4 |
|     837.2000 |    101.4523 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|     836.0000 |     90.8460 | most_recently_added  | bfs              | fifo            | all               |            64 |         4 |
|     836.0000 |     90.8460 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         4 |
|     833.8000 |     48.2759 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|     830.7500 |     44.7570 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         4 |
|     830.7500 |     44.7570 | most_recently_used   | bfs              | fifo            | all               |            64 |         4 |
|     823.7500 |     71.9318 | most_recently_used   | bfs              | random          | all               |            64 |         4 |
|     823.7500 |     71.9318 | most_recently_used   | dijkstra         | random          | all               |            64 |         4 |
|     818.7500 |    104.1210 | most_recently_used   | dijkstra         | random          | all               |           256 |         4 |
|     818.7500 |    104.1210 | most_recently_used   | bfs              | random          | all               |           256 |         4 |
|     816.0000 |     65.3261 | most_recently_added  | dijkstra         | random          | all               |            64 |         4 |
|     811.2500 |     70.1654 | most_recently_added  | dijkstra         | random          | all               |            32 |         4 |
|     810.5000 |     41.2402 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         4 |
|     810.5000 |     41.2402 | most_frequently_used | bfs              | fifo            | all               |            32 |         4 |
|     809.5000 |     43.6492 | most_recently_added  | bfs              | fifo            | all               |            32 |         4 |
|     809.5000 |     43.6492 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         4 |
|     798.2500 |     21.0758 | most_recently_added  | bfs              | random          | all               |           128 |         4 |
|     798.2500 |     21.0758 | most_recently_added  | dijkstra         | random          | all               |           128 |         4 |
|     795.7500 |     62.5075 | most_recently_used   | bfs              | fifo            | all               |            32 |         4 |
|     795.7500 |     62.5075 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         4 |
|     793.5000 |     37.0978 | most_recently_added  | bfs              | random          | all               |            64 |         4 |
|     779.8000 |    168.8874 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|     777.5000 |     90.4226 | most_recently_used   | random           | lfu             | all               |           128 |         4 |
|     772.2000 |    116.4344 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|     765.0000 |     82.5803 | most_recently_added  | random           | lfu             | all               |           256 |         4 |
|     761.8000 |    127.9100 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|     761.8000 |    127.9100 | most_recently_added  | random           | random          | all               |          1024 |         5 |
|     760.0000 |     72.5913 | most_recently_added  | bfs              | random          | all               |            32 |         4 |
|     746.2000 |    117.0152 | most_recently_added  | random           | random          | all               |           512 |         5 |
|     745.8000 |    115.8402 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|     744.7500 |     81.7569 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         4 |
|     744.7500 |     81.7569 | most_frequently_used | bfs              | fifo            | all               |            64 |         4 |
|     738.0000 |    136.2112 | most_recently_added  | random           | lru             | all               |           256 |         4 |
|     736.8000 |    158.3078 | most_recently_used   | random           | random          | all               |            64 |         5 |
|     735.5000 |     49.9875 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         4 |
|     731.8000 |    123.0502 | most_recently_used   | random           | random          | all               |           128 |         5 |
|     730.8000 |    160.1454 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|     727.7500 |     46.1052 | most_recently_used   | bfs              | fifo            | all               |            16 |         4 |
|     725.4000 |    176.5362 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|     723.5000 |     54.4679 | most_recently_added  | bfs              | fifo            | all               |            16 |         4 |
|     718.5000 |    105.2461 | most_recently_added  | random           | lru             | all               |          1024 |         4 |
|     718.5000 |    105.2461 | most_recently_added  | random           | lfu             | all               |          1024 |         4 |
|     717.0000 |    135.9412 | most_recently_added  | random           | random          | all               |           256 |         5 |
|     714.0000 |     15.4110 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         4 |
|     714.0000 |    121.9475 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|     704.7500 |     32.9725 | most_frequently_used | bfs              | fifo            | all               |            16 |         4 |
|     697.2500 |    241.9663 | most_recently_used   | random           | lfu             | all               |           256 |         4 |
|     695.5000 |    135.2581 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         4 |
|     693.2500 |    114.6045 | most_recently_added  | random           | lru             | all               |            32 |         4 |
|     691.0000 |    100.6901 | most_recently_used   | random           | lfu             | all               |            32 |         4 |
|     685.7500 |    132.6148 | most_recently_added  | random           | lfu             | all               |            16 |         4 |
|     685.4000 |    132.3142 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|     683.2500 |     85.4704 | most_recently_added  | random           | lru             | all               |           512 |         4 |
|     683.2500 |     85.4704 | most_recently_added  | random           | lfu             | all               |           512 |         4 |
|     674.4000 |     64.3944 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|     670.0000 |    262.0389 | most_recently_used   | random           | random          | all               |           256 |         5 |
|     669.0000 |    100.1699 | most_recently_added  | random           | lru             | all               |            16 |         4 |
|     667.2000 |    141.6297 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|     665.5000 |     47.1937 | most_recently_used   | random           | lru             | all               |            16 |         4 |
|     664.7500 |     82.5087 | most_recently_added  | random           | lfu             | all               |            32 |         4 |
|     660.2500 |    278.1154 | most_recently_added  | random           | lru             | all               |            64 |         4 |
|     657.6000 |    148.2816 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|     656.6000 |     98.4512 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|     656.6000 |    176.5510 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|     655.8000 |     90.8150 | most_recently_used   | random           | random          | all               |           512 |         5 |
|     655.6000 |    150.7655 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|     653.0000 |    116.3508 | most_recently_used   | dijkstra         | random          | all               |            16 |         4 |
|     652.0000 |     95.1709 | most_frequently_used | dijkstra         | random          | all               |            32 |         4 |
|     651.4000 |    131.6823 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|     647.6000 |     88.8270 | most_frequently_used | bfs              | random          | all               |            64 |         5 |
|     646.2500 |    119.8569 | most_recently_added  | random           | lru             | all               |             8 |         4 |
|     646.0000 |     78.0948 | most_frequently_used | bfs              | random          | all               |            32 |         5 |
|     646.0000 |     99.2673 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|     644.5000 |     99.0694 | most_frequently_used | dijkstra         | random          | all               |            64 |         4 |
|     643.8000 |     81.3349 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|     641.4000 |    129.1117 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|     635.5000 |     77.5387 | most_recently_used   | bfs              | random          | all               |            32 |         4 |
|     635.5000 |    108.4677 | most_frequently_used | random           | random          | all               |            64 |         4 |
|     633.0000 |    157.4001 | most_recently_added  | random           | random          | all               |           128 |         5 |
|     631.2000 |     96.7789 | most_recently_used   | random           | random          | all               |          1024 |         5 |
|     631.2000 |     96.7789 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|     631.2000 |     96.7789 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|     629.5000 |    170.1242 | most_frequently_used | dijkstra         | random          | all               |           128 |         4 |
|     626.0000 |    226.9626 | most_recently_used   | random           | lfu             | all               |            16 |         4 |
|     623.2500 |     62.1022 | most_recently_used   | random           | lfu             | all               |           512 |         4 |
|     619.0000 |    121.7210 | most_frequently_used | dijkstra         | random          | all               |            16 |         4 |
|     618.5000 |    278.8499 | most_recently_added  | random           | lfu             | all               |             4 |         4 |
|     617.6000 |    197.4645 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|     617.0000 |    204.0747 | most_recently_added  | random           | lru             | all               |           128 |         4 |
|     615.5000 |    221.2787 | most_frequently_used | random           | lfu             | all               |            32 |         4 |
|     615.0000 |     86.5014 | most_frequently_used | bfs              | fifo            | all               |           128 |         4 |
|     615.0000 |     86.5014 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         4 |
|     614.6000 |    191.7880 | most_recently_added  | random           | random          | all               |            64 |         5 |
|     613.8000 |    149.9058 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|     610.7500 |     78.2891 | most_frequently_used | bfs              | fifo            | all               |           256 |         4 |
|     610.7500 |     78.2891 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         4 |
|     602.6000 |    161.3947 | most_frequently_used | bfs              | random          | all               |           128 |         5 |
|     601.8000 |    188.6069 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|     600.4000 |     59.4932 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|     600.2000 |     76.5334 | most_frequently_used | bfs              | random          | all               |            16 |         5 |
|     598.5000 |     79.7574 | most_recently_used   | random           | lfu             | all               |          1024 |         4 |
|     598.2500 |     86.1202 | most_recently_used   | dijkstra         | random          | all               |            32 |         4 |
|     597.0000 |     87.1063 | most_recently_added  | random           | lfu             | all               |            64 |         4 |
|     595.5000 |    142.9799 | most_recently_used   | random           | lru             | all               |             8 |         4 |
|     594.4000 |    143.2894 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|     583.4000 |     75.0056 | most_recently_added  | random           | random          | all               |            32 |         5 |
|     582.5000 |     63.3265 | most_recently_added  | random           | lfu             | all               |             8 |         4 |
|     575.7500 |    111.7170 | most_frequently_used | random           | lfu             | all               |           128 |         4 |
|     575.7500 |     19.4342 | most_recently_added  | bfs              | random          | all               |            16 |         4 |
|     571.2500 |     79.7100 | most_recently_used   | random           | lfu             | all               |            64 |         4 |
|     569.8000 |    151.9913 | most_frequently_used | bfs              | random          | all               |           256 |         5 |
|     569.8000 |    254.5847 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|     566.2000 |     88.6733 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|     563.0000 |    263.2079 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|     561.8000 |    165.9860 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|     560.6000 |    248.3615 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|     557.0000 |     61.7382 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|     556.7500 |     74.8344 | most_frequently_used | bfs              | lru             | all               |             4 |         4 |
|     551.7500 |    125.6948 | most_frequently_used | random           | lfu             | all               |            64 |         4 |
|     549.5000 |     59.6343 | most_frequently_used | bfs              | fifo            | all               |             8 |         4 |
|     549.5000 |     59.6343 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         4 |
|     549.5000 |     59.6343 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         4 |
|     549.5000 |     59.6343 | most_recently_used   | bfs              | fifo            | all               |             8 |         4 |
|     549.2000 |    156.1261 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|     547.2000 |    133.6359 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|     544.2000 |    192.5320 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|     542.8000 |    209.6763 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|     540.8000 |     78.8452 | most_recently_used   | random           | random          | all               |            32 |         5 |
|     537.6000 |    148.6117 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|     535.8000 |    118.5874 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|     535.8000 |    262.1514 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|     533.0000 |    193.8234 | most_frequently_used | random           | random          | all               |           256 |         4 |
|     532.2500 |     82.6419 | most_recently_used   | bfs              | random          | all               |            16 |         4 |
|     528.0000 |    226.3449 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|     525.7500 |    174.9134 | most_frequently_used | dijkstra         | lru             | all               |             8 |         4 |
|     524.7500 |    113.6164 | most_recently_added  | dijkstra         | random          | all               |             8 |         4 |
|     520.7500 |    129.7967 | most_frequently_used | dijkstra         | random          | all               |           256 |         4 |
|     518.8000 |    169.3250 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|     517.8000 |    102.7062 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|     516.5000 |     62.4680 | most_recently_added  | dijkstra         | random          | all               |            16 |         4 |
|     513.0000 |    233.8692 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|     513.0000 |    134.5734 | most_recently_added  | random           | lfu             | all               |           128 |         4 |
|     512.4000 |     80.9163 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|     510.0000 |     88.8369 | most_recently_added  | bfs              | fifo            | all               |             8 |         4 |
|     509.2500 |     61.1612 | most_recently_used   | bfs              | random          | all               |             8 |         4 |
|     508.2000 |    186.1262 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|     507.2000 |     79.6553 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|     505.2500 |    219.7810 | most_frequently_used | random           | lfu             | all               |             4 |         4 |
|     503.2500 |    249.4067 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         4 |
|     499.0000 |     68.2386 | most_frequently_used | bfs              | lfu             | all               |            64 |         4 |
|     499.0000 |     69.8198 | most_frequently_used | bfs              | random          | all               |          1024 |         5 |
|     497.5000 |    142.4807 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         4 |
|     496.2500 |    166.3872 | most_frequently_used | random           | lfu             | all               |            16 |         4 |
|     492.0000 |     68.4142 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         4 |
|     492.0000 |     68.4142 | most_frequently_used | bfs              | fifo            | all               |           512 |         4 |
|     488.5000 |    255.6702 | most_recently_used   | random           | lru             | all               |             4 |         4 |
|     486.4000 |     88.9103 | most_frequently_used | bfs              | random          | all               |           512 |         5 |
|     483.6000 |    170.1489 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|     482.2000 |    192.0712 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|     480.6000 |    222.1563 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|     480.6000 |    222.1563 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|     473.4000 |    191.1843 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|     473.4000 |    191.1843 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|     472.0000 |    201.5182 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|     471.0000 |    120.9029 | most_frequently_used | random           | random          | all               |           128 |         4 |
|     469.6000 |    116.8633 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|     468.0000 |    103.6219 | most_frequently_used | bfs              | lfu             | all               |            32 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | bfs              | fifo            | all               |          1024 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | bfs              | lfu             | all               |          1024 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | random          | all               |          1024 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         4 |
|     467.7500 |     34.7949 | most_frequently_used | bfs              | lru             | all               |          1024 |         4 |
|     467.2500 |    220.9405 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         4 |
|     466.0000 |    113.6464 | most_recently_used   | random           | lfu             | all               |             2 |         4 |
|     466.0000 |    113.6464 | most_frequently_used | random           | lfu             | all               |             2 |         4 |
|     461.0000 |    223.5856 | most_frequently_used | random           | random          | all               |           512 |         4 |
|     460.2500 |     68.2253 | most_frequently_used | dijkstra         | random          | all               |             8 |         4 |
|     456.7500 |     64.0132 | most_frequently_used | bfs              | lfu             | all               |           512 |         4 |
|     456.7500 |     64.0132 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         4 |
|     455.2000 |     98.7996 | most_recently_added  | random           | random          | all               |            16 |         5 |
|     454.2000 |     94.8017 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|     453.7500 |     55.0381 | most_frequently_used | bfs              | lru             | all               |           512 |         4 |
|     453.7500 |     55.0381 | most_frequently_used | dijkstra         | lru             | all               |           512 |         4 |
|     453.2500 |    154.4691 | most_frequently_used | random           | random          | all               |            32 |         4 |
|     453.0000 |     68.8912 | most_frequently_used | bfs              | lru             | all               |             2 |         4 |
|     452.7500 |     49.8466 | most_frequently_used | bfs              | lru             | all               |             8 |         4 |
|     452.4000 |    113.2300 | most_frequently_used | bfs              | random          | all               |             8 |         5 |
|     452.2500 |    109.9213 | most_frequently_used | dijkstra         | lru             | all               |            32 |         4 |
|     452.2500 |    109.9213 | most_frequently_used | bfs              | lru             | all               |            32 |         4 |
|     449.5000 |     55.4369 | most_frequently_used | dijkstra         | random          | all               |           512 |         4 |
|     441.5000 |    201.4975 | most_frequently_used | random           | fifo            | all               |          1024 |         4 |
|     441.5000 |    201.4975 | most_frequently_used | random           | random          | all               |          1024 |         4 |
|     438.2500 |    157.3553 | most_recently_used   | random           | lfu             | all               |             4 |         4 |
|     438.2500 |    224.0004 | most_frequently_used | random           | fifo            | all               |           512 |         4 |
|     434.7500 |    112.8879 | most_frequently_used | bfs              | lfu             | all               |            16 |         4 |
|     433.8000 |     56.0443 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|     430.2500 |     62.1545 | most_frequently_used | dijkstra         | lru             | all               |             4 |         4 |
|     429.2500 |    189.0957 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         4 |
|     428.2500 |     97.7481 | most_frequently_used | dijkstra         | lru             | all               |           128 |         4 |
|     428.2500 |     97.7481 | most_frequently_used | bfs              | lru             | all               |           128 |         4 |
|     427.2500 |     98.1768 | most_frequently_used | bfs              | lfu             | all               |           256 |         4 |
|     426.2000 |     87.8371 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|     425.2500 |     58.1480 | most_frequently_used | random           | lfu             | all               |             0 |         4 |
|     425.2500 |     58.1480 | most_recently_used   | random           | lfu             | all               |             0 |         4 |
|     425.2500 |     58.1480 | most_recently_added  | random           | lfu             | all               |             0 |         4 |
|     425.2500 |     58.1480 | most_recently_added  | random           | lru             | all               |             0 |         4 |
|     425.2500 |     58.1480 | most_recently_used   | random           | lru             | all               |             0 |         4 |
|     425.0000 |     79.5393 | most_recently_added  | bfs              | random          | all               |             8 |         4 |
|     423.0000 |    176.3281 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|     421.7500 |     64.1536 | most_recently_used   | dijkstra         | random          | all               |             8 |         4 |
|     420.8000 |     93.7046 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|     419.0000 |     69.7209 | most_frequently_used | bfs              | lru             | all               |           256 |         4 |
|     419.0000 |     69.7209 | most_frequently_used | dijkstra         | lru             | all               |           256 |         4 |
|     418.8000 |    179.3626 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|     417.8000 |    137.8280 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|     417.5000 |    101.2657 | most_recently_used   | bfs              | fifo            | all               |             4 |         4 |
|     417.5000 |    101.2657 | most_frequently_used | bfs              | fifo            | all               |             4 |         4 |
|     416.8000 |     95.0713 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|     415.6000 |     77.2285 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|     407.0000 |     80.5202 | most_frequently_used | dijkstra         | lru             | all               |            16 |         4 |
|     400.7500 |     58.4781 | most_recently_used   | bfs              | random          | all               |             4 |         4 |
|     398.8000 |     35.7402 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|     396.2000 |    154.5631 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|     391.2500 |     36.2172 | most_frequently_used | bfs              | lfu             | all               |           128 |         4 |
|     390.5000 |     46.3762 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         4 |
|     390.5000 |     46.3762 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         4 |
|     389.4000 |     45.6009 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|     387.2000 |     73.2404 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|     385.7500 |    105.6489 | most_frequently_used | random           | random          | all               |            16 |         4 |
|     383.8000 |     59.1047 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|     382.8000 |     85.1526 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|     380.5000 |     65.6677 | most_frequently_used | dijkstra         | lru             | all               |             2 |         4 |
|     380.0000 |     75.3206 | most_frequently_used | bfs              | random          | all               |             4 |         5 |
|     374.5000 |    196.0619 | most_frequently_used | random           | lfu             | all               |             8 |         4 |
|     374.2500 |     77.3737 | most_recently_added  | bfs              | random          | all               |             4 |         4 |
|     368.8000 |    122.3657 | most_recently_added  | random           | random          | all               |             8 |         5 |
|     367.0000 |     41.5030 | most_frequently_used | dijkstra         | random          | all               |             4 |         4 |
|     360.7500 |     48.7667 | most_recently_used   | dijkstra         | random          | all               |             4 |         4 |
|     360.7500 |     35.4709 | most_recently_added  | dijkstra         | random          | all               |             4 |         4 |
|     360.2500 |     74.2879 | most_recently_used   | dijkstra         | random          | all               |             2 |         4 |
|     360.2500 |     74.2879 | most_frequently_used | dijkstra         | random          | all               |             2 |         4 |
|     354.0000 |     51.0441 | most_frequently_used | bfs              | lru             | all               |            64 |         4 |
|     354.0000 |     51.0441 | most_frequently_used | dijkstra         | lru             | all               |            64 |         4 |
|     352.8000 |    153.9512 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|     352.0000 |     50.6211 | most_recently_added  | random           | lru             | all               |             4 |         4 |
|     348.7500 |     80.5431 | most_recently_used   | bfs              | random          | all               |             2 |         4 |
|     346.0000 |    154.7304 | most_recently_added  | random           | lfu             | all               |             2 |         4 |
|     346.0000 |    103.4601 | most_recently_used   | random           | random          | all               |            16 |         5 |
|     341.2000 |    132.9292 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|     341.0000 |    151.1440 | most_frequently_used | bfs              | lfu             | all               |             8 |         4 |
|     340.2000 |    131.1570 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|     336.6000 |     86.7401 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|     333.8000 |     77.9985 | most_frequently_used | bfs              | random          | all               |             2 |         5 |
|     331.7500 |     73.1039 | most_recently_added  | random           | lru             | all               |             2 |         4 |
|     329.6000 |    150.3803 | most_recently_added  | random           | random          | all               |             4 |         5 |
|     328.2500 |     70.4321 | most_recently_added  | random           | fifo            | all               |             2 |         4 |
|     326.8000 |    141.5308 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|     326.0000 |     53.6330 | most_recently_added  | bfs              | random          | all               |             2 |         4 |
|     318.4000 |    117.9586 | most_recently_used   | random           | random          | all               |             8 |         5 |
|     317.0000 |     68.8150 | most_frequently_used | random           | random          | all               |             4 |         4 |
|     315.0000 |     87.0431 | most_frequently_used | random           | random          | all               |             8 |         4 |
|     314.7500 |     57.5690 | most_frequently_used | bfs              | lru             | all               |            16 |         4 |
|     311.5000 |    168.7446 | most_recently_used   | random           | lfu             | all               |             8 |         4 |
|     311.0000 |     69.4622 | most_recently_added  | dijkstra         | random          | all               |             2 |         4 |
|     309.6000 |     71.8905 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|     306.8000 |     66.8353 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|     304.6000 |     66.2408 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|     304.5000 |     53.2283 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         4 |
|     295.5000 |     47.2467 | most_frequently_used | bfs              | fifo            | all               |             2 |         4 |
|     295.5000 |     47.2467 | most_recently_used   | bfs              | fifo            | all               |             2 |         4 |
|     291.6000 |     72.5689 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|     291.2000 |     97.3558 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|     291.2000 |     65.4535 | most_recently_used   | random           | random          | all               |             4 |         5 |
|     291.2000 |     97.3558 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|     287.0000 |     50.5239 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         3 |
|     280.2500 |     75.3338 | most_recently_used   | random           | lru             | all               |             2 |         4 |
|     276.2000 |     57.2797 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|     273.4000 |     68.7593 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|     271.6000 |     65.6859 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|     265.2500 |     42.4404 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         4 |
|     265.2500 |     42.4404 | most_frequently_used | bfs              | lru             | all               |             0 |         4 |
|     265.2500 |     42.4404 | most_frequently_used | dijkstra         | lru             | all               |             0 |         4 |
|     259.4000 |     45.1646 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|     259.4000 |     45.1646 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|     254.6000 |     43.5275 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|     254.4000 |    103.4768 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|     254.4000 |    103.4768 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|     253.0000 |     48.4252 | most_recently_used   | dijkstra         | random          | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_recently_used   | bfs              | fifo            | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_recently_used   | bfs              | random          | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_frequently_used | bfs              | fifo            | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_recently_added  | dijkstra         | random          | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_recently_added  | bfs              | random          | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_frequently_used | dijkstra         | random          | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         4 |
|     253.0000 |     48.4252 | most_frequently_used | bfs              | random          | all               |             0 |         4 |
|     220.0000 |     41.4198 | most_recently_added  | random           | random          | all               |             2 |         5 |
|     216.7500 |     37.0970 | most_frequently_used | random           | random          | all               |             2 |         4 |
|     206.4000 |     39.1081 | most_recently_used   | random           | random          | all               |             2 |         5 |
|     175.0000 |     34.8210 | most_recently_added  | random           | fifo            | all               |             0 |         4 |
|     175.0000 |     34.8210 | most_frequently_used | random           | random          | all               |             0 |         4 |
|     168.2000 |     33.9847 | most_recently_used   | random           | random          | all               |             0 |         5 |
|     168.2000 |     33.9847 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|     168.2000 |     33.9847 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|     168.2000 |     33.9847 | most_recently_added  | random           | random          | all               |             0 |         5 |

## Memory Size 0

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     425.2500 |     58.1480 | most_recently_added  | random           | lfu             | all               |         4 |
|     425.2500 |     58.1480 | most_recently_added  | random           | lru             | all               |         4 |
|     425.2500 |     58.1480 | most_recently_used   | random           | lfu             | all               |         4 |
|     425.2500 |     58.1480 | most_frequently_used | random           | lfu             | all               |         4 |
|     425.2500 |     58.1480 | most_recently_used   | random           | lru             | all               |         4 |
|     352.8000 |    153.9512 | most_frequently_used | random           | lru             | all               |         5 |
|     265.2500 |     42.4404 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     265.2500 |     42.4404 | most_frequently_used | bfs              | lru             | all               |         4 |
|     265.2500 |     42.4404 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     259.4000 |     45.1646 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     259.4000 |     45.1646 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     254.6000 |     43.5275 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_used   | bfs              | lru             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_added  | bfs              | lru             | all               |         5 |
|     254.6000 |     43.5275 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     254.6000 |     43.5275 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     253.0000 |     48.4252 | most_frequently_used | bfs              | random          | all               |         4 |
|     253.0000 |     48.4252 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     253.0000 |     48.4252 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     253.0000 |     48.4252 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     253.0000 |     48.4252 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     253.0000 |     48.4252 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     253.0000 |     48.4252 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     253.0000 |     48.4252 | most_recently_added  | bfs              | random          | all               |         4 |
|     253.0000 |     48.4252 | most_recently_used   | bfs              | random          | all               |         4 |
|     253.0000 |     48.4252 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     175.0000 |     34.8210 | most_recently_added  | random           | fifo            | all               |         4 |
|     175.0000 |     34.8210 | most_frequently_used | random           | random          | all               |         4 |
|     168.2000 |     33.9847 | most_frequently_used | random           | fifo            | all               |         5 |
|     168.2000 |     33.9847 | most_recently_added  | random           | random          | all               |         5 |
|     168.2000 |     33.9847 | most_recently_used   | random           | fifo            | all               |         5 |
|     168.2000 |     33.9847 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 2

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     667.2000 |    141.6297 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     657.6000 |    148.2816 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     561.8000 |    165.9860 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     508.2000 |    186.1262 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     497.5000 |    142.4807 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     472.0000 |    201.5182 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     466.0000 |    113.6464 | most_frequently_used | random           | lfu             | all               |         4 |
|     466.0000 |    113.6464 | most_recently_used   | random           | lfu             | all               |         4 |
|     453.0000 |     68.8912 | most_frequently_used | bfs              | lru             | all               |         4 |
|     416.8000 |     95.0713 | most_recently_used   | bfs              | lru             | all               |         5 |
|     387.2000 |     73.2404 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     383.8000 |     59.1047 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     382.8000 |     85.1526 | most_recently_added  | bfs              | lru             | all               |         5 |
|     380.5000 |     65.6677 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     360.2500 |     74.2879 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     360.2500 |     74.2879 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     348.7500 |     80.5431 | most_recently_used   | bfs              | random          | all               |         4 |
|     346.0000 |    154.7304 | most_recently_added  | random           | lfu             | all               |         4 |
|     333.8000 |     77.9985 | most_frequently_used | bfs              | random          | all               |         5 |
|     331.7500 |     73.1039 | most_recently_added  | random           | lru             | all               |         4 |
|     328.2500 |     70.4321 | most_recently_added  | random           | fifo            | all               |         4 |
|     326.0000 |     53.6330 | most_recently_added  | bfs              | random          | all               |         4 |
|     311.0000 |     69.4622 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     309.6000 |     71.8905 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     304.6000 |     66.2408 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     304.5000 |     53.2283 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     295.5000 |     47.2467 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     295.5000 |     47.2467 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     287.0000 |     50.5239 | most_frequently_used | dijkstra         | fifo            | all               |         3 |
|     280.2500 |     75.3338 | most_recently_used   | random           | lru             | all               |         4 |
|     273.4000 |     68.7593 | most_frequently_used | random           | lru             | all               |         5 |
|     254.4000 |    103.4768 | most_frequently_used | random           | fifo            | all               |         5 |
|     254.4000 |    103.4768 | most_recently_used   | random           | fifo            | all               |         5 |
|     220.0000 |     41.4198 | most_recently_added  | random           | random          | all               |         5 |
|     216.7500 |     37.0970 | most_frequently_used | random           | random          | all               |         4 |
|     206.4000 |     39.1081 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 4

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     618.5000 |    278.8499 | most_recently_added  | random           | lfu             | all               |         4 |
|     617.6000 |    197.4645 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     600.4000 |     59.4932 | most_recently_added  | bfs              | lru             | all               |         5 |
|     560.6000 |    248.3615 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     557.0000 |     61.7382 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     556.7500 |     74.8344 | most_frequently_used | bfs              | lru             | all               |         4 |
|     549.2000 |    156.1261 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     517.8000 |    102.7062 | most_recently_used   | bfs              | lru             | all               |         5 |
|     513.0000 |    233.8692 | most_frequently_used | random           | lru             | all               |         5 |
|     505.2500 |    219.7810 | most_frequently_used | random           | lfu             | all               |         4 |
|     488.5000 |    255.6702 | most_recently_used   | random           | lru             | all               |         4 |
|     469.6000 |    116.8633 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     438.2500 |    157.3553 | most_recently_used   | random           | lfu             | all               |         4 |
|     433.8000 |     56.0443 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     430.2500 |     62.1545 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     429.2500 |    189.0957 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     420.8000 |     93.7046 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     417.5000 |    101.2657 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     417.5000 |    101.2657 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     415.6000 |     77.2285 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     400.7500 |     58.4781 | most_recently_used   | bfs              | random          | all               |         4 |
|     390.5000 |     46.3762 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     390.5000 |     46.3762 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     380.0000 |     75.3206 | most_frequently_used | bfs              | random          | all               |         5 |
|     374.2500 |     77.3737 | most_recently_added  | bfs              | random          | all               |         4 |
|     367.0000 |     41.5030 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     360.7500 |     48.7667 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     360.7500 |     35.4709 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     352.0000 |     50.6211 | most_recently_added  | random           | lru             | all               |         4 |
|     340.2000 |    131.1570 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     329.6000 |    150.3803 | most_recently_added  | random           | random          | all               |         5 |
|     317.0000 |     68.8150 | most_frequently_used | random           | random          | all               |         4 |
|     291.6000 |     72.5689 | most_recently_added  | random           | fifo            | all               |         5 |
|     291.2000 |     97.3558 | most_frequently_used | random           | fifo            | all               |         5 |
|     291.2000 |     97.3558 | most_recently_used   | random           | fifo            | all               |         5 |
|     291.2000 |     65.4535 | most_recently_used   | random           | random          | all               |         5 |

## Memory Size 8

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     902.4000 |     29.8704 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     871.2000 |     62.9425 | most_recently_used   | bfs              | lru             | all               |         5 |
|     853.2000 |     58.3863 | most_recently_added  | bfs              | lru             | all               |         5 |
|     833.8000 |     48.2759 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     646.2500 |    119.8569 | most_recently_added  | random           | lru             | all               |         4 |
|     613.8000 |    149.9058 | most_frequently_used | random           | lru             | all               |         5 |
|     595.5000 |    142.9799 | most_recently_used   | random           | lru             | all               |         4 |
|     582.5000 |     63.3265 | most_recently_added  | random           | lfu             | all               |         4 |
|     569.8000 |    254.5847 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     563.0000 |    263.2079 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     549.5000 |     59.6343 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     549.5000 |     59.6343 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     549.5000 |     59.6343 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     549.5000 |     59.6343 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     535.8000 |    262.1514 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     525.7500 |    174.9134 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     524.7500 |    113.6164 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     510.0000 |     88.8369 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     509.2500 |     61.1612 | most_recently_used   | bfs              | random          | all               |         4 |
|     507.2000 |     79.6553 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     503.2500 |    249.4067 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     460.2500 |     68.2253 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     452.7500 |     49.8466 | most_frequently_used | bfs              | lru             | all               |         4 |
|     452.4000 |    113.2300 | most_frequently_used | bfs              | random          | all               |         5 |
|     425.0000 |     79.5393 | most_recently_added  | bfs              | random          | all               |         4 |
|     421.7500 |     64.1536 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     374.5000 |    196.0619 | most_frequently_used | random           | lfu             | all               |         4 |
|     368.8000 |    122.3657 | most_recently_added  | random           | random          | all               |         5 |
|     341.2000 |    132.9292 | most_recently_added  | random           | fifo            | all               |         5 |
|     341.0000 |    151.1440 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     336.6000 |     86.7401 | most_frequently_used | random           | fifo            | all               |         5 |
|     326.8000 |    141.5308 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     318.4000 |    117.9586 | most_recently_used   | random           | random          | all               |         5 |
|     315.0000 |     87.0431 | most_frequently_used | random           | random          | all               |         4 |
|     311.5000 |    168.7446 | most_recently_used   | random           | lfu             | all               |         4 |
|     306.8000 |     66.8353 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 16

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     899.2000 |     18.2910 | most_recently_added  | bfs              | lru             | all               |         5 |
|     885.2500 |     25.4693 | most_recently_used   | bfs              | lru             | all               |         4 |
|     881.0000 |     35.3610 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     880.4000 |     33.5476 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     735.5000 |     49.9875 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     727.7500 |     46.1052 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     723.5000 |     54.4679 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     714.0000 |     15.4110 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     704.7500 |     32.9725 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     685.7500 |    132.6148 | most_recently_added  | random           | lfu             | all               |         4 |
|     674.4000 |     64.3944 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|     669.0000 |    100.1699 | most_recently_added  | random           | lru             | all               |         4 |
|     665.5000 |     47.1937 | most_recently_used   | random           | lru             | all               |         4 |
|     656.6000 |    176.5510 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     653.0000 |    116.3508 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     626.0000 |    226.9626 | most_recently_used   | random           | lfu             | all               |         4 |
|     619.0000 |    121.7210 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     601.8000 |    188.6069 | most_frequently_used | random           | lru             | all               |         5 |
|     600.2000 |     76.5334 | most_frequently_used | bfs              | random          | all               |         5 |
|     575.7500 |     19.4342 | most_recently_added  | bfs              | random          | all               |         4 |
|     542.8000 |    209.6763 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     532.2500 |     82.6419 | most_recently_used   | bfs              | random          | all               |         4 |
|     528.0000 |    226.3449 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     516.5000 |     62.4680 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     496.2500 |    166.3872 | most_frequently_used | random           | lfu             | all               |         4 |
|     483.6000 |    170.1489 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     467.2500 |    220.9405 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     455.2000 |     98.7996 | most_recently_added  | random           | random          | all               |         5 |
|     434.7500 |    112.8879 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     417.8000 |    137.8280 | most_recently_added  | random           | fifo            | all               |         5 |
|     407.0000 |     80.5202 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     385.7500 |    105.6489 | most_frequently_used | random           | random          | all               |         4 |
|     346.0000 |    103.4601 | most_recently_used   | random           | random          | all               |         5 |
|     314.7500 |     57.5690 | most_frequently_used | bfs              | lru             | all               |         4 |
|     276.2000 |     57.2797 | most_frequently_used | random           | fifo            | all               |         5 |
|     271.6000 |     65.6859 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 32

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     910.0000 |     42.7036 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     899.7500 |     41.8830 | most_recently_used   | bfs              | lru             | all               |         4 |
|     869.4000 |     42.0837 | most_recently_added  | bfs              | lru             | all               |         5 |
|     869.4000 |     42.0837 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     853.4000 |     61.2359 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     837.2000 |    101.4523 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     811.2500 |     70.1654 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     810.5000 |     41.2402 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     810.5000 |     41.2402 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     809.5000 |     43.6492 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     809.5000 |     43.6492 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     795.7500 |     62.5075 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     795.7500 |     62.5075 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     779.8000 |    168.8874 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     760.0000 |     72.5913 | most_recently_added  | bfs              | random          | all               |         4 |
|     695.5000 |    135.2581 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     693.2500 |    114.6045 | most_recently_added  | random           | lru             | all               |         4 |
|     691.0000 |    100.6901 | most_recently_used   | random           | lfu             | all               |         4 |
|     664.7500 |     82.5087 | most_recently_added  | random           | lfu             | all               |         4 |
|     652.0000 |     95.1709 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     651.4000 |    131.6823 | most_recently_used   | random           | lru             | all               |         5 |
|     646.0000 |     78.0948 | most_frequently_used | bfs              | random          | all               |         5 |
|     641.4000 |    129.1117 | most_frequently_used | random           | lru             | all               |         5 |
|     635.5000 |     77.5387 | most_recently_used   | bfs              | random          | all               |         4 |
|     615.5000 |    221.2787 | most_frequently_used | random           | lfu             | all               |         4 |
|     598.2500 |     86.1202 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     583.4000 |     75.0056 | most_recently_added  | random           | random          | all               |         5 |
|     540.8000 |     78.8452 | most_recently_used   | random           | random          | all               |         5 |
|     512.4000 |     80.9163 | most_recently_added  | random           | fifo            | all               |         5 |
|     482.2000 |    192.0712 | most_recently_used   | random           | fifo            | all               |         5 |
|     468.0000 |    103.6219 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     453.2500 |    154.4691 | most_frequently_used | random           | random          | all               |         4 |
|     452.2500 |    109.9213 | most_frequently_used | bfs              | lru             | all               |         4 |
|     452.2500 |    109.9213 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     396.2000 |    154.5631 | most_frequently_used | random           | fifo            | all               |         5 |
|     389.4000 |     45.6009 | most_frequently_used | dijkstra         | lfu             | all               |         5 |

## Memory Size 64

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     900.4000 |     41.5047 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     893.0000 |     39.9650 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     872.6000 |     44.2656 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     866.4000 |     50.8157 | most_recently_added  | bfs              | lru             | all               |         5 |
|     866.4000 |     50.8157 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     863.8000 |     66.9878 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     843.0000 |     12.0167 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|     841.2500 |     12.8525 | most_recently_used   | bfs              | lru             | all               |         4 |
|     836.0000 |     90.8460 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     836.0000 |     90.8460 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     830.7500 |     44.7570 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     830.7500 |     44.7570 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     823.7500 |     71.9318 | most_recently_used   | bfs              | random          | all               |         4 |
|     823.7500 |     71.9318 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     816.0000 |     65.3261 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     793.5000 |     37.0978 | most_recently_added  | bfs              | random          | all               |         4 |
|     744.7500 |     81.7569 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     744.7500 |     81.7569 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     736.8000 |    158.3078 | most_recently_used   | random           | random          | all               |         5 |
|     685.4000 |    132.3142 | most_recently_used   | random           | lru             | all               |         5 |
|     660.2500 |    278.1154 | most_recently_added  | random           | lru             | all               |         4 |
|     647.6000 |     88.8270 | most_frequently_used | bfs              | random          | all               |         5 |
|     644.5000 |     99.0694 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     635.5000 |    108.4677 | most_frequently_used | random           | random          | all               |         4 |
|     614.6000 |    191.7880 | most_recently_added  | random           | random          | all               |         5 |
|     597.0000 |     87.1063 | most_recently_added  | random           | lfu             | all               |         4 |
|     571.2500 |     79.7100 | most_recently_used   | random           | lfu             | all               |         4 |
|     566.2000 |     88.6733 | most_recently_added  | random           | fifo            | all               |         5 |
|     551.7500 |    125.6948 | most_frequently_used | random           | lfu             | all               |         4 |
|     544.2000 |    192.5320 | most_frequently_used | random           | fifo            | all               |         5 |
|     537.6000 |    148.6117 | most_frequently_used | random           | lru             | all               |         5 |
|     518.8000 |    169.3250 | most_recently_used   | random           | fifo            | all               |         5 |
|     499.0000 |     68.2386 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     454.2000 |     94.8017 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     354.0000 |     51.0441 | most_frequently_used | bfs              | lru             | all               |         4 |
|     354.0000 |     51.0441 | most_frequently_used | dijkstra         | lru             | all               |         4 |

## Memory Size 128

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     917.4000 |     12.1754 | most_recently_added  | bfs              | lru             | all               |         5 |
|     917.4000 |     12.1754 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     875.6000 |     36.6911 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     875.0000 |     53.3713 | most_recently_used   | bfs              | lru             | all               |         4 |
|     875.0000 |     53.3713 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     865.6000 |     27.6810 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     861.4000 |     37.0600 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     861.2000 |     60.0646 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     860.7500 |     35.6467 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     860.7500 |     35.6467 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     850.2500 |     46.7353 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     850.2500 |     46.7353 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     840.5000 |     54.6877 | most_recently_used   | bfs              | random          | all               |         4 |
|     840.5000 |     54.6877 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     798.2500 |     21.0758 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     798.2500 |     21.0758 | most_recently_added  | bfs              | random          | all               |         4 |
|     777.5000 |     90.4226 | most_recently_used   | random           | lfu             | all               |         4 |
|     731.8000 |    123.0502 | most_recently_used   | random           | random          | all               |         5 |
|     714.0000 |    121.9475 | most_recently_used   | random           | fifo            | all               |         5 |
|     656.6000 |     98.4512 | most_frequently_used | random           | fifo            | all               |         5 |
|     655.6000 |    150.7655 | most_recently_used   | random           | lru             | all               |         5 |
|     633.0000 |    157.4001 | most_recently_added  | random           | random          | all               |         5 |
|     629.5000 |    170.1242 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     617.0000 |    204.0747 | most_recently_added  | random           | lru             | all               |         4 |
|     615.0000 |     86.5014 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     615.0000 |     86.5014 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     602.6000 |    161.3947 | most_frequently_used | bfs              | random          | all               |         5 |
|     594.4000 |    143.2894 | most_recently_added  | random           | fifo            | all               |         5 |
|     575.7500 |    111.7170 | most_frequently_used | random           | lfu             | all               |         4 |
|     535.8000 |    118.5874 | most_frequently_used | random           | lru             | all               |         5 |
|     513.0000 |    134.5734 | most_recently_added  | random           | lfu             | all               |         4 |
|     471.0000 |    120.9029 | most_frequently_used | random           | random          | all               |         4 |
|     428.2500 |     97.7481 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     428.2500 |     97.7481 | most_frequently_used | bfs              | lru             | all               |         4 |
|     398.8000 |     35.7402 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     391.2500 |     36.2172 | most_frequently_used | bfs              | lfu             | all               |         4 |

## Memory Size 256

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     924.8000 |     24.4491 | most_recently_added  | bfs              | lru             | all               |         5 |
|     924.8000 |     24.4491 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     913.2500 |     35.1879 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     913.2500 |     35.1879 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     902.0000 |     53.5574 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     902.0000 |     53.5574 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     890.0000 |     44.7158 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     890.0000 |     44.7158 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     884.2500 |     54.0619 | most_recently_used   | bfs              | lru             | all               |         4 |
|     884.2500 |     54.0619 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     883.8000 |     62.6431 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     883.8000 |     62.6431 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     879.5000 |     50.3115 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     879.5000 |     50.3115 | most_recently_added  | bfs              | random          | all               |         4 |
|     818.7500 |    104.1210 | most_recently_used   | bfs              | random          | all               |         4 |
|     818.7500 |    104.1210 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     772.2000 |    116.4344 | most_recently_added  | random           | fifo            | all               |         5 |
|     765.0000 |     82.5803 | most_recently_added  | random           | lfu             | all               |         4 |
|     738.0000 |    136.2112 | most_recently_added  | random           | lru             | all               |         4 |
|     730.8000 |    160.1454 | most_recently_used   | random           | fifo            | all               |         5 |
|     725.4000 |    176.5362 | most_recently_used   | random           | lru             | all               |         5 |
|     717.0000 |    135.9412 | most_recently_added  | random           | random          | all               |         5 |
|     697.2500 |    241.9663 | most_recently_used   | random           | lfu             | all               |         4 |
|     670.0000 |    262.0389 | most_recently_used   | random           | random          | all               |         5 |
|     610.7500 |     78.2891 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     610.7500 |     78.2891 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     569.8000 |    151.9913 | most_frequently_used | bfs              | random          | all               |         5 |
|     547.2000 |    133.6359 | most_frequently_used | random           | fifo            | all               |         5 |
|     533.0000 |    193.8234 | most_frequently_used | random           | random          | all               |         4 |
|     520.7500 |    129.7967 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     427.2500 |     98.1768 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     426.2000 |     87.8371 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|     423.0000 |    176.3281 | most_frequently_used | random           | lru             | all               |         5 |
|     419.0000 |     69.7209 | most_frequently_used | bfs              | lru             | all               |         4 |
|     419.0000 |     69.7209 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     418.8000 |    179.3626 | most_frequently_used | random           | lfu             | all               |         5 |

## Memory Size 512

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     906.2500 |      5.3092 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     906.2500 |      5.3092 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     903.0000 |      1.7321 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     903.0000 |      1.7321 | most_recently_added  | bfs              | random          | all               |         4 |
|     897.8000 |     20.5563 | most_recently_added  | bfs              | lru             | all               |         5 |
|     897.8000 |     20.5563 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     897.6000 |     23.8713 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     897.6000 |     23.8713 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     880.2000 |     47.6294 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     880.2000 |     47.6294 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     879.8000 |     59.4454 | most_recently_used   | bfs              | random          | all               |         5 |
|     873.7500 |     49.2310 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     872.7500 |     48.7051 | most_recently_used   | bfs              | lru             | all               |         4 |
|     872.7500 |     48.7051 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     867.2500 |     60.2469 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     854.6667 |     42.1294 | most_recently_used   | dijkstra         | fifo            | all               |         3 |
|     746.2000 |    117.0152 | most_recently_added  | random           | random          | all               |         5 |
|     745.8000 |    115.8402 | most_recently_added  | random           | fifo            | all               |         5 |
|     683.2500 |     85.4704 | most_recently_added  | random           | lfu             | all               |         4 |
|     683.2500 |     85.4704 | most_recently_added  | random           | lru             | all               |         4 |
|     655.8000 |     90.8150 | most_recently_used   | random           | random          | all               |         5 |
|     646.0000 |     99.2673 | most_recently_used   | random           | fifo            | all               |         5 |
|     643.8000 |     81.3349 | most_recently_used   | random           | lru             | all               |         5 |
|     623.2500 |     62.1022 | most_recently_used   | random           | lfu             | all               |         4 |
|     492.0000 |     68.4142 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     492.0000 |     68.4142 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     486.4000 |     88.9103 | most_frequently_used | bfs              | random          | all               |         5 |
|     480.6000 |    222.1563 | most_frequently_used | random           | lfu             | all               |         5 |
|     480.6000 |    222.1563 | most_frequently_used | random           | lru             | all               |         5 |
|     461.0000 |    223.5856 | most_frequently_used | random           | random          | all               |         4 |
|     456.7500 |     64.0132 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     456.7500 |     64.0132 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     453.7500 |     55.0381 | most_frequently_used | bfs              | lru             | all               |         4 |
|     453.7500 |     55.0381 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     449.5000 |     55.4369 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     438.2500 |    224.0004 | most_frequently_used | random           | fifo            | all               |         4 |

## Memory Size 1024

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     903.7500 |      1.7854 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     903.7500 |      1.7854 | most_recently_added  | bfs              | random          | all               |         4 |
|     903.7500 |      1.7854 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     903.7500 |      1.7854 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     893.6000 |     20.3627 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|     893.6000 |     20.3627 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|     893.6000 |     20.3627 | most_recently_added  | bfs              | lfu             | all               |         5 |
|     893.6000 |     20.3627 | most_recently_added  | bfs              | lru             | all               |         5 |
|     889.2000 |     55.9836 | most_recently_used   | bfs              | lfu             | all               |         5 |
|     889.2000 |     55.9836 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|     889.2000 |     55.9836 | most_recently_used   | bfs              | random          | all               |         5 |
|     881.5000 |     60.1768 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     881.5000 |     60.1768 | most_recently_used   | bfs              | lru             | all               |         4 |
|     881.5000 |     60.1768 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     881.5000 |     60.1768 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     881.5000 |     60.1768 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     761.8000 |    127.9100 | most_recently_added  | random           | fifo            | all               |         5 |
|     761.8000 |    127.9100 | most_recently_added  | random           | random          | all               |         5 |
|     718.5000 |    105.2461 | most_recently_added  | random           | lfu             | all               |         4 |
|     718.5000 |    105.2461 | most_recently_added  | random           | lru             | all               |         4 |
|     631.2000 |     96.7789 | most_recently_used   | random           | fifo            | all               |         5 |
|     631.2000 |     96.7789 | most_recently_used   | random           | lru             | all               |         5 |
|     631.2000 |     96.7789 | most_recently_used   | random           | random          | all               |         5 |
|     598.5000 |     79.7574 | most_recently_used   | random           | lfu             | all               |         4 |
|     499.0000 |     69.8198 | most_frequently_used | bfs              | random          | all               |         5 |
|     473.4000 |    191.1843 | most_frequently_used | random           | lru             | all               |         5 |
|     473.4000 |    191.1843 | most_frequently_used | random           | lfu             | all               |         5 |
|     467.7500 |     34.7949 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     467.7500 |     34.7949 | most_frequently_used | bfs              | lru             | all               |         4 |
|     467.7500 |     34.7949 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     467.7500 |     34.7949 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     441.5000 |    201.4975 | most_frequently_used | random           | fifo            | all               |         4 |
|     441.5000 |    201.4975 | most_frequently_used | random           | random          | all               |         4 |

