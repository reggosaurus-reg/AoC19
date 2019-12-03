data = open("input/day3.txt")
data = data.read()

print("A: ")

# Parse input into list... 
temp = ""
dirsA = []
dirsB = []
A = True
for char in data:
    if char == ',' and temp:
        if A:
            dirsA.append(temp)
        else:
            dirsB.append(temp)
        temp = ""
    elif char == '\n' and temp:
        if A:
            A = False
            dirsA.append(temp)
        else:
            dirsB.append(temp)
        temp = ""
    else:
        temp += char

# Add visited coordinates (and their "taken steps") to dicts
tuple_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
tuple_mult = lambda i, t: (i * t[0], i * t[1])
visitedA = {} 
visitedB = {} 

def visit(visited, dirs):
    d = (0, 0)
    location = (0, 0)
    travelled = 0
    for dirr in dirs:
        if dirr[0] == "R":
            d = (1, 0)
        if dirr[0] == "L":
            d = (-1, 0)
        if dirr[0] == "U":
            d = (0, 1)
        if dirr[0] == "D":
            d = (0, -1)

        val = int(dirr[1:])
        for i in range(1, val + 1):
            pos = tuple_add(location, tuple_mult(i, d))
            dist = travelled + i
            if pos in visited:
                dist = visited[pos]
            visited[pos] = dist
        location = pos
        travelled += val

visit(visitedA, dirsA)
visit(visitedB, dirsB)

# Compare paths and add total steps taken
crossingPaths = {} 
for node in visitedA:
    if node in visitedB:
        crossingPaths[node] = visitedA[node] + visitedB[node] 

# Find shortest distance and least taken steps
minDist = float("inf")
minSteps = float("inf")
for node, steps in crossingPaths.items():
    distance = abs(node[0]) + abs(node[1])
    if distance < minDist:
        minDist = distance
    if steps < minSteps:
        minSteps = steps

print(minDist)

print("B: ")

print(minSteps)
