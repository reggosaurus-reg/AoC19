from intcode_class import *


#### DAY 2 #### Intcode has one mode and add/mult

data = list(map(int, open("input/day2.txt").readline().split(',')))
c2a = Computer(data)
c2a.memory[1] = 12
c2a.memory[2] = 2
c2a.run()
r2a = c2a.memory[0]

assert r2a == 3267740, "Day 2 A failed."

output = 19690720
for noun in range(100):
    for verb in range(100):
        c2b = Computer(data)
        c2b.memory[1] = noun
        c2b.memory[2] = verb
        c2b.run()
        if c2b.memory[0] == output:
            r2b = 100 * noun + verb
            break

assert r2b == 7870, "Day 2 B failed."


#### DAY 5 #### Add input/output and immidiate mode in A, then jumps and comparators in B

data = list(map(int, open("input/day5.txt").readline().split(',')))
c5a = Computer(data)
c5a.run(1)
r5a = c5a.output_log 

# Should also only output zeros as diagnostic!
assert r5a[-1] == 2845163 and not any(r5a[:-1]), "Day 5 A failed."

c5b = Computer(data)
c5b.run(5)
r5b = c5b.output_log[0]

assert r5b == 9436229, "Day 5 B failed."


#### DAY 7 #### Nothing new in intcode

#  data = list(map(int, open("input/day7.txt").readline().split(',')))
#  
#  r7a = 0
#  assert r7a == 19650, "Day 7 A failed."
#  
#  r7b = 0
#  assert r7b == 35961106, "Day 7 B failed."


#### DAY 9 #### Last add: 

data = list(map(int, open("input/day9.txt").readline().split(',')))

c9a = Computer(data)
c9a.run(1)
r9a = c9a.output_log[0]

assert r9a == 2955820355, "Day 9 A failed."

c9b = Computer(data)
c9b.run(2)
r9b = c9b.output_log[0]

assert r9b == 46643, "Day 9 B failed."

print("All programs worked!")

