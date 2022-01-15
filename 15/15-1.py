from queue import PriorityQueue
from heapq import heappush, heappop

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/15/input.txt") as f:
    s = [list(map(int, x)) for x in f.read().strip().split("\n")]

print("yay")
l, w = len(s), len(s[0])

openGraph = [(0, 0, 0)]
visited = {(0, 0)}

# def children(x, y):
#     moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
#     valid = []
#     for move in moves:
#         if 0 <= (x_ := x + move[0]) < w and 0 <= (y_ := y + move[1]) < l:
#             valid.append((x_, y_))
#     return valid

scale = 5

while openGraph:
    risk, x, y = heappop(openGraph)
    if (x, y) == (w * scale - 1, l * scale - 1):
        print(risk)
        break
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        x_, y_ = x + dx, y + dy
        if x_ < 0 or y_ < 0 or x_ >= w * scale or y_ >= l * scale:
            continue

        a, a_ = divmod(x_, w)
        b, b_ = divmod(y_, l)
        _risk = (s[b_][a_] + a + b - 1) % 9 + 1
        if (x_, y_) not in visited:
            visited.add((x_, y_))
            heappush(openGraph, (_risk + risk, x_, y_))
