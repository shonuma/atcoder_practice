import sys

for i, line_ in enumerate(sys.stdin):
    n, target = [int(_) for _ in line_.split(' ')]

# N: 枚数, Y: 金額

# 1000円札の枚数は決まっている
# 0枚の場合は5になる
# initial = int(target % 5000 / 1000)
# interval = int(target % 5000 / 1000) or 5

# 1,000
# for i in range(initial, n + 1, interval):
for i in range(0, n + 1):
    # 5,000
    for j in range(0, n + 1):
        # 10,000
        # この時点で10000の枚数は決まる
        if i + j > n:
            break
        price = i * 1000 + j * 5000 + (n - i - j) * 10000
        if price == target:
            print(n - i - j, j, i)
            sys.exit(0)
"""
        for k in range(0, n + 1):
            price = i * 1000 + j * 5000 + k * 10000
            # print(price, i, j, k)
            if price == target and i + j + k == n:
                print(k, j, i)
                sys.exit(0)
            if price > target:
                break
            if i + j + k > n:
                break
"""
print(-1, -1, -1)