import string

with open("2018/5/input.txt") as f:
    s = f.read().strip()


def main(s):
    while True:
        for i in range(1, len(s)):
            if s[i].lower() == s[i - 1].lower() and (
                s[i].islower() == s[i - 1].isupper()
                or s[i].isupper() == s[i - 1].islower()
            ):
                s = s[: (i - 1)] + s[(i + 1) :]
                break
        else:
            return len(s)


part2 = []

for i in string.ascii_lowercase:
    q = s[:]
    q = q.replace(str(i), "")
    q = q.replace(str(i).upper(), "")
    print(i)
    part2.append(main(q))

print(part2)
print(min(part2))

# LOL for part 2 this one took eight minutes
