from math import ceil
data = open("input/day16.txt").readline()

offset = int(data[:7])
base_pattern = [0, 1, 0, -1]
original_signal = []
while data[0] != '\n':
    original_signal.append(int(data[0]))
    data = data[1:]


print("A:")

def fftA(signal):
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
for phases in range(100):
    signal = fftA(signal)
    phases += 1 

res = signal[:8]
string = ""
for char in res:
    string += str(char)
print(string)


print("B:")

""" Insights: 
offset > le(signal) / 2, so pattern will never have -1
offset > le(signal) / 4, so pattern will never even have 0
only difference between row sums is the "first" digit
so, the first interesting digit will be counted once, the second twice...
... and the last len(interesting_signal)
"""

def fftB(signal):
    new_signal = signal.copy()
    summ = signal[-1] # Last will never change
    for i in range(2, len(signal) + 1): 
        summ = (summ + signal[-i]) % 10
        new_signal[-i] = summ % 10
    return new_signal

# Only keep the (repeated) part after our offset
interesting_signal = (original_signal*10000)[offset:]

for phases in range(100):
    interesting_signal = fftB(interesting_signal)

res = interesting_signal[:8]
string = ""
for char in res:
    string += str(char)
print(string) 
