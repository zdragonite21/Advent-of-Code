from collections import defaultdict
from itertools import combinations

s = open(
    "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/13/input.txt"
).readlines()

s, n = s[:-13], s[-12:]

n = [x[11:].strip().split("=") for x in n]

s1 = []

for a in s:
    x, y = a.strip().split(",")
    x, y = int(x), int(y)
    s1.append((x, y))

s = s1

grid = set()

count = []

for e in n:
    d, r = e
    r = int(r)
    for x, y in s:
        # x=655
        if d == "x":
            if x > r:
                x1 = r - (x - r)
                y1 = y
                grid.add((x1, y1))
            else:
                grid.add((x, y))
        if d == "y":
            if y > r:
                y1 = r - (y - r)
                x1 = x
                grid.add((x1, y1))
            else:
                grid.add((x, y))

    count.append(grid)

    s = list(grid)
    grid = set()

print(count[-1])

# HKGLBZRJ
# JRZBLGKH
