from itertools import product
from functools import reduce
data = open("input/day12.txt")

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
    moon['pos'] = pos 
    moon['vel'] = [0, 0, 0]
    moons.append(moon)

print("A:")

# Change to {pos: (x, y, z), vel: (xyz)} ?

tup_add = lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2])

steps = 0

while steps < 1000:
    # Apply gravity
    for first in moons:
        for second in moons: 
            if first != second:
                #print(first, second)
                for axis in range(3):
                    if first['pos'][axis] > second['pos'][axis]:
                        first['vel'][axis] += -0.5 # Should be 1, but counts every pair twice...
                        second['vel'][axis] += 0.5
                    if first['pos'][axis] < second['pos'][axis]:
                        first['vel'][axis] += 0.5 
                        second['vel'][axis] += -0.5
    
    # Move
    for moon in moons:
        vel = moon['vel']
        moon['pos'] = tup_add(moon['pos'], vel)

    steps += 1

energies = []
add = lambda a, b: abs(a) + abs(b)
for moon in moons:
    pot = reduce(add, moon['pos'])
    kin = reduce(add, moon['vel'])
    energies.append((pot, kin))

totalify = lambda t: t[0] * t[1]
total = int(reduce(add, map(totalify, energies)))
print(total)
