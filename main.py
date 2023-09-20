import pygame
import random

### global variables ###

# game states
done = False
boardIsFull = False
gameOver = False
shouldGenerate = True

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clrBackground = (186, 136, 75)
clr2 = (206, 116, 75)
clr4 = (226, 96, 75)
clr8 = (246, 56, 75)
clr16 = (0, 138, 255)
clr32 = (0, 108, 255)
clr64 = (0, 78, 255)
clr128 = (0, 68, 255)
clr256 = (200, 0, 200)
clr512 = (220, 20, 200)
clr1024 = (240, 40, 200)
clr2048 = (255, 255, 0)

colors = [clr2, clr4, clr8, clr16, clr32, clr64, clr128, clr256, clr512, clr1024, clr2048]

# creates checkerboard pattern

row1 = [0, 0, 0, 0]
row2 = [0, 0, 0, 0]
row3 = [0, 0, 0, 0]
row4 = [0, 0, 0, 0]

columns = [row1, row2, row3, row4]

### functions ###

def combine(tile1, tile2):
    sum = tile1+tile2
    return sum

def moveTiles(direction):
    global boardIsFull, shouldGenerate

    temp = False
    shouldGenerate = True
    if direction == 'up':
        for i in range(4):
            if columns[i][0] == columns[i][1] and columns[i][0] != 0:
                columns[i][0] = combine(columns[i][0], columns[i][1])
                columns[i][1] = 0
                temp = True

            elif columns[i][1] == columns[i][2] and columns[i][1] != 0:
                columns[i][1] = combine(columns[i][1], columns[i][2])
                columns[i][2] = 0
                temp = True

            elif columns[i][0] == columns[i][2] and columns[i][1] == 0 and columns[i][0] != 0:
                columns[i][0] = 2*columns[i][0]
                columns[i][2] = 0
                temp = True

            elif columns[i][1] == columns[i][3] and columns[i][2] == 0 and columns[i][1] != 0:
                columns[i][1] = 2*columns[i][1]
                columns[i][3] = 0
                temp = True

            elif columns[i][0] == columns[i][3] and columns[i][1] == 0 and columns[i][2] == 0 and columns[i][0] != 0:
                columns[i][0] = 2*columns[i][0]
                columns[i][3] = 0
                temp = True

            else:
                shouldGenerate = False

            if columns[i][2] == columns[i][3] and columns[i][2] != 0:
                columns[i][2] = combine(columns[i][2], columns[i][3])
                columns[i][3] = 0
                temp = True


            for k in range(4):
                if columns[i][k] == 0:
                    for l in range(4-k):
                        if columns[i][k+l] != 0:
                            columns[i][k] = columns[i][k+l]
                            columns[i][k+l] = 0
                            temp = True
                            break






    if direction == 'down':
        for i in range(4):
            if columns[i][3] == columns[i][2] and columns[i][3] != 0:
                columns[i][3] = combine(columns[i][3], columns[i][2])
                columns[i][2] = 0
                temp = True

            elif columns[i][2] == columns[i][1] and columns[i][2] != 0:
                columns[i][2] = combine(columns[i][2], columns[i][1])
                columns[i][1] = 0
                temp = True

            elif columns[i][3] == columns[i][1] and columns[i][2] == 0 and columns[i][3] != 0:
                columns[i][3] = 2*columns[i][3]
                columns[i][1] = 0
                temp = True

            elif columns[i][2] == columns[i][0] and columns[i][1] == 0 and columns[i][2] != 0:
                columns[i][2] = 2*columns[i][2]
                columns[i][0] = 0
                temp = True

            elif columns[i][3] == columns[i][0] and columns[i][2] == 0 and columns[i][1] == 0 and columns[i][3] != 0:
                columns[i][3] = 2*columns[i][3]
                columns[i][0] = 0
                temp = True

            else:
                shouldGenerate = False

            if columns[i][1] == columns[i][0] and columns[i][1] != 0:
                columns[i][1] = combine(columns[i][1], columns[i][0])
                columns[i][0] = 0
                temp = True

            for k in range(4):
                m = 3-k
                if columns[i][m] != 0 and m != 3:
                    for l in range(k):
                        if columns[i][3-l] == 0:
                            columns[i][3-l] = columns[i][m]
                            columns[i][m] = 0
                            temp = True
                            break



    if direction == 'left':
        for i in range(4):
            if columns[0][i] == columns[1][i] and columns[0][i] != 0:
                columns[0][i] = combine(columns[0][i], columns[1][i])
                columns[1][i] = 0
                temp = True

            elif columns[1][i] == columns[2][i] and columns[1][i] != 0:
                columns[1][i] = combine(columns[1][i], columns[2][i])
                columns[2][i] = 0
                temp = True

            elif columns[0][i] == columns[2][i] and columns[1][i] == 0 and columns[0][i] != 0:
                columns[0][i] = 2 * columns[0][i]
                columns[2][i] = 0
                temp = True

            elif columns[1][i] == columns[3][i] and columns[2][i] == 0 and columns[1][i] != 0:
                columns[1][i] = 2 * columns[1][i]
                columns[3][i] = 0
                temp = True

            elif columns[0][i] == columns[3][i] and columns[1][i] == 0 and columns[2][i] == 0 and columns[0][i] != 0:
                columns[0][i] = 2 * columns[0][i]
                columns[3][i] = 0
                temp = True

            else:
                shouldGenerate = False

            if columns[2][i] == columns[3][i] and columns[2][i] != 0:
                columns[2][i] = combine(columns[2][i], columns[3][i])
                columns[3][i] = 0
                temp = True

            for k in range(4):
                if columns[k][i] != 0:
                    if k != 0:
                        for l in range(k):
                            if columns[l][i] == 0:
                                columns[l][i] = columns[k][i]
                                columns[k][i] = 0
                                temp = True
                                break


    if direction == 'right':
        for i in range(4):
            if columns[3][i] == columns[2][i] and columns[3][i] != 0:
                columns[3][i] = combine(columns[3][i], columns[2][i])
                columns[2][i] = 0
                temp = True

            elif columns[2][i] == columns[1][i] and columns[2][i] != 0:
                columns[2][i] = combine(columns[2][i], columns[1][i])
                columns[1][i] = 0
                temp = True

            elif columns[3][i] == columns[1][i] and columns[2][i] == 0 and columns[3][i] != 0:
                columns[3][i] = 2 * columns[3][i]
                columns[1][i] = 0
                temp = True

            elif columns[2][i] == columns[0][i] and columns[1][i] == 0 and columns[2][i] != 0:
                columns[2][i] = 2 * columns[2][i]
                columns[0][i] = 0
                temp = True

            elif columns[3][i] == columns[0][i] and columns[2][i] == 0 and columns[1][i] == 0 and columns[3][i] != 0:
                columns[3][i] = 2 * columns[3][i]
                columns[0][i] = 0
                temp = True

            else:
                shouldGenerate = False

            if columns[1][i] == columns[0][i] and columns[1][i] != 0:
                columns[1][i] = combine(columns[1][i], columns[0][i])
                columns[0][i] = 0
                temp = True

            for m in range(4):
                k = 3-m
                if columns[k][i] != 0:
                    if k != 3:
                        for w in range(m):
                            l = 3-w
                            if columns[l][i] == 0:
                                columns[l][i] = columns[k][i]
                                columns[k][i] = 0
                                temp = True
                                break

    if temp == True:
        shouldGenerate = True
    checkIfFull()


