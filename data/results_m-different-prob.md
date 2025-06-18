# Results for m-different-prob

Total configurations: 396
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|     857.7500 |     21.9018 | most_recently_added  | dijkstra         | lru             | all               |           128 |         4 |
|     857.7500 |     21.9018 | most_recently_added  | bfs              | lru             | all               |           128 |         4 |
|     853.7500 |     82.1960 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         4 |
|     853.7500 |     75.2043 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         4 |
|     853.7500 |     75.2043 | most_recently_added  | bfs              | lfu             | all               |           256 |         4 |
|     849.2500 |     88.3470 | most_recently_added  | bfs              | lfu             | all               |           512 |         4 |
|     849.2500 |     88.3470 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         4 |
|     848.7500 |     30.6788 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         4 |
|     848.0000 |     79.0475 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | bfs              | lfu             | all               |          1024 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | bfs              | lru             | all               |          1024 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | bfs              | random          | all               |          1024 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | random          | all               |          1024 |         4 |
|     846.2500 |     42.0082 | most_recently_added  | bfs              | random          | all               |           256 |         4 |
|     846.2500 |     42.0082 | most_recently_added  | dijkstra         | random          | all               |           256 |         4 |
|     845.0000 |     90.5511 | most_recently_added  | bfs              | lru             | all               |           512 |         4 |
|     845.0000 |     90.5511 | most_recently_added  | dijkstra         | lru             | all               |           512 |         4 |
|     844.0000 |     80.7063 | most_recently_added  | dijkstra         | random          | all               |           512 |         4 |
|     844.0000 |     80.7063 | most_recently_added  | bfs              | random          | all               |           512 |         4 |
|     839.0000 |     22.6605 | most_recently_added  | bfs              | lfu             | all               |           128 |         4 |
|     833.8000 |     31.8207 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|     833.5000 |     35.5704 | most_recently_used   | dijkstra         | lru             | all               |           128 |         4 |
|     833.2500 |     36.2034 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         4 |
|     832.7500 |     68.6527 | most_recently_added  | bfs              | lru             | all               |           256 |         4 |
|     832.7500 |     68.6527 | most_recently_added  | dijkstra         | lru             | all               |           256 |         4 |
|     832.0000 |     32.8710 | most_recently_added  | dijkstra         | lru             | all               |            64 |         4 |
|     832.0000 |     32.8710 | most_recently_added  | bfs              | lru             | all               |            64 |         4 |
|     825.2500 |     50.2612 | most_recently_used   | bfs              | lfu             | all               |           128 |         4 |
|     822.0000 |     97.1453 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|     821.5000 |     57.5739 | most_recently_used   | dijkstra         | lru             | all               |           256 |         4 |
|     820.8000 |     97.3024 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|     820.7500 |     25.4301 | most_recently_used   | dijkstra         | lru             | all               |            32 |         4 |
|     820.7500 |     25.4301 | most_recently_used   | bfs              | lru             | all               |            32 |         4 |
|     820.7500 |     29.3034 | most_recently_added  | dijkstra         | random          | all               |           128 |         4 |
|     819.6000 |     90.6920 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|     819.5000 |     28.2002 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         4 |
|     819.0000 |     51.7378 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|     817.5000 |     29.0560 | most_recently_used   | bfs              | fifo            | all               |           256 |         4 |
|     817.5000 |     29.0560 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         4 |
|     810.5000 |     71.4195 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         4 |
|     810.5000 |     71.4195 | most_recently_used   | bfs              | lfu             | all               |           256 |         4 |
|     808.0000 |     18.9077 | most_recently_added  | bfs              | lru             | all               |            32 |         4 |
|     808.0000 |     18.9077 | most_recently_added  | dijkstra         | lru             | all               |            32 |         4 |
|     807.0000 |     69.8427 | most_recently_used   | bfs              | fifo            | all               |           512 |         4 |
|     807.0000 |     69.8427 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         4 |
|     805.7500 |     66.0847 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         4 |
|     802.0000 |     79.6586 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         4 |
|     802.0000 |     79.6586 | most_recently_used   | bfs              | fifo            | all               |           128 |         4 |
|     796.5000 |     79.2764 | most_recently_used   | bfs              | random          | all               |           512 |         4 |
|     796.5000 |     79.2764 | most_recently_used   | dijkstra         | random          | all               |           512 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | bfs              | random          | all               |          1024 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | bfs              | fifo            | all               |          1024 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | bfs              | lfu             | all               |          1024 |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | random          | all               |          1024 |         4 |
|     790.8000 |     30.7987 | most_recently_added  | bfs              | random          | all               |           128 |         5 |
|     790.2000 |     62.4833 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|     786.7500 |     40.7883 | most_recently_added  | dijkstra         | lru             | all               |            16 |         4 |
|     786.7500 |     92.0554 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         4 |
|     786.7500 |     92.0554 | most_recently_used   | bfs              | lfu             | all               |           512 |         4 |
|     786.2500 |     41.2939 | most_recently_used   | bfs              | fifo            | all               |            64 |         4 |
|     786.2500 |     41.2939 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         4 |
|     780.2500 |     89.5024 | most_recently_used   | dijkstra         | lru             | all               |           512 |         4 |
|     779.8000 |     83.3100 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|     777.2500 |     44.3981 | most_recently_used   | bfs              | lru             | all               |            64 |         4 |
|     777.2500 |     44.3981 | most_recently_used   | dijkstra         | lru             | all               |            64 |         4 |
|     776.2000 |     80.4622 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|     772.5000 |     22.9401 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         4 |
|     769.8000 |     21.2170 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|     765.2000 |     83.6932 | most_recently_used   | dijkstra         | random          | all               |           256 |         5 |
|     762.7500 |     93.4114 | most_recently_used   | bfs              | random          | all               |           256 |         4 |
|     761.0000 |     18.5068 | most_recently_added  | bfs              | lru             | all               |            16 |         4 |
|     756.0000 |     27.6496 | most_recently_added  | bfs              | lfu             | all               |            64 |         4 |
|     747.0000 |     53.5724 | most_recently_used   | bfs              | random          | all               |           128 |         4 |
|     746.2000 |     47.9433 | most_recently_used   | dijkstra         | random          | all               |           128 |         5 |
|     744.7500 |     38.7967 | most_recently_used   | dijkstra         | lru             | all               |            16 |         4 |
|     738.8000 |     37.4454 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|     733.2000 |     85.0609 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|     729.7500 |     39.7704 | most_frequently_used | bfs              | fifo            | all               |           128 |         4 |
|     729.5000 |     36.2388 | most_recently_used   | bfs              | lru             | all               |            16 |         4 |
|     727.0000 |     32.5038 | most_frequently_used | bfs              | fifo            | all               |            64 |         4 |
|     721.8000 |     38.9636 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|     704.5000 |    103.2824 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         4 |
|     702.2500 |     65.2280 | most_frequently_used | bfs              | fifo            | all               |           256 |         4 |
|     700.4000 |     64.3882 | most_recently_used   | dijkstra         | random          | all               |            64 |         5 |
|     698.2500 |     70.5208 | most_recently_used   | bfs              | random          | all               |            64 |         4 |
|     696.7500 |    157.5823 | most_recently_added  | bfs              | lfu             | all               |            32 |         4 |
|     678.5000 |    102.8336 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         4 |
|     673.5000 |    109.1662 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         4 |
|     665.5000 |     60.4421 | most_frequently_used | dijkstra         | random          | all               |           128 |         4 |
|     658.2500 |     50.7069 | most_frequently_used | bfs              | random          | all               |           128 |         4 |
|     649.7500 |     85.9778 | most_frequently_used | bfs              | random          | all               |            64 |         4 |
|     648.0000 |     54.7037 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         4 |
|     645.7500 |     83.7985 | most_frequently_used | bfs              | lfu             | all               |            32 |         4 |
|     642.5000 |    126.5711 | most_recently_used   | bfs              | lfu             | all               |            64 |         4 |
|     641.2500 |     38.9575 | most_frequently_used | bfs              | fifo            | all               |           512 |         4 |
|     641.2500 |     38.9575 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         4 |
|     635.7500 |     84.4019 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         4 |
|     631.2500 |     68.3644 | most_frequently_used | bfs              | lfu             | all               |           128 |         4 |
|     631.2500 |     68.3644 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         4 |
|     626.7500 |     49.7814 | most_frequently_used | bfs              | lru             | all               |           128 |         4 |
|     626.7500 |     49.7814 | most_frequently_used | dijkstra         | lru             | all               |           128 |         4 |
|     625.5000 |     35.2456 | most_frequently_used | bfs              | lru             | all               |           512 |         4 |
|     625.5000 |     35.2456 | most_frequently_used | dijkstra         | lru             | all               |           512 |         4 |
|     625.5000 |     67.4852 | most_frequently_used | bfs              | random          | all               |           256 |         4 |
|     625.5000 |     67.4852 | most_frequently_used | dijkstra         | random          | all               |           256 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | bfs              | lru             | all               |          1024 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | bfs              | fifo            | all               |          1024 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | random          | all               |          1024 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | bfs              | random          | all               |          1024 |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         4 |
|     623.2500 |     32.0965 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         4 |
|     623.2500 |     32.0965 | most_frequently_used | bfs              | lfu             | all               |           512 |         4 |
|     622.7500 |    126.8806 | most_recently_added  | bfs              | lfu             | all               |            16 |         4 |
|     616.0000 |     37.9934 | most_frequently_used | bfs              | random          | all               |           512 |         4 |
|     616.0000 |     37.9934 | most_frequently_used | dijkstra         | random          | all               |           512 |         4 |
|     614.7500 |     32.6219 | most_recently_used   | bfs              | lfu             | all               |            16 |         4 |
|     610.5000 |     64.2359 | most_frequently_used | bfs              | lru             | all               |            64 |         4 |
|     610.5000 |     64.2359 | most_frequently_used | dijkstra         | lru             | all               |            64 |         4 |
|     610.0000 |     28.4341 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         4 |
|     609.2500 |     49.9068 | most_frequently_used | dijkstra         | lru             | all               |           256 |         4 |
|     609.2500 |     49.9068 | most_frequently_used | bfs              | lru             | all               |           256 |         4 |
|     609.0000 |     25.5108 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|     608.7500 |     51.5576 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         4 |
|     608.7500 |     51.5576 | most_frequently_used | bfs              | lfu             | all               |           256 |         4 |
|     608.2000 |     46.3267 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|     603.7500 |     84.7861 | most_frequently_used | dijkstra         | random          | all               |            64 |         4 |
|     603.0000 |    108.0208 | most_recently_used   | bfs              | lfu             | all               |            32 |         4 |
|     600.0000 |    167.8124 | most_recently_added  | dijkstra         | random          | all               |            64 |         4 |
|     599.7500 |     76.6139 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         4 |
|     599.5000 |     27.5726 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         4 |
|     593.0000 |    105.6811 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         4 |
|     587.0000 |     61.9258 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|     586.8000 |     35.4028 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|     584.2500 |     58.2425 | most_frequently_used | dijkstra         | lru             | all               |            32 |         4 |
|     583.2500 |     14.9227 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         4 |
|     583.2500 |     14.9227 | most_frequently_used | bfs              | fifo            | all               |            32 |         4 |
|     581.2000 |     52.4496 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|     580.0000 |     82.8251 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         4 |
|     579.5000 |     79.6068 | most_frequently_used | dijkstra         | lru             | all               |            16 |         4 |
|     570.7500 |     43.8542 | most_frequently_used | dijkstra         | lru             | all               |             8 |         4 |
|     567.8000 |    163.3284 | most_recently_added  | bfs              | random          | all               |            64 |         5 |
|     566.2500 |     38.1928 | most_recently_used   | dijkstra         | lru             | all               |             8 |         4 |
|     560.2500 |     43.2803 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         4 |
|     556.2500 |     52.8175 | most_recently_used   | bfs              | lru             | all               |             8 |         4 |
|     552.5000 |    147.3372 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         4 |
|     551.6000 |     55.7229 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|     547.2500 |     43.5165 | most_frequently_used | bfs              | lfu             | all               |            64 |         4 |
|     542.7500 |     56.4197 | most_recently_added  | dijkstra         | lru             | all               |             8 |         4 |
|     538.0000 |    139.6009 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|     537.2500 |     92.3238 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         4 |
|     532.0000 |    119.3868 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|     531.7500 |     10.1088 | most_recently_added  | bfs              | lru             | all               |             8 |         4 |
|     530.5000 |    100.1736 | most_frequently_used | bfs              | lfu             | all               |            16 |         4 |
|     527.0000 |    136.4331 | most_recently_used   | bfs              | lfu             | all               |             8 |         4 |
|     514.5000 |     73.9003 | most_frequently_used | dijkstra         | random          | all               |            32 |         4 |
|     508.5000 |     34.0478 | most_frequently_used | bfs              | random          | all               |            32 |         4 |
|     506.0000 |     98.0892 | most_frequently_used | bfs              | lfu             | all               |             8 |         4 |
|     501.2500 |     65.7890 | most_recently_used   | bfs              | random          | all               |            32 |         4 |
|     499.2500 |     78.2923 | most_recently_added  | bfs              | lfu             | all               |             8 |         4 |
|     488.0000 |    198.6492 | most_recently_added  | random           | random          | all               |           256 |         4 |
|     484.7500 |    219.6786 | most_recently_added  | random           | random          | all               |          1024 |         4 |
|     484.7500 |    219.6786 | most_recently_added  | random           | fifo            | all               |          1024 |         4 |
|     484.0000 |    213.5263 | most_recently_added  | random           | random          | all               |           512 |         4 |
|     480.4000 |     72.3867 | most_recently_added  | bfs              | random          | all               |            32 |         5 |
|     474.6667 |     48.5547 | most_frequently_used | random           | lfu             | all               |            64 |         3 |
|     473.7500 |     63.1244 | most_recently_added  | dijkstra         | random          | all               |            32 |         4 |
|     472.5000 |    208.1784 | most_recently_added  | random           | fifo            | all               |           512 |         4 |
|     471.2500 |    146.0503 | most_recently_added  | random           | fifo            | all               |           256 |         4 |
|     469.8000 |    121.6970 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|     469.2500 |    224.5032 | most_recently_used   | random           | lfu             | all               |             8 |         4 |
|     462.2500 |    111.7908 | most_recently_used   | random           | lfu             | all               |            64 |         4 |
|     458.6000 |    203.3279 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|     458.6000 |    203.3279 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|     456.4000 |    190.5126 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|     454.8000 |     25.7480 | most_recently_used   | dijkstra         | random          | all               |            32 |         5 |
|     454.4000 |    191.0116 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|     450.0000 |    126.0258 | most_recently_used   | random           | lru             | all               |            64 |         4 |
|     437.4000 |    199.8005 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|     436.5000 |    142.7682 | most_recently_used   | random           | lru             | all               |            32 |         4 |
|     428.8000 |    235.7790 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|     423.2500 |    184.3304 | most_recently_used   | random           | lfu             | all               |            32 |         4 |
|     414.3333 |    117.3182 | most_frequently_used | random           | lru             | all               |            64 |         3 |
|     414.2000 |    180.0638 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|     407.2500 |     19.8037 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         4 |
|     407.0000 |     21.5314 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|     406.0000 |    110.1771 | most_recently_added  | dijkstra         | random          | all               |            16 |         4 |
|     405.5000 |     23.8380 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         4 |
|     405.2000 |     18.1813 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|     401.0000 |     16.9115 | most_frequently_used | dijkstra         | random          | all               |            16 |         4 |
|     400.8000 |    181.5163 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|     397.8000 |    154.2523 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|     387.5000 |    139.6361 | most_recently_used   | random           | lfu             | all               |           256 |         4 |
|     387.0000 |     14.5774 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         4 |
|     387.0000 |     14.5774 | most_frequently_used | bfs              | fifo            | all               |            16 |         4 |
|     386.5000 |     53.1719 | most_recently_used   | bfs              | random          | all               |            16 |         4 |
|     386.5000 |     70.6842 | most_frequently_used | bfs              | lfu             | all               |             2 |         4 |
|     384.2500 |     70.5315 | most_recently_added  | bfs              | lfu             | all               |             4 |         4 |
|     382.0000 |     96.4754 | most_frequently_used | random           | lfu             | all               |            32 |         4 |
|     379.0000 |     74.7503 | most_recently_used   | dijkstra         | random          | all               |            16 |         5 |
|     378.2500 |    103.4925 | most_recently_added  | random           | fifo            | all               |           128 |         4 |
|     377.6000 |    188.3461 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|     377.0000 |     31.5674 | most_frequently_used | bfs              | random          | all               |            16 |         4 |
|     375.4000 |     20.2247 | most_recently_added  | bfs              | random          | all               |            16 |         5 |
|     369.2500 |    240.6557 | most_recently_added  | random           | random          | all               |           128 |         4 |
|     364.7500 |     63.2273 | most_recently_added  | bfs              | lru             | all               |             4 |         4 |
|     363.7500 |    142.7084 | most_recently_used   | random           | fifo            | all               |           128 |         4 |
|     358.2500 |     88.5928 | most_frequently_used | bfs              | lfu             | all               |             4 |         4 |
|     356.0000 |    264.5515 | most_frequently_used | random           | lfu             | all               |             8 |         4 |
|     354.5000 |    248.8559 | most_recently_used   | random           | random          | all               |           512 |         4 |
|     353.5000 |     66.7252 | most_recently_used   | bfs              | lfu             | all               |             2 |         4 |
|     353.2500 |    247.3968 | most_recently_used   | random           | lfu             | all               |           512 |         4 |
|     352.0000 |    247.7529 | most_recently_used   | random           | fifo            | all               |          1024 |         4 |
|     352.0000 |    247.7529 | most_recently_used   | random           | lfu             | all               |          1024 |         4 |
|     352.0000 |    247.7529 | most_recently_used   | random           | random          | all               |          1024 |         4 |
|     348.5000 |    242.7432 | most_recently_used   | random           | fifo            | all               |           512 |         4 |
|     341.6000 |    102.0149 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|     341.0000 |     68.8876 | most_recently_used   | dijkstra         | lru             | all               |             4 |         4 |
|     341.0000 |     68.8876 | most_frequently_used | dijkstra         | lru             | all               |             4 |         4 |
|     339.2500 |    101.6892 | most_recently_added  | bfs              | lfu             | all               |             2 |         4 |
|     330.0000 |    159.8609 | most_recently_used   | random           | random          | all               |            32 |         4 |
|     329.7500 |    206.4187 | most_frequently_used | random           | random          | all               |           512 |         4 |
|     326.0000 |    202.8706 | most_frequently_used | random           | fifo            | all               |          1024 |         4 |
|     326.0000 |    202.8706 | most_frequently_used | random           | lru             | all               |          1024 |         4 |
|     326.0000 |    202.8706 | most_frequently_used | random           | random          | all               |          1024 |         4 |
|     324.5000 |    201.2020 | most_frequently_used | random           | fifo            | all               |           512 |         4 |
|     324.0000 |    171.4016 | most_frequently_used | random           | random          | all               |            32 |         4 |
|     323.5000 |    128.8846 | most_recently_added  | random           | fifo            | all               |            64 |         4 |
|     322.5000 |    204.0839 | most_recently_used   | random           | fifo            | all               |           256 |         4 |
|     322.5000 |    186.1887 | most_frequently_used | random           | fifo            | all               |            64 |         4 |
|     322.2000 |     15.3545 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|     322.0000 |    109.6768 | most_frequently_used | random           | random          | all               |           256 |         4 |
|     321.0000 |    197.8118 | most_frequently_used | random           | lru             | all               |           512 |         4 |
|     321.0000 |    120.2082 | most_frequently_used | random           | lru             | all               |            32 |         3 |
|     319.5000 |    260.0620 | most_recently_used   | random           | random          | all               |            64 |         4 |
|     316.7500 |     12.0908 | most_recently_used   | bfs              | lru             | all               |             4 |         4 |
|     311.7500 |    173.5488 | most_recently_used   | random           | lru             | all               |            16 |         4 |
|     309.8000 |     46.5592 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|     309.3333 |    166.6320 | most_frequently_used | random           | lru             | all               |             8 |         3 |
|     309.2500 |     51.6739 | most_recently_used   | bfs              | lfu             | all               |             4 |         4 |
|     308.5000 |     16.3783 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         4 |
|     305.0000 |     20.3347 | most_recently_added  | bfs              | fifo            | all               |             8 |         4 |
|     301.0000 |    153.0082 | most_recently_used   | random           | lfu             | all               |            16 |         4 |
|     300.5000 |     26.4055 | most_recently_added  | dijkstra         | random          | all               |             8 |         4 |
|     298.5000 |    206.5593 | most_frequently_used | random           | random          | all               |           128 |         4 |
|     293.5000 |     86.6328 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         4 |
|     293.5000 |     15.9138 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         4 |
|     291.6000 |     14.7323 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|     284.5000 |    117.5468 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         4 |
|     283.7500 |     18.2671 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         4 |
|     283.7500 |     18.2671 | most_frequently_used | bfs              | fifo            | all               |             8 |         4 |
|     283.5000 |    162.7890 | most_frequently_used | random           | lru             | all               |           128 |         4 |
|     282.5000 |    108.8221 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         4 |
|     279.0000 |     67.5426 | most_recently_used   | random           | lru             | all               |           256 |         3 |
|     278.2500 |    109.2231 | most_recently_used   | random           | fifo            | all               |            64 |         4 |
|     277.7500 |    183.9910 | most_frequently_used | random           | lru             | all               |           256 |         4 |
|     274.5000 |     46.3923 | most_recently_added  | dijkstra         | lru             | all               |             4 |         4 |
|     272.7500 |     43.4935 | most_recently_added  | random           | random          | all               |            16 |         4 |
|     271.7500 |    158.3309 | most_recently_used   | random           | lru             | all               |           128 |         4 |
|     271.7500 |    116.3559 | most_frequently_used | random           | fifo            | all               |           128 |         4 |
|     271.7500 |    248.4164 | most_recently_used   | random           | random          | all               |           256 |         4 |
|     269.0000 |    171.4905 | most_recently_used   | random           | lru             | all               |             8 |         4 |
|     267.5000 |    221.5564 | most_recently_used   | random           | lfu             | all               |           128 |         4 |
|     266.8000 |     44.8928 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|     266.0000 |     27.4864 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         4 |
|     263.3333 |    197.9063 | most_frequently_used | random           | lfu             | all               |          1024 |         3 |
|     261.2500 |    168.2117 | most_frequently_used | random           | fifo            | all               |            32 |         4 |
|     259.3333 |    192.2539 | most_frequently_used | random           | lfu             | all               |           512 |         3 |
|     255.2500 |     15.7857 | most_recently_used   | bfs              | random          | all               |             8 |         4 |
|     254.5000 |     14.5688 | most_frequently_used | bfs              | random          | all               |             8 |         4 |
|     254.3333 |    207.4582 | most_recently_used   | random           | lru             | all               |           512 |         3 |
|     252.2500 |     37.1912 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         4 |
|     251.5000 |    118.0942 | most_frequently_used | random           | fifo            | all               |           256 |         4 |
|     251.3333 |    203.2410 | most_recently_used   | random           | lru             | all               |          1024 |         3 |
|     245.0000 |    270.8764 | most_recently_used   | random           | random          | all               |           128 |         4 |
|     240.7500 |     63.3181 | most_recently_added  | random           | random          | all               |            32 |         4 |
|     240.0000 |    203.6922 | most_frequently_used | random           | random          | all               |            64 |         4 |
|     237.2000 |     48.1265 | most_recently_added  | bfs              | random          | all               |             8 |         5 |
|     234.5000 |     46.0787 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         4 |
|     234.5000 |     46.0787 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         4 |
|     230.4000 |     67.8722 | most_recently_used   | dijkstra         | random          | all               |             8 |         5 |
|     228.5000 |     24.4182 | most_frequently_used | dijkstra         | random          | all               |             4 |         4 |
|     226.7500 |    210.3335 | most_recently_added  | random           | random          | all               |            64 |         4 |
|     226.0000 |    148.6898 | most_frequently_used | random           | lfu             | all               |           128 |         3 |
|     225.5000 |     26.7628 | most_recently_used   | dijkstra         | random          | all               |             4 |         4 |
|     222.7500 |     37.7318 | most_recently_added  | bfs              | fifo            | all               |             4 |         4 |
|     218.7500 |     56.9885 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         4 |
|     218.7500 |     56.9885 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         4 |
|     217.7500 |    127.0519 | most_recently_added  | random           | fifo            | all               |            32 |         4 |
|     214.4000 |     34.3779 | most_recently_added  | bfs              | random          | all               |             4 |         5 |
|     214.0000 |     46.7707 | most_recently_used   | dijkstra         | lru             | all               |             2 |         4 |
|     214.0000 |    169.9431 | most_frequently_used | random           | lfu             | all               |           256 |         3 |
|     214.0000 |     46.7707 | most_frequently_used | dijkstra         | lru             | all               |             2 |         4 |
|     208.0000 |     57.4848 | most_frequently_used | dijkstra         | random          | all               |             8 |         4 |
|     207.8000 |     19.9138 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|     207.2500 |    109.7597 | most_frequently_used | random           | lfu             | all               |            16 |         4 |
|     205.7500 |     77.2411 | most_recently_used   | bfs              | lru             | all               |             2 |         4 |
|     204.0000 |     20.5791 | most_frequently_used | bfs              | fifo            | all               |             4 |         4 |
|     202.8000 |     69.3380 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|     195.5000 |    127.5255 | most_frequently_used | random           | random          | all               |            16 |         4 |
|     193.7500 |     40.4436 | most_recently_added  | bfs              | lru             | all               |             2 |         4 |
|     193.0000 |     21.2720 | most_recently_used   | dijkstra         | random          | all               |             2 |         4 |
|     193.0000 |     21.2720 | most_frequently_used | dijkstra         | random          | all               |             2 |         4 |
|     191.7500 |     37.9827 | most_recently_added  | dijkstra         | lru             | all               |             2 |         4 |
|     187.2500 |     31.6415 | most_frequently_used | bfs              | fifo            | all               |             2 |         4 |
|     184.0000 |    103.6750 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         4 |
|     181.7500 |     95.2297 | most_recently_used   | random           | lru             | all               |             2 |         4 |
|     180.0000 |     31.7994 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|     176.5000 |     98.8395 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         4 |
|     176.0000 |     23.1840 | most_recently_added  | dijkstra         | random          | all               |             2 |         4 |
|     174.7500 |     84.1052 | most_recently_added  | dijkstra         | random          | all               |             4 |         4 |
|     171.7500 |     73.5574 | most_recently_used   | random           | fifo            | all               |            16 |         4 |
|     170.2500 |     20.2778 | most_recently_used   | bfs              | random          | all               |             4 |         4 |
|     170.2500 |     20.2778 | most_frequently_used | bfs              | random          | all               |             4 |         4 |
|     170.0000 |    117.8749 | most_recently_used   | random           | random          | all               |            16 |         4 |
|     165.7500 |     10.8253 | most_recently_added  | bfs              | fifo            | all               |             2 |         4 |
|     164.2500 |     53.5835 | most_recently_added  | random           | fifo            | all               |             8 |         4 |
|     164.0000 |     36.6947 | most_recently_added  | random           | random          | all               |             4 |         4 |
|     156.2500 |     74.4526 | most_recently_used   | random           | random          | all               |             8 |         4 |
|     155.2500 |     66.6122 | most_recently_added  | random           | random          | all               |             8 |         4 |
|     150.8000 |    106.8127 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|     150.0000 |     55.6192 | most_frequently_used | random           | random          | all               |             4 |         4 |
|     147.5000 |    131.1650 | most_recently_used   | random           | fifo            | all               |            32 |         4 |
|     147.5000 |     63.1051 | most_recently_used   | random           | random          | all               |             4 |         4 |
|     145.3333 |     82.3826 | most_frequently_used | random           | lru             | all               |             2 |         3 |
|     142.6000 |     62.0567 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|     141.6667 |     81.4876 | most_frequently_used | random           | lru             | all               |             4 |         3 |
|     139.7500 |     62.5994 | most_frequently_used | bfs              | random          | all               |             2 |         4 |
|     139.7500 |     62.5994 | most_recently_used   | bfs              | random          | all               |             2 |         4 |
|     134.0000 |     15.9374 | most_recently_used   | bfs              | random          | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_recently_added  | dijkstra         | random          | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_recently_used   | dijkstra         | random          | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_frequently_used | bfs              | random          | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_frequently_used | bfs              | fifo            | all               |             0 |         4 |
|     134.0000 |     44.2888 | most_frequently_used | random           | fifo            | all               |             4 |         4 |
|     134.0000 |     15.9374 | most_frequently_used | dijkstra         | random          | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_recently_added  | bfs              | fifo            | all               |             0 |         4 |
|     134.0000 |     15.9374 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         4 |
|     132.5000 |     69.8910 | most_frequently_used | random           | lfu             | all               |             2 |         4 |
|     132.5000 |     69.8910 | most_recently_used   | random           | lfu             | all               |             2 |         4 |
|     132.2000 |     44.6650 | most_recently_added  | bfs              | random          | all               |             2 |         5 |
|     131.4000 |     15.1737 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|     131.4000 |     15.1737 | most_recently_added  | bfs              | random          | all               |             0 |         5 |
|     125.4000 |     89.6652 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|     123.2500 |     50.2960 | most_recently_added  | random           | random          | all               |             2 |         4 |
|     118.7500 |     74.6203 | most_frequently_used | random           | fifo            | all               |             8 |         4 |
|     118.6667 |     73.8708 | most_frequently_used | random           | lru             | all               |            16 |         3 |
|     118.4000 |     54.7598 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|     118.4000 |     54.7598 | most_recently_added  | random           | lru             | all               |             0 |         5 |
|     118.0000 |     30.5614 | most_recently_used   | random           | lfu             | all               |             4 |         4 |
|     116.3333 |     36.9715 | most_recently_used   | random           | fifo            | all               |             4 |         3 |
|     113.7500 |     85.5464 | most_recently_used   | random           | lru             | all               |             4 |         4 |
|     113.6667 |     85.7334 | most_recently_used   | random           | fifo            | all               |             8 |         3 |
|     110.5000 |     77.6676 | most_frequently_used | random           | random          | all               |             2 |         4 |
|     110.5000 |     77.6676 | most_recently_used   | random           | random          | all               |             2 |         4 |
|     109.4000 |     41.4613 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|     108.2500 |     46.2838 | most_recently_used   | dijkstra         | lru             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_frequently_used | bfs              | lfu             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_frequently_used | dijkstra         | lru             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_added  | bfs              | lfu             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_used   | bfs              | lru             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_added  | bfs              | lru             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_added  | dijkstra         | lru             | all               |             0 |         4 |
|     108.2500 |     46.2838 | most_recently_used   | bfs              | lfu             | all               |             0 |         4 |
|     107.5000 |     74.5067 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         4 |
|     107.0000 |     28.6269 | most_frequently_used | random           | lfu             | all               |             4 |         4 |
|     106.0000 |     49.9850 | most_frequently_used | random           | random          | all               |             8 |         4 |
|     105.5000 |     25.8892 | most_recently_added  | random           | fifo            | all               |             2 |         4 |
|     103.0000 |     42.4343 | most_frequently_used | random           | lru             | all               |             0 |         3 |
|      97.7500 |     51.7560 | most_recently_added  | random           | fifo            | all               |             4 |         4 |
|      97.0000 |     38.1903 | most_frequently_used | random           | lfu             | all               |             0 |         4 |
|      97.0000 |     38.1903 | most_recently_used   | random           | lru             | all               |             0 |         4 |
|      97.0000 |     38.1903 | most_recently_used   | random           | lfu             | all               |             0 |         4 |
|      94.4000 |     66.9376 | most_recently_added  | random           | fifo            | all               |             0 |         5 |
|      90.5000 |     46.4408 | most_frequently_used | random           | fifo            | all               |             2 |         4 |
|      86.5000 |     73.2854 | most_recently_added  | random           | fifo            | all               |            16 |         4 |
|      86.2000 |     53.1654 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|      83.6667 |     51.8545 | most_recently_used   | random           | fifo            | all               |             2 |         3 |
|      73.0000 |     53.9877 | most_recently_used   | random           | fifo            | all               |             0 |         3 |
|      68.5000 |     47.3999 | most_frequently_used | random           | random          | all               |             0 |         4 |
|      68.5000 |     47.3999 | most_recently_used   | random           | random          | all               |             0 |         4 |
|      68.5000 |     47.3999 | most_frequently_used | random           | fifo            | all               |             0 |         4 |
|      68.5000 |     47.3999 | most_recently_added  | random           | random          | all               |             0 |         4 |
|      56.5000 |     28.4825 | most_frequently_used | random           | fifo            | all               |            16 |         4 |

