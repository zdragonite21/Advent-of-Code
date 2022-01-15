score = 92.57

# calc - 58/100
# chem - 65/100
# World History - 80/100
# AP Chinese - 31/100
# World Lit -- 80/100


def calc(score, percentage):
    return (90 - (score * (1 - percentage))) / percentage


print(calc(score, 0.2))
