from math import acos, atan, atan2, pi
import os
data = open("input/day10.txt")
#data = open("test10.txt")
asteroids = []
for row in data:
    asteroids.append(list(row[:-1]))

def print_asteroids():
    for row in asteroids:
        for a in row:
            print(a, end='')
        print()

print("B:")


dist = lambda b: abs(b[0] - bestStation[0]) + abs(b[1] - bestStation[1]) 
angle = lambda b: (atan2(bestStation[1] - b[1], bestStation[0] - b[0])) % (2*pi)
char = lambda t: asteroids[t[0]][t[1]]
def set_char(t, c): asteroids[t[0]][t[1]] = c

width, height = len(asteroids[0]), len(asteroids) 
best = (3, 8)
best = (13, 11)
best = (19, 20) #from A?
bestStation = best
stations = {}
for y in range(len(asteroids)):
    row = asteroids[y]
    for x in range(len(row)):
        station = asteroids[y][x]
        if station != '.' and (y, x) != bestStation:
            stations[(y, x)] = 0


vaporized = 0
print_asteroids()
slopes = {}
for asteroid in stations:
    slope = angle(asteroid)
    if slope in slopes:
        slopes[slope].append(asteroid)
    else:
        slopes[slope] = [asteroid]
for slope in slopes:
    pos = slopes[slope]
    slopes[slope] = sorted(pos, key=dist)

slopeList = list(reversed(sorted(slopes)))
if slopeList[-1] == 0.0:
    slopeList = [0.0] + slopeList[:-1]

while slopeList:
    for slope in slopeList:
        if not slopes[slope]:
            continue
        coord = slopes[slope][0]
        if vaporized == 199:
            print(coord)
            print(slope)
            slopeList = 0
            break
        new_list = slopes[slope][1:]  
        set_char(coord, ",")
        vaporized += 1

        #input("Step? ")
        os.system("clear")
        print("B:")
        print_asteroids()

        slopes[slope] = new_list



# 908, 1025 too high, 525, 316 fel
