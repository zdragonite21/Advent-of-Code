with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/25/input.txt") as f:
    s = [list(x) for x in f.read().strip().split("\n")]

step = 0

w, h = len(s), len(s[0])

while True:
    move = False
    step += 1
    g = [[s[r][c] for c in range(h)] for r in range(w)]
    for i in range(len(g)):
        for j in range(len(g[0])):
            a = s[i][j]
            b = s[i][(j + 1) % len(g[0])]
            if a == ">" and b == ".":
                g[i][j] = "."
                g[i][(j + 1) % len(g[0])] = ">"
                move = True

    g1 = [[g[r][c] for c in range(h)] for r in range(w)]
    for i in range(len(g1)):
        for j in range(len(g1[0])):
            a = g[i][j]
            b = g[(i + 1) % len(g1)][j]
            if a == "v" and b == ".":
                g1[i][j] = "."
                g1[(i + 1) % len(g1)][j] = "v"
                move = True
    if not move:
        print(step)
        break
    s = g1