def checkIfFull():
    global boardIsFull
    var = checkGameOver()
    for i in range(4):
        toBreak = False
        for j in range(4):
            if columns[i][j] == 0:
                print('broke while loop')
                boardIsFull = False
                toBreak = True

            elif i == 3 and j == 3:
                print('board is full')
                boardIsFull = True

        if toBreak == True:
            print('broken!!!!!!!')
            break

def display(txt):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(txt, True, BLACK)
    screen.blit(text, [250, 250])

def generateNewTile():
    global boardIsFull
    newTilePosX = random.randrange(0, 4)
    newTilePosY = random.randrange(0, 4)

    while not columns[newTilePosX][newTilePosY] == 0 and not boardIsFull:
        newTilePosX = random.randrange(0, 4)
        newTilePosY = random.randrange(0, 4)
        checkIfFull()


    if boardIsFull == False:
        fourOrTwo = random.randrange(0, 10)
        if fourOrTwo == 0:
            newTileValue = 4
        else:
            newTileValue = 2

        columns[newTilePosX][newTilePosY] = newTileValue

    else:
        print('boardIsFull = True')


def checkGameOver():
    for i in range(4):
        for j in range(4):
            if columns[i][j] == 2048:
                return 'Win'
            else:
                if i != 0:
                    if columns[i-1][j] == columns[i][j]:
                        return 'Active'
                if i != 3:
                    if columns[i][j] == columns[i+1][j]:
                        return 'Active'
                if j != 0:
                    if columns[i][j-1] == columns[i][j]:
                        return 'Active'
                if j != 3:
                    if columns[i][j+1] == columns[i][j]:
                        return 'Active'
                if columns[i][j] == 0:
                    return 'Active'
    return 'Lose'


