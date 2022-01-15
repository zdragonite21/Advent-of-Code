from collections import defaultdict

s = open(
    "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/12/input.txt"
).readlines()


graph = defaultdict(set)

for a in s:
    r, c = a.strip().split("-")
    graph[r].add(c)
    graph[c].add(r)


def dfs(G, v, seen, part2):
    if v == "end":
        return 1

    d = 0
    for neighbor in G[v]:
        if neighbor not in seen:
            if neighbor == neighbor.lower():
                new = {neighbor}
            else:
                new = set()
            d += dfs(G, neighbor, seen | new, part2)
        elif neighbor != "start" and part2:
            d += dfs(G, neighbor, seen, False)

    return d


print(dfs(graph, "start", {"start"}, False))
print(dfs(graph, "start", {"start"}, True))
