data = open("input/day2.txt")
data = data.read()

temp = ""
seqA = []
# Parse input into list... 
for char in data:
    if char == ',' and temp:
        seqA.append(int(temp))
        temp = ""
    elif char != '\n':
        temp += char


print("A: ")

seqB = seqA.copy()
seqA[1] = 12
seqA[2] = 2

def simulate_program(seq):
    i = 0
    while i < len(seq):
        opcode = seq[i]
        if opcode == 99:
            break
        op1 = seq[seq[i + 1]]
        op2 = seq[seq[i + 2]]
        res = seq[i + 3]
        i += 4
        if opcode == 1:
            seq[res] = op1 + op2  
        if opcode == 2:
            seq[res] = op1 * op2  

simulate_program(seqA)
print(seqA[0])

print("B: ")

output = 19690720
for noun in range(100):
    for verb in range(100):
        seq = seqB.copy()
        seq[1] = noun
        seq[2] = verb
        simulate_program(seq)
        if seq[0] == output:
            print(100 * noun + verb)
            break
