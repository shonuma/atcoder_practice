import sys


for i, line_ in enumerate(sys.stdin):
    n, a, b = [int(_) for _ in line_.split(' ')]


res = 0
for i in range(1, n + 1):
    sum_ = sum([int(_) for _ in list(str(i))])
    if sum_ >= a and sum_ <= b:
        res += i
print(res)
# print(n, a, b)