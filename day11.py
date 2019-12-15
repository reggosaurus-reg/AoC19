from intcode_class import * 

data = list(map(int, open("input/day11.txt").readline().split(',')))

print("A:")

tup_add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def robot(first_color):
    pos = (0, 0) 
    positions = [pos]
    painted = {}
    color = first_color
    dirrIndex = 1
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    computer = Computer(data)
    running = 1

    while (running):
        running = computer.run(color)
        if not running: 
            break
        running = computer.run() 
        color, turn = computer.output_log[-2:] 
        painted[pos] = color
        if turn == 0: # turn "left"
            dirrIndex = (dirrIndex - 1) % 4
        if turn == 1: # turn "right"
            dirrIndex = (dirrIndex + 1) % 4
        pos = tup_add(pos, dirs[dirrIndex])
        color = painted[pos] if pos in painted else 0

    return painted

colors = robot(0)
print(len(colors))

print("B:")

def paint_plate(colors):
    maxWidth = max(colors, key = lambda x: x[0])[0]
    maxHeight = max(colors, key = lambda x: x[1])[1]
    minWidth = min(colors, key = lambda x: x[0])[0]
    minHeight = min(colors, key = lambda x: x[1])[1]

    get_sign = lambda p: 'I' if p in colors and colors[p] else ' '
    for y in range(minHeight, maxHeight + 1):
        for x in range(minWidth, maxWidth + 1):
            print(get_sign((x, y)), end='')
        print()

paint_plate(robot(1))
