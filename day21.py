from intcode_class import * 

program = read_program("input/day21.txt")

def jumpyjump(instructions, mode):

    def transform_inner(lst):
        if not lst:
            return mode + "\n"
        else:
            return lst[0] + '\n' + transform_inner(lst[1:])
    transformed = list(map(ord, transform_inner(instructions)))

    computer = Computer(program.copy())
    computer.run_until_end(transformed)

    # Present result
    result = computer.output_log
    if result[-1] > 1000:
        print(result[-1])
    else:
        for c in result:
            print(chr(c), end='')
        print()
    

print("A:")

# D and ~(A and B and C)
instructions = [
        "NOT J J", # Should jump?
        "AND A J",
        "AND B J",
        "AND C J",
        "NOT J J", 

        "AND D J"  # Can jump
        ]

jumpyjump(instructions, "WALK")


print("B:")

# D and ~(A and B and C) and (E or H)
instructions = [
        "NOT J J", # Should jump?
        "AND A J",
        "AND B J",
        "AND C J",
        "NOT J J", 

        "OR H T", # Can jump or walk when arrived?
        "OR E T", 

        "AND T J", # Can jump
        "AND D J"
        ]

jumpyjump(instructions, "RUN")
