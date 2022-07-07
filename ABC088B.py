import sys

for i, line_ in enumerate(sys.stdin):
    if i == 0:
        card_count = int(line_)
    elif i == 1:
        cards = [int(_) for _ in line_.split(' ')]

cards.sort(reverse=True)

alice = 0
bob = 0
for i, number in enumerate(cards):
    if i % 2 == 0:
        alice += number
    elif i % 2 == 1:
        bob += number
print(alice - bob)