## Memory Size 0

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     134.0000 |     15.9374 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     134.0000 |     15.9374 | most_frequently_used | bfs              | random          | all               |         4 |
|     134.0000 |     15.9374 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     134.0000 |     15.9374 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     134.0000 |     15.9374 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     134.0000 |     15.9374 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     134.0000 |     15.9374 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     134.0000 |     15.9374 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     134.0000 |     15.9374 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     134.0000 |     15.9374 | most_recently_used   | bfs              | random          | all               |         4 |
|     131.4000 |     15.1737 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     131.4000 |     15.1737 | most_recently_added  | bfs              | random          | all               |         5 |
|     118.4000 |     54.7598 | most_recently_added  | random           | lru             | all               |         5 |
|     118.4000 |     54.7598 | most_recently_added  | random           | lfu             | all               |         5 |
|     109.4000 |     41.4613 | most_frequently_used | bfs              | lru             | all               |         5 |
|     108.2500 |     46.2838 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_added  | bfs              | lru             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     108.2500 |     46.2838 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     108.2500 |     46.2838 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_used   | bfs              | lru             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     108.2500 |     46.2838 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     103.0000 |     42.4343 | most_frequently_used | random           | lru             | all               |         3 |
|      97.0000 |     38.1903 | most_frequently_used | random           | lfu             | all               |         4 |
|      97.0000 |     38.1903 | most_recently_used   | random           | lfu             | all               |         4 |
|      97.0000 |     38.1903 | most_recently_used   | random           | lru             | all               |         4 |
|      94.4000 |     66.9376 | most_recently_added  | random           | fifo            | all               |         5 |
|      73.0000 |     53.9877 | most_recently_used   | random           | fifo            | all               |         3 |
|      68.5000 |     47.3999 | most_frequently_used | random           | fifo            | all               |         4 |
|      68.5000 |     47.3999 | most_frequently_used | random           | random          | all               |         4 |
|      68.5000 |     47.3999 | most_recently_added  | random           | random          | all               |         4 |
|      68.5000 |     47.3999 | most_recently_used   | random           | random          | all               |         4 |

