from itertools import product
from functools import reduce
from math import gcd
data = open("input/day12.txt")

# Load moon data
moonsA = []
for i in range(4): 
    row = data.readline()
    seq = list(row[1:-2].split(', '))
    pos = []
    for j in range(3):
        elem = seq[j]
        val = int(elem[2:])
        pos.append(val)
    moon = pos + [0, 0, 0]
    moonsA.append(tuple(moon))
moonsB = moonsA.copy()

add = lambda a, b: abs(a) + abs(b)
totalify = lambda t: t[0] * t[1]
add_vel = lambda a: (a[0] + a[3], a[1] + a[4], a[2] + a[5], a[3], a[4], a[5])
update_vel = lambda tup, axis, val: tup[:axis] + (val + tup[axis],) + tup[axis + 1:]  

print("A:")

steps = 0
while steps < 1000:
    # Update
    for nr in range(len(moonsB)):
        for i in range(nr + 1, len(moonsB)):
            first = moonsA[nr]
            second = moonsA[i]
            # Apply gravity
            for axis in range(3):
                if first[axis] > second[axis]:
                    first = update_vel(first, axis + 3, -1)
                    second = update_vel(second, axis + 3, 1)
                if first[axis] < second[axis]:
                    first = update_vel(first, axis + 3, 1)
                    second = update_vel(second, axis + 3, -1)
            moonsA[nr] = first
            moonsA[i] = second
            
        # Move
        moonsA[nr] = add_vel(moonsA[nr])

    steps += 1

energies = []
for moon in moonsA:
    pot = reduce(add, moon[:3])
    kin = reduce(add, moon[3:])
    energies.append((pot, kin))

total = int(reduce(add, map(totalify, energies)))
print(total)

print("B:")

def lcm(a, b):
    return (a * b) // gcd(a, b)

steps = 0
states = [{} for _ in range(3)]
cycle = [False for _ in range(3)]
first_state = None
while not all(cycle):
    # Update
    for nr in range(len(moonsB)):
        for i in range(nr + 1, len(moonsB)):
            first = moonsB[nr]
            second = moonsB[i]
            # Apply gravity
            for axis in range(3):
                if first[axis] > second[axis]:
                    first = update_vel(first, axis + 3, -1)
                    second = update_vel(second, axis + 3, 1)
                if first[axis] < second[axis]:
                    first = update_vel(first, axis + 3, 1)
                    second = update_vel(second, axis + 3, -1)
            moonsB[nr] = first
            moonsB[i] = second
            
        # Move
        moonsB[nr] = add_vel(moonsB[nr])

    steps += 1

    # Save axis wise
    new_state = []
    for axis in range(3):
        new_state.append(tuple((moon[axis], moon[axis + 3]) for moon in moonsB))
    new_state = tuple(new_state)


    # Revisit?
    for axis in range(3):
        if (old := states[axis].get(new_state[axis])) is not None and not cycle[axis]:
            cycle[axis] = steps - old 
            #print(nr, moonsB[nr], "at delta", steps - old, moonsB[nr] == origin[nr])
        else:
            states[axis][new_state[axis]] = steps

print(reduce(lcm, cycle))
