from intcode_class import * 
import os

program = read_program("input/day13.txt")

print("A:")

game = {}
computer = Computer(program.copy())
computer.run_until_end()
output = computer.output_log

blocks = 0
while len(output) >= 3:
    x = output[0]
    y = output[1]
    tile = output[2]
    if tile == 2:
        blocks += 1
    elif tile == 3:
        paddle = (x, y)
    elif tile == 4:
        ball = (x, y)
    game[(x, y)] = tile
    output = output[3:]

print(blocks)

print("B:")

def game_bot():
    cheatProgram = program.copy()
    computer = Computer(cheatProgram)
    computer.memory[0] = 2
    blocksLeft = True
    score = 0
    game = {}
    ballPos, paddlePos = (0, 0), (0, 0)


    def step_game(joystick = 0):
        nonlocal ballPos, paddlePos, score
        if not computer.run(joystick):
            return 0
        computer.run(joystick)
        computer.run(joystick)
        output = computer.output_log
        x = output[-3]
        y = output[-2]
        tile = output[-1]
        if x == -1 and y == 0:
            score = tile
        elif tile == 3:
            paddlePos = (x, y)
        elif tile == 4:
            ballPos = (x, y)
        game[(x, y)] = tile
        return 1

    for num_of_tiles in range(20 * 40):
        step_game(0)

    while blocksLeft:
        if paddlePos[0] < ballPos[0]:
            direction = 1
        if paddlePos[0] == ballPos[0]:
            direction = 0 
        if paddlePos[0] > ballPos[0]:
            direction = -1
        blocksLeft = step_game(direction)
        #draw(game, score)

    return score

def draw(board, score = -1):
    global blocks
    width = max(board, key = lambda x: x[0])[0] 
    height = max(board, key = lambda x: x[1])[1] 

    os.system("clear")
    print("A:\n{}\nB:\nScore: {}".format(blocks, score))

    for y in range(height + 1):
        for x in range(width + 1):
            tile = board.get((x, y), 100)
            if tile == 0:
                sign = " "
            elif tile == 1:
                sign = "|"
            elif tile == 2:
                sign = "#"
            elif tile == 3:
                sign = "-"
            elif tile == 4:
                sign = "O"
            elif tile == 100:
                sign = "?"
            else:
                sign = "!"
                #raise Exception("Unkown tile", tile, "at", x, y)
            print(sign, end='')
        print()

print(game_bot())
