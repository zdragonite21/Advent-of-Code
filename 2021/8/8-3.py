from itertools import permutations

count = 0

s = open(
    "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/8/input.txt"
).readlines()

diction = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

for line in s:
    x, y = line.split(" | ")
    x = x.split()
    y = y.split()
    for per in permutations("abcdefg"):
        converter = str.maketrans("".join(per), "abcdefg")
        x1 = ["".join(sorted(seg.translate(converter))) for seg in x]
        y1 = ["".join(sorted(seg.translate(converter))) for seg in y]
        if all(seg in diction for seg in x1):
            count += int("".join(str(diction[seg]) for seg in y1))
            break

print(count)
