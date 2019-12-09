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
    res = get_param(memory, i, 1, True)
    memory[res] = int(input("Enter an integer!: "))
    return i + 2


def do_output(memory, i):
    res = get_param(memory, i, 1)
    print(res)
    return i + 2

def change_base(memory, i):
    global base
    base += get_param(memory, i, 1)
    return i + 2

################ MAIN PROGRAM ###############

def simulate_program(memory):
    i = 0
    global base
    base = 0
    while i < len(memory):
        opcode = get_opcode(memory[i])
        if opcode == 99:
            break
        if opcode == 1: 
            i = do_add(memory, i)
        if opcode == 2:
            i = do_multiply(memory, i)
        if opcode == 3:
            i = take_input(memory, i)
        if opcode == 4:
            i = do_output(memory, i)
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
    open("input/day9.txt").readline().split(','))))

print("A:") # Write 1
simulate_program(memory.copy())

print("B:") # Write 2
simulate_program(memory.copy())
