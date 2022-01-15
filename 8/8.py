s = [i.strip() for i in open(
    "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/8/input.txt")]
n = []

letters = [2, 3, 4, 7]

counter = 0

for i in range(len(s)):
    n.append([])
    a = s[i].split(" | ")
    n[i].append(a[0].split())
    n[i].append(a[1].split())

for i in n:
    i[0] = list(filter(lambda x: len(x) in letters, i[0]))
    i[0] = list(map(lambda x: "".join(sorted(x)), i[0]))

print(n)

for i in n:
    for x in i[1]:
        if "".join(sorted(x)) in i[0]:
            counter += 1

print(counter)
