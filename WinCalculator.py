###################### 
#Ultimate Tic-Tac-Toe# 
#####Samar Dhoat###### 
###December 19,2019### 
######################

#This define function defines which team wins
def SetWin(Grid,Team,TotalGrid):
    for x in range(9):
        for y in range(9):
            Grid[x][y] = Team
    for x in TotalGrid:
        for y in x:
            y = Team
            
#This define function colors in the boxes if and when a team wins a big box  
def winSetter(OC,Team,Grid,TotalGrid):
        TotalGrid[OC[0]//3][OC[1]//3] = Team
        for x in range((OC[0]//3) * 3,(OC[0]//3) *3 + 3):
                for y in range((OC[1]//3) * 3,(OC[1]//3) *3 + 3):
                        Grid[x][y] = Team
        for x in range(0,3):  
            if TotalGrid[x][0] == Team and TotalGrid[x][1] == Team and TotalGrid[x][2] == Team:
                    if Team == 1:
                            SetWin(Grid,1,TotalGrid)
                            import image
                            X = image.Image("xwins.gif")  
                            X_w = X.getWidth()  
                            X_h = X.getHeight()  
                            wn = image.ImageWin(X_w * 2, X_h * 2) 
                            X_new = image.EmptyImage(X_w * 2, X_h * 2)  
                            for r in range(X_h):  
                                for c in range(X_w):  
                                    pixel = X.getPixel(c , r)  
                                    X_new.setPixel(2*c, 2*r , pixel)  
                                    X_new.setPixel(2*c +1, 2*r , pixel)  
                                    X_new.setPixel(2*c, 2*r+1 , pixel) 
                                    X_new.setPixel(2*c +1, 2*r+1 , pixel)  
                            X_new.draw(wn) 
                            wn.exitonclick() 
                    else:
                            SetWin(Grid,2,TotalGrid)
                            import image
                            O = image.Image("owins.gif") 
                            O_w = O.getWidth()  
                            O_h = O.getHeight()  
                            wn = image.ImageWin(O_w * 2, O_h * 2)  
                            O_new = image.EmptyImage(O_w * 2, O_h * 2)  
                            for r in range(O_h):  
                                for c in range(O_w):  
                                    pixel = O.getPixel(c , r) 
                                    O_new.setPixel(2*c, 2*r , pixel)  
                                    O_new.setPixel(2*c +1, 2*r , pixel)  
                                    O_new.setPixel(2*c, 2*r+1 , pixel) 
                                    O_new.setPixel(2*c +1, 2*r+1 , pixel) 
                            O_new.draw(wn)  
                            wn.exitonclick() 
        for y in range(0,3):  
            if TotalGrid[0][y] == Team and TotalGrid[1][y] == Team and TotalGrid[2][y] == Team:   
                if Team == 1:
                        SetWin(Grid,1,TotalGrid)
                        import image
                        X = image.Image("xwins.gif")  
                        X_w = X.getWidth()  
                        X_h = X.getHeight()  
                        wn = image.ImageWin(X_w * 2, X_h * 2) 
                        X_new = image.EmptyImage(X_w * 2, X_h * 2)  
                        for r in range(X_h):  
                            for c in range(X_w):  
                                pixel = X.getPixel(c , r)  
                                X_new.setPixel(2*c, 2*r , pixel)  
                                X_new.setPixel(2*c +1, 2*r , pixel)  
                                X_new.setPixel(2*c, 2*r+1 , pixel) 
                                X_new.setPixel(2*c +1, 2*r+1 , pixel)  
                        X_new.draw(wn) 
                        wn.exitonclick()
                else:
                        SetWin(Grid,2,TotalGrid)
                        import image
                        O = image.Image("owins.gif") 
                        O_w = O.getWidth()  
                        O_h = O.getHeight()  
                        wn = image.ImageWin(O_w * 2, O_h * 2)  
                        O_new = image.EmptyImage(O_w * 2, O_h * 2)  
                        for r in range(O_h):  
                            for c in range(O_w):  
                                pixel = O.getPixel(c , r) 
                                O_new.setPixel(2*c, 2*r , pixel)  
                                O_new.setPixel(2*c +1, 2*r , pixel)  
                                O_new.setPixel(2*c, 2*r+1 , pixel) 
                                O_new.setPixel(2*c +1, 2*r+1 , pixel) 
                        O_new.draw(wn)  
                        wn.exitonclick() 
                if Team == 1:
                        SetWin(Grid,1,TotalGrid)
                        import image
                        X = image.Image("xwins.gif")  
                        X_w = X.getWidth()  
                        X_h = X.getHeight()  
                        wn = image.ImageWin(X_w * 2, X_h * 2) 
                        X_new = image.EmptyImage(X_w * 2, X_h * 2)  
                        for r in range(X_h):  
                            for c in range(X_w):  
                                pixel = X.getPixel(c , r)  
                                X_new.setPixel(2*c, 2*r , pixel)  
                                X_new.setPixel(2*c +1, 2*r , pixel)  
                                X_new.setPixel(2*c, 2*r+1 , pixel) 
                                X_new.setPixel(2*c +1, 2*r+1 , pixel)  
                        X_new.draw(wn) 
                        wn.exitonclick()
                else:
                        SetWin(Grid,2,TotalGrid)
                        import image
                        O = image.Image("owins.gif") 
                        O_w = O.getWidth()  
                        O_h = O.getHeight()  
                        wn = image.ImageWin(O_w * 2, O_h * 2)  
                        O_new = image.EmptyImage(O_w * 2, O_h * 2)  
                        for r in range(O_h):  
                            for c in range(O_w):  
                                pixel = O.getPixel(c , r) 
                                O_new.setPixel(2*c, 2*r , pixel)  
                                O_new.setPixel(2*c +1, 2*r , pixel)  
                                O_new.setPixel(2*c, 2*r+1 , pixel) 
                                O_new.setPixel(2*c +1, 2*r+1 , pixel) 
                        O_new.draw(wn)  
                        wn.exitonclick() 

#This define function describes all the ways to win, except for diagonal of the 3x3 big one
def winCalc(OuterCords,Grid,TotalGrid):  
    OC = OuterCords 
    IC = (OC[0]%3,OC[1]%3)
    thisTileTeam = Grid[OC[0]][OC[1]]
    Team = thisTileTeam
    if IC == (0,0):
            if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]+2][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid)
            elif Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]+2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid)
            elif Grid[OC[0]+1][OC[1]+1] == thisTileTeam and Grid[OC[0]+2][OC[1]+2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (1,0):
            if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]-1][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid)
            elif Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]+2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (2,0): 
            if Grid[OC[0]-1][OC[1]] == thisTileTeam and Grid[OC[0]-2][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]+2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]-1][OC[1]+1] == thisTileTeam and Grid[OC[0]-2][OC[1]+2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (0,1):
            if Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]-1] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid)
            elif Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]+2][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (1,1): 
            if Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]-1] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]-1][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]-1][OC[1]-1] == thisTileTeam and Grid[OC[0]+1][OC[1]+1] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]-1][OC[1]+1] == thisTileTeam and Grid[OC[0]+1][OC[1]-1] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (2,1): 
            if Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]-1] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]-1][OC[1]] == thisTileTeam and Grid[OC[0]-2][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid)
    elif IC == (0,2): 
            if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]+2][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]][OC[1]-1] == thisTileTeam and Grid[OC[0]][OC[1]-2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]+1][OC[1]-1] == thisTileTeam and Grid[OC[0]+2][OC[1]-2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (1,2):
            if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]-1][OC[1]] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid)
            elif Grid[OC[0]][OC[1]-1] == thisTileTeam and Grid[OC[0]][OC[1]-2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    elif IC == (2,2): 
            if (Grid[OC[0]][OC[1]-1] == thisTileTeam and Grid[OC[0]][OC[1]-2] == thisTileTeam):
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif (Grid[OC[0]-1][OC[1]] == thisTileTeam and Grid[OC[0]-2][OC[1]] == thisTileTeam):
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
            elif Grid[OC[0]-1][OC[1]-1] == thisTileTeam and Grid[OC[0]-2][OC[1]-2] == thisTileTeam:
                    winSetter(OC,thisTileTeam,Grid,TotalGrid) 
    amtused = 0
    for x in range(OC[0]-IC[0],OC[0]-IC[0]+3):
            for y in range(OC[1]-IC[1],OC[1]-IC[1]+3):
                    if Grid[x][y] != 0:
                            amtused = amtused + 1 
    if amtused == 9:
            if TotalGrid[OC[0]//3][OC[1]//3] == 0:
                    TotalGrid[OC[0]//3][OC[1]//3] = -1
