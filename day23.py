from intcode_class import *
program = read_program("input/day23.txt")

num_of_computers = 50
NAT = None
sent_NAT_ys = set()

# Initialize all computers
machines = []
for address in range(num_of_computers):
    computer = Computer(program.copy())
    computer.run([address])
    machines.append(computer)

# Start running
idle = 0
while True:
    for idd in range(len(machines)):
        computer = machines[idd]
        computer.run()

        if not computer.input and not computer.output_log:
            idle += 1

        while len(computer.output_log) >= 3:
            idle = 0

            address, x, y = computer.output_log[:3]
            computer.output_log = computer.output_log[3:]

            # Send packet to correct computer
            if address == 255:
                NAT = (address, x, y)
                if not sent_NAT_ys:
                    print("A:\n{}".format(NAT[2]))
            else:
                receiving_computer = machines[address]
                receiving_computer.input.append(x)
                receiving_computer.input.append(y)

    # Treat NAT if system goes idle
    if idle > 10 * num_of_computers:
        idle = 0
        if NAT[2] in sent_NAT_ys:
            print("B:\n{}".format(NAT[2]))
            break
        sent_NAT_ys.add(NAT[2])
        machines[0].input = [NAT[1], NAT[2]]
