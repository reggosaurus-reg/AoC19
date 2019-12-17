from intcode_class import * 

program = read_program("input/day17.txt")

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
            elif pos == (-12, -12): # Ugly hardcoded...
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
scaffolds = {}
computer = Computer(program.copy())
computer.run_until_end()
chars = list(map(chr, computer.output_log))

row = 0
column = 0
for i in range(len(chars)):
    char = chars[i]
    if char == '#':
        scaffolds[(row, column)] = '#'
    if char == '^':
        current_pos = (row, column)
        scaffolds[(row, column)] = '#' # No need but still
    column += 1
    if char == '\n':
        row += 1
        column = 0
        continue

alignment_sum = 0
for pos in scaffolds: # TODO: Use dirs and map or something
    if tup_add(pos, (1, 0)) in scaffolds \
    and tup_add(pos, (-1, 0)) in scaffolds \
    and tup_add(pos, (0, 1)) in scaffolds \
    and tup_add(pos, (0, -1)) in scaffolds:
            alignment_sum += pos[0] * pos[1]

print(alignment_sum)

print("B:")

computer = Computer(program.copy())
computer.memory[0] = 2

# Path to walk:

dirr = (-1, 0) # inverted... Computer is mirrored on y
path = ""
turn = "X"
steps = 0
walked = 0
new_scaffolds = {} 
finished = False
while not finished: 
    old_pos = current_pos
    #print(current_pos, steps, dirr)
    new_pos_up = tup_add(current_pos, dirr) 
    new_pos_right = tup_add(current_pos, (- dirr[1], dirr[0]))
    new_pos_left = tup_add(current_pos, (dirr[1], - dirr[0]))

    new_scaffolds[current_pos] = 'x'
    if new_pos_up in scaffolds: # Go forward  
        current_pos = new_pos_up 
        steps += 1
        continue

    # Need to turn
    q = turn + "," + str(steps) + "," 
    path += turn + "," + str(steps) + "," 
    steps = 0

    walked += 1

    if new_pos_left in scaffolds: # Turn left
        dirr = (dirr[1], - dirr[0])
        turn = "R" # Since mirrored in y 
    elif new_pos_right in scaffolds: # Turn right
        dirr = (- dirr[1], dirr[0])
        turn = "L" # Since mirrored in y 
    else:
        finished = True

path = path[4:-1]

# for i in range(51):
#     for j in range(51):
#         print(new_scaffolds[(i, j)] if (i, j) in new_scaffolds else ".", end='')
#     print()
         

# Construct routines (NOT more than 20 chars including commas!)
"""
L,8,R,10,L,8,R,8,L,12,R,8,R,8,L,8, R,10,L,8,R,8,L,8, R,6,R,6,R,10,L,8 ,L,8,R,6,R,6,R,10,L,8,
L,8,R,10,L,8,R,8,L,12,R,8,R,8,L,8, R,6,R,6,R,10,L,8, L,12,R,8,R,8,L,12,R,8,R,8
"""
"""
ABAC DCC ABAC AEEBA AEEBA ABAC DCC AEEBA DCC DCC
"""
main = "A,B,A,C,C,A,B,C,B,B"
A = "L,8,R,10,L,8,R,8"
B = "L,12,R,8,R,8"
C = "L,8,R,6,R,6,R,10,L,8"

def give_function(func):
    computer.run(list(map(ord,func)) + [ord('\n')])

give_function(main)
give_function(A)
give_function(B)
give_function(C)

# Run with visual feed (y/n)
computer.run_until_end([ord('n'), ord('\n')])

# Visualize visual feed (output_log)
chars = list(map(chr, computer.output_log))
#for c in chars:
#    print(c, end = '')

dust = computer.output_log[-1]
print(dust)
