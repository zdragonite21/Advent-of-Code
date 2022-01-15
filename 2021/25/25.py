with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/25/input.txt") as f:
    s = [list(x) for x in f.read().strip().split("\n")]

step = 0

w, h = len(s), len(s[0])


def moveEast():
    global s
    g = [[s[r][c] for c in range(h)] for r in range(w)]
    move = False
    for i in range(len(g)):
        for j in range(len(g[0])):
            a = s[i][j]
            b = s[i][(j + 1) % len(g[0])]
            if a == ">" and b == ".":
                g[i][j] = "."
                g[i][(j + 1) % len(g[0])] = ">"
                move = True
    s = [[g[r][c] for c in range(h)] for r in range(w)]

    if not move:
        return True


def moveSouth():
    global s
    g = [[s[r][c] for c in range(h)] for r in range(w)]
    move = False
    for i in range(len(g)):
        for j in range(len(g[0])):
            a = s[i][j]
            b = s[(i + 1) % len(g)][j]
            if a == "v" and b == ".":
                g[i][j] = "."
                g[(i + 1) % len(g)][j] = "v"
                move = True
    s = [[g[r][c] for c in range(h)] for r in range(w)]
    if not move:
        return True


while True:
    step += 1
    if moveEast() and moveSouth():
        print(step)
        break
