data = open("input/day5.txt")
seqA = list(map(int, data.readline().split(',')))
seqB = seqA.copy()

get_opcode = lambda code: code % 100
get_mode = lambda code, i: (code % (10**(i + 2))) // (10**(i + 1)) 

print("A: ")

def get_param(seq, i, pos):
    """ Returns the value for the pos:th parameter. """
    mode = get_mode(seq[i], pos)
    if mode == 0:
        return seq[seq[i + pos]]
    else:
        return seq[i + pos]

def do_add(seq, i):
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    res = seq[i + 3]
    seq[res] = op1 + op2  
    return i + 4

def do_multiply(seq, i):
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    res = seq[i + 3]
    seq[res] = op1 * op2  
    return i + 4

def take_input(seq, i, default):
    res = seq[i + 1]
    seq[res] = int(input("Enter an integer! ({} for default elf TEST): ".format(default)))
    return i + 2

def do_output(seq, i):
    res = seq[i + 1]
    print(seq[res])
    return i + 2

def simulate_program(seq):
    i = 0
    while i < len(seq):
        opcode = get_opcode(seq[i])
        if opcode == 99:
            break
        if opcode == 1: 
            i = do_add(seq, i)
        if opcode == 2:
            i = do_multiply(seq, i)
        if opcode == 3:
            i = take_input(seq, i, 1)
        if opcode == 4:
            i = do_output(seq, i)

simulate_program(seqA)

print("B: ")

def do_true_jump(seq, i):
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    if op1:
        return op2
    else:
        return i + 3

def do_false_jump(seq, i):
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    if not op1:
        return op2
    else:
        return i + 3

def do_less(seq, i):
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    res = seq[i + 3]
    seq[res] = op1 < op2
    return i + 4

def do_equals(seq, i):
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    res = seq[i + 3]
    seq[res] = op1 == op2
    return i + 4

def simulate_warmer_program(seq):
    i = 0
    while i < len(seq):
        opcode = get_opcode(seq[i])
        if opcode == 99:
            break
        if opcode == 1: 
            i = do_add(seq, i)
        if opcode == 2:
            i = do_multiply(seq, i)
        if opcode == 3:
            i = take_input(seq, i, 5)
        if opcode == 4:
            i = do_output(seq, i)
        if opcode == 5: 
            i = do_true_jump(seq, i)
        if opcode == 6: 
            i = do_false_jump(seq, i)
        if opcode == 7:
            i = do_less(seq, i)
        if opcode == 8:
            i = do_equals(seq, i)

simulate_warmer_program(seqB)
