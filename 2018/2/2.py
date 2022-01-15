from collections import defaultdict

with open("2018/2/input.txt") as f:
    s = f.read().strip().split("\n")


twos = 0
threes = 0

for i in s:
    d = defaultdict(int)
    for j in range(len(i)):
        d[i[j]] += 1

    a = 0
    b = 0
    for x in d.values():
        if x == 2:
            a += 1
        if x == 3:
            b += 1
    if a >= 1:
        twos += 1
    if b >= 1:
        threes += 1

print(twos * threes)


def returnChar(a, b):
    count = 0
    remove = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
        else:
            remove = i
    return (len(a) - count, remove)


def main():
    for i in range(len(s)):
        for x in range(len(s)):
            u, t = returnChar(s[i], s[x])
            if u == 1:
                print(s[i][0:t] + s[i][(t + 1) :])
                return None


main()
