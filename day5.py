data = open("input/day5.txt")
seqA = list(map(int, data.readline().split(',')))
seqB = seqA.copy()

print("A: ")

def simulate_program(seq):
    i = 0
    while i < len(seq):
        code = seq[i]
        opcode = code % 100
        mode1 = (code % 1000) // 100 
        mode2 = (code % 10000) // 1000 
        mode3 = (code % 100000) // 10000 
        if opcode == 99:
            break
        if opcode == 1:
            if mode1 == 0:
                op1 = seq[seq[i + 1]]
            else:
                op1 = seq[i + 1] 
            if mode2 == 0:
                op2 = seq[seq[i + 2]]
            else: 
                op2 = seq[i + 2]
            res = seq[i + 3]
            seq[res] = op1 + op2  
            i += 4
        if opcode == 2:
            if mode1 == 0:
                op1 = seq[seq[i + 1]]
            else:
                op1 = seq[i + 1]
            if mode2 == 0:
                op2 = seq[seq[i + 2]]
            else: 
                op2 = seq[i + 2]
            res = seq[i + 3]
            seq[res] = op1 * op2  
            i += 4
        if opcode == 3:
            res = seq[i + 1]
            seq[res] = int(input("Enter an integer!: "))
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
        def value(mode, off):
            if mode == 0:
                return seq[seq[i + off]]
            else:
                return seq[i + off]
        code = seq[i]
        opcode = code % 100
        mode1 = (code % 1000) // 100 
        mode2 = (code % 10000) // 1000 
        mode3 = (code % 100000) // 10000 
        if opcode > 10:
            break
        if opcode == 99:
            break
        if opcode == 1:
            op1 = value(mode1, 1)
            op2 = value(mode2, 2)
            res = seq[i + 3]
            seq[res] = op1 + op2  
            i += 4
        if opcode == 2:
            op1 = value(mode1, 1)
            op2 = value(mode2, 2)
            res = seq[i + 3]
            seq[res] = op1 * op2  
            i += 4
        if opcode == 3:
            res = seq[i + 1]
            seq[res] = int(input("Enter an integer!: "))
            i += 2
        if opcode == 4:
            res = seq[i + 1]
            print(seq[res])
            i += 2
        if opcode == 5:
            op1 = value(mode1, 1)
            op2 = value(mode2, 2)
            if op1 != 0:
                i = op2
            else:
                i += 3
        if opcode == 6:
            op1 = value(mode1, 1)
            op2 = value(mode2, 2)
            if op1 == 0:
                i = op2
            else:
                i += 3
        if opcode == 7:
            op1 = value(mode1, 1)
            op2 = value(mode2, 2)
            res = seq[i + 3]
            if op1 < op2:
                seq[res] = 1
            else:
                seq[res] = 0
            i += 4
        if opcode == 8:
            op1 = value(mode1, 1)
            op2 = value(mode2, 2)
            op3 = value(mode3, 3)
            res = seq[i + 3]
            if op1 == op2:
                seq[res] = 1
            else:
                seq[res] = 0
            i += 4


simulate_warmer_program(seqB)
