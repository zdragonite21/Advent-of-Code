with open("2018/1/input.txt") as f:
    s = f.read().strip().split("\n")
    s, c = [int(x[1:]) for x in s], [x[0] for x in s]

part1 = 0

for i, j in enumerate(s):
    if c[i] == "-":
        part1 -= j
    else:
        part1 += j

print(part1)

seen = [0]

part2 = 0

i, j = 0, 0

while True:
    j = s[i]
    if c[i] == "-":
        part2 -= j
    else:
        part2 += j
    # print(part2, i)
    if part2 in seen:
        print(part2)
        break
    seen.append(part2)
    i += 1
    if i > (len(s) - 1):
        i = 0

# for i, j in enumerate(s):
#     if c[i] == "-":
#         part2 -= j
#     else:
#         part2 += j
#     seen.append(part2)
#     if part2 in seen:


# print(seen)
