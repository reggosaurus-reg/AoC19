data = open("input/day4.txt").read()
low = int(data[:6])
high = int(data[7:13])

print("A: ")

passwordsA = 0
passwordsB = 0
for candidate in range(low, high + 1):
    candidate = str(candidate)
    decreasing = A = B = False
    doubles = [0 for i in range(10)]

    for i in range(5):
        left = candidate[i]
        right = candidate[i + 1]
        if left > right:
            decreasing = True
        if left == right:
            doubles[int(left)] += 1 

    if not decreasing:
        for n in range(10):
            if doubles[n] > 0:
                A = True
            if doubles[n] == 1:
                B = True
        if A:
            passwordsA += 1
        if B:
            passwordsB += 1

print(passwordsA)

print("B: ")

print(passwordsB)
