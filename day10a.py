data = open("input/day10.txt")
#data = open("test.txt")
asteroids = []
for row in data:
    asteroids.append(row[:-1])

print("A:")

def slopeTo(a, b):
    # NEver used here
    if a[0] == b[0] and a[1] == b[1]:
        return 'same'

    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 'left' + str(0)
        return 'right' + str(0)

    elif a[0] == b[0]:
        if a[1] > b[1]:
            return 'up' + str(0) # up
        return 'down' + str(0) # down

    else:
        absDist = (b[1] - a[1]) / (b[0] - a[0])
        if a[0] > b[0]:
            return 'left' + str(absDist) # left
        if a[0] < b[0]:
            return 'right' + str(absDist) # right
        if a[1] > b[1]:
            return 'up' + str(absDist)
        if a[1] < b[1]:
            return 'down' + str(absDist)


stations = {} 
vaporized = 0
for y in range(len(asteroids)):
    row = asteroids[y]
    for x in range(len(row)):
        station = asteroids[y][x]
        if station == '#':
            stations[(x, y)] = 0
            
for origo in stations:
    slopes = set() 
    #slopes = {}
    #slopes = []
    for asteroid in stations:
        if asteroid == origo:
            continue
        slope = slopeTo(origo, asteroid)
        #slopes[asteroid] = slope 
        slopes.add(slope)
        #if slope not in slopes:
        #    slopes.append(slope)
    stations[origo] = len(slopes)


print(max(stations.values()))# key=lambda x: stations[x]))

print("B:")

origo = (3, 8) #max(stations, key=lambda x: stations[x])
