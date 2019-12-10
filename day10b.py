#data = open("input/day10.txt")
data = open("test.txt")
asteroids = []
for row in data:
    asteroids.append(row[:-1])

print("A:")

def slopeTo(origo, b):
    # NEver used here
    if origo[0] == b[0] and origo[1] == b[1]:
        return 'same'

    if origo[1] == b[1]:
        slope = '0'
    elif origo[0] == b[0]:
        slope = '0'
    else:
        slope = str( (b[1] - origo[1]) / (b[0] - origo[0]) )

    if b[0] < origo[0] and b[1] >= origo[1]:
        return 'a' + slope 
    if b[0] >= origo[0] and b[1] > origo[1]:
        return 'b' + slope 
    if b[0] > origo[0] and b[1] <= origo[1]:
        return 'c' + slope 
    if b[0] <= origo[0] and b[1] < origo[1]:
        return 'd' + slope 

stations = {} 
vaporized = 0
for y in range(len(asteroids)):
    row = asteroids[y]
    for x in range(len(row)):
        station = asteroids[y][x]
        if station != '.':
            stations[(x, y)] = 0
            
for origo in stations:
    #slopes = set() 
    slopes = {}
    #slopes = []
    for asteroid in stations:
        if asteroid == origo:
            continue
        slope = slopeTo(origo, asteroid)
        if slope not in slopes:
            slopes[slope] = asteroid # TODO: Invert dict?
        #slopes.add(slope)
        #if slope not in slopes:
        #    slopes.append(slope)
    #slopes.sort()
    stations[origo] = slopes


bestStation = max(stations, key = lambda x: len(stations[x]))
slopes = stations[bestStation]
print(len(slopes))

print("B:")
print(bestStation)
# TODO: Verify getting corect slopes/ quantiles
#for entry in stations[origo]:
