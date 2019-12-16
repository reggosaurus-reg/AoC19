from functools import reduce
data = open("input/day16.txt").readline()
data = open("test16.txt").readline()

base_pattern = [0, 1, 0, -1]
original_signal = []
offset = int(data[:7])
while data[0] != '\n':
    original_signal.append(int(data[0]))
    data = data[1:]


print("A:")

def fft(signal):
    new_signal = []
    for i in range(len(signal)):
        # Construct pattern for this position (not with skipped first)
        pattern = [] 
        for k in range(0, 4):
            pattern += [base_pattern[k] for j in range(i + 1)]

        # Multiply with pattern
        period = len(pattern)
        summ = 0
        for pos in range(len(signal)): # By mult. all signal digits with i:th pattern
            # Sum 
            summ += signal[pos] * pattern[(pos + 1) % period] # +1 to skip in pattern

        # Keep only 1 digit
        new_signal.append(abs(summ) % 10)

    return new_signal
        
phases = 0
signal = original_signal.copy()
while phases < 100:
    signal = fft(signal)
    phases += 1 

res = signal[:8]
string = ""
for char in res:
    string += str(char)
print(string)


print("B:")
# Need to optimize...

signal = []
for i in range(10000):
    signal += original_signal.copy()

phases = 0
while phases < 100:
    signal = fft(signal)
    phases += 1 

offset = offset % len(original_signal)
res = signal[offset:offset + 8]
string = ""
for char in res:
    string += str(char)
print(string) 

# 82380114 wrong
