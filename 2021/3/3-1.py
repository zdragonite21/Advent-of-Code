from statistics import mode

s = [
    list(lines.strip())
    for lines in open(
        "C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/3/input.txt"
    ).readlines()
]

gamma = []
epsilon = []

OGR = 0
CO2 = 0

for i in range(len(s[0])):
    gamma.append(mode([bin[i] for bin in s]))

for l in gamma:
    epsilon.append("1" if l == "0" else "0")


def life(nums, sim):
    for i in range(len(s[0])):
        zero = sum(num[i] == "0" for num in nums)
        one = len(nums) - zero
        if sim:
            if one >= zero:
                bit = "1"
            else:
                bit = "0"
        else:
            if one < zero:
                bit = "1"
            else:
                bit = "0"
        nums = [num for num in nums if num[i] == bit]
        if len(nums) == 1:
            return int("".join(nums[0]), 2)


print(life(s[:], False) * life(s[:], True))

gamma, epsilon = int("".join(gamma), 2), int("".join(epsilon), 2)

print(gamma * epsilon)