## Memory Size 2

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     386.5000 |     70.6842 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     353.5000 |     66.7252 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     339.2500 |    101.6892 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     252.2500 |     37.1912 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     218.7500 |     56.9885 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     218.7500 |     56.9885 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     214.0000 |     46.7707 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     214.0000 |     46.7707 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     205.7500 |     77.2411 | most_recently_used   | bfs              | lru             | all               |         4 |
|     202.8000 |     69.3380 | most_frequently_used | bfs              | lru             | all               |         5 |
|     193.7500 |     40.4436 | most_recently_added  | bfs              | lru             | all               |         4 |
|     193.0000 |     21.2720 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     193.0000 |     21.2720 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     191.7500 |     37.9827 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     187.2500 |     31.6415 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     184.0000 |    103.6750 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     181.7500 |     95.2297 | most_recently_used   | random           | lru             | all               |         4 |
|     180.0000 |     31.7994 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     176.5000 |     98.8395 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     176.0000 |     23.1840 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     165.7500 |     10.8253 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     145.3333 |     82.3826 | most_frequently_used | random           | lru             | all               |         3 |
|     142.6000 |     62.0567 | most_recently_added  | random           | lfu             | all               |         5 |
|     139.7500 |     62.5994 | most_frequently_used | bfs              | random          | all               |         4 |
|     139.7500 |     62.5994 | most_recently_used   | bfs              | random          | all               |         4 |
|     132.5000 |     69.8910 | most_frequently_used | random           | lfu             | all               |         4 |
|     132.5000 |     69.8910 | most_recently_used   | random           | lfu             | all               |         4 |
|     132.2000 |     44.6650 | most_recently_added  | bfs              | random          | all               |         5 |
|     123.2500 |     50.2960 | most_recently_added  | random           | random          | all               |         4 |
|     110.5000 |     77.6676 | most_recently_used   | random           | random          | all               |         4 |
|     110.5000 |     77.6676 | most_frequently_used | random           | random          | all               |         4 |
|     107.5000 |     74.5067 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     105.5000 |     25.8892 | most_recently_added  | random           | fifo            | all               |         4 |
|      90.5000 |     46.4408 | most_frequently_used | random           | fifo            | all               |         4 |
|      86.2000 |     53.1654 | most_recently_added  | random           | lru             | all               |         5 |
|      83.6667 |     51.8545 | most_recently_used   | random           | fifo            | all               |         3 |

