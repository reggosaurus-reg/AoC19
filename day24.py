tup_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
bugs = set()
SIZE = 5

print("A:")

y = 0
#for row in open("test24.txt"):
for row in open("input/day24.txt"):
    for x in range(SIZE):
        if row[x] == "#":
            bugs.add((x, y))
    y += 1


def draw_bugs(bugs):
    for y in range(SIZE):
        for x in range(SIZE):
            if (x, y) in bugs:
                sign = "#"
            else:
                sign = "."
            print(sign, end = "")
        print()

def simulate_step(bugs):
    dirrs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    is_alive = lambda p: p in bugs

    next_generation = set()
    for y in range(SIZE):
        for x in range(SIZE):
            curr = (x, y)
            alive_neighbours = []
            for dirr in dirrs:
                neighbour = tup_add(curr, dirr)
                if is_alive(neighbour):
                    alive_neighbours.append(neighbour)
            if is_alive(curr) and len(alive_neighbours) == 1:
                next_generation.add(curr)
            elif not is_alive(curr) and 0 < len(alive_neighbours) < 3:
                next_generation.add(curr)
    return next_generation


seen_layouts = [] 
while True:
    bugs = simulate_step(bugs)
    if [bugs] in seen_layouts:
        #draw_bugs(bugs)
        break
    else:
        seen_layouts.append([bugs])

bio_diversity = lambda y, x: 2 ** (5 * x + y)
            
res = 0
for pos in bugs:
    res += bio_diversity(pos[0], pos[1])

print(res)


