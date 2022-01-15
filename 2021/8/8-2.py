from itertools import permutations

s = [
    i.split(" | ")
    for i in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/8/input.txt"
    ).readlines()
]
letters = ["a", "b", "c", "d", "e", "f", "g"]
numerical = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6],
]
correct = sorted(numerical)
n = []
bruter = []
total = 0
for i, j in s:
    l = ["".join(sorted(x)) for x in i.split()]
    x = ["".join(sorted(k)) for k in j.split()]
    n.append([l, x])


def bruteforce(lets):
    return permutations(lets, len(lets))


bruter = list(bruteforce(letters))


def magic():
    # where all the magic happens
    for i in bruter:
        number = []
        for x in n:
            for b in x[0]:
                number.append(sorted([i.index(g) for g in b]))

        print(number)
        if sorted(number) == correct:
            print(i)
            # add(i)


def add(ls):
    global total
    number = []
    numstr = ""
    for i in ls:
        number.append([s.index(b) for b in i])
    for i in number:
        numstr += str(numerical.index(i))

    total += int(numstr)


magic()

print(total)
