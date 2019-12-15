from intcode_class import * 

program = read_program("input/day15.txt")

print("A:")

def draw(world):
    # +/- 1 for margins and to always get origin
    maxWidth = max(world, key = lambda x: x[0])[0] + 1
    maxHeight = max(world, key = lambda x: x[1])[1] + 1
    minWidth = min(world, key = lambda x: x[0])[0] - 1
    minHeight = min(world, key = lambda x: x[1])[1] - 1

    for y in range(minHeight, maxHeight + 1):
        for x in range(minWidth, maxWidth + 1):
            pos = x, y
            if pos == (0, 0):
                sign = "x"
            elif pos == (-12, -12):
                sign = "O"
            elif pos not in world:
                sign = "?"
            elif world[pos] == 0:
                sign = "#"
            elif world[pos] == 1:
                sign = "."
            elif world[pos] == 2:
                sign = "o"
            print(sign, end='')
        print()

dirs = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
discovered = {}
computer = Computer(program)
origins = [((0, 0), computer, 0)]
while origins:
    origin, originComp, steps = origins[0]
    origins = origins[1:]
    for movement in dirs:
        new_pos = tup_add(origin, dirs[movement])
        if new_pos in discovered:
            continue

        # New computer at each... To avoid backtrack - just let go
        computer = originComp.copy()
        computer.run(movement)
        found = computer.output_log[-1]
        discovered[new_pos] = int(found)
        if found == 0: # Wall (did not move) - let go 
            continue
        if found == 1: # Nothing (did move) - keep looking
            origins.append((new_pos, computer, steps + 1))
        if found == 2: # Oxygen! (did move) We're done
            oxygenPos = new_pos
            steps_to_oxygen = steps + 1
            break

print(steps_to_oxygen)

print("B:")

dirs = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
origins = [(oxygenPos, 0)]
minutes = 0
while origins:
    curr, steps = origins[0]
    origins = origins[1:]
    for movement in dirs:
        neighbour = tup_add(curr, dirs[movement])
        if discovered[neighbour] != 1:
            continue
        discovered[neighbour] = 2
        origins.append((neighbour, steps + 1))
        minutes = max(steps + 1, minutes)
print(minutes)
