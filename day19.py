from intcode_class import * 

program = read_program("input/day19.txt")

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
            if pos not in world:
                sign = "?"
            elif world[pos] == 0:
                sign = "."
            elif world[pos] == 1:
                sign = "#"
            print(sign, end='')
        print()

space = {}
pulled = 0
area = 50
for x in range(area):
    for y in range(area):
        computer = Computer(program.copy())
        computer.run_until_end([x, y])
        space[(x, y)] = computer.output_log[-1]
        pulled += computer.output_log[-1]

print(pulled)
draw(space)
