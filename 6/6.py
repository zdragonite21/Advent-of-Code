from collections import defaultdict

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/6/input.txt") as f:
    s = list(map(int, f.read().strip().split(",")))

step = 0

# while step < 10:
#     step += 1
#     stack = 0
#     for i in range(len(s)):
#         if s[i] > 0:
#             s[i] -= 1
#         else:
#             s[i] = 6
#             stack += 1
#     s = s + [8] * stack

# print(len(s))
# # 365131

steps = 0

d = defaultdict(int)

for i in s:
    d[i] += 1

while steps < 256:
    steps += 1
    six = d[0]
    eight = d[0]
    for i in range(1, len(d) + 1):
        d[i - 1] = d[i]
    d[6] += six
    d[8] = eight


print(sum(d.values()))