## Memory Size 4

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     384.2500 |     70.5315 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     364.7500 |     63.2273 | most_recently_added  | bfs              | lru             | all               |         4 |
|     358.2500 |     88.5928 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     341.0000 |     68.8876 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     341.0000 |     68.8876 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     322.2000 |     15.3545 | most_frequently_used | bfs              | lru             | all               |         5 |
|     316.7500 |     12.0908 | most_recently_used   | bfs              | lru             | all               |         4 |
|     309.2500 |     51.6739 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     293.5000 |     86.6328 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     284.5000 |    117.5468 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     282.5000 |    108.8221 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     274.5000 |     46.3923 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     266.0000 |     27.4864 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     234.5000 |     46.0787 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     234.5000 |     46.0787 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     228.5000 |     24.4182 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     225.5000 |     26.7628 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     222.7500 |     37.7318 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     214.4000 |     34.3779 | most_recently_added  | bfs              | random          | all               |         5 |
|     207.8000 |     19.9138 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     204.0000 |     20.5791 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     174.7500 |     84.1052 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     170.2500 |     20.2778 | most_frequently_used | bfs              | random          | all               |         4 |
|     170.2500 |     20.2778 | most_recently_used   | bfs              | random          | all               |         4 |
|     164.0000 |     36.6947 | most_recently_added  | random           | random          | all               |         4 |
|     150.8000 |    106.8127 | most_recently_added  | random           | lfu             | all               |         5 |
|     150.0000 |     55.6192 | most_frequently_used | random           | random          | all               |         4 |
|     147.5000 |     63.1051 | most_recently_used   | random           | random          | all               |         4 |
|     141.6667 |     81.4876 | most_frequently_used | random           | lru             | all               |         3 |
|     134.0000 |     44.2888 | most_frequently_used | random           | fifo            | all               |         4 |
|     125.4000 |     89.6652 | most_recently_added  | random           | lru             | all               |         5 |
|     118.0000 |     30.5614 | most_recently_used   | random           | lfu             | all               |         4 |
|     116.3333 |     36.9715 | most_recently_used   | random           | fifo            | all               |         3 |
|     113.7500 |     85.5464 | most_recently_used   | random           | lru             | all               |         4 |
|     107.0000 |     28.6269 | most_frequently_used | random           | lfu             | all               |         4 |
|      97.7500 |     51.7560 | most_recently_added  | random           | fifo            | all               |         4 |

