# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:01:48 2020

@author: Bouadi Khadija
"""

               ##################################################### ConnectGame #############################################

from pprint import pprint
class ConnectGame:
    def __init__(self,inPlay,p1,p2):
        self.p1=p1
        self.p2=p2
        self.inPlay=inPlay
        self.L=[["-" for i in range(7)] for j in range(6)]
        self.lastInput=[0,0]
        
    def showTable(self):
        pprint(self.L)
        
    def passTo(self):
        if(self.inPlay=="X"):
            self.inPlay="O"
        else:
            self.inPlay="X"
            
    def fillTurn(self,column):
        for i in range(5,-1,-1):
            if(self.L[i][column]=="-"):
                self.L[i][column]=self.inPlay;
                self.lastInput=[i,column]
                return True
        return False
    
    def checkWin(self): 
# Check horizontally
        if(self.lastInput[1]==0):
            if(self.L[self.lastInput[1]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]==self.inPlay):
                return True
        if(self.lastInput[1]==1):
             if(self.L[self.lastInput[0]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==2):
             if(self.L[self.lastInput[0]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==3):
             if(self.L[self.lastInput[0]][0]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True;
        if(self.lastInput[1]==4):
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][1]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==5):
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][2]==self.L[self.lastInput[0]][3]):
                 return True
        if(self.lastInput[1]==6):
             if(self.L[self.lastInput[0]][4]==self.L[self.lastInput[0]][5]==self.L[self.lastInput[0]][6]==self.L[self.lastInput[0]][3]):
                 return True
# Check vertically       
        if(self.lastInput[0]<3):
              if(self.L[self.lastInput[0]][self.lastInput[1]]==self.L[self.lastInput[0]+1][self.lastInput[1]]==self.L[self.lastInput[0]+2][self.lastInput[1]]==self.L[self.lastInput[0]+3][self.lastInput[1]]):
                  return True 
        
        
# Check diagonale bottom-right to top-left
        if self.lastInput[0] >= 3 and self.lastInput[1] >= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]-1][self.lastInput[1]-1] == self.L[self.lastInput[0]-2][self.lastInput[1]-2] == self.L[self.lastInput[0]-3][self.lastInput[1]-3]):
               return True
# Check diagonale bottom-left to top-right
        if self.lastInput[0] >= 3 and self.lastInput[1] <= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]-1][self.lastInput[1]+1] == self.L[self.lastInput[0]-2][self.lastInput[1]+2] == self.L[self.lastInput[0]-3][self.lastInput[1]+3]):
              return True
# Check diagonale top-left to bottom-right
        if self.lastInput[0] <= 2 and self.lastInput[1] <= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]+1][self.lastInput[1]+1] == self.L[self.lastInput[0]+2][self.lastInput[1]+2] == self.L[self.lastInput[0]+3][self.lastInput[1]+3]):
               return True
# Check diagonale top-right to bottom-left
        if self.lastInput[0] <= 2 and self.lastInput[1] >= 3:
             if (self.L[self.lastInput[0]][self.lastInput[1]] == self.L[self.lastInput[0]+1][self.lastInput[1]-1] == self.L[self.lastInput[0]+2][self.lastInput[1]-2] == self.L[self.lastInput[0]+3][self.lastInput[1]-3]):
                return True


        return False

        
    
c=ConnectGame("X", "Omar", "Ali")
while True:
    if(c.fillTurn(int(input("Player "+c.inPlay+" give the column to play:")))):
        c.showTable()
        c.passTo()
    else:
        print("Impossible")
    if(c.checkWin()):
        c.passTo()
        print("Player "+ c.inPlay+ " has won !")
        break
    
