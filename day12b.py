from itertools import product
from functools import reduce
data = open("input/day12.txt")
data = open("test12.txt")

# Load moon data
moons = []
for i in range(4): 
    row = data.readline()
    seq = list(row[1:-2].split(', '))
    moon = {}
    pos = []
    for j in range(3):
        elem = seq[j]
        val = int(elem[2:])
        pos.append(val)
    moon = tuple(pos + [0, 0, 0]) 
    moons.append(moon)

print(moons)
print("A:")

# [(moon), (xP, yP, zP, xV, yV, zV)]

add_vel = lambda a: (a[0] + a[3], a[1] + a[4], a[2] + a[5], a[3], a[4], a[5])

steps = 0

while steps < 10:
    # Apply gravity
    for i in range(len(moons)):
        for j in range(len(moons)):
            first = list(moons[i])
            second = list(moons[j])
            if first != second:
                for axis in range(3):
                    if first[axis] > second[axis]:
                        first[axis + 3] += -0.5 # 1, but counts every pair twice...
                        second[axis + 3] += 0.5
                    if first[axis] < second[axis]:
                        first[axis + 3] += 0.5 
                        second[axis + 3] += -0.5
            moons[i] = tuple(first)
            moons[j] = tuple(second)
    
    # Move
    for i in range(len(moons)):
        moons[i] = add_vel(moons[i])

    steps += 1

energies = []
add = lambda a, b: abs(a) + abs(b)
for moon in moons:
    pot = reduce(add, moon[:3])
    kin = reduce(add, moon[3:])
    energies.append((pot, kin))

totalify = lambda t: t[0] * t[1]
total = int(reduce(add, map(totalify, energies)))
print(total)
