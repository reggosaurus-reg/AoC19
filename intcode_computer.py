## The elf ship's intcode computer so far ##


############### META FUNCIONS ##############


# for an opcode of two digits
get_opcode = lambda code: code % 100
get_address_mode = lambda code, i: code // (10 ** (i + 1)) % 10 


def get_param(seq, i, pos):
    """ Returns the value for the pos:th parameter. """
    mode = get_address_mode(seq[i], pos)
    if mode == 0:
        return seq[seq[i + pos]]  # position mode 
    else:
        return seq[i + pos]  # immediate mode


def do_operation(seq, i, func):
    """ Stores the result of the given func and returns program pointer. """
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    res = seq[i + 3]
    seq[res] = func(op1,  op2)  
    return i + 4


def do_jump(seq, i, func):
    """ Returns the result of the given func as program pointer. """
    op1 = get_param(seq, i, 1)
    op2 = get_param(seq, i, 2)
    return func(op1, op2)


############## OPCODE FUNCIONS ##############

 
do_add          = lambda seq, i: do_operation(seq, i, 
                  (lambda a, b: a + b))
do_multiply     = lambda seq, i: do_operation(seq, i, 
                  (lambda a, b: a * b))
do_less         = lambda seq, i: do_operation(seq, i, 
                  (lambda a, b: a < b))
do_equals       = lambda seq, i: do_operation(seq, i, 
                  (lambda a, b: a == b))
do_true_jump    = lambda seq, i: do_jump(seq, i, 
                  (lambda cond, adr: adr if cond else i + 3))
do_false_jump   = lambda seq, i: do_jump(seq, i, 
                  (lambda cond, adr: adr if not cond else i + 3))


def take_input(seq, i):
    res = seq[i + 1]
    seq[res] = int(input("Enter an integer!: "))
    return i + 2


def do_output(seq, i):
    res = seq[i + 1]
    print(seq[res])
    return i + 2


################ MAIN PROGRAM ###############


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
            i = take_input(seq, i)
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
