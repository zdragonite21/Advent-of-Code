from queue import PriorityQueue

q = PriorityQueue()

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/15/input.txt") as f:
    s = [tuple(map(int, x)) for x in f.read().strip().split("\n")]

l, w = len(s), len(s[0])

openGraph = [(0, 0)]
visited = set()

q.put((1, (0, 0)))
q.put((6, (0, 0)))
q.put((8, (23, 83)))
q.put((3, (100000, 10000)))

while not q.empty():
    print(q.get())

print(1 & 9)
