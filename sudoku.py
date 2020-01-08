
import pygame
from pygame.locals import *
import sys

#Global variable

SCREEN=pygame.display.set_mode((415,415))
pygame.display.set_caption('Sudoku Solver 1.0')
pygame.display.set_icon(pygame.image.load('images1.jpg'))
FPS=600
WIDTH = 35
HEIGHT = 35
 
# This sets the margin between each cell
MARGIN = 10
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
keySpace=False
numColor=BLACK
# numx=21
# numy=12


def zeroFinder(l,temp):
    for i in range(9):
        for j in range(9):
            if l[i][j]==0:
                temp[0]=i
                temp[1]=j
                return True
        
    return False



def isInRow(row,column,num,l):
    for j in range(9):
        if j==column:
            continue
        if l[row][j]==num:
            return True
       
    return False

def isInCol(row,column,num,l):
    for i in range(9):
        if i==row:
            continue
        if l[i][column]==num:
            return True
    return False

def subMatrix(row,column,num,l):
    for i in range(3):
        for j in range(3):
            if i==row and j==column:
                continue
            if l[i+row][j+column]==num:
                return True
    return False




def solve(l):
    # print("hello1")
    global numColor
    temp=[0,0]
    # row,column=zeroFinder(t)

    if not zeroFinder(l,temp):
        return True
    row=temp[0]
    column=temp[1]
    # print(row,column)
    for num in range(1,10):

        if not isInRow(row,column,num,l) and not isInCol(row,column,num,l) and not subMatrix(row - row%3,column - column%3,num,l) :
            l[row][column]=num
            if not keySpace:
                mainScreen(l)

            if solve(l):
                return True
            l[row][column]=0
            # numColor=RED

    return False

def welcomeScreen():
    # pygame.init()
    color=WHITE

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                return False
            elif event.type==KEYDOWN :#Press any key to continue#and (event.key==K_SPACE or event.key == K_UP):
                return
            else :
                SCREEN.blit(pygame.image.load('1.jpg'),(0,0))
                SCREEN.blit(pygame.image.load('output-onlinepngtools.png'),(20,280))
                SCREEN.blit(pygame.image.load('5.png'),(110,290))
                
                # SCREEN.blit(pygame.image.load('5.png').convert(),(10,160))

                # SCREEN.fill(RED)
                # pygame.draw.rect(SCREEN,
                #                  color,
                #                  [0,410,415,60])
                SCREEN.blit(welcomeFont.render('Welcome To Sudoku Solver 1.0', 1, WHITE),(8,110))
                SCREEN.blit(infoFont.render('Shows How Algorithm Solves the Sudoku Problem', 1, BLACK),(60,150))
                # SCREEN.blit(welcomeFont.render('Press any key ', 1, WHITE),(130,300))
                # SCREEN.blit(welcomeFont.render('To Continue!', 1, WHITE),(140,330))

                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainScreen(l):
    global keySpace
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                return False
            elif event.type==KEYDOWN and event.key==K_SPACE:
                keySpace=True
            
        for row in range(9):
            for column in range(9):
                color = WHITE
                # if grid[row][column] == 1:
                #     color = GREEN
                pygame.draw.rect(SCREEN,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        numx=21
        numy=12
        for row in range(9):
            numy=12+45*row
            for column in range(9):
                numx=21+45*column
                if l[row][column]==0:

                    numberShow=myFont.render('', 1, numColor)
                    
                else:
                    numberShow=myFont.render(str(l[row][column]), 1, numColor)
                SCREEN.blit(numberShow,((numx,numy)))
        # pygame.display.flip()
        # SCREEN.blit(myFont.render(str(FPSCLOCK), 1, numColor),(200,435))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        pygame.time.wait(100)
        return

def endScreen(l):
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False
            
        for row in range(9):
            for column in range(9):
                color = WHITE
                # if grid[row][column] == 1:
                #     color = GREEN
                pygame.draw.rect(SCREEN,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        numx=21
        numy=12
        for row in range(9):
            numy=12+45*row
            for column in range(9):
                numx=21+45*column
                if l[row][column]==0:

                    numberShow=myFont.render('', 1, BLACK)
                    
                else:
                    numberShow=myFont.render(str(l[row][column]), 1, BLACK)
                SCREEN.blit(numberShow,((numx,numy)))
        # pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick(FPS)



if __name__ == '__main__':
    l=[[3,0,6,5,0,8,4,0,0], 
      [5,2,0,0,0,0,0,0,0], 
      [0,8,7,0,0,0,0,3,1], 
      [0,0,3,0,1,0,0,8,0], 
      [9,0,0,8,6,3,0,0,5], 
      [0,5,0,0,9,0,6,0,0], 
      [1,3,0,0,0,0,2,5,0], 
      [0,0,0,0,0,0,0,7,4], 
      [0,0,5,2,0,6,3,0,0]] 

    pygame.init()
    myFont = pygame.font.SysFont("Times New Roman", 25)
    welcomeFont= pygame.font.SysFont("comicsansms", 28)
    infoFont=pygame.font.SysFont("Times New Roman", 15)
    FPSCLOCK = pygame.time.Clock()
    welcomeScreen()
    # SCREEN.fill(RED)
    SCREEN.blit(pygame.image.load('1.jpg'),(0,0))
    solve(l)
    endScreen(l)

   