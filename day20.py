# NOTE: (y, x)
dirrs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
tup_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
tup_sub = lambda a, b: (a[0] - b[0], a[1] - b[1])

maze = []
#for row in open("test20.txt"):
for row in open("input/day20.txt"):
    maze.append(list(row[:-1]))

width = len(maze[0])
height = len(maze)
inside = lambda pos: 0 <= pos[0] <= height - 1 and 0 <= pos[1] <= width - 1
sign = lambda pos: maze[pos[0]][pos[1]]

# Locate portals in maze
entrances = {}
for y in range(height):
    for x in range(width):
        pos = (y, x)
        # looking for letters
        if not sign(pos).isupper():
            continue

        # examine surroundings
        for d in dirrs:
            new_pos = tup_add((y, x), d)
            if not inside(new_pos):
                continue
            if sign(new_pos).isupper(): # Found the other end of portal!
                # Find entrance of portal
                candidates = [tup_add(new_pos, d), tup_sub(pos, d)]
                for cand_pos in candidates:
                    if inside(cand_pos) and sign(cand_pos) == '.':
                        entrance = cand_pos
                # Store entrance
                portal_code = sign(pos) + sign(new_pos) 
                if portal_code == 'AA':
                    start = entrance
                elif portal_code == 'ZZ':
                    end = entrance
                else:
                    entrances[entrance] = sorted(portal_code)
                break
print("A:")

def other_side(pos):
    portal = entrances[pos]
    for entrance in entrances:
        if entrances[entrance] == portal and entrance != pos:
            return entrance

visited = {} 
to_visit = [(start, 0)]

def will_visit(pos, steps):
    if pos not in visited:
        to_visit.append((pos, steps))

def show_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if (y, x) in visited:
                print("+", end = '')
            else:
                print(maze[y][x], end = '')
        print()


# BFS (with portals!)
while to_visit:
    curr, steps = to_visit[0]
    to_visit = to_visit[1:]
    visited[curr] = steps
    if curr == end:
        #show_maze(maze)
        break
    if curr in entrances: # TODO: Store openings or portals?
        will_visit(other_side(curr), steps + 1)
    for dirr in dirrs:
        neighbour = tup_add(curr, dirr)
        tile = maze[neighbour[0]][neighbour[1]]
        if tile != '.':
            continue
        
        will_visit(neighbour, steps + 1)

    #input("step ")
    #show_maze(maze)

print(visited[end])
