from queue import PriorityQueue

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/15/input.txt") as f:
    s = [tuple(map(int, x)) for x in f.read().strip().split("\n")]

l, w = len(s), len(s[0])

openGraph = PriorityQueue()
openGraph.put((0, (0, 0)))
visited = set()


def children(x, y):
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    valid = []
    for move in moves:
        if 0 <= (x_ := x + move[0]) < w and 0 <= (y_ := y + move[1]) < l:
            valid.append((x_, y_))
    return valid


while not openGraph.empty():
    risk, cur = openGraph.get()
    visited.add(cur)
    if cur == (w - 1, l - 1):
        print(risk)
        break
    for child in children(cur[0], cur[1]):
        _risk = s[child[1]][child[0]]
        if child in visited:
            continue
        # if (_risk, child) in openGraph:
        #     continue
        openGraph.put((_risk + risk, child))
