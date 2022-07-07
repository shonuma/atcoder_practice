import sys

mochis = set()

for i, line_ in enumerate(sys.stdin):
    if i == 0:
        mochi_count = int(line_)
    else:
        mochis.add(line_)

print(len(mochis))