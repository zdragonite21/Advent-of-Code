inp = "target area: x=253..280, y=-73..-46"

X, Y = inp.strip("target area: ").split(", ")
X = list(map(int, X.strip("x=").split("..")))
Y = list(map(int, Y.strip("y=").split("..")))

print(X, Y)

vel = 400

velocities = []
ypos = []


for vx in range(1, vel):
  for vy in range(1, vel):
    inv = (vx, vy)
    x, y = 0, 0
    highest = 0
    for step in range(vel):
      x, y = x + vx, y + vy
      highest = max(y, highest)
      vx -= 1 if vx > 0 else 0
      vy -= 1
      if X[0] <= x <= X[1] and Y[0] <= y <= Y[1]:
        velocities.append(inv)
        ypos.append(highest)
      elif x > X[1] or y < Y[1]:
        break
      elif x < X[0] and vx == 0:
        break
      elif vy < (Y[0] - Y[1]):
        break



print("hi")
print(velocities)
print(ypos)
print(max(ypos))
