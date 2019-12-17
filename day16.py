from functools import reduce
from time import process_time as time
data = open("input/day16.txt").readline()
#data = open("test16.txt").readline()

base_pattern = [0, 1, 0, -1]
original_signal = []
offset = int(data[:7])
while data[0] != '\n':
    original_signal.append(int(data[0]))
    data = data[1:]


print("A:")
# 24465799
# (took 0.032308121) 

def fft(signal):
    new_signal = []
    for i in range(len(signal)): 
        # Construct pattern for this position (not with skipped first)
        repeat = i + 1
        plus_index = i
        minus_index = i + 2 * repeat
        cycle_interval = 4 * repeat

        # Skip zeros, add 1 positions and subtract -1 positions
        summ = 0
        pos = i
        while pos < len(signal):
            if pos == plus_index:
                summ += sum(signal[plus_index:plus_index + repeat])
                pos = minus_index
                plus_index += cycle_interval
            elif pos == minus_index:
                summ -= sum(signal[minus_index:minus_index + repeat])
                pos = plus_index
                minus_index += cycle_interval

        # Keep only 1 digit
        new_signal.append(abs(summ) % 10)

    return new_signal
        
signal = original_signal.copy()
start_t = time()
for phases in range(100):
    signal = fft(signal)
    phases += 1 
print("(took {})".format(time() - start_t))

res = signal[:8]
string = ""
for char in res:
    string += str(char)
print(string)


print("B:")

little = len(original_signal)
big = little * 10000
interesting_signal = original_signal.copy()[offset % little:]
for i in range((big - offset) // little):
    interesting_signal += original_signal.copy() 

#for phases in range(100):
#    signal = fft(signal)
#    phases += 1 
#
#string = ""
#for char in res:
#    string += str(char)
#print(string) 

# 82380114 wrong
