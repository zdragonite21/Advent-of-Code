fwd, dwn, up, s = [], [], [], []
part1, part2 = 0, 0


for lines in open(
    "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/2/input.txt"
).readlines():
    line = lines.split()
    if line[0] == "forward":
        fwd.append(int(line[1]))
        s.append((0, int(line[1])))
    elif line[0] == "down":
        dwn.append(int(line[1]))
        s.append((1, int(line[1])))
    else:
        up.append(int(line[1]))
        s.append((2, int(line[1])))

part1 = sum(fwd) * (sum(dwn) - sum(up))
print(part1)

hor, aim, depth = 0, 0, 0
for i in s:
    if i[0] == 0:
        hor += i[1]
        depth += aim * i[1]
    elif i[0] == 1:
        aim += i[1]
    else:
        aim -= i[1]

part2 = hor * depth

print(part2)