## Memory Size 8

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     599.7500 |     76.6139 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     570.7500 |     43.8542 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     566.2500 |     38.1928 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     556.2500 |     52.8175 | most_recently_used   | bfs              | lru             | all               |         4 |
|     552.5000 |    147.3372 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     551.6000 |     55.7229 | most_frequently_used | bfs              | lru             | all               |         5 |
|     542.7500 |     56.4197 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     537.2500 |     92.3238 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     531.7500 |     10.1088 | most_recently_added  | bfs              | lru             | all               |         4 |
|     527.0000 |    136.4331 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     506.0000 |     98.0892 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     499.2500 |     78.2923 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     469.2500 |    224.5032 | most_recently_used   | random           | lfu             | all               |         4 |
|     356.0000 |    264.5515 | most_frequently_used | random           | lfu             | all               |         4 |
|     309.8000 |     46.5592 | most_recently_added  | random           | lfu             | all               |         5 |
|     309.3333 |    166.6320 | most_frequently_used | random           | lru             | all               |         3 |
|     308.5000 |     16.3783 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     305.0000 |     20.3347 | most_recently_added  | bfs              | fifo            | all               |         4 |
|     300.5000 |     26.4055 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     293.5000 |     15.9138 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     291.6000 |     14.7323 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     283.7500 |     18.2671 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     283.7500 |     18.2671 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     269.0000 |    171.4905 | most_recently_used   | random           | lru             | all               |         4 |
|     266.8000 |     44.8928 | most_recently_added  | random           | lru             | all               |         5 |
|     255.2500 |     15.7857 | most_recently_used   | bfs              | random          | all               |         4 |
|     254.5000 |     14.5688 | most_frequently_used | bfs              | random          | all               |         4 |
|     237.2000 |     48.1265 | most_recently_added  | bfs              | random          | all               |         5 |
|     230.4000 |     67.8722 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     208.0000 |     57.4848 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     164.2500 |     53.5835 | most_recently_added  | random           | fifo            | all               |         4 |
|     156.2500 |     74.4526 | most_recently_used   | random           | random          | all               |         4 |
|     155.2500 |     66.6122 | most_recently_added  | random           | random          | all               |         4 |
|     118.7500 |     74.6203 | most_frequently_used | random           | fifo            | all               |         4 |
|     113.6667 |     85.7334 | most_recently_used   | random           | fifo            | all               |         3 |
|     106.0000 |     49.9850 | most_frequently_used | random           | random          | all               |         4 |

