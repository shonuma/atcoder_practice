import sys

coins = [0,0,0]

target = 0

for i, line_ in enumerate(sys.stdin):
    if i == 0:
        # 500y
        coins[0] = int(line_)
    elif i == 1:
        # 100y
        coins[1] = int(line_)
    elif i == 2:
        # 50y
        coins[2] = int(line_)
    elif i == 3:
        # target
        target = int(line_)

# 50でのあまりが0でない場合は結果がでないので0を出力
if target % 50 != 0:
    print(0)
    sys.exit(0)

# min_combと同様のエントリを作っていく

results = []

# 500円の枚数
for i in range(0, int(target / 500) + 1):
    for j in range(0, int(target / 100) + 1):
        for k in range(0, int(target / 50) + 1):
            if i * 500 + j * 100 + k * 50 == target:
                results.append([i, j, k])

count = 0
for result in results:
    if result[0] <= coins[0] and result[1] <= coins[1] and result[2] <= coins[2]:
        count += 1

print(count)