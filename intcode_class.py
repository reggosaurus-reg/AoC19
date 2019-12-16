####### General computer related functions

tup_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
read_program = lambda path: list(map(int, open(path).readline().split(',')))

class Computer():

    ####### Interface

    def __init__(self, program):
        self.memory = dict(enumerate(program.copy()))
        self.pointer = 0
        self.base = 0
        self.input = "nope"
        self.max_pointer = len(self.memory)
        self.output_log = []

    def copy(self):
        new = Computer(self.get_memory())
        new.pointer = self.pointer
        new.base = self.base
        return new

    def get_memory(self):
        return list(self.memory.values())

    def run_until_end(self, first = "nope"):
        running = True
        while running:
            running = self.run(first)
    
    def run(self, first_input = "nope"):
        if first_input != "nope":
            self.input = first_input

        while self.pointer < self.max_pointer:
            opcode = self.get_opcode()
            if opcode == 99:
                return 0
            elif opcode == 1:
                self.do_add()
            elif opcode == 2:
                self.do_mult()
            elif opcode == 3:
                self.take_input()
            elif opcode == 4:
                self.give_output()
                return 1
            elif opcode == 5:
                self.do_true_jump()
            elif opcode == 6:
                self.do_false_jump()
            elif opcode == 7:
                self.do_less()
            elif opcode == 8:
                self.do_equals()
            elif opcode == 9:
                self.change_base()
            else:
                raise Exception("Invalid opcode {}!".format(opcode))

    ####### Meta functions

    def get_opcode(self):
        code = self.memory[self.pointer]
        return code % 100

    def get_mode(self, offset):
        code = self.memory[self.pointer]
        return code // (10 ** (offset + 1)) % 10 

    def get_param(self, offset, only_address = False):
        mode = self.get_mode(offset)
        pos = self.pointer + offset
        if mode == 0: # position mode
            address = self.memory[pos]
        if mode == 1: # immidiate mode
            address = pos 
        if mode == 2: # relative mode
            address = self.base + self.memory[pos]

        if address not in self.memory:
            self.memory[address] = 0

        if only_address:
            return address
        else:
            return self.read(address)

    def do_operation(self, func):
        p1 = self.get_param(1)
        p2 = self.get_param(2)
        p3 = self.get_param(3, True)
        self.write(func(p1, p2), p3)
        self.pointer += 4

    def do_jump(self, func):
        p1 = self.get_param(1)
        p2 = self.get_param(2)
        self.pointer = func(p1, p2)

    def write(self, data, address):
        self.memory[address] = data

    def read(self, address):
        return self.memory[address]


    ####### Operations

    def do_add(self):
        self.do_operation(lambda a, b: a + b)

    def do_mult(self):
        self.do_operation(lambda a, b: a * b)

    def do_less(self):
        self.do_operation(lambda a, b: a < b)

    def do_equals(self):
        self.do_operation(lambda a, b: a == b)

    def take_input(self):
        if self.input == 'nope':
            raise Exception("No input given.")
        p1 = self.get_param(1, True)
        self.write(self.input, p1)
        self.pointer += 2

    def give_output(self):
        p1 = self.get_param(1)
        self.output_log.append(p1)
        self.pointer += 2

    def do_true_jump(self):
        self.do_jump(lambda a, b: b if a else self.pointer + 3)

    def do_false_jump(self):
        self.do_jump(lambda a, b: b if not a else self.pointer + 3)

    def change_base(self):
        p1 = self.get_param(1)
        self.base += p1
        self.pointer += 2
