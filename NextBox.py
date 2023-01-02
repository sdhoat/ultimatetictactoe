######################
#Ultimate Tic-Tac-Toe#
#####Samar Dhoat######
###December 19,2019###
######################
#This define function chooses which box the ring goes to after every added Purple or Gold
def NextBox(Ccords,TotalGrid): 
    boxFull = False 
    if TotalGrid[Ccords[0]%3][Ccords[1]%3] != 0: 
        return (-1,-1) 
    else: 

        return((Ccords[0]%3)*3,(Ccords[1]%3)*3) 
