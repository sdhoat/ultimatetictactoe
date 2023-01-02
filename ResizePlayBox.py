###################### 
#Ultimate Tic-Tac-Toe# 
#####Samar Dhoat###### 
###December 19,2019### 
######################
#This function defines each rectangle after a suqare had been clicked, so you can't click the same box twice
def ResizePlayBox(playrect,allowedx,allowedy):
    if allowedx == -1 and allowedy == -1:
        playrect[0] = 5
        playrect[1] = 5
        playrect[2] = 245
        playrect[3] = 245
    else:
        playrect[1]= allowedy * 80 + 10 + ((allowedy//3 -1) *5)
        playrect[0]= allowedx * 80 + 10 + ((allowedx//3 -1) *5)
        playrect[2]= 245
        playrect[3]= 245