## Memory Size 16

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     786.7500 |     40.7883 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     761.0000 |     18.5068 | most_recently_added  | bfs              | lru             | all               |         4 |
|     744.7500 |     38.7967 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     729.5000 |     36.2388 | most_recently_used   | bfs              | lru             | all               |         4 |
|     678.5000 |    102.8336 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     622.7500 |    126.8806 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     614.7500 |     32.6219 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     593.0000 |    105.6811 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     587.0000 |     61.9258 | most_frequently_used | bfs              | lru             | all               |         5 |
|     580.0000 |     82.8251 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     579.5000 |     79.6068 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     530.5000 |    100.1736 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     407.2500 |     19.8037 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     407.0000 |     21.5314 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     406.0000 |    110.1771 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     405.5000 |     23.8380 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     405.2000 |     18.1813 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     401.0000 |     16.9115 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     397.8000 |    154.2523 | most_recently_added  | random           | lfu             | all               |         5 |
|     387.0000 |     14.5774 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     387.0000 |     14.5774 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     386.5000 |     53.1719 | most_recently_used   | bfs              | random          | all               |         4 |
|     379.0000 |     74.7503 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     377.0000 |     31.5674 | most_frequently_used | bfs              | random          | all               |         4 |
|     375.4000 |     20.2247 | most_recently_added  | bfs              | random          | all               |         5 |
|     341.6000 |    102.0149 | most_recently_added  | random           | lru             | all               |         5 |
|     311.7500 |    173.5488 | most_recently_used   | random           | lru             | all               |         4 |
|     301.0000 |    153.0082 | most_recently_used   | random           | lfu             | all               |         4 |
|     272.7500 |     43.4935 | most_recently_added  | random           | random          | all               |         4 |
|     207.2500 |    109.7597 | most_frequently_used | random           | lfu             | all               |         4 |
|     195.5000 |    127.5255 | most_frequently_used | random           | random          | all               |         4 |
|     171.7500 |     73.5574 | most_recently_used   | random           | fifo            | all               |         4 |
|     170.0000 |    117.8749 | most_recently_used   | random           | random          | all               |         4 |
|     118.6667 |     73.8708 | most_frequently_used | random           | lru             | all               |         3 |
|      86.5000 |     73.2854 | most_recently_added  | random           | fifo            | all               |         4 |
|      56.5000 |     28.4825 | most_frequently_used | random           | fifo            | all               |         4 |

