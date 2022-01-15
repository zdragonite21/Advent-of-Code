from heapq import heappush, heappop

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/23/input.txt") as f:
    s = [tuple(map(int, x)) for x in f.read().strip().split("\n")]

l, w = len(s), len(s[0])

openGraph = PriorityQueue()
openGraph.put((0, (0, 0)))
visited = set()

scale = 5
# ###########
# ...........
# ##B#C#B#D##
# ##A#D#C#A##
# ###########

#  # # # # # # #  #  #  #  #
#  0 1 2 5 6 9 10 13 14 17 18
#  # # 3 # 7 # 11 #  15 #  #
#  # # 4 # 8 # 12 #  16 #  #
#  # # # # # # #  #  #  #  #

while not openGraph.empty():
    risk, cur = openGraph.get()
    visited.add(cur)
    if cur == (w * scale - 1, l * scale - 1):
        print(risk)
        break
    x, y = cur[0], cur[1]
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        x_, y_ = x + dx, y + dy
        if x_ < 0 or y_ < 0 or x_ >= w * scale or y_ >= l * scale:
            continue
        if (x_, y_) in visited:
            continue
        a, a_ = divmod(x_, w)
        b, b_ = divmod(y_, l)
        _risk = (s[a_][b_] + a + b - 1) % 9 + 1
        openGraph.put((_risk + risk, (x_, y_)))
