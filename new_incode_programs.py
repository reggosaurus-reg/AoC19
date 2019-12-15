from intcode_class import *

# TODO: Test all examples from all days if still can't work out the new ones


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


#### DAY 5 #### Add input/output and immidiate mode in A, then

data = list(map(int, open("input/day5.txt").readline().split(',')))

r5a = 0
assert r5a == 2845163, "Day 5 A failed."

r5b = 0
assert r5b == 9436229, "Day 5 B failed."


#### DAY 7 #### Nothing new in intcode

data = list(map(int, open("input/day7.txt").readline().split(',')))

r7a = 0
assert r7a == 19650, "Day 7 A failed."

r7b = 0
assert r7b == 35961106, "Day 7 B failed."


#### DAY 9 #### Last add: 

data = list(map(int, open("input/day9.txt").readline().split(',')))

r9a = 0
assert r9a == 2955820355, "Day 9 A failed."

r9b = 0
assert r9b == 46643, "Day 9 B failed."


#### DAY 11 ###
#### DAY 13 ###
#### DAY 15 ###



print("All programs worked!")

