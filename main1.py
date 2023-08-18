import pygame,keyboard, time, math

pygame.init()
clock= pygame.time.Clock()

size = (1200, 900)

white = (255, 255, 255)
grey = (125, 125, 125)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("A* Pathfinding")
gameRun = True
barrierList = []
start = []
target = []

def drawGrid():
    count = 0
    for i in range(0, 36):
        for j in range(0, 48):
            posY, posX = math.floor(mousePos[1] / 25), math.floor(mousePos[0] / 25)

            if posY == i and posX == j and buttonsPressed[0] == True: #yes it's a nested if statment, leave me alone
                if not start:
                    print(start)
                    start.append([posY, posX])
                    print(start)
                elif not target:
                    target.append([posY, posX])
                elif [posY, posX] not in barrierList and not [posY, posX] in start and [posY, posX] not in target:
                    barrierList.append([posY, posX])

            
            
            if [i, j] in barrierList:
                pygame.draw.rect(screen, black, [(j * 25), (i * 25), 23, 23])

            elif posY == i and posX == j:
                pygame.draw.rect(screen, grey, [(j * 25), (i * 25), 23, 23])
            else:
                pygame.draw.rect(screen, white, [(j * 25), (i * 25), 23, 23])
            





while gameRun == True:


    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        buttonsPressed = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            gameRun = False
    drawGrid()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
