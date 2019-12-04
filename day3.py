data = open("input/day3.txt")
dirsA = data.readline().split(',')
dirsB = data.readline().split(',')

print("A: ")

# Add visited coordinates (and their "taken steps") to dicts
tuple_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
tuple_mult = lambda i, t: (i * t[0], i * t[1])

def visit(dirs):
    visited = {}
    allDirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    location = (0, 0)
    travelled = 0
    for dirr in dirs:
        d = allDirs[dirr[0]]
        val = int(dirr[1:])
        for i in range(1, val + 1):
            pos = tuple_add(location, tuple_mult(i, d))
            dist = travelled + i
            if pos in visited:
                dist = visited[pos]
            visited[pos] = dist
        location = pos
        travelled += val
    return visited

visitedA = visit(dirsA)
visitedB = visit(dirsB)

# Compare (intersect) paths and add total steps taken
crossingPaths = {} 
for node in visitedA:
    if node in visitedB:
        crossingPaths[node] = visitedA[node] + visitedB[node] 

# Find shortest distance and least taken steps
minDist = float("inf")
minSteps = float("inf")
for node, steps in crossingPaths.items():
    distance = abs(node[0]) + abs(node[1])
    minDist = min(distance, minDist)
    minSteps = min(steps, minSteps)

print(minDist)

print("B: ")

print(minSteps)
