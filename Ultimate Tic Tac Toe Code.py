###################### 
#Ultimate Tic-Tac-Toe# 
#####Samar Dhoat###### 
###December 19,2019### 
######################

#importing the modules I will be using
import pygame
import image

#importing define functions
from ResizePlayBox import ResizePlayBox
from NextBox import NextBox
from WinCalculator import winCalc
from WinCalculator import winSetter

#defined colors that are being used
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
#The X color
PURPLE = (255 , 0 , 255)
#The O color
GOLD = (255 , 215 , 0)
#Color of ring outside the box your clicking on
MainColor = [0 , 255 , 255]

#The empty lists for the dimensions
grid = []
TotalGrid = []

#Adding slots to the grid
for row in range(3):
    TotalGrid.append([])
    for column in range(3):
        TotalGrid[row].append(0)
for row in range(9):
    grid.append([])
    for column in range(9):
        grid[row].append(0)

#The size of the playing area
playrect = [5,5,735,735]

#initializing game
pygame.init()
#creating screem
screen = pygame.display.set_mode([745,745])
#making sure certain clicked x and y values are not allowed
allowedx = -1
allowedy = -1
#The width of the inside boxes
playwidth = int(75//20)
if playwidth == 0:
    playwidth = 1
#Create a true statement to be able to choose the opposite of something because I can not write true because it is not a define function.
Which_Color_Playing = True

#while loop that is running the game until someone wins
print("X is Purple and Gold is O. Try to get Tic-Tac-Toc 3 boxes in a row to win. Good Luck!")

while not False:
    #game start event
    for event in pygame.event.get():
        #button to click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #finding the position of the click
            pos = pygame.mouse.get_pos()
            xcord = ((pos[0] - ((pos[0]//450)-1)*5) - 10) // 80
            ycord = ((pos[1] - ((pos[1]//450)-1)*5) - 10) // 80
            #for certain co-oridinates the code works
            if xcord /8 <= 1 and ycord /8 <= 1:
                if grid[xcord][ycord] == 0:
                    #if the x and y values are the minimum then this goes to the define functions of the resizing of the playbox, the next box, and the winner calculations
                    if allowedx == -1 and allowedy == -1:
                        if Which_Color_Playing == True:
                            grid[xcord][ycord] = 1
                            Which_Color_Playing = False
                            playcolour = PURPLE
                        else:
                            grid[xcord][ycord] = 2
                            Which_Color_Playing = True
                            playcolour = GOLD
                        winCalc([xcord,ycord],grid,TotalGrid)
                        allowedx,allowedy = NextBox([xcord,ycord],TotalGrid)
                        ResizePlayBox(playrect,allowedx,allowedy)
                    #if the x and y values are greater than the minimum then it goes to the define functions of the resizing of the playbox, the next box, and the winner calculations
                    elif allowedx <= xcord <= allowedx+2 and allowedy <= ycord <= allowedy+2:
                        if Which_Color_Playing == True:
                            grid[xcord][ycord] = 1
                            Which_Color_Playing = False
                            playcolour = PURPLE
                        else:
                            grid[xcord][ycord] = 2
                            Which_Color_Playing = True
                            playcolour = GOLD
                        winCalc([xcord , ycord] , grid , TotalGrid)
                        allowedx,allowedy = NextBox([xcord , ycord] , TotalGrid)
                        ResizePlayBox(playrect , allowedx , allowedy)
                        
    #this next section is for the asthetic of the tictactoe
    screen.fill(BLACK)
    marginx = 0
    marginy = 0
    #color filler for each box
    for row in range(9):
        if row % 3 == 0:
            marginy = marginy + 5
        for column in range(9):
            color = WHITE
            if column % 3 == 0:
                marginx = marginx + 5
            if grid[column][row] == 1:
                color = PURPLE
            if grid[column][row] == 2:
                color = GOLD
            pygame.draw.rect(screen , color ,[80 * column + 5 + marginx, 80 * row + 5 + marginy, 75, 75])
            pygame.draw.rect(screen , MainColor , playrect , playwidth)
        marginx = 0
    #this command allows pygame to focus only on this code and not everything else in its data base
    pygame.display.flip()
#quit to stop using computer memory
pygame.quit()
