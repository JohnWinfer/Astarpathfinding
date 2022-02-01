import pygame
import keyboard
import time
import math
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.time import *
pygame.init()

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0 , 0)
lightgrey = (194, 194, 194)
lightGreen = (194, 255, 194)
lightRed = (255, 194, 194)

size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A* Pathfinding")

programRunning = True

xcord = 0
ycord = 0
barrierList = []
openList = []
closeList = []
draw = False
sNode = 9999
fNode = 9999
cNode = 9999
sX = 9999
sY = 9999
fX = 9999
fY = 9999
start = False
count = 0

def drawGrid():
    global xcord, ycord, barrierList, draw, sNode, fNode, sX, sY, fX, fY, count
    count = 0
    for i in range(0, 36):
        for y in range(0, 48):
            (xPos, yPos) = mousePos
            draw = buttonsPressed[0]
            erase = buttonsPressed[2]
            if xPos >= xcord and xPos < (xcord + 25) and yPos >= ycord and yPos < (ycord + 25) and draw == True and sNode == 9999 and count != fNode:
                sNode = count
                sX = xcord
                sY = ycord

            elif xPos >= xcord and xPos < (xcord + 25) and yPos >= ycord and yPos < (ycord + 25) and draw == True and fNode == 9999 and sNode != 9999 and count != sNode:
                fNode = count
                fX = xcord
                fY = ycord

            elif xPos >= xcord and xPos < (xcord + 25) and yPos >= ycord and yPos < (ycord + 25) and draw == True and count not in barrierList and count != fNode and count != sNode:
                barrierList.append(count)

            if xPos >= xcord and xPos < (xcord + 25) and yPos >= ycord and yPos < (ycord + 25) and erase  == True:
                try:
                    barrierList.remove(count)
                except ValueError:
                    pass
                if count == sNode:
                    sNode = 9999
                if count == fNode:
                    fNode = 9999

            if sNode == count:
                pygame.draw.rect(screen, green, [xcord, ycord, 25, 25], 0)
            elif fNode == count:
                pygame.draw.rect(screen, red, [xcord, ycord, 25, 25], 0) 
            elif count in barrierList:
                pygame.draw.rect(screen, black, [xcord, ycord, 25, 25], 0)
            elif xPos >= xcord and xPos < (xcord + 25) and yPos >= ycord and yPos < (ycord + 25):
                if (sNode == 9999):
                    pygame.draw.rect(screen, lightGreen, [xcord, ycord, 25, 25], 0)
                elif (fNode == 9999):
                    pygame.draw.rect(screen, lightRed, [xcord, ycord, 25, 25], 0)
                else:
                    pygame.draw.rect(screen, lightgrey, [xcord, ycord, 25, 25], 0)
            else:
                pygame.draw.rect(screen, white, [xcord, ycord, 25, 25], 0)
            pygame.draw.rect(screen, black, [xcord, ycord, 25, 25], 1)
            

            
            count = count + 1
            xcord = xcord + 25
        xcord = 0
        ycord = ycord + 25



def StartSearch():
    global barrierList, count, sNode, fNode, sX, sY, fX, fY, start, openList, closeList
    if fNode == 9999 or sNode == 9999:
        print("Start/Finish node not placed!")
        start = False
    else:
        openList.append(sNode)
        while(openList != 0): #possible problem
            print("stop")



while programRunning:
    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        buttonsPressed = pygame.mouse.get_pressed()

        if event.type == pygame.QUIT:
            programRunning = False
    screen.fill(white)
    
    if keyboard.is_pressed(' '):
        sNode = 9999
        fNode = 9999
        barrierList.clear()

    if keyboard.is_pressed('enter'):
        start = True
    
    if start == True:
        print("search")


    xcord = 0
    ycord = 0
    
    if start == True:
        StartSearch()
    
    
    drawGrid()
    
    dist = round(math.sqrt(((sX-fX)**2 + (sY-fY)**2) / 625), 1) * 10
    print(dist)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()

