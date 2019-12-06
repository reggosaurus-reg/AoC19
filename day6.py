orbits = {row[4:-1]:row[:3] for row in open("input/day6.txt")}

def findParentsOf(orb, circling):
    """ Finds the number of centers that circling is circling around """
    parent = orb[circling]
    if parent == "COM":
        return 1
    else:
        return 1 + findParentsOf(orb, parent)

def findPathOf(orb, circling, path):
    """ Returns the path from circling to the center of mass """ 
    parent = orb[circling]
    if parent == "COM":
        return [parent] + path
    else:
        return findPathOf(orb, parent, [parent] + path)

print("A: ")

# Count number of orbits and find paths to center of mass
numOfOrbits = 0
for circling in orbits.keys():
    if circling == "YOU":
        numOfOrbits += findParentsOf(orbits, circling)
        youOrbit = findPathOf(orbits, circling, [])
    if circling == "SAN":
        numOfOrbits += findParentsOf(orbits, circling)
        sanOrbit = findPathOf(orbits, circling, []) 
    numOfOrbits += findParentsOf(orbits, circling)

print(numOfOrbits)

print("B: ")

# Find number of centers not in common path
for i in range(min(len(youOrbit), len(sanOrbit))):
    if youOrbit[i] != sanOrbit[i]:
        print(len(youOrbit[i:]) + len(sanOrbit[i:]))
        break
