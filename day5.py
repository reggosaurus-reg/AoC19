data = open("input/day5.txt")
seqA = list(map(int, data.readline().split(',')))
seqB = seqA.copy()

get_opcode = lambda code: code % 100
get_mode = lambda code, i: (code % (10**(i + 2))) // (10**(i + 1)) 

print("A: ")

def simulate_program(seq):
    i = 0
    while i < len(seq):
        code = seq[i]

        def get_param(pos):
            """ Returns the value for the pos:th parameter. """
            mode = get_mode(code, pos)
            if mode == 0:
                return seq[seq[i + pos]]
            else:
                return seq[i + pos]

        opcode = get_opcode(code)
        if opcode == 99:
            break
        if opcode == 1:
            op1 = get_param(1)
            op2 = get_param(2)
            res = seq[i + 3]
            seq[res] = op1 + op2  
            i += 4
        if opcode == 2:
            op1 = get_param(1)
            op2 = get_param(2)
            res = seq[i + 3]
            seq[res] = op1 * op2  
            i += 4
        if opcode == 3:
            res = seq[i + 1]
            seq[res] = int(input("Enter an integer! (1 for default elf TEST): "))
            i += 2
        if opcode == 4:
            res = seq[i + 1]
            print(seq[res])
            i += 2

simulate_program(seqA)

print("B: ")

def simulate_warmer_program(seq):
    i = 0
    while i < len(seq):
        code = seq[i]

        def get_param(pos):
            """ Returns the value for the pos:th parameter. """
            mode = get_mode(code, pos)
            if mode == 0:
                return seq[seq[i + pos]]
            else:
                return seq[i + pos]

        opcode = get_opcode(code)
        if opcode == 99: # Terminate
            break
        if opcode == 1: # Add
            op1 = get_param(1)
            op2 = get_param(2)
            res = seq[i + 3]
            seq[res] = op1 + op2  
            i += 4
        if opcode == 2: # Multiply
            op1 = get_param(1)
            op2 = get_param(2)
            res = seq[i + 3]
            seq[res] = op1 * op2  
            i += 4
        if opcode == 3: # Input
            res = seq[i + 1]
            seq[res] = int(input("Enter an integer! (5 for default elf TEST): "))
            i += 2
        if opcode == 4: # Output
            res = seq[i + 1]
            print(seq[res])
            i += 2
        if opcode == 5: # Jump if true
            op1 = get_param(1)
            op2 = get_param(2)
            if op1 != 0:
                i = op2
            else:
                i += 3
        if opcode == 6: # Jump if false
            op1 = get_param(1)
            op2 = get_param(2)
            if op1 == 0:
                i = op2
            else:
                i += 3
        if opcode == 7: # Less than
            op1 = get_param(1)
            op2 = get_param(2)
            res = seq[i + 3]
            if op1 < op2:
                seq[res] = 1
            else:
                seq[res] = 0
            i += 4
        if opcode == 8: # Equals
            op1 = get_param(1)
            op2 = get_param(2)
            res = seq[i + 3]
            if op1 == op2:
                seq[res] = 1
            else:
                seq[res] = 0
            i += 4

simulate_warmer_program(seqB)
