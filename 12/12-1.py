from collections import defaultdict

s = sorted(
    [
        x.strip().split("-")
        for x in open(
            "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/12/input.txt"
        ).readlines()
    ]
)

graph = defaultdict(list)

elem = set()

for a in s:
    r, c = a[0], a[1]
    graph[r].append(c)
    if r != "start" and c != "end":
        graph[c].append(r)

for a in s:
    elem.add(a[0])
    elem.add(a[1])

V = len(elem)

print(graph, V)

visited = set()

conv = list(graph.keys())


# def DFS(x, visited, graph):
#     if x == "end":
#         return
#     if x == "start" or x.islower():
#         visited.add(x)
#     print(x, end=" ")

#     for neighbour in graph[x]:
#         if neighbour not in visited:
#             DFS(neighbour, visited, graph)


def counter(start, end):
    visited = [False] * V

    pathCount = [0]
    countPathsUtil(start, end, visited, pathCount)
    return pathCount[0]


def countPathsUtil(u, d, visited, pathCount):
    visited[conv.index(u)] = True

    if u == d:
        pathCount[0] += 1

    else:

        i = 0
        while i < len(graph[u]):
            if not visited[conv.index(graph[u][i])]:
                countPathsUtil(graph[u][i], d, visited, pathCount)
            i += 1

    visited[conv.index(u)] = False


print(counter("start", "end"))
