############### META FUNCIONS ##############

class Computer():

    def __init__(self, program, start=None):
        self.memory = dict(enumerate(program.copy()))
        self.pointer = 0
        self.base = 0
        self.input = start
        self.max_pointer = len(self.memory)

    def get_memory(self):
        return list(self.memory.values())

    def run(self):
        while self.pointer < self.max_pointer:
            opcode = self.get_opcode()
            if opcode == 99:
                return # Mark halt?
            elif opcode == 1:
                self.do_add()
            elif opcode == 2:
                self.do_mult()
            else:
                raise Exception("Invalid opcode {}!".format(opcode))

    ####### Meta functions

    def get_opcode(self):
        return self.memory[self.pointer] % 100

    def get_param(self, offset, only_address = False):
        mode = 0 # TODO
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
        p3 = self.get_param(3, True) # ???
        #print(p1, "and", p2, "=> addr", p3)
        self.write(func(p1, p2), p3)
        self.pointer += 4

    def write(self, data, address):
        self.memory[address] = data

    def read(self, address):
        return self.memory[address]


    ####### Operations

    def do_add(self):
        self.do_operation(lambda a, b: a + b)

    def do_mult(self):
        self.do_operation(lambda a, b: a * b)


