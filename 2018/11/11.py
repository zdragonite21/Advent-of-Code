s = 8868

grid = [[0 for x in range(300)] for y in range(300)]

for i in range(len(grid)):
    for j in range(len(grid)):
        rackID = 0
        power = 0
        x, y = i + 1, j + 1
        rackID = x + 10
        power = rackID * y
        power += s
        power *= rackID
        power = int(str(power)[-3])
        power -= 5
        grid[j][i] = power

part1 = []
tl = []

for size in range(1, 301):
    print(size)
    for i in range(0, len(grid) - size):
        for j in range(0, len(grid) - size):
            total = 0
            for q in range(i, i + size):
                for v in range(j, j + size):
                    total += grid[v][q]
            part1.append(total)
            tl.append((i, j))

part1.append(sum(sum(grid[x]) for x in range(len(grid))))
tl.append((0, 0))

print(part1)
print(tl)
print(tl[part1.index(max(part1))])
