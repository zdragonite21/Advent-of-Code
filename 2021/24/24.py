with open("C:/Users/Zachary/Downloads/Python/Advent Of Code/2021/24/input.txt") as f:
    s = f.read().strip().split("\n")
s = [tuple(x.split(" ")) for x in s]

x, y, z, w = 0, 0, 0, 0


def inp(a):
    global x, y, z, w
    w = int(a)


def ad(a, b):
    global x, y, z, w
    globals()[a] = int(globals()[a]) + int(b)


def mul(a, b):
    global x, y, z, w
    globals()[a] = int(globals()[a]) * int(b)


def div(a, b):
    global x, y, z, w
    globals()[a] = int(globals()[a]) / int(b)


def mod(a, b):
    global x, y, z, w
    globals()[a] = int(globals()[a]) % int(b)


def eql(a, b):
    global x, y, z, w
    globals()[a] = 1 if a == b else 0


ALU = {
    "inp": inp,
    "add": ad,
    "mul": mul,
    "div": div,
    "mod": mod,
    "eql": eql,
}

x = 2

ALU["mul"]("x", 4)

print(x)

i = 100000000000000

while True:
    i -= 1
    if "0" in str(i):
        continue
    print(i)
    if i < 9999999999999:
        break
