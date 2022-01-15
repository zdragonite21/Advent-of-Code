import numpy as n


with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/5/input.txt") as f:
    s = [
        [tuple(map(int, y.split(","))) for y in x.split(" -> ")]
        for x in f.read().strip().split("\n")
    ]

board = [[0 for x in range(1000)] for y in range(1000)]

count = 0

for i in s:
    a, b = i
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        q = min(y1, y2)
        for j in range(abs(y1 - y2) + 1):
            board[q + j][x1] += 1
    elif y1 == y2:
        q = min(x1, x2)
        for j in range(abs(x1 - x2) + 1):
            board[y1][q + j] += 1

    else:
        q1 = x2 - x1
        q2 = y2 - y1
        x_ = n.sign(q1)
        y_ = n.sign(q2)
        x = x1
        y = y1

        while x != x2 and y != y2:
            board[y][x] += 1
            x += x_
            y += y_
        board[y][x] += 1


for i in board:
    for j in i:
        if j > 1:
            count += 1

print(count)
