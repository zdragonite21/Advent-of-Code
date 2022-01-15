from collections import defaultdict

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/14/input.txt") as f:
    tpl, s = f.read().strip().split("\n\n")

d = defaultdict()

# PKHOVVOSCNVHHCVVCBOH

for line in s.split("\n"):
    key, val = line.split(" -> ")
    d[key] = val

# tpl_ = list(tpl)

# step = 10
# while step > 0:
#     print(step)
#     a = 0

#     for i in range(len(tpl_) - 1):
#         i += a
#         pair = "".join(tpl_[i : i + 2])
#         tpl_.insert(i + 1, d[pair])
#         a += 1
#     step -= 1

# cnt = defaultdict(int)

# for i in tpl_:
#     cnt[i] += 1
# x = list(cnt.values())
# print(max(x) - min(x))

cnt = defaultdict(int)

for i in range(len(tpl) - 1):
    cnt[tpl[i : i + 2]] += 1

step = 40
while step > 0:
    print(step)
    cnt_ = defaultdict(int)
    for pair in cnt:
        l, r = pair
        m = d[pair]
        cnt_[l + m] += cnt[pair]
        cnt_[m + r] += cnt[pair]

    cnt = cnt_
    step -= 1

cnt__ = defaultdict(int)
for pair in cnt:
    l, r = pair
    cnt__[l] += cnt[pair]

cnt__[tpl[-1]] += 1

x = list(cnt__.values())

print(max(x) - min(x))
