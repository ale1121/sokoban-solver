# Experimental Results

### 1. Beam Search (pull_cost=10, beam_width=10)

[beam_search_10_10.csv](beam_search_10_10.csv)

| Test | Explored States | Pull Moves | Time (s)    |
|------|-----------------|------------|-------------|
| easy_map1       | 40   | 0 | 0.012862682342529297 |
| easy_map2       | 37   | 0 | 0.010638236999511719 |
| medium_map1     | 60   | 0 | 0.09831452369689941  |
| medium_map2     | 130  | 0 | 0.2816891670227051   |
| hard_map1       | 138  | 0 | 0.20992016792297363  |
| hard_map2       | 89   | 0 | 0.1436927318572998   |
| super_hard_map1 | 360  | 2 | 1.140479564666748    |
| large_map1      | 129  | 0 | 1.4969253540039062   |
| large_map2      | 171  | 0 | 4.799420118331909    |


### 2. Beam Search (pull_cost=10, beam_width=70)

[beam_search_10_70.csv](beam_search_10_70.csv)

| Test | Explored States | Pull Moves | Time (s)    |
|------|-----------------|------------|-------------|
| easy_map1       | 54   | 0 | 0.014677047729492188 |
| easy_map2       | 48   | 0 | 0.011864662170410156 |
| medium_map1     | 326  | 0 | 0.5188462734222412   |
| medium_map2     | 849  | 0 | 1.555600881576538    |
| hard_map1       | 887  | 0 | 1.0588595867156982   |
| hard_map2       | 549  | 0 | 0.7769937515258789   |
| super_hard_map1 | 1340 | 0 | 4.022235870361328    |
| large_map1      | 819  | 0 | 6.179705381393433    |
| large_map2      | 998  | 0 | 20.94870400428772    |


### 3. IDA* (pull_cost=1.5)

[ida_star_1_5.csv](ida_star_1_5.csv)

| Test | Explored States | Pull Moves | Time (s)     |
|------|-----------------|------------|--------------|
| easy_map1       | 6    | 0 | 0.0029349327087402344 |
| easy_map2       | 6    | 0 | 0.0025572776794433594 |
| medium_map1     | 8    | 0 | 0.01949310302734375   |
| medium_map2     | 8    | 3 | 0.028412818908691406  |
| hard_map1       | 897  | 2 | 1.6840641498565674    |
| hard_map2       | 1188 | 1 | 4.636122226715088     |
| super_hard_map1 | 5017 | 2 | 18.08839225769043     |
| large_map1      | 15   | 0 | 0.20203256607055664   |
| large_map2      | 391  | 3 | 11.402560234069824    |


### 4. IDA* (pull_cost=10)

[ida_star_10.csv](ida_star_10.csv)

| Test | Explored States | Pull Moves | Time (s)     |
|------|-----------------|------------|--------------|
| easy_map1       | 6    | 0 | 0.0028667449951171875 |
| easy_map2       | 6    | 0 | 0.002791881561279297  |
| medium_map1     | 8    | 0 | 0.02118515968322754   |
| medium_map2     | 404  | 0 | 1.176868200302124     |
| hard_map1       | 1398 | 0 | 2.923788070678711     |
| hard_map2       | 181  | 0 | 0.6594152450561523    |
| super_hard_map1 | -    | - | -                     |
| large_map1      | 15   | 0 | 0.26973438262939453   |
| large_map2      | -    | - | -                     |
