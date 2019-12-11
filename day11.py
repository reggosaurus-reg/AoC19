############### META FUNCIONS ##############


# for an opcode of two digits
get_opcode = lambda code: code % 100
get_address_mode = lambda code, i: code // (10 ** (i + 1)) % 10 


def get_param(memory, i, pos, only_address = False):
    """ Returns the value for the pos:th parameter. """
    mode = get_address_mode(memory[i], pos)
    if mode == 0:
        address = memory[i + pos]  # position mode 
    if mode == 1:
        address = i + pos  # immediate mode
    if mode == 2:
        global base
        address = base + memory[i + pos]  # relative mode 

    if address not in memory:
        memory[address] = 0

    if only_address:
        return address
    else:
        return memory[address]


def do_operation(memory, i, func):
    """ Stores the result of the given func and returns program pointer. """
    op1 = get_param(memory, i, 1)
    op2 = get_param(memory, i, 2)
    res = get_param(memory, i, 3, True) 
    memory[res] = func(op1,  op2)  
    return i + 4


def do_jump(memory, i, func):
    """ Returns the result of the given func as program pointer. """
    op1 = get_param(memory, i, 1)
    op2 = get_param(memory, i, 2)
    return func(op1, op2)


############## OPCODE FUNCIONS ##############

 
do_add          = lambda memory, i: do_operation(memory, i, 
                  (lambda a, b: a + b))
do_multiply     = lambda memory, i: do_operation(memory, i, 
                  (lambda a, b: a * b))
do_less         = lambda memory, i: do_operation(memory, i, 
                  (lambda a, b: a < b))
do_equals       = lambda memory, i: do_operation(memory, i, 
                  (lambda a, b: a == b))
do_true_jump    = lambda memory, i: do_jump(memory, i, 
                  (lambda cond, adr: adr if cond else i + 3))
do_false_jump   = lambda memory, i: do_jump(memory, i, 
                  (lambda cond, adr: adr if not cond else i + 3))

def take_input(memory, i):
    global currInput
    global lastOutput
    global index
    res = get_param(memory, i, 1, True)
    # if index % 2 == 0:
    #     memory[res] = currInput
    # else:
    #     memory[res] = lastOutput
    memory[res] = lastOutput
    if index != -1:
        index += 1
    return i + 2


def do_output(memory, i):
    global lastOutput
    res = get_param(memory, i, 1)
    lastOutput = res
    return i + 2


# def take_input(memory, i):
#     res = get_param(memory, i, 1, True)
#     memory[res] = int(input("Enter an integer!: "))
#     return i + 2
# 
# 
# def do_output(memory, i):
#     res = get_param(memory, i, 1)
#     print(res)
#     return i + 2

def change_base(memory, i):
    global base
    base += get_param(memory, i, 1)
    return i + 2

################ MAIN PROGRAM ###############


def simulate_program(memory, i):
    global base
    base = 0
    while i < len(memory):
        opcode = get_opcode(memory[i])
        if opcode == 99:
            return -1
        if opcode == 1: 
            i = do_add(memory, i)
        if opcode == 2:
            i = do_multiply(memory, i)
        if opcode == 3:
            i = take_input(memory, i)
        if opcode == 4:
            i = do_output(memory, i)
            return i
        if opcode == 5: 
            i = do_true_jump(memory, i)
        if opcode == 6: 
            i = do_false_jump(memory, i)
        if opcode == 7:
            i = do_less(memory, i)
        if opcode == 8:
            i = do_equals(memory, i)
        if opcode == 9:
            i = change_base(memory, i)

################ DAY SPECIFIC ###############


memory = dict(enumerate(map(int, 
    open("input/day11.txt").readline().split(','))))

print("A:") # Write 1

tup_add = lambda a, b: (a[0] + b[0], a[1] + b[1])

def run_continuously(memory, firstInput):
    """ DOESN'T RUN CONTINUOUSLY ATM; ONLY A MALL. """
    global index
    global currInput
    global lastOutput
    global paints 
    index = 0
    #currInput = firstInput
    lastOutput = firstInput
    is_running = lambda p: p != -1
    dirr = (0, -1) # Facing up
    pos = (0, 0)
    paints = {pos: lastOutput}
    get_color = lambda p: paints[pos] if pos in paints else 0
    pointer = 0
    dirrIndex = 1 # facing up - left = left, right = right
    dirrs = [(-1, 0), (0, -1), (1, 0), (0, 1)] # left, up, right, down

    while (pointer != -1):
            index = -1
            pointer = simulate_program(memory, pointer)
            color = lastOutput 
            print("------")
            print(color)
            paints[pos] = color
            if pointer == -1:
                return
            pointer = simulate_program(memory, pointer)
            turn = lastOutput   
            if turn == 0: # turn "left"
                dirrIndex = (dirrIndex - 1) % 4
            if turn == 1: # turn "right"
                dirrIndex = (dirrIndex + 1) % 4
            pos = tup_add(pos, dirrs[dirrIndex])
            lastOutput = get_color(pos)
            print(turn, pos)


run_continuously(memory.copy(), 0) # All panels black at start
print(len(paints))

print("B:") 
#run_continuously(memory.copy(), 1)

width = max(paints, key = lambda x: abs(x[0]))
height = max(paints, key = lambda x: abs(x[1]))
width = abs(width[0])
height = abs(height[1])
#print(width, height)

#get_sign = lambda p: '#' if p in paints and paints[p] else '.'
#for x in range(width):
#    for y in range(height):
#        print(get_sign((x, y)), end='')
#    print()
#print(lastOutput)