## Memory Size 32

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     820.7500 |     25.4301 | most_recently_used   | bfs              | lru             | all               |         4 |
|     820.7500 |     25.4301 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     808.0000 |     18.9077 | most_recently_added  | bfs              | lru             | all               |         4 |
|     808.0000 |     18.9077 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     704.5000 |    103.2824 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     696.7500 |    157.5823 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     673.5000 |    109.1662 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     648.0000 |     54.7037 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     645.7500 |     83.7985 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     610.0000 |     28.4341 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     609.0000 |     25.5108 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     603.0000 |    108.0208 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     599.5000 |     27.5726 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     586.8000 |     35.4028 | most_recently_used   | bfs              | fifo            | all               |         5 |
|     584.2500 |     58.2425 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     583.2500 |     14.9227 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     583.2500 |     14.9227 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     581.2000 |     52.4496 | most_frequently_used | bfs              | lru             | all               |         5 |
|     538.0000 |    139.6009 | most_recently_added  | random           | lfu             | all               |         5 |
|     514.5000 |     73.9003 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     508.5000 |     34.0478 | most_frequently_used | bfs              | random          | all               |         4 |
|     501.2500 |     65.7890 | most_recently_used   | bfs              | random          | all               |         4 |
|     480.4000 |     72.3867 | most_recently_added  | bfs              | random          | all               |         5 |
|     473.7500 |     63.1244 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     469.8000 |    121.6970 | most_recently_added  | random           | lru             | all               |         5 |
|     454.8000 |     25.7480 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     436.5000 |    142.7682 | most_recently_used   | random           | lru             | all               |         4 |
|     423.2500 |    184.3304 | most_recently_used   | random           | lfu             | all               |         4 |
|     382.0000 |     96.4754 | most_frequently_used | random           | lfu             | all               |         4 |
|     330.0000 |    159.8609 | most_recently_used   | random           | random          | all               |         4 |
|     324.0000 |    171.4016 | most_frequently_used | random           | random          | all               |         4 |
|     321.0000 |    120.2082 | most_frequently_used | random           | lru             | all               |         3 |
|     261.2500 |    168.2117 | most_frequently_used | random           | fifo            | all               |         4 |
|     240.7500 |     63.3181 | most_recently_added  | random           | random          | all               |         4 |
|     217.7500 |    127.0519 | most_recently_added  | random           | fifo            | all               |         4 |
|     147.5000 |    131.1650 | most_recently_used   | random           | fifo            | all               |         4 |

## Memory Size 64

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     832.0000 |     32.8710 | most_recently_added  | bfs              | lru             | all               |         4 |
|     832.0000 |     32.8710 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     805.7500 |     66.0847 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     786.2500 |     41.2939 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     786.2500 |     41.2939 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     777.2500 |     44.3981 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     777.2500 |     44.3981 | most_recently_used   | bfs              | lru             | all               |         4 |
|     772.5000 |     22.9401 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     769.8000 |     21.2170 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     756.0000 |     27.6496 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     738.8000 |     37.4454 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     727.0000 |     32.5038 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     700.4000 |     64.3882 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     698.2500 |     70.5208 | most_recently_used   | bfs              | random          | all               |         4 |
|     649.7500 |     85.9778 | most_frequently_used | bfs              | random          | all               |         4 |
|     642.5000 |    126.5711 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     635.7500 |     84.4019 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     610.5000 |     64.2359 | most_frequently_used | bfs              | lru             | all               |         4 |
|     610.5000 |     64.2359 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     603.7500 |     84.7861 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     600.0000 |    167.8124 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     567.8000 |    163.3284 | most_recently_added  | bfs              | random          | all               |         5 |
|     560.2500 |     43.2803 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     547.2500 |     43.5165 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     532.0000 |    119.3868 | most_recently_added  | random           | lfu             | all               |         5 |
|     474.6667 |     48.5547 | most_frequently_used | random           | lfu             | all               |         3 |
|     462.2500 |    111.7908 | most_recently_used   | random           | lfu             | all               |         4 |
|     450.0000 |    126.0258 | most_recently_used   | random           | lru             | all               |         4 |
|     414.3333 |    117.3182 | most_frequently_used | random           | lru             | all               |         3 |
|     400.8000 |    181.5163 | most_recently_added  | random           | lru             | all               |         5 |
|     323.5000 |    128.8846 | most_recently_added  | random           | fifo            | all               |         4 |
|     322.5000 |    186.1887 | most_frequently_used | random           | fifo            | all               |         4 |
|     319.5000 |    260.0620 | most_recently_used   | random           | random          | all               |         4 |
|     278.2500 |    109.2231 | most_recently_used   | random           | fifo            | all               |         4 |
|     240.0000 |    203.6922 | most_frequently_used | random           | random          | all               |         4 |
|     226.7500 |    210.3335 | most_recently_added  | random           | random          | all               |         4 |

## Memory Size 128

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     857.7500 |     21.9018 | most_recently_added  | bfs              | lru             | all               |         4 |
|     857.7500 |     21.9018 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     848.7500 |     30.6788 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     839.0000 |     22.6605 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     833.8000 |     31.8207 | most_recently_used   | bfs              | lru             | all               |         5 |
|     833.5000 |     35.5704 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     833.2500 |     36.2034 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     825.2500 |     50.2612 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     820.7500 |     29.3034 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     819.5000 |     28.2002 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     802.0000 |     79.6586 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     802.0000 |     79.6586 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     790.8000 |     30.7987 | most_recently_added  | bfs              | random          | all               |         5 |
|     779.8000 |     83.3100 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     747.0000 |     53.5724 | most_recently_used   | bfs              | random          | all               |         4 |
|     746.2000 |     47.9433 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     729.7500 |     39.7704 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     721.8000 |     38.9636 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     665.5000 |     60.4421 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     658.2500 |     50.7069 | most_frequently_used | bfs              | random          | all               |         4 |
|     631.2500 |     68.3644 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     631.2500 |     68.3644 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     626.7500 |     49.7814 | most_frequently_used | bfs              | lru             | all               |         4 |
|     626.7500 |     49.7814 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     428.8000 |    235.7790 | most_recently_added  | random           | lru             | all               |         5 |
|     378.2500 |    103.4925 | most_recently_added  | random           | fifo            | all               |         4 |
|     377.6000 |    188.3461 | most_recently_added  | random           | lfu             | all               |         5 |
|     369.2500 |    240.6557 | most_recently_added  | random           | random          | all               |         4 |
|     363.7500 |    142.7084 | most_recently_used   | random           | fifo            | all               |         4 |
|     298.5000 |    206.5593 | most_frequently_used | random           | random          | all               |         4 |
|     283.5000 |    162.7890 | most_frequently_used | random           | lru             | all               |         4 |
|     271.7500 |    116.3559 | most_frequently_used | random           | fifo            | all               |         4 |
|     271.7500 |    158.3309 | most_recently_used   | random           | lru             | all               |         4 |
|     267.5000 |    221.5564 | most_recently_used   | random           | lfu             | all               |         4 |
|     245.0000 |    270.8764 | most_recently_used   | random           | random          | all               |         4 |
|     226.0000 |    148.6898 | most_frequently_used | random           | lfu             | all               |         3 |

