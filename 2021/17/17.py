from collections import defaultdict

with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/17/input.txt") as f:
    x_, y_ = f.read().strip().strip("target area: ").split(", ")

x_ = x_.strip("x=").split("..")
y_ = y_.strip("y=").split("..")

x_ = list(map(int, x_))
y_ = list(map(int, y_))

# x_ = [20, 30]
# y_ = [-10, -5]


pos = (0, 0)

vel = (6, 3)

move = [(-1, -1), (1, -1)]

int_y = []

dic = defaultdict()


def add(ls1, ls2):
    return (ls1[0] + ls2[0], ls1[1] + ls2[1])


for i in range(x_[1] - x_[0]):
    print(i)
    for j in range(y_[1] - y_[0]):
        pos = (0, 0)
        vel = (i, j)
        int_vel = vel[:]
        for step in range(1000):
            pos = add(pos, vel)
            if vel[1] == 0:
                dic[int_vel] = pos
            if x_[0] <= pos[0] <= x_[1] and y_[0] <= pos[1] <= y_[1]:
                print("hit")
                int_y.append(int_vel)
            elif pos[0] > x_[1] or pos[1] < y_[1]:
                print("no hit")
                break

            if vel[0] > 0:
                vel = add(vel, move[0])
            elif vel[0] < 0:
                vel = add(vel, move[1])

ys = max([x[1] for x in int_y])

for x in int_y:
    if ys == x[1]:
        print(dic[x])
