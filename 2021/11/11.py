from collections import defaultdict

s = [
    [int(y) for y in x.strip()]
    for x in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/11/input.txt"
    ).readlines()
]

move = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

flashes = 0

tens = []

h, w = len(s), len(s[0])


def stepUp(grid):
    for i in range(h):
        for j in range(w):
            grid[i][j] += 1

    for x in range(h):
        for y in range(w):
            if grid[x][y] == 10:
                tens.append((x, y))
    return grid


def light(x, y, grid):
    for dx, dy in move:
        if 0 <= (x1 := x + dx) < h and 0 <= (y1 := y + dy) < w and grid[x1][y1] < 10:
            grid[x1][y1] += 1
            if grid[x1][y1] == 10:
                tens.append((x1, y1))
    return grid


def countFlash(grid, flash):
    global flashes
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 10:
                flash += 1
                grid[i][j] = 0
    return grid, flash


for step in range(400):
    flash = 0
    s = stepUp(s)
    while tens:
        a, b = tens.pop()
        s = light(a, b, s)
    s, flash = countFlash(s, flash)
    flashes += flash
    if flash == 100:
        print(step + 1)

print(flashes)
