#Project start date:22/12/18
#Aim: to create a fully functional tic tac toe game
#step1:Devlop logic for tic tac toe
#step2:use turtle to execute the commands
#step3:create an UI
import os as sys
import numpy as np
def gamecreater():
     #creates a matrix to hold our values
     matrix=np.zeros(dtype="int",shape=(3,3))
     return matrix

def playerid():
    #assigns player ids
    print("Player 1 choose symbol (X or O):")
    playersym=input()
    player1id=1
    player2id=2

    if playersym=="x" or "X":
        player2sym="O"
        player1sym="X"

    else:
        player2sym=="X"
        player1sym=="O"

    return player1id,player2id,player1sym,player2sym

def gamerefree(matrix):
    rindex=0   #row index
    winnerr=None  #id of the winner
    rowcheck=0
    while rindex<3:  #checks for unfilled values in each row
        wl=matrix[rindex]
        if 0 in wl:
            rindex=rindex+1
            continue
        else:
            if wl[2]==wl[1]:
                if wl[0]==wl[1]:
                    rowcheck=True
                    winnerr=wl[1]
                    break
    cindex=0   #col index
    winnerc=None
    colcheck=0
    while cindex<3:
        wl=[]
        fele=matrix[0][cindex] #fele-first element
        sele=matrix[1][cindex]
        tele=matrix[2][cindex]
        wl.append(fele)
        wl.append(sele)
        wl.append(tele)
        if 0 in wl:
            cindex=cindex+1
            continue
        else:
            if wl[2]==wl[1]:
                if wl[0]==wl[1]:
                    colcheck=True
                    winnerc=wl[1]
                    break
    diagcheck=None
    winnerd=0
    if matrix[0][0]==matrix[1][1]==matrix[2][2]:
        if matrix[0][0]!=0:
            diagcheck=True
            winnerd=matrix[0][0]
    elif matrix[0][2]==matrix[1][1]==matrix[2][0]:
        if matrix[1][1]!=0:
            diagcheck=True
            winnerd=matrix[1][1]




    if rowcheck==True:
        return "Finished",winnerr
    elif colcheck==True:
        return "Finished",winnerc
    elif diagcheck==True:
        return "Finished",winnerd
    else:
        return "play",0

superl=[] #master list keeping track of all the loctions used


def backplay(matrix,p1turns,p2turns):
    '''
    Main player fuction which executes user commands
    '''

    status,playerid=gamerefree(matrix) #Calls up game ref for status
    if status=="play":
        if p1turns==p2turns:
            print("Player1->")
            l=[]
            ip1,ip2=input("Give mat loc(, sep):").split(",")
            p1row=int(ip1)
            p1col=int(ip2)
            l.append(p1row)
            l.append(p1col)
            if l in superl:
                print("Wrong pos!!!!!")
                return matrix,True,0,0  #True signifies the game is still on
                #0,0 says how many turs of each player executed in each iter.
            else:
                superl.append(l)
                matrix[p1row,p1col] =1
                print(matrix)
                status,playerid=gamerefree(matrix)
                if status=="Finished":
                    print("Player "+str(playerid)+"Wins!!!!!")
                    sys.exit()
                elif status=="Draw":
                    print("Well thats no good it was a draw!!!!!")
            print("Player2's turn now:")
            l1=[]
            ip1,ip2=input("Give mat loc(, sep):").split(",")
            p2row=int(ip1)
            p2col=int(ip2)
            l1.append(p2row)
            l1.append(p2col)
            if l1 in superl:
                print("Wrong pos!!!!")
                return matrix,True,1,0
            else:
                superl.append(l1)
                matrix[p2row,p2col]=2
                print(matrix)
                status,playerid=gamerefree(matrix)
                if status=="Finished":
                    print("Player "+str(playerid)+"Wins!!!!!")
                    sys.exit()
                elif status=="Draw":
                    print("Well thats no good it was a draw!!!!!")
        elif p2turns<p1turns:
            print("Player2's turn now:")
            l1=[]
            ip1,ip2=input("Give mat loc(, sep):").split(",")
            p2row=int(ip1)
            p2col=int(ip2)
            l1.append(p2row)
            l1.append(p2col)
            if l1 in superl:
                print("Wrong pos!!!!")
                return matrix,True,1,0
            else:
                superl.append(l1)
                matrix[p2row,p2col]=2
                print(matrix)
                status,playerid=gamerefree(matrix)
                if status=="Finished":
                    print("Player "+str(playerid)+"Wins!!!!!")
                    sys.exit()
                elif status=="Draw":
                    print("Well thats no good it was a draw!!!!!")

        return matrix,True,1,1

    elif status=="Finished":
        print("The winner is:"+str(playerid))#add name feature later
        return matrix,False

    elif status=="Draw":
        print("The battle of wits comes to a draw")
        return matrix,False

def gamecontrol():
    player1id,player2id,player1sym,player2sym=playerid()
    p1turns=0
    p2turns=0
    inmatrix=gamecreater()
    retval,status,p1ad,p2ad=backplay(inmatrix,p1turns,p2turns)#first play
    p1turns=1
    p2turns=1
    while status!=False:
        p1ad,p2ad=0,0
        retval,status,p1ad,p2ad=backplay(retval,p1turns,p2turns)
        p1turns=p1turns +p1ad#increments no of playes
        p2turns=p2turns +p2ad
        if p1turns+p2turns>=9:
            print("That was a draw go again!!!")
            break

gamecontrol()
