from collections import defaultdict

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/23/input.txt") as f:
    s = f.read().strip().split("\n")

a, b = tuple(s[2:4])
s = [list(x[1 : len(x) - 1]) for x in s[1 : len(s) - 1]]
s[2].append(" ")

print(s)

move = ((0, 1), (-1, 0), (1, 0))

a = list(a.replace("#", ""))
b = list(b.strip(" ").replace("#", ""))

r = list(zip(a, b))

space = [False] * 11


def legal_move(x, y):
    # if s[x]
    if 0 <= y < len(s) and 0 <= x < len(s[0]) and s[y][x] == ".":
        return True
    return False
