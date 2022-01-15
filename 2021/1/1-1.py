s = [
    int(lines)
    for lines in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/1/input.txt"
    ).readlines()
]

part1, part2, l = 0, 0, len(s)

for i in range(2, l - 1):
    x = s[i] + s[i - 1] + s[i - 2]
    y = s[i + 1] + s[i] + s[i - 1]
    if x < y:
        part2 += 1


print(part2)
