from itertools import product
from functools import reduce
data = open("input/day12.txt")
#data = open("test12.txt")

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
states = {tuple(moons)}
revisit = False

while not revisit:
    # Apply gravity
    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            first = list(moons[i])
            second = list(moons[j])
            #if first != second:
            for axis in range(3):
                if first[axis] > second[axis]:
                    first[axis + 3] += -1
                    second[axis + 3] += 1
                if first[axis] < second[axis]:
                    first[axis + 3] += 1 
                    second[axis + 3] += -1
            moons[i] = tuple(first)
            moons[j] = tuple(second)
    # Move
        moons[i] = add_vel(moons[i])

    # Revisit?
    steps += 1
    revisit = tuple(moons) in states
    states.add(tuple(moons))

    # States get very long... How to search efficiently?
    # Need to improve algorithm?


print("B:")
print(steps)
