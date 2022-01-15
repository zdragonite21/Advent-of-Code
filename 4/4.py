with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/4/input.txt") as f:
    s = f.read().strip().split("\n\n")

call = list(map(int, s[0].split(",")))

boards = [
    [
        [int(z) for z in filter(lambda x: False if x == "" else True, y.split(" "))]
        for y in x.split("\n")
    ]
    for x in s[1:]
]

mark = [
    [[0 for z in range(len(boards[0][0]))] for y in range(len(boards[0]))]
    for x in range(len(boards))
]

winners = [False for x in boards]


def winner():
    for i in range(len(boards)):
        for j in range(len(boards[0])):
            if all(x == 1 for x in mark[i][j]):
                winners[i] = True
            elif all(mark[i][x][j] == 1 for x in range(len(mark[i][j]))):
                winners[i] = True
            if all(winners):
                return sum(
                    boards[i][x][y]
                    for x in range(len(mark[i]))
                    for y in range(len(mark[i][x]))
                    if mark[i][x][y] == 0
                )


def main():
    while True:
        for n in call:
            for x in range(len(boards)):
                if winners[x]:
                    continue
                for y in range(len(boards[0])):
                    for z in range(len(boards[0][0])):
                        if boards[x][y][z] == n:
                            mark[x][y][z] = 1
            total = winner()
            if total:
                return total * n


print(main())
