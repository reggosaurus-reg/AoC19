############### META FUNCIONS ##############


# for an opcode of two digits
get_opcode = lambda code: code % 100
get_address_mode = lambda code, i: code // (10 ** (i + 1)) % 10 


def get_param(memory, i, pos, only_address = False):
    """ Returns the value for the pos:th parameter. """
    mode = get_address_mode(memory[i], pos)
    if mode == 0:
        address = memory[i + pos]  # position mode 
    elif mode == 1:
        address = i + pos  # immediate mode
    elif mode == 2:
        global base
        address = base + memory[i + pos]  # relative mode 
    else:
        raise Exception("Invalid mode {}!".format(mode))

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
    global curr_io
    global pad_pos
    global game # TODO: Move into move_pad()
    res = get_param(memory, i, 1, True)
    delta = int(input("Move (-1, 0, 1): "))
    memory[res] = delta
    old_pos = pad_pos
    pad_pos = (pad_pos[0] + delta, pad_pos[1])
    game[old_pos] = game[pad_pos]
    game[pad_pos] = "_"
    return i + 2


def do_output(memory, i):
    global curr_io
    curr_io = get_param(memory, i, 1)
    return i + 2

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
        elif opcode == 1: 
            i = do_add(memory, i)
        elif opcode == 2:
            i = do_multiply(memory, i)
        elif opcode == 3:
            i = take_input(memory, i)
        elif opcode == 4:
            i = do_output(memory, i)
            return i
        elif opcode == 5: 
            i = do_true_jump(memory, i)
        elif opcode == 6: 
            i = do_false_jump(memory, i)
        elif opcode == 7:
            i = do_less(memory, i)
        elif opcode == 8:
            i = do_equals(memory, i)
        elif opcode == 9:
            i = change_base(memory, i)
        else:
            raise Exception("Invalid opcode {}!".format(opcode))

################ DAY SPECIFIC ###############


memory = dict(enumerate(map(int, 
    open("input/day13.txt").readline().split(','))))

print("A:")

def count_blocks(memory, first_input):
    global curr_io
    curr_io = first_input
    pointer = 0
    blocks = 0
    game = {}
    while (pointer != -1):
        pointer = simulate_program(memory, pointer)
        x = curr_io
        if pointer == -1:
            break
        pointer = simulate_program(memory, pointer)
        y = curr_io
        if pointer == -1:
            break
        pointer = simulate_program(memory, pointer)
        if curr_io == 2:
            blocks += 1
    print(blocks)


count_blocks(memory.copy(), 1)

print("B:")

import os
import time

def draw_board(data, score):
    width = max(data, key=lambda a: a[0])[0]
    height = max(data, key=lambda a: a[1])[1]
    board = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(data[x, y])
        board.append(row)

    for y in range(height):
        for x in range(width):
            char = board[y][x]
            if char == "B:":
                print(char + str(score))
                continue
            print(char, end='')
        print()

def has_won(game):
    return not "#" in game.values() 

def play_pong(memory, first_input):
    global curr_io
    global game
    global pad_pos
    curr_io = first_input
    pointer = 0
    blocks = 0
    score = 0
    game = {}
    while (pointer != -1):
        pointer = simulate_program(memory, pointer)
        x = curr_io
        if pointer == -1:
            break
        pointer = simulate_program(memory, pointer)
        y = curr_io
        if pointer == -1:
            break
        pointer = simulate_program(memory, pointer)
        if (x, y) == (-1, 0):
            score = curr_io
        tile = "B:"
        if curr_io == 0:
            tile = " "
        if curr_io == 1:
            tile = "|"
        if curr_io == 2:
            tile = "#"
            blocks += 1
        if curr_io == 3:
            pad_pos = (x, y)
            print(pad_pos)
            tile = "-"
        if curr_io == 4:
            tile = "O"
        game[(x, y)] = tile
        #draw_board(game, score)
        

memory = memory.copy()
memory[0] = 2
play_pong(memory, 0)