def addNewTileMse(x, y):
    colX = x//100
    colY = y//100
    columns[colX][colY] = 2


def drawValues():
    for i in range(4):
        for j in range(4):
            font = pygame.font.SysFont('Calibri', 25, True, False)
            if columns[i][j] != 0:
                text = font.render(str(columns[i][j]), True, BLACK)
                screen.blit(text, [15+100*i, 15+100*j])

def drawLines():
    for i in range(3):
        pygame.draw.line(screen, BLACK, [100+100*i, 0], [100+100*i, 400])
        pygame.draw.line(screen, BLACK, [0, 100+100*i], [400, 100+100*i])

def drawTiles():
    for i in range(len(columns)):
        for j in range(len(columns[i])):
            if columns[i][j] != 0:
                index = -1
                temp = columns[i][j]
                while temp != 1:
                    index += 1
                    temp /= 2
                    #print('index is', index)
                color = colors[index]

                #print(color)
                pygame.draw.rect(screen, color, [0+100*i, 0+100*j, 100, 100])
                # print('Drew square at ', str(i), str(j))

def drawEndText():
    var = checkGameOver()
    if var == 'Win':
        font = pygame.font.Font(None, 25)
        text = font.render("You win!", True, BLACK)
        text_rect = text.get_rect(center=(400 / 2, 400 / 2))
        screen.blit(text, text_rect)

    elif var == 'Lose':
        font = pygame.font.Font(None, 25)
        text = font.render("You lose!", True, BLACK)
        text_rect = text.get_rect(center=(400 / 2, 400 / 2))
        screen.blit(text, text_rect)

##### pygame start #####

pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('2048')
clock = pygame.time.Clock()

generateNewTile()

screen.fill(clrBackground)
drawTiles()
drawValues()
drawLines()
pygame.display.flip()


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if not checkGameOver() == "Win":
                    moveTiles('up')
                    print(shouldGenerate)
                    if shouldGenerate:
                        generateNewTile()

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if not checkGameOver() == 'Win':
                    moveTiles('down')
                    if shouldGenerate:
                        generateNewTile()

            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if not checkGameOver() == 'Win':
                    moveTiles('left')
                    if shouldGenerate:
                        generateNewTile()

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if not checkGameOver() == 'Win':
                    moveTiles('right')
                    if shouldGenerate:
                        generateNewTile()

            elif event.key == pygame.K_SPACE:
                generateNewTile()

            elif event.key == pygame.K_ESCAPE:
                done = True

            screen.fill(clrBackground)
            drawTiles()
            drawValues()
            drawLines()
            drawEndText()
            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                #print("Left Mouse key was clicked")
                pass
            if mouse_presses[1]:
                #print("middle scroll wheel was pressed down")
                pass

            if mouse_presses[2]:
                print('right clicked')
                print(columns)
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                print(pos)
                addNewTileMse(x, y)

            screen.fill(clrBackground)
            drawTiles()
            drawValues()
            drawLines()
            pygame.display.flip()




    clock.tick(30)

pygame.quit()



