# Results for s-different-prob

Total configurations: 297
Memory sizes: [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

## Overall Results (All Memory Sizes)

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   memory_size |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|--------------:|----------:|
|         927 |         23 | most_recently_added  | dijkstra         | lfu             | all               |           256 |         5 |
|         927 |         23 | most_recently_added  | bfs              | lfu             | all               |           256 |         5 |
|         911 |         34 | most_recently_used   | bfs              | lru             | all               |          1024 |         5 |
|         911 |         34 | most_recently_used   | dijkstra         | lru             | all               |          1024 |         5 |
|         911 |         34 | most_recently_used   | bfs              | fifo            | all               |          1024 |         5 |
|         911 |         26 | most_recently_used   | dijkstra         | lfu             | all               |           256 |         5 |
|         911 |         34 | most_recently_used   | bfs              | lfu             | all               |          1024 |         5 |
|         911 |         26 | most_recently_used   | bfs              | lfu             | all               |           256 |         5 |
|         911 |         34 | most_recently_used   | dijkstra         | fifo            | all               |          1024 |         5 |
|         911 |         34 | most_recently_used   | dijkstra         | lfu             | all               |          1024 |         5 |
|         910 |         28 | most_recently_added  | bfs              | lfu             | all               |           128 |         5 |
|         908 |         32 | most_recently_used   | dijkstra         | lru             | all               |           512 |         5 |
|         908 |         32 | most_recently_used   | bfs              | lru             | all               |           512 |         5 |
|         906 |         24 | most_recently_added  | dijkstra         | lru             | all               |           256 |         5 |
|         906 |         24 | most_recently_added  | bfs              | lru             | all               |           256 |         5 |
|         906 |         27 | most_recently_added  | dijkstra         | lfu             | all               |           128 |         5 |
|         904 |         33 | most_recently_used   | bfs              | lfu             | all               |           512 |         5 |
|         904 |         33 | most_recently_used   | dijkstra         | lfu             | all               |           512 |         5 |
|         904 |         28 | most_recently_used   | bfs              | fifo            | all               |           512 |         5 |
|         904 |         28 | most_recently_used   | dijkstra         | fifo            | all               |           512 |         5 |
|         902 |         37 | most_recently_used   | bfs              | lru             | all               |           256 |         5 |
|         902 |         30 | most_recently_used   | dijkstra         | lru             | all               |             8 |         5 |
|         902 |         37 | most_recently_used   | dijkstra         | lru             | all               |           256 |         5 |
|         901 |         41 | most_recently_used   | bfs              | lru             | all               |           128 |         5 |
|         901 |         41 | most_recently_used   | dijkstra         | lru             | all               |           128 |         5 |
|         900 |         26 | most_recently_used   | dijkstra         | fifo            | all               |           128 |         5 |
|         900 |         26 | most_recently_used   | bfs              | fifo            | all               |           128 |         5 |
|         900 |         32 | most_recently_added  | bfs              | fifo            | all               |          1024 |         5 |
|         900 |         32 | most_recently_added  | dijkstra         | lru             | all               |          1024 |         5 |
|         900 |         32 | most_recently_added  | dijkstra         | fifo            | all               |          1024 |         5 |
|         900 |         32 | most_recently_added  | bfs              | lru             | all               |          1024 |         5 |
|         900 |         32 | most_recently_added  | bfs              | lfu             | all               |          1024 |         5 |
|         900 |         19 | most_recently_added  | bfs              | lfu             | all               |           512 |         5 |
|         900 |         19 | most_recently_added  | dijkstra         | lfu             | all               |           512 |         5 |
|         900 |         32 | most_recently_added  | dijkstra         | lfu             | all               |          1024 |         5 |
|         899 |         18 | most_recently_added  | bfs              | lru             | all               |            16 |         5 |
|         897 |         47 | most_recently_used   | bfs              | lfu             | all               |           128 |         5 |
|         897 |         47 | most_recently_used   | dijkstra         | lfu             | all               |           128 |         5 |
|         896 |         23 | most_recently_added  | dijkstra         | lru             | all               |           512 |         5 |
|         896 |         23 | most_recently_added  | bfs              | lru             | all               |           512 |         5 |
|         896 |         40 | most_recently_added  | dijkstra         | lru             | all               |            32 |         5 |
|         896 |         39 | most_recently_used   | dijkstra         | fifo            | all               |           256 |         5 |
|         896 |         39 | most_recently_used   | bfs              | fifo            | all               |           256 |         5 |
|         894 |         29 | most_recently_used   | bfs              | lru             | all               |            16 |         5 |
|         894 |         30 | most_recently_added  | bfs              | fifo            | all               |           512 |         5 |
|         894 |         30 | most_recently_added  | dijkstra         | fifo            | all               |           512 |         5 |
|         893 |         40 | most_recently_added  | bfs              | lru             | all               |            32 |         5 |
|         888 |         23 | most_recently_added  | bfs              | fifo            | all               |           256 |         5 |
|         888 |         23 | most_recently_added  | dijkstra         | fifo            | all               |           256 |         5 |
|         881 |         35 | most_recently_used   | dijkstra         | lru             | all               |            16 |         5 |
|         880 |         34 | most_recently_added  | dijkstra         | lru             | all               |            16 |         5 |
|         877 |         45 | most_recently_used   | bfs              | lru             | all               |            32 |         5 |
|         876 |         57 | most_recently_used   | bfs              | fifo            | all               |            64 |         5 |
|         876 |         57 | most_recently_used   | dijkstra         | fifo            | all               |            64 |         5 |
|         875 |         48 | most_recently_used   | dijkstra         | lru             | all               |            32 |         5 |
|         871 |         63 | most_recently_used   | bfs              | lru             | all               |             8 |         5 |
|         866 |         41 | most_recently_added  | dijkstra         | lru             | all               |           128 |         5 |
|         866 |         41 | most_recently_added  | bfs              | lru             | all               |           128 |         5 |
|         863 |         49 | most_recently_used   | dijkstra         | lfu             | all               |            64 |         5 |
|         853 |         58 | most_recently_added  | bfs              | lru             | all               |             8 |         5 |
|         852 |         73 | most_recently_added  | bfs              | fifo            | all               |           128 |         5 |
|         852 |         73 | most_recently_added  | dijkstra         | fifo            | all               |           128 |         5 |
|         848 |         65 | most_recently_used   | bfs              | lru             | all               |            64 |         5 |
|         848 |         65 | most_recently_used   | dijkstra         | lru             | all               |            64 |         5 |
|         846 |         76 | most_recently_used   | bfs              | lfu             | all               |            64 |         5 |
|         846 |         52 | most_recently_added  | dijkstra         | fifo            | all               |            64 |         5 |
|         846 |         52 | most_recently_added  | bfs              | fifo            | all               |            64 |         5 |
|         843 |         38 | most_recently_added  | bfs              | lru             | all               |            64 |         5 |
|         843 |         38 | most_recently_added  | dijkstra         | lru             | all               |            64 |         5 |
|         834 |         48 | most_recently_added  | dijkstra         | lru             | all               |             8 |         5 |
|         825 |        113 | most_recently_used   | bfs              | lfu             | all               |            32 |         5 |
|         823 |         34 | most_recently_added  | dijkstra         | lfu             | all               |            32 |         5 |
|         810 |         42 | most_recently_used   | bfs              | fifo            | all               |            32 |         5 |
|         810 |         42 | most_recently_used   | dijkstra         | fifo            | all               |            32 |         5 |
|         808 |        101 | most_frequently_used | bfs              | fifo            | all               |            64 |         5 |
|         808 |        101 | most_frequently_used | dijkstra         | fifo            | all               |            64 |         5 |
|         799 |         50 | most_recently_added  | bfs              | fifo            | all               |            32 |         5 |
|         799 |         50 | most_recently_added  | dijkstra         | fifo            | all               |            32 |         5 |
|         797 |        117 | most_recently_added  | bfs              | lfu             | all               |            32 |         5 |
|         791 |         70 | most_recently_added  | dijkstra         | lfu             | all               |            64 |         5 |
|         780 |         24 | most_frequently_used | bfs              | fifo            | all               |            32 |         5 |
|         780 |         24 | most_frequently_used | dijkstra         | fifo            | all               |            32 |         5 |
|         780 |        146 | most_recently_used   | dijkstra         | lfu             | all               |            32 |         5 |
|         772 |        116 | most_recently_added  | random           | fifo            | all               |           256 |         5 |
|         763 |         86 | most_recently_used   | random           | lfu             | all               |           128 |         5 |
|         763 |        131 | most_recently_added  | random           | lru             | all               |           256 |         5 |
|         762 |        128 | most_recently_added  | random           | fifo            | all               |          1024 |         5 |
|         762 |        128 | most_recently_added  | random           | lru             | all               |          1024 |         5 |
|         762 |        128 | most_recently_added  | random           | lfu             | all               |          1024 |         5 |
|         746 |        116 | most_recently_added  | random           | fifo            | all               |           512 |         5 |
|         745 |         84 | most_recently_added  | random           | lfu             | all               |           256 |         5 |
|         731 |        160 | most_recently_used   | random           | fifo            | all               |           256 |         5 |
|         725 |        177 | most_recently_used   | random           | lru             | all               |           256 |         5 |
|         722 |        125 | most_recently_added  | bfs              | lfu             | all               |            64 |         5 |
|         719 |         45 | most_recently_used   | bfs              | fifo            | all               |            16 |         5 |
|         717 |        104 | most_recently_used   | random           | lfu             | all               |            32 |         5 |
|         715 |        100 | most_recently_added  | random           | lfu             | all               |           512 |         5 |
|         715 |        100 | most_recently_added  | random           | lru             | all               |           512 |         5 |
|         714 |        122 | most_recently_used   | random           | fifo            | all               |           128 |         5 |
|         713 |        271 | most_recently_added  | random           | lru             | all               |            64 |         5 |
|         713 |         53 | most_recently_added  | bfs              | fifo            | all               |            16 |         5 |
|         710 |         68 | most_frequently_used | dijkstra         | fifo            | all               |            16 |         5 |
|         701 |         29 | most_recently_used   | dijkstra         | fifo            | all               |            16 |         5 |
|         699 |        107 | most_recently_added  | random           | lru             | all               |            16 |         5 |
|         693 |         38 | most_frequently_used | bfs              | fifo            | all               |            16 |         5 |
|         687 |        217 | most_recently_used   | random           | lfu             | all               |           256 |         5 |
|         686 |        119 | most_recently_added  | random           | lfu             | all               |            16 |         5 |
|         685 |        132 | most_recently_used   | random           | lru             | all               |            64 |         5 |
|         674 |         64 | most_recently_added  | dijkstra         | fifo            | all               |            16 |         5 |
|         670 |        117 | most_recently_added  | random           | lru             | all               |             8 |         5 |
|         669 |         74 | most_recently_added  | random           | lfu             | all               |            32 |         5 |
|         667 |        142 | most_recently_used   | dijkstra         | lfu             | all               |             2 |         5 |
|         666 |         42 | most_recently_used   | random           | lru             | all               |            16 |         5 |
|         658 |        148 | most_recently_used   | bfs              | lfu             | all               |             2 |         5 |
|         657 |        177 | most_recently_used   | bfs              | lfu             | all               |            16 |         5 |
|         657 |         98 | most_frequently_used | random           | fifo            | all               |           128 |         5 |
|         656 |        151 | most_recently_used   | random           | lru             | all               |           128 |         5 |
|         652 |        210 | most_recently_used   | random           | lfu             | all               |            16 |         5 |
|         652 |         79 | most_recently_used   | random           | lfu             | all               |           512 |         5 |
|         651 |        132 | most_recently_used   | random           | lru             | all               |            32 |         5 |
|         646 |        126 | most_recently_added  | random           | lfu             | all               |            64 |         5 |
|         646 |         99 | most_recently_used   | random           | fifo            | all               |           512 |         5 |
|         644 |        206 | most_frequently_used | random           | lfu             | all               |            32 |         5 |
|         644 |         81 | most_recently_used   | random           | lru             | all               |           512 |         5 |
|         641 |        129 | most_frequently_used | random           | lru             | all               |            32 |         5 |
|         636 |        154 | most_recently_added  | random           | lru             | all               |            32 |         5 |
|         635 |         84 | most_frequently_used | dijkstra         | fifo            | all               |           128 |         5 |
|         635 |         84 | most_frequently_used | bfs              | fifo            | all               |           128 |         5 |
|         631 |         97 | most_recently_used   | random           | lfu             | all               |          1024 |         5 |
|         631 |         97 | most_recently_used   | random           | fifo            | all               |          1024 |         5 |
|         631 |         97 | most_recently_used   | random           | lru             | all               |          1024 |         5 |
|         618 |        197 | most_recently_used   | dijkstra         | lfu             | all               |             4 |         5 |
|         614 |        150 | most_frequently_used | random           | lru             | all               |             8 |         5 |
|         614 |        183 | most_recently_added  | random           | lru             | all               |           128 |         5 |
|         614 |         84 | most_recently_added  | random           | lfu             | all               |             8 |         5 |
|         613 |         90 | most_frequently_used | bfs              | fifo            | all               |           256 |         5 |
|         613 |         90 | most_frequently_used | dijkstra         | fifo            | all               |           256 |         5 |
|         607 |        130 | most_recently_used   | random           | lru             | all               |             8 |         5 |
|         602 |        189 | most_frequently_used | random           | lru             | all               |            16 |         5 |
|         600 |         59 | most_recently_added  | bfs              | lru             | all               |             4 |         5 |
|         594 |        143 | most_recently_added  | random           | fifo            | all               |           128 |         5 |
|         588 |        200 | most_frequently_used | dijkstra         | lru             | all               |             8 |         5 |
|         582 |         75 | most_recently_used   | random           | lfu             | all               |            64 |         5 |
|         580 |        246 | most_frequently_used | random           | lfu             | all               |             4 |         5 |
|         573 |        263 | most_recently_added  | dijkstra         | lfu             | all               |             8 |         5 |
|         570 |        255 | most_recently_added  | bfs              | lfu             | all               |             8 |         5 |
|         566 |         89 | most_recently_added  | random           | fifo            | all               |            64 |         5 |
|         563 |        263 | most_recently_used   | dijkstra         | lfu             | all               |             8 |         5 |
|         562 |        166 | most_frequently_used | bfs              | lfu             | all               |             2 |         5 |
|         561 |        275 | most_recently_added  | random           | lfu             | all               |             4 |         5 |
|         561 |        248 | most_recently_used   | bfs              | lfu             | all               |             4 |         5 |
|         557 |         62 | most_recently_added  | dijkstra         | lru             | all               |             4 |         5 |
|         549 |        156 | most_recently_added  | bfs              | lfu             | all               |             4 |         5 |
|         547 |        134 | most_frequently_used | random           | fifo            | all               |           256 |         5 |
|         546 |        116 | most_frequently_used | random           | lfu             | all               |           128 |         5 |
|         545 |         54 | most_recently_used   | dijkstra         | fifo            | all               |             8 |         5 |
|         545 |         54 | most_frequently_used | bfs              | fifo            | all               |             8 |         5 |
|         545 |         54 | most_recently_used   | bfs              | fifo            | all               |             8 |         5 |
|         545 |         54 | most_frequently_used | dijkstra         | fifo            | all               |             8 |         5 |
|         544 |        193 | most_frequently_used | random           | fifo            | all               |            64 |         5 |
|         543 |        210 | most_recently_used   | dijkstra         | lfu             | all               |            16 |         5 |
|         541 |        247 | most_recently_added  | dijkstra         | lfu             | all               |            16 |         5 |
|         538 |        149 | most_frequently_used | random           | lru             | all               |            64 |         5 |
|         536 |        262 | most_recently_used   | bfs              | lfu             | all               |             8 |         5 |
|         536 |        119 | most_frequently_used | random           | lru             | all               |           128 |         5 |
|         528 |        226 | most_recently_added  | bfs              | lfu             | all               |            16 |         5 |
|         526 |        154 | most_frequently_used | bfs              | lru             | all               |             8 |         5 |
|         525 |         97 | most_frequently_used | dijkstra         | fifo            | all               |           512 |         5 |
|         525 |         97 | most_frequently_used | bfs              | fifo            | all               |           512 |         5 |
|         523 |        252 | most_recently_added  | dijkstra         | lfu             | all               |             4 |         5 |
|         519 |        169 | most_recently_used   | random           | fifo            | all               |            64 |         5 |
|         518 |        103 | most_recently_used   | bfs              | lru             | all               |             4 |         5 |
|         518 |        103 | most_frequently_used | bfs              | lru             | all               |             4 |         5 |
|         513 |        234 | most_frequently_used | random           | lru             | all               |             4 |         5 |
|         513 |        234 | most_recently_used   | random           | lru             | all               |             4 |         5 |
|         512 |         81 | most_recently_added  | random           | fifo            | all               |            32 |         5 |
|         508 |        186 | most_frequently_used | dijkstra         | lfu             | all               |             2 |         5 |
|         507 |         80 | most_recently_added  | dijkstra         | fifo            | all               |             8 |         5 |
|         507 |         80 | most_recently_added  | bfs              | fifo            | all               |             8 |         5 |
|         506 |         92 | most_frequently_used | dijkstra         | lfu             | all               |          1024 |         5 |
|         506 |         92 | most_frequently_used | bfs              | lfu             | all               |          1024 |         5 |
|         506 |         92 | most_frequently_used | bfs              | fifo            | all               |          1024 |         5 |
|         506 |         92 | most_frequently_used | dijkstra         | fifo            | all               |          1024 |         5 |
|         506 |         92 | most_frequently_used | bfs              | lru             | all               |          1024 |         5 |
|         506 |         92 | most_frequently_used | dijkstra         | lru             | all               |          1024 |         5 |
|         504 |        148 | most_frequently_used | random           | lfu             | all               |            64 |         5 |
|         502 |        190 | most_recently_used   | random           | lfu             | all               |             4 |         5 |
|         490 |         63 | most_frequently_used | bfs              | lru             | all               |           256 |         5 |
|         490 |         63 | most_frequently_used | dijkstra         | lru             | all               |           256 |         5 |
|         487 |        131 | most_recently_added  | random           | lfu             | all               |           128 |         5 |
|         487 |         95 | most_frequently_used | dijkstra         | lfu             | all               |           512 |         5 |
|         487 |         95 | most_frequently_used | bfs              | lfu             | all               |           512 |         5 |
|         484 |        170 | most_frequently_used | dijkstra         | lfu             | all               |            16 |         5 |
|         482 |        192 | most_recently_used   | random           | fifo            | all               |            32 |         5 |
|         481 |         93 | most_frequently_used | dijkstra         | lru             | all               |           512 |         5 |
|         481 |         93 | most_frequently_used | bfs              | lru             | all               |           512 |         5 |
|         481 |        222 | most_frequently_used | random           | lru             | all               |           512 |         5 |
|         481 |        222 | most_frequently_used | random           | lfu             | all               |           512 |         5 |
|         481 |        106 | most_frequently_used | random           | lfu             | all               |             2 |         5 |
|         481 |        106 | most_recently_used   | random           | lfu             | all               |             2 |         5 |
|         473 |        191 | most_frequently_used | random           | fifo            | all               |          1024 |         5 |
|         473 |        191 | most_frequently_used | random           | lfu             | all               |          1024 |         5 |
|         473 |        191 | most_frequently_used | random           | lru             | all               |          1024 |         5 |
|         472 |        202 | most_recently_added  | bfs              | lfu             | all               |             2 |         5 |
|         470 |        210 | most_frequently_used | random           | fifo            | all               |           512 |         5 |
|         470 |        117 | most_frequently_used | dijkstra         | lfu             | all               |             4 |         5 |
|         459 |         80 | most_frequently_used | bfs              | lfu             | all               |            32 |         5 |
|         457 |        151 | most_recently_added  | dijkstra         | lfu             | all               |             2 |         5 |
|         453 |         78 | most_frequently_used | dijkstra         | lru             | all               |            64 |         5 |
|         453 |         78 | most_frequently_used | bfs              | lru             | all               |            64 |         5 |
|         448 |        104 | most_frequently_used | bfs              | lfu             | all               |            16 |         5 |
|         434 |         56 | most_recently_used   | dijkstra         | lru             | all               |             4 |         5 |
|         434 |         56 | most_frequently_used | dijkstra         | lru             | all               |             4 |         5 |
|         430 |        199 | most_frequently_used | random           | lfu             | all               |            16 |         5 |
|         429 |        161 | most_recently_added  | random           | lru             | all               |             4 |         5 |
|         426 |         69 | most_frequently_used | bfs              | lru             | all               |            32 |         5 |
|         423 |         65 | most_frequently_used | dijkstra         | lru             | all               |            32 |         5 |
|         423 |        176 | most_frequently_used | random           | lru             | all               |           256 |         5 |
|         421 |         94 | most_recently_added  | dijkstra         | fifo            | all               |             4 |         5 |
|         420 |        173 | most_frequently_used | bfs              | lru             | all               |           128 |         5 |
|         420 |        173 | most_frequently_used | dijkstra         | lru             | all               |           128 |         5 |
|         420 |         91 | most_frequently_used | bfs              | fifo            | all               |             4 |         5 |
|         420 |         91 | most_recently_used   | bfs              | fifo            | all               |             4 |         5 |
|         419 |        179 | most_frequently_used | random           | lfu             | all               |           256 |         5 |
|         418 |        138 | most_recently_added  | random           | fifo            | all               |            16 |         5 |
|         417 |         95 | most_recently_used   | bfs              | lru             | all               |             2 |         5 |
|         417 |         95 | most_frequently_used | bfs              | lru             | all               |             2 |         5 |
|         416 |         54 | most_frequently_used | bfs              | lfu             | all               |            64 |         5 |
|         416 |         77 | most_recently_added  | bfs              | fifo            | all               |             4 |         5 |
|         414 |         98 | most_frequently_used | bfs              | lfu             | all               |           128 |         5 |
|         412 |         97 | most_frequently_used | dijkstra         | lfu             | all               |           128 |         5 |
|         407 |         82 | most_frequently_used | dijkstra         | lfu             | all               |           256 |         5 |
|         407 |         82 | most_frequently_used | bfs              | lfu             | all               |           256 |         5 |
|         403 |         48 | most_recently_used   | dijkstra         | fifo            | all               |             4 |         5 |
|         403 |         48 | most_frequently_used | dijkstra         | fifo            | all               |             4 |         5 |
|         397 |         75 | most_frequently_used | dijkstra         | lru             | all               |            16 |         5 |
|         396 |        155 | most_frequently_used | random           | fifo            | all               |            32 |         5 |
|         395 |        225 | most_recently_used   | random           | lfu             | all               |             8 |         5 |
|         387 |         73 | most_recently_added  | dijkstra         | lru             | all               |             2 |         5 |
|         384 |         59 | most_frequently_used | dijkstra         | lru             | all               |             2 |         5 |
|         384 |         59 | most_recently_used   | dijkstra         | lru             | all               |             2 |         5 |
|         383 |         85 | most_recently_added  | bfs              | lru             | all               |             2 |         5 |
|         382 |        176 | most_frequently_used | random           | lfu             | all               |             8 |         5 |
|         381 |         70 | most_frequently_used | dijkstra         | lfu             | all               |            32 |         5 |
|         368 |        104 | most_frequently_used | dijkstra         | lfu             | all               |            64 |         5 |
|         353 |        154 | most_frequently_used | random           | lfu             | all               |             0 |         5 |
|         353 |        154 | most_recently_added  | random           | lfu             | all               |             0 |         5 |
|         353 |        154 | most_recently_added  | random           | lru             | all               |             0 |         5 |
|         353 |        154 | most_frequently_used | random           | lru             | all               |             0 |         5 |
|         353 |        154 | most_recently_used   | random           | lfu             | all               |             0 |         5 |
|         353 |        154 | most_recently_used   | random           | lru             | all               |             0 |         5 |
|         341 |        133 | most_recently_added  | random           | fifo            | all               |             8 |         5 |
|         340 |        131 | most_frequently_used | bfs              | lfu             | all               |             4 |         5 |
|         337 |        140 | most_recently_added  | random           | lfu             | all               |             2 |         5 |
|         337 |         87 | most_frequently_used | random           | fifo            | all               |             8 |         5 |
|         327 |         66 | most_recently_added  | random           | lru             | all               |             2 |         5 |
|         327 |        142 | most_frequently_used | dijkstra         | lfu             | all               |             8 |         5 |
|         321 |        141 | most_frequently_used | bfs              | lfu             | all               |             8 |         5 |
|         320 |         65 | most_recently_added  | random           | fifo            | all               |             2 |         5 |
|         310 |         72 | most_recently_added  | dijkstra         | fifo            | all               |             2 |         5 |
|         307 |         67 | most_recently_used   | random           | fifo            | all               |             8 |         5 |
|         305 |         55 | most_frequently_used | bfs              | lru             | all               |            16 |         5 |
|         305 |         66 | most_recently_added  | bfs              | fifo            | all               |             2 |         5 |
|         304 |         48 | most_frequently_used | dijkstra         | fifo            | all               |             2 |         5 |
|         304 |         48 | most_recently_used   | dijkstra         | fifo            | all               |             2 |         5 |
|         301 |         44 | most_frequently_used | bfs              | fifo            | all               |             2 |         5 |
|         301 |         44 | most_recently_used   | bfs              | fifo            | all               |             2 |         5 |
|         292 |         73 | most_recently_added  | random           | fifo            | all               |             4 |         5 |
|         291 |         97 | most_recently_used   | random           | fifo            | all               |             4 |         5 |
|         291 |         97 | most_frequently_used | random           | fifo            | all               |             4 |         5 |
|         276 |         57 | most_frequently_used | random           | fifo            | all               |            16 |         5 |
|         273 |         69 | most_recently_used   | random           | lru             | all               |             2 |         5 |
|         273 |         69 | most_frequently_used | random           | lru             | all               |             2 |         5 |
|         272 |         66 | most_recently_used   | random           | fifo            | all               |            16 |         5 |
|         259 |         45 | most_recently_used   | dijkstra         | fifo            | all               |             0 |         5 |
|         259 |         45 | most_recently_added  | bfs              | fifo            | all               |             0 |         5 |
|         259 |         45 | most_recently_added  | dijkstra         | fifo            | all               |             0 |         5 |
|         259 |         45 | most_recently_used   | bfs              | fifo            | all               |             0 |         5 |
|         259 |         45 | most_frequently_used | bfs              | fifo            | all               |             0 |         5 |
|         259 |         45 | most_frequently_used | dijkstra         | fifo            | all               |             0 |         5 |
|         255 |         44 | most_recently_used   | bfs              | lfu             | all               |             0 |         5 |
|         255 |         44 | most_recently_added  | bfs              | lfu             | all               |             0 |         5 |
|         255 |         44 | most_recently_used   | dijkstra         | lru             | all               |             0 |         5 |
|         255 |         44 | most_frequently_used | dijkstra         | lfu             | all               |             0 |         5 |
|         255 |         44 | most_recently_added  | bfs              | lru             | all               |             0 |         5 |
|         255 |         44 | most_frequently_used | bfs              | lru             | all               |             0 |         5 |
|         255 |         44 | most_recently_used   | bfs              | lru             | all               |             0 |         5 |
|         255 |         44 | most_frequently_used | dijkstra         | lru             | all               |             0 |         5 |
|         255 |         44 | most_recently_used   | dijkstra         | lfu             | all               |             0 |         5 |
|         255 |         44 | most_frequently_used | bfs              | lfu             | all               |             0 |         5 |
|         255 |         44 | most_recently_added  | dijkstra         | lfu             | all               |             0 |         5 |
|         255 |         44 | most_recently_added  | dijkstra         | lru             | all               |             0 |         5 |
|         254 |        103 | most_recently_used   | random           | fifo            | all               |             2 |         5 |
|         254 |        103 | most_frequently_used | random           | fifo            | all               |             2 |         5 |
|         168 |         34 | most_recently_used   | random           | fifo            | all               |             0 |         5 |
|         168 |         34 | most_frequently_used | random           | fifo            | all               |             0 |         5 |
|         168 |         34 | most_recently_added  | random           | fifo            | all               |             0 |         5 |

## Memory Size 0

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         353 |        154 | most_frequently_used | random           | lru             | all               |         5 |
|         353 |        154 | most_frequently_used | random           | lfu             | all               |         5 |
|         353 |        154 | most_recently_added  | random           | lru             | all               |         5 |
|         353 |        154 | most_recently_used   | random           | lfu             | all               |         5 |
|         353 |        154 | most_recently_used   | random           | lru             | all               |         5 |
|         353 |        154 | most_recently_added  | random           | lfu             | all               |         5 |
|         259 |         45 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         259 |         45 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         259 |         45 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         259 |         45 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         259 |         45 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         259 |         45 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         255 |         44 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         255 |         44 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         255 |         44 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         255 |         44 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         255 |         44 | most_frequently_used | bfs              | lru             | all               |         5 |
|         255 |         44 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         255 |         44 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         255 |         44 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         255 |         44 | most_recently_added  | bfs              | lru             | all               |         5 |
|         255 |         44 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         255 |         44 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         255 |         44 | most_recently_used   | bfs              | lru             | all               |         5 |
|         168 |         34 | most_frequently_used | random           | fifo            | all               |         5 |
|         168 |         34 | most_recently_added  | random           | fifo            | all               |         5 |
|         168 |         34 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 2

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         667 |        142 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         658 |        148 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         562 |        166 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         508 |        186 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         481 |        106 | most_recently_used   | random           | lfu             | all               |         5 |
|         481 |        106 | most_frequently_used | random           | lfu             | all               |         5 |
|         472 |        202 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         457 |        151 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         417 |         95 | most_frequently_used | bfs              | lru             | all               |         5 |
|         417 |         95 | most_recently_used   | bfs              | lru             | all               |         5 |
|         387 |         73 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         384 |         59 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         384 |         59 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         383 |         85 | most_recently_added  | bfs              | lru             | all               |         5 |
|         337 |        140 | most_recently_added  | random           | lfu             | all               |         5 |
|         327 |         66 | most_recently_added  | random           | lru             | all               |         5 |
|         320 |         65 | most_recently_added  | random           | fifo            | all               |         5 |
|         310 |         72 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         305 |         66 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         304 |         48 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         304 |         48 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         301 |         44 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         301 |         44 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         273 |         69 | most_recently_used   | random           | lru             | all               |         5 |
|         273 |         69 | most_frequently_used | random           | lru             | all               |         5 |
|         254 |        103 | most_frequently_used | random           | fifo            | all               |         5 |
|         254 |        103 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 4

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         618 |        197 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         600 |         59 | most_recently_added  | bfs              | lru             | all               |         5 |
|         580 |        246 | most_frequently_used | random           | lfu             | all               |         5 |
|         561 |        275 | most_recently_added  | random           | lfu             | all               |         5 |
|         561 |        248 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         557 |         62 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         549 |        156 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         523 |        252 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         518 |        103 | most_recently_used   | bfs              | lru             | all               |         5 |
|         518 |        103 | most_frequently_used | bfs              | lru             | all               |         5 |
|         513 |        234 | most_frequently_used | random           | lru             | all               |         5 |
|         513 |        234 | most_recently_used   | random           | lru             | all               |         5 |
|         502 |        190 | most_recently_used   | random           | lfu             | all               |         5 |
|         470 |        117 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         434 |         56 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         434 |         56 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         429 |        161 | most_recently_added  | random           | lru             | all               |         5 |
|         421 |         94 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         420 |         91 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         420 |         91 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         416 |         77 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         403 |         48 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         403 |         48 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         340 |        131 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         292 |         73 | most_recently_added  | random           | fifo            | all               |         5 |
|         291 |         97 | most_frequently_used | random           | fifo            | all               |         5 |
|         291 |         97 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 8

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         902 |         30 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         871 |         63 | most_recently_used   | bfs              | lru             | all               |         5 |
|         853 |         58 | most_recently_added  | bfs              | lru             | all               |         5 |
|         834 |         48 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         670 |        117 | most_recently_added  | random           | lru             | all               |         5 |
|         614 |        150 | most_frequently_used | random           | lru             | all               |         5 |
|         614 |         84 | most_recently_added  | random           | lfu             | all               |         5 |
|         607 |        130 | most_recently_used   | random           | lru             | all               |         5 |
|         588 |        200 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         573 |        263 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         570 |        255 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         563 |        263 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         545 |         54 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         545 |         54 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         545 |         54 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         545 |         54 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         536 |        262 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         526 |        154 | most_frequently_used | bfs              | lru             | all               |         5 |
|         507 |         80 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         507 |         80 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         395 |        225 | most_recently_used   | random           | lfu             | all               |         5 |
|         382 |        176 | most_frequently_used | random           | lfu             | all               |         5 |
|         341 |        133 | most_recently_added  | random           | fifo            | all               |         5 |
|         337 |         87 | most_frequently_used | random           | fifo            | all               |         5 |
|         327 |        142 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         321 |        141 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         307 |         67 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 16

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         899 |         18 | most_recently_added  | bfs              | lru             | all               |         5 |
|         894 |         29 | most_recently_used   | bfs              | lru             | all               |         5 |
|         881 |         35 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         880 |         34 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         719 |         45 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         713 |         53 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         710 |         68 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         701 |         29 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         699 |        107 | most_recently_added  | random           | lru             | all               |         5 |
|         693 |         38 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         686 |        119 | most_recently_added  | random           | lfu             | all               |         5 |
|         674 |         64 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         666 |         42 | most_recently_used   | random           | lru             | all               |         5 |
|         657 |        177 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         652 |        210 | most_recently_used   | random           | lfu             | all               |         5 |
|         602 |        189 | most_frequently_used | random           | lru             | all               |         5 |
|         543 |        210 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         541 |        247 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         528 |        226 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         484 |        170 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         448 |        104 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         430 |        199 | most_frequently_used | random           | lfu             | all               |         5 |
|         418 |        138 | most_recently_added  | random           | fifo            | all               |         5 |
|         397 |         75 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         305 |         55 | most_frequently_used | bfs              | lru             | all               |         5 |
|         276 |         57 | most_frequently_used | random           | fifo            | all               |         5 |
|         272 |         66 | most_recently_used   | random           | fifo            | all               |         5 |

## Memory Size 32

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         896 |         40 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         893 |         40 | most_recently_added  | bfs              | lru             | all               |         5 |
|         877 |         45 | most_recently_used   | bfs              | lru             | all               |         5 |
|         875 |         48 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         825 |        113 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         823 |         34 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         810 |         42 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         810 |         42 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         799 |         50 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         799 |         50 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         797 |        117 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         780 |         24 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         780 |         24 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         780 |        146 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         717 |        104 | most_recently_used   | random           | lfu             | all               |         5 |
|         669 |         74 | most_recently_added  | random           | lfu             | all               |         5 |
|         651 |        132 | most_recently_used   | random           | lru             | all               |         5 |
|         644 |        206 | most_frequently_used | random           | lfu             | all               |         5 |
|         641 |        129 | most_frequently_used | random           | lru             | all               |         5 |
|         636 |        154 | most_recently_added  | random           | lru             | all               |         5 |
|         512 |         81 | most_recently_added  | random           | fifo            | all               |         5 |
|         482 |        192 | most_recently_used   | random           | fifo            | all               |         5 |
|         459 |         80 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         426 |         69 | most_frequently_used | bfs              | lru             | all               |         5 |
|         423 |         65 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         396 |        155 | most_frequently_used | random           | fifo            | all               |         5 |
|         381 |         70 | most_frequently_used | dijkstra         | lfu             | all               |         5 |

## Memory Size 64

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         876 |         57 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         876 |         57 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         863 |         49 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         848 |         65 | most_recently_used   | bfs              | lru             | all               |         5 |
|         848 |         65 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         846 |         76 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         846 |         52 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         846 |         52 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         843 |         38 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         843 |         38 | most_recently_added  | bfs              | lru             | all               |         5 |
|         808 |        101 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         808 |        101 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         791 |         70 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         722 |        125 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         713 |        271 | most_recently_added  | random           | lru             | all               |         5 |
|         685 |        132 | most_recently_used   | random           | lru             | all               |         5 |
|         646 |        126 | most_recently_added  | random           | lfu             | all               |         5 |
|         582 |         75 | most_recently_used   | random           | lfu             | all               |         5 |
|         566 |         89 | most_recently_added  | random           | fifo            | all               |         5 |
|         544 |        193 | most_frequently_used | random           | fifo            | all               |         5 |
|         538 |        149 | most_frequently_used | random           | lru             | all               |         5 |
|         519 |        169 | most_recently_used   | random           | fifo            | all               |         5 |
|         504 |        148 | most_frequently_used | random           | lfu             | all               |         5 |
|         453 |         78 | most_frequently_used | bfs              | lru             | all               |         5 |
|         453 |         78 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         416 |         54 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         368 |        104 | most_frequently_used | dijkstra         | lfu             | all               |         5 |

## Memory Size 128

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         910 |         28 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         906 |         27 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         901 |         41 | most_recently_used   | bfs              | lru             | all               |         5 |
|         901 |         41 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         900 |         26 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         900 |         26 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         897 |         47 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         897 |         47 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         866 |         41 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         866 |         41 | most_recently_added  | bfs              | lru             | all               |         5 |
|         852 |         73 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         852 |         73 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         763 |         86 | most_recently_used   | random           | lfu             | all               |         5 |
|         714 |        122 | most_recently_used   | random           | fifo            | all               |         5 |
|         657 |         98 | most_frequently_used | random           | fifo            | all               |         5 |
|         656 |        151 | most_recently_used   | random           | lru             | all               |         5 |
|         635 |         84 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         635 |         84 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         614 |        183 | most_recently_added  | random           | lru             | all               |         5 |
|         594 |        143 | most_recently_added  | random           | fifo            | all               |         5 |
|         546 |        116 | most_frequently_used | random           | lfu             | all               |         5 |
|         536 |        119 | most_frequently_used | random           | lru             | all               |         5 |
|         487 |        131 | most_recently_added  | random           | lfu             | all               |         5 |
|         420 |        173 | most_frequently_used | bfs              | lru             | all               |         5 |
|         420 |        173 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         414 |         98 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         412 |         97 | most_frequently_used | dijkstra         | lfu             | all               |         5 |

## Memory Size 256

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         927 |         23 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         927 |         23 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         911 |         26 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         911 |         26 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         906 |         24 | most_recently_added  | bfs              | lru             | all               |         5 |
|         906 |         24 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         902 |         37 | most_recently_used   | bfs              | lru             | all               |         5 |
|         902 |         37 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         896 |         39 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         896 |         39 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         888 |         23 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         888 |         23 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         772 |        116 | most_recently_added  | random           | fifo            | all               |         5 |
|         763 |        131 | most_recently_added  | random           | lru             | all               |         5 |
|         745 |         84 | most_recently_added  | random           | lfu             | all               |         5 |
|         731 |        160 | most_recently_used   | random           | fifo            | all               |         5 |
|         725 |        177 | most_recently_used   | random           | lru             | all               |         5 |
|         687 |        217 | most_recently_used   | random           | lfu             | all               |         5 |
|         613 |         90 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         613 |         90 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         547 |        134 | most_frequently_used | random           | fifo            | all               |         5 |
|         490 |         63 | most_frequently_used | bfs              | lru             | all               |         5 |
|         490 |         63 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         423 |        176 | most_frequently_used | random           | lru             | all               |         5 |
|         419 |        179 | most_frequently_used | random           | lfu             | all               |         5 |
|         407 |         82 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         407 |         82 | most_frequently_used | bfs              | lfu             | all               |         5 |

## Memory Size 512

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         908 |         32 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         908 |         32 | most_recently_used   | bfs              | lru             | all               |         5 |
|         904 |         33 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         904 |         33 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         904 |         28 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         904 |         28 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         900 |         19 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         900 |         19 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         896 |         23 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         896 |         23 | most_recently_added  | bfs              | lru             | all               |         5 |
|         894 |         30 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         894 |         30 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         746 |        116 | most_recently_added  | random           | fifo            | all               |         5 |
|         715 |        100 | most_recently_added  | random           | lru             | all               |         5 |
|         715 |        100 | most_recently_added  | random           | lfu             | all               |         5 |
|         652 |         79 | most_recently_used   | random           | lfu             | all               |         5 |
|         646 |         99 | most_recently_used   | random           | fifo            | all               |         5 |
|         644 |         81 | most_recently_used   | random           | lru             | all               |         5 |
|         525 |         97 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         525 |         97 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         487 |         95 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         487 |         95 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         481 |         93 | most_frequently_used | bfs              | lru             | all               |         5 |
|         481 |         93 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         481 |        222 | most_frequently_used | random           | lru             | all               |         5 |
|         481 |        222 | most_frequently_used | random           | lfu             | all               |         5 |
|         470 |        210 | most_frequently_used | random           | fifo            | all               |         5 |

## Memory Size 1024

Total configurations: 27

|   test_mean |   test_std | qa_policy            | explore_policy   | forget_policy   | remember_policy   |   n_seeds |
|------------:|-----------:|:---------------------|:-----------------|:----------------|:------------------|----------:|
|         911 |         34 | most_recently_used   | bfs              | lru             | all               |         5 |
|         911 |         34 | most_recently_used   | dijkstra         | fifo            | all               |         5 |
|         911 |         34 | most_recently_used   | bfs              | fifo            | all               |         5 |
|         911 |         34 | most_recently_used   | dijkstra         | lru             | all               |         5 |
|         911 |         34 | most_recently_used   | dijkstra         | lfu             | all               |         5 |
|         911 |         34 | most_recently_used   | bfs              | lfu             | all               |         5 |
|         900 |         32 | most_recently_added  | dijkstra         | lfu             | all               |         5 |
|         900 |         32 | most_recently_added  | bfs              | lru             | all               |         5 |
|         900 |         32 | most_recently_added  | bfs              | fifo            | all               |         5 |
|         900 |         32 | most_recently_added  | bfs              | lfu             | all               |         5 |
|         900 |         32 | most_recently_added  | dijkstra         | fifo            | all               |         5 |
|         900 |         32 | most_recently_added  | dijkstra         | lru             | all               |         5 |
|         762 |        128 | most_recently_added  | random           | lru             | all               |         5 |
|         762 |        128 | most_recently_added  | random           | fifo            | all               |         5 |
|         762 |        128 | most_recently_added  | random           | lfu             | all               |         5 |
|         631 |         97 | most_recently_used   | random           | lfu             | all               |         5 |
|         631 |         97 | most_recently_used   | random           | fifo            | all               |         5 |
|         631 |         97 | most_recently_used   | random           | lru             | all               |         5 |
|         506 |         92 | most_frequently_used | bfs              | fifo            | all               |         5 |
|         506 |         92 | most_frequently_used | dijkstra         | lfu             | all               |         5 |
|         506 |         92 | most_frequently_used | dijkstra         | fifo            | all               |         5 |
|         506 |         92 | most_frequently_used | bfs              | lfu             | all               |         5 |
|         506 |         92 | most_frequently_used | dijkstra         | lru             | all               |         5 |
|         506 |         92 | most_frequently_used | bfs              | lru             | all               |         5 |
|         473 |        191 | most_frequently_used | random           | lfu             | all               |         5 |
|         473 |        191 | most_frequently_used | random           | fifo            | all               |         5 |
|         473 |        191 | most_frequently_used | random           | lru             | all               |         5 |

