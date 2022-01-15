with open("2018/3/input.txt") as f:
    s = f.read().strip().split("\n")

id = [int(x.split(" @ ")[0].strip("#")) for x in s]
tl = [tuple(map(int, x.split(" @ ")[1].split(": ")[0].strip().split(","))) for x in s]
area = [tuple(map(int, x.split(" @ ")[1].split(": ")[1].strip().split("x"))) for x in s]

grid = [[0 for x in range(1000)] for y in range(1000)]

for i in range(len(tl)):
    for x in range(tl[i][0], tl[i][0] + area[i][0]):
        for y in range(tl[i][1], tl[i][1] + area[i][1]):
            grid[y][x] += 1

part1 = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] > 1:
            part1 += 1

print(part1)


def part2():
    for i in range(len(tl)):
        intact = True
        for x in range(tl[i][0], tl[i][0] + area[i][0]):
            for y in range(tl[i][1], tl[i][1] + area[i][1]):
                if grid[y][x] != 1:
                    intact = False
        if intact:
            print(i + 1)
            print(id[i])
            return None


part2()
