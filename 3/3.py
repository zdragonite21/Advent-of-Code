from statistics import mode

s = [
    list(lines.strip())
    for lines in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/3/input.txt"
    ).readlines()
]

gamma = []
epsilon = []

OGR = s.copy()
CO2 = s.copy()

for i in range(len(s[0])):
    gamma.append(mode([bin[i] for bin in s]))

for l in gamma:
    epsilon.append("1" if l == "0" else "0")


def intersect(str1, str2):
    count = 0
    for x in range(len(str1)):
        if str1[x] == str2[x]:
            count += 1
        else:
            break
    return count


count = [[], []]

for a in s:
    str1 = "".join(a)
    str2 = "".join(gamma)
    count[0].append(intersect(str1, str2))
    str1 = "".join(a)
    str2 = "".join(epsilon)
    count[1].append(intersect(str1, str2))

# for a in range(len(gamma)):
#     for x in list(OGR):
#         if x[a] != gamma[a]:
#             if len(OGR) == 1:
#                 break
#             OGR.remove(x)

# for a in range(len(epsilon)):
#     for x in list(CO2):
#         if x[a] != epsilon[a]:
#             if len(CO2) == 1:
#                 break
#             CO2.remove(x)


# OGR, CO2 = int("".join(OGR[0]), 2), int("".join(CO2[0]), 2)


OGR = int("".join(s[count[0].index(max(count[0]))]), 2)
CO2 = int("".join(s[count[1].index(max(count[1]))]), 2)

print(OGR * CO2)

gamma, epsilon = int("".join(gamma), 2), int("".join(epsilon), 2)

print(gamma * epsilon)
