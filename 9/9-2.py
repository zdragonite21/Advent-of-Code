from itertools import permutations
from math import prod

part1 = 0
part2 = []
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

s = [
    [int(number) for number in num]
    for lines in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/9/input.txt"
    ).readlines()
    for num in lines.split()
]

h, w = len(s), len(s[0])

for a in range(h):
    for b in range(w):
        if any(
            s[a][b] >= s[x][y]
            for i, j in move
            if 0 <= (x := a + i) < h and 0 <= (y := b + j) < w
        ):
            continue

        part1 += s[a][b] + 1

        visited, visiting = [], set([(a, b)])

        while visiting:
            r, c = visiting.pop()
            visited.append((r, c))

            for i, j in move:
                if (
                    0 <= (x := r + i) < h
                    and 0 <= (y := c + j) < w
                    and s[x][y] < 9
                    and (x, y) not in visited
                ):
                    visiting.add((x, y))

        part2.append(len(visited))

print(part1)
print(prod(sorted(part2)[-3:]))
