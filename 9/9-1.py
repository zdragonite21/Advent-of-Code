from itertools import permutations
from math import prod

count = 0

s = [
    [int(number) for number in num]
    for lines in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/9/input.txt"
    ).readlines()
    for num in lines.split()
]


def ind(ls, i, x):
    hor = len(ls[0]) - 1
    ver = len(ls) - 1
    if i == 0:
        if x == hor:
            return [1], [-1]
        if x == 0:
            return [1], [1]
        else:
            return [1], [1, -1]
    if i == ver:
        if x == hor:
            return [-1], [-1]
        if x == 0:
            return [-1], [1]
        else:
            return [-1], [1, -1]
    if x == 0:
        return [-1, 1], [1]
    if x == hor:
        return [-1, 1], [-1]
    return [-1, 1], [-1, 1]


for i in range(len(s)):
    for x in range(len(s[i])):
        x1 = s[i][x]
        if x1 == 9:
            continue
        ver, hor = ind(s, i, x)
        if all(x1 < s[i][x + a] for a in hor) and all(x1 < s[i + a][x] for a in ver):
            count += s[i][x] + 1

print(count)
