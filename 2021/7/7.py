from math import floor

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/7/input.txt") as f:
    s = list(map(int, f.read().strip().split(",")))

s.sort()

a = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
b = [0, 1, 2, 4, 7, 14, 16]

num = s[len(s) // 2]


def avg(ls):
    return sum(ls) // len(ls)


def bruter(n):
    return sum(i for i in range(1, n + 1))


mean = floor((sum(s) + 1) / len(s))

print(sum(bruter(abs(x - mean)) for x in s))
# 87640209


# first method lol brute force dummy

# i = 0
# new = 0
# low = 100000000000000
# while i < 2000:
#     new = sum(bruter(abs(x - i)) for x in s)
#     low = min(low, new)
#     i += 1
#     print(i)


# print(low)

# hahhahah so sad but ok

# print(sum(abs(num - x) for x in s))
