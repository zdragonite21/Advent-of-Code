with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/17/input.txt") as f:
    X, Y = f.read().strip("target area: ").strip().split(", ")

X = list(map(int, X.strip("x=").split("..")))
Y = list(map(int, Y.strip("y=").split("..")))

maxX = X[1] - X[0]
minX = 4
maxY = Y[1] - Y[0]

print(maxX, maxY)

for i in range(1, maxX + 1):
    s = sum((i + j) for j in range(i, 0, -1))
    if s >= 27:
        break
    else:
        print(i, s)

for i in range(1, 50):
    # i is intial y
    s = sum(j for j in range(i, -maxY, -1))
    # adds the decreasing velocity all the way until the velocity is greater than the size
    if s > Y[1]:
        break
    elif s >= Y[0]:
        print(i, s)