## Memory Size 256

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     853.7500 |     75.2043 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     853.7500 |     75.2043 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     848.0000 |     79.0475 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     846.2500 |     42.0082 | most_recently_added  | bfs              | random          | all               |         4 |
|     846.2500 |     42.0082 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     832.7500 |     68.6527 | most_recently_added  | bfs              | lru             | all               |         4 |
|     832.7500 |     68.6527 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     821.5000 |     57.5739 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     819.6000 |     90.6920 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     819.0000 |     51.7378 | most_recently_used   | bfs              | lru             | all               |         5 |
|     817.5000 |     29.0560 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     817.5000 |     29.0560 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     810.5000 |     71.4195 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     810.5000 |     71.4195 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     765.2000 |     83.6932 | most_recently_used   | dijkstra         | random          | all               |         5 |
|     762.7500 |     93.4114 | most_recently_used   | bfs              | random          | all               |         4 |
|     733.2000 |     85.0609 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|     702.2500 |     65.2280 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     625.5000 |     67.4852 | most_frequently_used | bfs              | random          | all               |         4 |
|     625.5000 |     67.4852 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     609.2500 |     49.9068 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     609.2500 |     49.9068 | most_frequently_used | bfs              | lru             | all               |         4 |
|     608.7500 |     51.5576 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     608.7500 |     51.5576 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     488.0000 |    198.6492 | most_recently_added  | random           | random          | all               |         4 |
|     471.2500 |    146.0503 | most_recently_added  | random           | fifo            | all               |         4 |
|     437.4000 |    199.8005 | most_recently_added  | random           | lfu             | all               |         5 |
|     414.2000 |    180.0638 | most_recently_added  | random           | lru             | all               |         5 |
|     387.5000 |    139.6361 | most_recently_used   | random           | lfu             | all               |         4 |
|     322.5000 |    204.0839 | most_recently_used   | random           | fifo            | all               |         4 |
|     322.0000 |    109.6768 | most_frequently_used | random           | random          | all               |         4 |
|     279.0000 |     67.5426 | most_recently_used   | random           | lru             | all               |         3 |
|     277.7500 |    183.9910 | most_frequently_used | random           | lru             | all               |         4 |
|     271.7500 |    248.4164 | most_recently_used   | random           | random          | all               |         4 |
|     251.5000 |    118.0942 | most_frequently_used | random           | fifo            | all               |         4 |
|     214.0000 |    169.9431 | most_frequently_used | random           | lfu             | all               |         3 |

## Memory Size 512

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     853.7500 |     82.1960 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     849.2500 |     88.3470 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     849.2500 |     88.3470 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     845.0000 |     90.5511 | most_recently_added  | bfs              | lru             | all               |         4 |
|     845.0000 |     90.5511 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     844.0000 |     80.7063 | most_recently_added  | bfs              | random          | all               |         4 |
|     844.0000 |     80.7063 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     822.0000 |     97.1453 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     807.0000 |     69.8427 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     807.0000 |     69.8427 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     796.5000 |     79.2764 | most_recently_used   | bfs              | random          | all               |         4 |
|     796.5000 |     79.2764 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     786.7500 |     92.0554 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     786.7500 |     92.0554 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     780.2500 |     89.5024 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     776.2000 |     80.4622 | most_recently_used   | bfs              | lru             | all               |         5 |
|     641.2500 |     38.9575 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     641.2500 |     38.9575 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     625.5000 |     35.2456 | most_frequently_used | bfs              | lru             | all               |         4 |
|     625.5000 |     35.2456 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     623.2500 |     32.0965 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     623.2500 |     32.0965 | most_frequently_used | bfs              | lfu             | all               |         4 |
|     616.0000 |     37.9934 | most_frequently_used | bfs              | random          | all               |         4 |
|     616.0000 |     37.9934 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     484.0000 |    213.5263 | most_recently_added  | random           | random          | all               |         4 |
|     472.5000 |    208.1784 | most_recently_added  | random           | fifo            | all               |         4 |
|     456.4000 |    190.5126 | most_recently_added  | random           | lru             | all               |         5 |
|     454.4000 |    191.0116 | most_recently_added  | random           | lfu             | all               |         5 |
|     354.5000 |    248.8559 | most_recently_used   | random           | random          | all               |         4 |
|     353.2500 |    247.3968 | most_recently_used   | random           | lfu             | all               |         4 |
|     348.5000 |    242.7432 | most_recently_used   | random           | fifo            | all               |         4 |
|     329.7500 |    206.4187 | most_frequently_used | random           | random          | all               |         4 |
|     324.5000 |    201.2020 | most_frequently_used | random           | fifo            | all               |         4 |
|     321.0000 |    197.8118 | most_frequently_used | random           | lru             | all               |         4 |
|     259.3333 |    192.2539 | most_frequently_used | random           | lfu             | all               |         3 |
|     254.3333 |    207.4582 | most_recently_used   | random           | lru             | all               |         3 |

## Memory Size 1024

Total configurations: 36

|   mean_score |   std_score | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|-------------:|------------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | lru             | all               |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | lfu             | all               |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | random          | all               |         4 |
|     846.7500 |     92.0200 | most_recently_added  | dijkstra         | fifo            | all               |         4 |
|     846.7500 |     92.0200 | most_recently_added  | bfs              | lru             | all               |         4 |
|     846.7500 |     92.0200 | most_recently_added  | bfs              | random          | all               |         4 |
|     846.7500 |     92.0200 | most_recently_added  | bfs              | lfu             | all               |         4 |
|     820.8000 |     97.3024 | most_recently_added  | bfs              | fifo            | all               |         5 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | fifo            | all               |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | lfu             | all               |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | lru             | all               |         4 |
|     791.0000 |     69.8355 | most_recently_used   | dijkstra         | random          | all               |         4 |
|     791.0000 |     69.8355 | most_recently_used   | bfs              | random          | all               |         4 |
|     791.0000 |     69.8355 | most_recently_used   | bfs              | fifo            | all               |         4 |
|     791.0000 |     69.8355 | most_recently_used   | bfs              | lfu             | all               |         4 |
|     790.2000 |     62.4833 | most_recently_used   | bfs              | lru             | all               |         5 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | fifo            | all               |         4 |
|     624.5000 |     36.8001 | most_frequently_used | bfs              | random          | all               |         4 |
|     624.5000 |     36.8001 | most_frequently_used | bfs              | lru             | all               |         4 |
|     624.5000 |     36.8001 | most_frequently_used | bfs              | fifo            | all               |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | lru             | all               |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | lfu             | all               |         4 |
|     624.5000 |     36.8001 | most_frequently_used | dijkstra         | random          | all               |         4 |
|     608.2000 |     46.3267 | most_frequently_used | bfs              | lfu             | all               |         5 |
|     484.7500 |    219.6786 | most_recently_added  | random           | fifo            | all               |         4 |
|     484.7500 |    219.6786 | most_recently_added  | random           | random          | all               |         4 |
|     458.6000 |    203.3279 | most_recently_added  | random           | lfu             | all               |         5 |
|     458.6000 |    203.3279 | most_recently_added  | random           | lru             | all               |         5 |
|     352.0000 |    247.7529 | most_recently_used   | random           | fifo            | all               |         4 |
|     352.0000 |    247.7529 | most_recently_used   | random           | lfu             | all               |         4 |
|     352.0000 |    247.7529 | most_recently_used   | random           | random          | all               |         4 |
|     326.0000 |    202.8706 | most_frequently_used | random           | lru             | all               |         4 |
|     326.0000 |    202.8706 | most_frequently_used | random           | random          | all               |         4 |
|     326.0000 |    202.8706 | most_frequently_used | random           | fifo            | all               |         4 |
|     263.3333 |    197.9063 | most_frequently_used | random           | lfu             | all               |         3 |
|     251.3333 |    203.2410 | most_recently_used   | random           | lru             | all               |         3 |

