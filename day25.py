from intcode_class_25 import *

program = read_program("input/day25.txt")

computer = Computer(program)
computer.run_until_end()

