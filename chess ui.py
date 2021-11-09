# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:47:50 2021

@author: Snehangsu
"""

import pygame 
from pygame.locals import *
import copy
        
class Pieces(pygame.sprite.Sprite):
    
    def __init__(self,name,wPH,x,y,s,color,piece):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.wPH = wPH
        self.x = x
        self.y = y
        self.s = s
        self.color=color
        self.piece=piece
        
    def change_piece(self,img,color,piece):
        self.wPH=img
        self.color=color
        self.piece=piece
      
    def update_setup(self):
        self.s.blit(self.wPH,(self.x,self.y))
        
    def updateloc(self,x,y):
        self.s.blit(self.wPH,(x,y))
        
    def updateloc_permanent(self,x,y):
        self.x=x
        self.y=y
        
    def check_pos(self, alpha, num, mouse):
        position=alpha.get(int(self.x/60))+num.get(int(self.y/60))
        if mouse[0]>=self.x and mouse[0]<=self.x+60 and mouse[1]>=self.y and mouse[1]<=self.y+60 :

            return self.name  
        
    def get_square(self,alpha,num):
        position=alpha.get(int(self.x/60))+num.get(int(self.y/60))
        return position
                
    def get_pos(self):
        return (self.x,self.y)
    
    def get_color(self):
        return self.color
    
    def get_piece(self):
        return self.piece
    
    def get_name(self):
        return self.name
 
    
class CheckMove(object):
    
    def __init__(self,items,newx,newy,color,piece,pos_table,wboardstate,bboardstate):
        self.items=items
        self.newx=newx
        self.newy=newy
        self.color=color
        self.piece=piece
        self.pos_table=pos_table
        self.wboardstate=wboardstate
        self.bboardstate=bboardstate
        self.columns=["A","B","C","D","E","F","G","H"]
        self.rows=["1","2","3","4","5","6","7","8"]
        #if self.piece=="K":
            #self.king()
            
    def get_moves(self):
        moves=[]
        #print(self.newx,self.newy)
        if self.piece=="K":
            moves=self.King()
        elif self.piece=="Q":
            moves=self.Queen()
        elif self.piece=="B":
            moves=self.Bishop()
        elif self.piece=="N":
            moves=self.Knight()
        elif self.piece=="R":
            moves=self.Rook()
        elif self.piece=="P":   
            moves=self.Pawn_attack()
        
        return moves
        
            
    def King(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break
        posibilityspace=[]
        #print(square)
        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        col_index-=1
        row_index-=1
        for i in range(3):
            for j in range(3):
                if col_index==-1 or col_index==8 or row_index==-1 or row_index==8 or col_index==orig_col and row_index==orig_row:
                    row_index+=1
                    continue
                else:
                    posibilityspace.append(self.columns[col_index]+self.rows[row_index])
                    row_index+=1
            col_index+=1
            row_index-=3
        if self.color=="W":    
            c = [x for x in posibilityspace if x not in self.wboardstate]
            return c
        elif self.color=="B":
            c = [x for x in posibilityspace if x not in self.bboardstate]
            return c
        
    def Queen(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break
    
        col=square[0:1]
        row=square[1:2]
        #print(col,row)
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate,self.bboardstate]
        if self.color=="W":
            boardst=boardst
        else:
            boardst.reverse()
            
        run=True
        iterator=1
        leftbegin=[]
        rightbegin=[]
        
        downl=0
        upl=0
        downr=0
        upr=0
        
        while run:
            if downl==0 and (col_index-iterator<0 or row_index-iterator<0):
                downl=1
            elif downl==0 and self.columns[col_index-iterator]+self.rows[row_index-iterator] in boardst[0]:
                downl=1
            elif downl==0 and self.columns[col_index-iterator]+self.rows[row_index-iterator] in boardst[1]:
                leftbegin.append(self.columns[col_index-iterator]+self.rows[row_index-iterator])
                downl=1
            elif downl==0:
                leftbegin.append(self.columns[col_index-iterator]+self.rows[row_index-iterator])
                
            if upl==0 and (col_index+iterator>7 or row_index+iterator>7):
                upl=1
            elif upl==0 and self.columns[col_index+iterator]+self.rows[row_index+iterator] in boardst[0]:
                upl=1
            elif upl==0 and self.columns[col_index+iterator]+self.rows[row_index+iterator] in boardst[1]:
                leftbegin.append(self.columns[col_index+iterator]+self.rows[row_index+iterator])
                upl=1
            elif upl==0:
                leftbegin.append(self.columns[col_index+iterator]+self.rows[row_index+iterator])
                
            
            if downr==0 and (col_index+iterator>7 or row_index-iterator<0):  #here
                downr=1
            elif downr==0 and self.columns[col_index+iterator]+self.rows[row_index-iterator] in boardst[0]:
                downr=1
            elif downr==0 and self.columns[col_index+iterator]+self.rows[row_index-iterator] in boardst[1]:
                rightbegin.append(self.columns[col_index+iterator]+self.rows[row_index-iterator])
                downr=1
            elif downr==0:
                rightbegin.append(self.columns[col_index+iterator]+self.rows[row_index-iterator])
                
            if upr==0 and (col_index-iterator<0 or row_index+iterator>7):
                upr=1
            elif upr==0 and self.columns[col_index-iterator]+self.rows[row_index+iterator] in boardst[0]:
                upr=1
            elif upr==0 and self.columns[col_index-iterator]+self.rows[row_index+iterator] in boardst[1]:
                rightbegin.append(self.columns[col_index-iterator]+self.rows[row_index+iterator])
                upr=1
            elif upr==0:
                rightbegin.append(self.columns[col_index-iterator]+self.rows[row_index+iterator])
                
            if upl==1 and downl==1 and upr==1 and downr==1:
                run=False
                break
            
            iterator+=1
                
        leftbegin.extend(rightbegin)
        leftbegin=list(set(leftbegin))
                
        vertical=[]
        horizontal=[]
        
        up=0
        down=0
        left=0
        right=0
        
        for i in range(1,8):
                       
            if down==0 and row_index-i<0:
                down=1
            elif down==0 and self.columns[col_index]+self.rows[row_index-i] in boardst[0]:
                down=1
            elif down==0 and self.columns[col_index]+self.rows[row_index-i] in boardst[1]:
                vertical.append(self.columns[col_index]+self.rows[row_index-i])
                down=1
            elif down==0:
                vertical.append(self.columns[col_index]+self.rows[row_index-i])
                                           
            if up==0 and row_index+i>7:
                up=1
            elif up==0 and self.columns[col_index]+self.rows[row_index+i] in boardst[0]:
                up=1
            elif up==0 and self.columns[col_index]+self.rows[row_index+i] in boardst[1]:
                vertical.append(self.columns[col_index]+self.rows[row_index+i])
                up=1
            elif up==0:
                vertical.append(self.columns[col_index]+self.rows[row_index+i])
                    
            if left==0 and col_index-i<0:
                left=1
            elif left==0 and self.columns[col_index-i]+self.rows[row_index] in boardst[0]:
                left=1
            elif left==0 and self.columns[col_index-i]+self.rows[row_index] in boardst[1]:
                horizontal.append(self.columns[col_index-i]+self.rows[row_index])
                left=1
            elif left==0:
                horizontal.append(self.columns[col_index-i]+self.rows[row_index])
                        
                        
            if right==0 and col_index+i>7:
                right=1
            elif right==0 and self.columns[col_index+i]+self.rows[row_index] in boardst[0]:
                right=1
            elif right==0 and self.columns[col_index+i]+self.rows[row_index] in boardst[1]:
                horizontal.append(self.columns[col_index+i]+self.rows[row_index])
                right=1
            elif right==0:
                horizontal.append(self.columns[col_index+i]+self.rows[row_index])
                        
            if up==1 and down==1 and left==1 and right==1:
                break
        
        
        vertical.extend(horizontal)
        vertical=list(set(vertical))
        
        vertical.extend(leftbegin)
        vertical=list(set(vertical))
        return vertical
        
    
    def Bishop(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break
        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate,self.bboardstate]
        if self.color=="W":
            boardst=boardst
        else:
            boardst.reverse()
        
        run=True
        iterator=1
        leftbegin=[]
        rightbegin=[]
        
        downl=0
        upl=0
        downr=0
        upr=0
        
        while run:
            if downl==0 and (col_index-iterator<0 or row_index-iterator<0):
                downl=1
            elif downl==0 and self.columns[col_index-iterator]+self.rows[row_index-iterator] in boardst[0]:
                downl=1
            elif downl==0 and self.columns[col_index-iterator]+self.rows[row_index-iterator] in boardst[1]:
                leftbegin.append(self.columns[col_index-iterator]+self.rows[row_index-iterator])
                downl=1
            elif downl==0:
                leftbegin.append(self.columns[col_index-iterator]+self.rows[row_index-iterator])
                
            if upl==0 and (col_index+iterator>7 or row_index+iterator>7):
                upl=1
            elif upl==0 and self.columns[col_index+iterator]+self.rows[row_index+iterator] in boardst[0]:
                upl=1
            elif upl==0 and self.columns[col_index+iterator]+self.rows[row_index+iterator] in boardst[1]:
                leftbegin.append(self.columns[col_index+iterator]+self.rows[row_index+iterator])
                upl=1
            elif upl==0:
                leftbegin.append(self.columns[col_index+iterator]+self.rows[row_index+iterator])
                
            
            if downr==0 and (col_index+iterator>7 or row_index-iterator<0):  #here
                downr=1
            elif downr==0 and self.columns[col_index+iterator]+self.rows[row_index-iterator] in boardst[0]:
                downr=1
            elif downr==0 and self.columns[col_index+iterator]+self.rows[row_index-iterator] in boardst[1]:
                rightbegin.append(self.columns[col_index+iterator]+self.rows[row_index-iterator])
                downr=1
            elif downr==0:
                rightbegin.append(self.columns[col_index+iterator]+self.rows[row_index-iterator])
                
            if upr==0 and (col_index-iterator<0 or row_index+iterator>7):
                upr=1
            elif upr==0 and self.columns[col_index-iterator]+self.rows[row_index+iterator] in boardst[0]:
                upr=1
            elif upr==0 and self.columns[col_index-iterator]+self.rows[row_index+iterator] in boardst[1]:
                rightbegin.append(self.columns[col_index-iterator]+self.rows[row_index+iterator])
                upr=1
            elif upr==0:
                rightbegin.append(self.columns[col_index-iterator]+self.rows[row_index+iterator])
                
            if upl==1 and downl==1 and upr==1 and downr==1:
                run=False
                break
            
            iterator+=1
                
        leftbegin.extend(rightbegin)
        leftbegin=list(set(leftbegin))
        return leftbegin
    
    def Rook(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break

        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        vertical=[]
        horizontal=[]
        
        up=0
        down=0
        left=0
        right=0
        
        boardst=[self.wboardstate,self.bboardstate]
        if self.color=="W":
            boardst=boardst
        else:
            boardst.reverse()
            
        for i in range(1,8):
                       
            if down==0 and row_index-i<0:
                down=1
            elif down==0 and self.columns[col_index]+self.rows[row_index-i] in boardst[0]:
                down=1
            elif down==0 and self.columns[col_index]+self.rows[row_index-i] in boardst[1]:
                vertical.append(self.columns[col_index]+self.rows[row_index-i])
                down=1
            elif down==0:
                vertical.append(self.columns[col_index]+self.rows[row_index-i])
                                           
            if up==0 and row_index+i>7:
                up=1
            elif up==0 and self.columns[col_index]+self.rows[row_index+i] in boardst[0]:
                up=1
            elif up==0 and self.columns[col_index]+self.rows[row_index+i] in boardst[1]:
                vertical.append(self.columns[col_index]+self.rows[row_index+i])
                up=1
            elif up==0:
                vertical.append(self.columns[col_index]+self.rows[row_index+i])
                    
            if left==0 and col_index-i<0:
                left=1
            elif left==0 and self.columns[col_index-i]+self.rows[row_index] in boardst[0]:
                left=1
            elif left==0 and self.columns[col_index-i]+self.rows[row_index] in boardst[1]:
                horizontal.append(self.columns[col_index-i]+self.rows[row_index])
                left=1
            elif left==0:
                horizontal.append(self.columns[col_index-i]+self.rows[row_index])
                        
                        
            if right==0 and col_index+i>7:
                right=1
            elif right==0 and self.columns[col_index+i]+self.rows[row_index] in boardst[0]:
                right=1
            elif right==0 and self.columns[col_index+i]+self.rows[row_index] in boardst[1]:
                horizontal.append(self.columns[col_index+i]+self.rows[row_index])
                right=1
            elif right==0:
                horizontal.append(self.columns[col_index+i]+self.rows[row_index])
                        
            if up==1 and down==1 and left==1 and right==1:
                break
        
        
        vertical.extend(horizontal)
        vertical=list(set(vertical))
        return vertical
    
    def Knight(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break

        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate,self.bboardstate]
        if self.color=="W":
            boardst=boardst
        else:
            boardst.reverse()
            
        move=[]
        
        if row_index-2>-1:
            if col_index-1>-1:
                if self.columns[col_index-1]+self.rows[row_index-2] in boardst[0]:
                    pass
                elif self.columns[col_index-1]+self.rows[row_index-2] in boardst[1]:
                    move.append(self.columns[col_index-1]+self.rows[row_index-2])
                else:
                    move.append(self.columns[col_index-1]+self.rows[row_index-2])
                    
            if col_index+1<8:
                if self.columns[col_index+1]+self.rows[row_index-2] in boardst[0]:
                    pass
                elif self.columns[col_index+1]+self.rows[row_index-2] in boardst[1]:
                    move.append(self.columns[col_index+1]+self.rows[row_index-2])
                else:
                    move.append(self.columns[col_index+1]+self.rows[row_index-2])
                    
        if row_index+2<8:
            if col_index-1>-1:
                if self.columns[col_index-1]+self.rows[row_index+2] in boardst[0]:
                    pass
                elif self.columns[col_index-1]+self.rows[row_index+2] in boardst[1]:
                    move.append(self.columns[col_index-1]+self.rows[row_index+2])
                else:
                    move.append(self.columns[col_index-1]+self.rows[row_index+2])
                    
            if col_index+1<8:
                if self.columns[col_index+1]+self.rows[row_index+2] in boardst[0]:
                    pass
                elif self.columns[col_index+1]+self.rows[row_index+2] in boardst[1]:
                    move.append(self.columns[col_index+1]+self.rows[row_index+2])
                else:
                    move.append(self.columns[col_index+1]+self.rows[row_index+2])
                    
        if col_index-2>-1:
            if row_index-1>-1:
                if self.columns[col_index-2]+self.rows[row_index-1] in boardst[0]:
                    pass
                elif self.columns[col_index-2]+self.rows[row_index-1] in boardst[1]:
                    move.append(self.columns[col_index-2]+self.rows[row_index-1])
                else:
                    move.append(self.columns[col_index-2]+self.rows[row_index-1])
                    
            if row_index+1<8:
                if self.columns[col_index-2]+self.rows[row_index+1] in boardst[0]:
                    pass
                elif self.columns[col_index-2]+self.rows[row_index+1] in boardst[1]:
                    move.append(self.columns[col_index-2]+self.rows[row_index+1])
                else:
                    move.append(self.columns[col_index-2]+self.rows[row_index+1])
                    
        if col_index+2<8:
            if row_index-1>-1:
                if self.columns[col_index+2]+self.rows[row_index-1] in boardst[0]:
                    pass
                elif self.columns[col_index+2]+self.rows[row_index-1] in boardst[1]:
                    move.append(self.columns[col_index+2]+self.rows[row_index-1])
                else:
                    move.append(self.columns[col_index+2]+self.rows[row_index-1])
                    
            if row_index+1<8:
                if self.columns[col_index+2]+self.rows[row_index+1] in boardst[0]:
                    pass
                elif self.columns[col_index+2]+self.rows[row_index+1] in boardst[1]:
                    move.append(self.columns[col_index+2]+self.rows[row_index+1])
                else:
                    move.append(self.columns[col_index+2]+self.rows[row_index+1])
                    
                    
        return move
    
    def Pawn(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break

        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate,self.bboardstate]
        if self.color=="W":
            boardst=boardst
        else:
            boardst.reverse()
            
        main=[]    
        move=[]
        cp=[]

        if self.color=="W" and row_index<7:
            if row_index==1:
                if self.columns[col_index]+self.rows[row_index+2] not in self.wboardstate and self.columns[col_index]+self.rows[row_index+1] not in self.bboardstate:
                    move.append(self.columns[col_index]+self.rows[row_index+2])
            
            
            if self.columns[col_index]+self.rows[row_index+1] not in self.wboardstate and self.columns[col_index]+self.rows[row_index+1] not in self.bboardstate:
                move.append(self.columns[col_index]+self.rows[row_index+1])
            if col_index-1>-1 and self.columns[col_index-1]+self.rows[row_index+1] in self.bboardstate:
                move.append(self.columns[col_index-1]+self.rows[row_index+1])
            if col_index+1<8 and self.columns[col_index+1]+self.rows[row_index+1] in self.bboardstate:
                move.append(self.columns[col_index+1]+self.rows[row_index+1])
                    
        if self.color=="B" and row_index>0:
            if row_index==6:
                if self.columns[col_index]+self.rows[row_index-2] not in self.wboardstate and self.columns[col_index]+self.rows[row_index-2] not in self.bboardstate:
                    move.append(self.columns[col_index]+self.rows[row_index-2])
            
            
            if self.columns[col_index]+self.rows[row_index-1] not in self.wboardstate and self.columns[col_index]+self.rows[row_index-1] not in self.bboardstate:
                move.append(self.columns[col_index]+self.rows[row_index-1])
            if col_index-1>-1 and self.columns[col_index-1]+self.rows[row_index-1] in self.wboardstate:
                move.append(self.columns[col_index-1]+self.rows[row_index-1])
            if col_index+1<8 and self.columns[col_index+1]+self.rows[row_index-1] in self.wboardstate:
                move.append(self.columns[col_index+1]+self.rows[row_index-1])
                
        if self.color=="B" and row_index==1:
            cp.append(1)
        elif self.color=="W" and row_index==6:
            cp.append(2)
                        
        main.append(move)    
        main.append(cp)
        
        #print("here")
                               
        return main
    
    def Pawn_attack(self):
        square=""
        for k,v in self.pos_table.items():
            if v==(self.newx,self.newy):
                square=k
                break

        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate,self.bboardstate]
        if self.color=="W":
            boardst=boardst
        else:
            boardst.reverse()
            
        move=[]
            
        if self.color=="W" and row_index<7:
            if col_index-1>-1 and self.columns[col_index-1]+self.rows[row_index+1] not in self.wboardstate:
                move.append(self.columns[col_index-1]+self.rows[row_index+1])
            if col_index+1<8 and self.columns[col_index+1]+self.rows[row_index+1] not in self.wboardstate:
                move.append(self.columns[col_index+1]+self.rows[row_index+1])
                
        if self.color=="B" and row_index>0:
            if col_index-1>-1 and self.columns[col_index-1]+self.rows[row_index-1] not in self.bboardstate:
                move.append(self.columns[col_index-1]+self.rows[row_index-1])
            if col_index+1<8 and self.columns[col_index+1]+self.rows[row_index-1] not in self.bboardstate:
                move.append(self.columns[col_index+1]+self.rows[row_index-1])
                
        return move
    
    
                        
def main():
    pygame.init()
    
    pygame.font.init()
    surface = pygame.display.set_mode((500,500))
    colorw = (235,235,208) 
    colorb = (119, 148, 85)
    pygame.display.set_caption('CHESS')
    font = pygame.font.SysFont('Comic Sans MS', 15)
    white=(255,255,255)
    running=True
    
    clock = pygame.time.Clock()  
    
    positions={"A1":(0,420),"B1":(60,420),"C1":(120,420),"D1":(180,420),"E1":(240,420),"F1":(300,420),"G1":(360,420),"H1":(420,420),
           "A2":(0,360),"B2":(60,360),"C2":(120,360),"D2":(180,360),"E2":(240,360),"F2":(300,360),"G2":(360,360),"H2":(420,360),
           "A3":(0,300),"B3":(60,300),"C3":(120,300),"D3":(180,300),"E3":(240,300),"F3":(300,300),"G3":(360,300),"H3":(420,300),
           "A4":(0,240),"B4":(60,240),"C4":(120,240),"D4":(180,240),"E4":(240,240),"F4":(300,240),"G4":(360,240),"H4":(420,240),
           "A5":(0,180),"B5":(60,180),"C5":(120,180),"D5":(180,180),"E5":(240,180),"F5":(300,180),"G5":(360,180),"H5":(420,180),
           "A6":(0,120),"B6":(60,120),"C6":(120,120),"D6":(180,120),"E6":(240,120),"F6":(300,120),"G6":(360,120),"H6":(420,120),
           "A7":(0,60),"B7":(60,60),"C7":(120,60),"D7":(180,60),"E7":(240,60),"F7":(300,60),"G7":(360,60),"H7":(420,60),
           "A8":(0,0),"B8":(60,0),"C8":(120,0),"D8":(180,0),"E8":(240,0),"F8":(300,0),"G8":(360,0),"H8":(420,0)} 
    
    alphachart={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}
    numchart={0:"8",1:"7",2:"6",3:"5",4:"4",5:"3",6:"2",7:"1"}
    
    bK = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bK.png')
    bBC = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bB.png')
    bBF = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bB.png')
    bNB = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bN.png')
    bNG = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bN.png')
    bPA = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPB = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPC = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPD = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPE = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPF = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPG = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bPH = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bp.png')
    bQ = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bQ.png') 
    bRA = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bR.png')
    bRH = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bR.png')
    wK = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wK.png')
    wBC = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wB.png')
    wBF = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wB.png')
    wNB = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wN.png')
    wNG = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wN.png')
    wPA = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPB = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPC = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPD = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPE = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPF = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPG = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wPH = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wp.png')
    wQ = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wQ.png')
    wRA = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wR.png')
    wRH = pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wR.png')
    
    imgw=pygame.image.load('C:/Users/babai/Desktop/chess_pieces/wQ.png')
    imgb=pygame.image.load('C:/Users/babai/Desktop/chess_pieces/bQ.png')
    
    A = font.render('A', False, (255, 255, 255))
    B = font.render('B', False, (255, 255, 255))
    C = font.render('C', False, (255, 255, 255))
    D = font.render('D', False, (255, 255, 255))
    E = font.render('E', False, (255, 255, 255))
    F = font.render('F', False, (255, 255, 255))
    G = font.render('G', False, (255, 255, 255))
    H = font.render('H', False, (255, 255, 255))
        
    n1 = font.render('1', False, (255, 255, 255))
    n2 = font.render('2', False, (255, 255, 255))
    n3 = font.render('3', False, (255, 255, 255))
    n4 = font.render('4', False, (255, 255, 255))
    n5 = font.render('5', False, (255, 255, 255))
    n6 = font.render('6', False, (255, 255, 255))
    n7 = font.render('7', False, (255, 255, 255))
    n8 = font.render('8', False, (255, 255, 255))
    
    alpha_num=[A,B,C,D,E,F,G,H,n1,n2,n3,n4,n5,n6,n7,n8]
    
    z=1
    
    #WhiteKing=Pieces("WhiteKing",wK,240,420,surface,"W","K")
    #BlackKing=Pieces("BlackKing",bK,240,0,surface,"B","K")
    
    items={'WhiteKing':Pieces("WhiteKing",wK,240,420,surface,"W","K"),'BlackKing':Pieces("BlackKing",bK,240,0,surface,"B","K"),'WhiteQueen':Pieces("WhiteQueen",wQ,180,420,surface,"W","Q"),'BlackQueen':Pieces("BlackQueen",bQ,180,0,surface,"B","Q"),
           'BlackRookA':Pieces("BlackRookA",bRA,0,0,surface,"B","R"),'BlackRookH':Pieces("BlackRookH",bRH,420,0,surface,"B","R"),'WhiteRookA':Pieces("WhiteRookA",wRA,0,420,surface,"W","R"),'WhiteRookH':Pieces("WhiteRookH",wRH,420,420,surface,"W","R"),
           'BlackKnightB':Pieces("BlackKnightB",bNB,60,0,surface,"B","N"),'BlackKnightG':Pieces("BlackKnightG",bNG,360,0,surface,"B","N"),'WhiteKnightB':Pieces("WhiteKnightB",wNB,60,420,surface,"W","N"),'WhiteKnightG':Pieces("WhiteKnightG",wNG,360,420,surface,"W","N"),
           'BlackBishopC':Pieces("BlackBishopC",bBC,120,0,surface,"B","B"),'BlackBishopF':Pieces("BlackBishopF",bBF,300,0,surface,"B","B"),'WhiteBishopC':Pieces("WhiteBishopC",wBC,120,420,surface,"W","B"),'WhiteBishopF':Pieces("WhiteBishopF",wBF,300,420,surface,"W","B"),
           'BlackPawnA':Pieces("BlackPawnA",bPA,0,60,surface,"B","P"),'BlackPawnB':Pieces("BlackPawnB",bPB,60,60,surface,"B","P"),'BlackPawnC':Pieces("BlackPawnC",bPC,120,60,surface,"B","P"),'BlackPawnD':Pieces("BlackPawnD",bPD,180,60,surface,"B","P"),
           'BlackPawnE':Pieces("BlackPawnE",bPE,240,60,surface,"B","P"),'BlackPawnF':Pieces("BlackPawnF",bPF,300,60,surface,"B","P"),'BlackPawnG':Pieces("BlackPawnG",bPG,360,60,surface,"B","P"),'BlackPawnH':Pieces("BlackPawnH",bPH,420,60,surface,"B","P"),
           'WhitePawnA':Pieces("WhitePawnA",wPA,0,360,surface,"W","P"),'WhitePawnB':Pieces("WhitePawnB",wPB,60,360,surface,"W","P"),'WhitePawnC':Pieces("WhitePawnC",wPC,120,360,surface,"W","P"),'WhitePawnD':Pieces("WhitePawnD",wPD,180,360,surface,"W","P"),
           'WhitePawnE':Pieces("WhitePawnE",wPE,240,360,surface,"W","P"),'WhitePawnF':Pieces("WhitePawnF",wPF,300,360,surface,"W","P"),'WhitePawnG':Pieces("WhitePawnG",wPG,360,360,surface,"W","P"),'WhitePawnH':Pieces("WhitePawnH",wPH,420,360,surface,"W","P")}

    
    down=False
    checkclick=""
    sq=""
    x=0
    y=0
    x2=0
    y2=0
    render=0
    check=0
    #wboard=[]
    #bboard=[]
    turn=["White","Black"]
    whitemoves=[]
    blackmoves=[]
    while running:
        clock.tick(120)
        
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 0, 500, 500))
        
        surface.blit(alpha_num[0], (25,480))
        surface.blit(alpha_num[1], (85,480))
        surface.blit(alpha_num[2], (145,480))
        surface.blit(alpha_num[3], (205,480))
        surface.blit(alpha_num[4], (265,480))
        surface.blit(alpha_num[5], (325,480))
        surface.blit(alpha_num[6], (385,480))
        surface.blit(alpha_num[7], (445,480))
            
        surface.blit(alpha_num[15], (485,25))
        surface.blit(alpha_num[14], (485,85))
        surface.blit(alpha_num[13], (485,145))
        surface.blit(alpha_num[12], (485,205))
        surface.blit(alpha_num[11], (485,265))
        surface.blit(alpha_num[10], (485,325))
        surface.blit(alpha_num[9], (485,385))
        surface.blit(alpha_num[8], (485,445))
        
        A8=pygame.draw.rect(surface, colorw, pygame.Rect(0, 0, 60, 60))   
        B8=pygame.draw.rect(surface, colorb, pygame.Rect(60, 0, 60, 60))
        C8=pygame.draw.rect(surface, colorw, pygame.Rect(120, 0, 60, 60))
        D8=pygame.draw.rect(surface, colorb, pygame.Rect(180, 0, 60, 60))
        E8=pygame.draw.rect(surface, colorw, pygame.Rect(240, 0, 60, 60))
        F8=pygame.draw.rect(surface, colorb, pygame.Rect(300, 0, 60, 60))
        G8=pygame.draw.rect(surface, colorw, pygame.Rect(360, 0, 60, 60))
        H8=pygame.draw.rect(surface, colorb, pygame.Rect(420, 0, 60, 60))
        
        A7=pygame.draw.rect(surface, colorb, pygame.Rect(0, 60, 60, 60))   
        B7=pygame.draw.rect(surface, colorw, pygame.Rect(60, 60, 60, 60))
        C7=pygame.draw.rect(surface, colorb, pygame.Rect(120, 60, 60, 60))
        D7=pygame.draw.rect(surface, colorw, pygame.Rect(180, 60, 60, 60))
        E7=pygame.draw.rect(surface, colorb, pygame.Rect(240, 60, 60, 60))
        F7=pygame.draw.rect(surface, colorw, pygame.Rect(300, 60, 60, 60))
        G7=pygame.draw.rect(surface, colorb, pygame.Rect(360, 60, 60, 60))
        H7=pygame.draw.rect(surface, colorw, pygame.Rect(420, 60, 60, 60))
        
        A6=pygame.draw.rect(surface, colorw, pygame.Rect(0, 120, 60, 60))   
        B6=pygame.draw.rect(surface, colorb, pygame.Rect(60, 120, 60, 60))
        C6=pygame.draw.rect(surface, colorw, pygame.Rect(120, 120, 60, 60))
        D6=pygame.draw.rect(surface, colorb, pygame.Rect(180, 120, 60, 60))
        E6=pygame.draw.rect(surface, colorw, pygame.Rect(240, 120, 60, 60))
        F6=pygame.draw.rect(surface, colorb, pygame.Rect(300, 120, 60, 60))
        G6=pygame.draw.rect(surface, colorw, pygame.Rect(360, 120, 60, 60))
        H6=pygame.draw.rect(surface, colorb, pygame.Rect(420, 120, 60, 60))
        
        A5=pygame.draw.rect(surface, colorb, pygame.Rect(0, 180, 60, 60))   
        B5=pygame.draw.rect(surface, colorw, pygame.Rect(60, 180, 60, 60))
        C5=pygame.draw.rect(surface, colorb, pygame.Rect(120, 180, 60, 60))
        D5=pygame.draw.rect(surface, colorw, pygame.Rect(180, 180, 60, 60))
        E5=pygame.draw.rect(surface, colorb, pygame.Rect(240, 180, 60, 60))
        F5=pygame.draw.rect(surface, colorw, pygame.Rect(300, 180, 60, 60))
        G5=pygame.draw.rect(surface, colorb, pygame.Rect(360, 180, 60, 60))
        H5=pygame.draw.rect(surface, colorw, pygame.Rect(420, 180, 60, 60))
        
        A4=pygame.draw.rect(surface, colorw, pygame.Rect(0, 240, 60, 60))   
        B4=pygame.draw.rect(surface, colorb, pygame.Rect(60, 240, 60, 60))
        C4=pygame.draw.rect(surface, colorw, pygame.Rect(120, 240, 60, 60))
        D4=pygame.draw.rect(surface, colorb, pygame.Rect(180, 240, 60, 60))
        E4=pygame.draw.rect(surface, colorw, pygame.Rect(240, 240, 60, 60))
        F4=pygame.draw.rect(surface, colorb, pygame.Rect(300, 240, 60, 60))
        G4=pygame.draw.rect(surface, colorw, pygame.Rect(360, 240, 60, 60))
        H4=pygame.draw.rect(surface, colorb, pygame.Rect(420, 240, 60, 60))
        
        A3=pygame.draw.rect(surface, colorb, pygame.Rect(0, 300, 60, 60))   
        B3=pygame.draw.rect(surface, colorw, pygame.Rect(60, 300, 60, 60))
        C3=pygame.draw.rect(surface, colorb, pygame.Rect(120, 300, 60, 60))
        D3=pygame.draw.rect(surface, colorw, pygame.Rect(180, 300, 60, 60))
        E3=pygame.draw.rect(surface, colorb, pygame.Rect(240, 300, 60, 60))
        F3=pygame.draw.rect(surface, colorw, pygame.Rect(300, 300, 60, 60))
        G3=pygame.draw.rect(surface, colorb, pygame.Rect(360, 300, 60, 60))
        H3=pygame.draw.rect(surface, colorw, pygame.Rect(420, 300, 60, 60))
        
        A2=pygame.draw.rect(surface, colorw, pygame.Rect(0, 360, 60, 60))   
        B2=pygame.draw.rect(surface, colorb, pygame.Rect(60, 360, 60, 60))
        C2=pygame.draw.rect(surface, colorw, pygame.Rect(120, 360, 60, 60))
        D2=pygame.draw.rect(surface, colorb, pygame.Rect(180, 360, 60, 60))
        E2=pygame.draw.rect(surface, colorw, pygame.Rect(240, 360, 60, 60))
        F2=pygame.draw.rect(surface, colorb, pygame.Rect(300, 360, 60, 60))
        G2=pygame.draw.rect(surface, colorw, pygame.Rect(360, 360, 60, 60))
        H2=pygame.draw.rect(surface, colorb, pygame.Rect(420, 360, 60, 60))
        
        A1=pygame.draw.rect(surface, colorb, pygame.Rect(0, 420, 60, 60))   
        B1=pygame.draw.rect(surface, colorw, pygame.Rect(60, 420, 60, 60))
        C1=pygame.draw.rect(surface, colorb, pygame.Rect(120, 420, 60, 60))
        D1=pygame.draw.rect(surface, colorw, pygame.Rect(180, 420, 60, 60))
        E1=pygame.draw.rect(surface, colorb, pygame.Rect(240, 420, 60, 60))
        F1=pygame.draw.rect(surface, colorw, pygame.Rect(300, 420, 60, 60))
        G1=pygame.draw.rect(surface, colorb, pygame.Rect(360, 420, 60, 60))
        H1=pygame.draw.rect(surface, colorw, pygame.Rect(420, 420, 60, 60))
        
        allmoves=[]
        
     
        
        wboard=[]
        bboard=[]
        cont=0
        
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == MOUSEBUTTONDOWN:
                if down==False:
                    x,y = pygame.mouse.get_pos()
                    if x<=480 and y<=480:
                        new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                        for k,v in items.items():
                            checkclick=items[k].check_pos(alphachart,numchart,(x,y))
                            if checkclick:
                                down=True
                                render=1
                                break
                   
            elif event.type == MOUSEBUTTONUP:
                
                down=False
                delete=True
                piece_delete=""
                
                for k,v in items.items():
                    if(items[k].get_color()=="W"):
                        wboard.append(items[k].get_square(alphachart,numchart))
                    else:
                        bboard.append(items[k].get_square(alphachart,numchart))
                        

                if check==1:
                    #print(checkclick,wboard,bboard,whitemoves,blackmoves,turn,positions,alphachart,numchart,items[checkclick].get_square(alphachart,numchart))
                    moveset=pieceset(items,checkclick,wboard,bboard,whitemoves,blackmoves,turn,positions,alphachart,numchart,items[checkclick].get_square(alphachart,numchart))
                    if alphachart.get(int(x2/60))+numchart.get(int(y2/60)) in moveset:
                        check=0
                        cont=1

                    else:
                        print("wrong move still in check")
                        print(moveset)
                    
                    
                if bool(alphachart.get(int(x2/60))) == True and bool(numchart.get(int(y2/60))) == True and bool(checkclick) == True and checkclick[0:5]==turn[0] and check==0:

                    new=positions.get(alphachart.get(int(x2/60))+numchart.get(int(y2/60)))
                
                    checkmove=CheckMove(items,positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))[0],positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))[1],items[checkclick].get_color(),items[checkclick].get_piece(),positions,wboard,bboard)
                    piece=items[checkclick].get_piece()
                    movementspace=[]
                    
                    if piece=="P":
                        movementspace=checkmove.Pawn()

                        if movementspace[1]==[2]:

                            items[checkclick].change_piece(imgw,"W","Q")
                        elif movementspace[1]==[1]:
                            items[checkclick].change_piece(imgb,"B","Q")
                            
                        movementspace=movementspace[0]            
                        
                    elif piece=="K":
                        movementspace=checkmove.King()
                        
                    elif piece=="Q":
                        movementspace=checkmove.Queen()
                        
                    elif piece=="B":
                        movementspace=checkmove.Bishop()
                        
                    elif piece=="R":
                        movementspace=checkmove.Rook()
                        
                    elif piece=="N":
                        movementspace=checkmove.Knight()
                        
                    print("final",movementspace)
                        
                    move=alphachart.get(int(x2/60))+numchart.get(int(y2/60))
                    print(move)

                    if move in movementspace:
                        for k,v in items.items():
                            if k==checkclick:
                                continue
                            elif items[k].get_pos()==(new[0],new[1]):
                                if k[0:5]==checkclick[0:5]:
                                    delete= False
                                else:
                                    delete=True
                                    piece_delete=k
                                    break
                                               
                        if delete==True:
                            
                            
                            if turn[0]=="White":
                                i=wboard.index(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                                del wboard[i]
                                wboard.append(alphachart.get(int(x2/60))+numchart.get(int(y2/60)))
                                
                            elif turn[0]=="Black":
                                i=bboard.index(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                                del bboard[i]
                                bboard.append(alphachart.get(int(x2/60))+numchart.get(int(y2/60)))
                           
                            whitemoves=[]
                            blackmoves=[]
                                                            
                            for i in items.keys():
                                

                                checkmove=CheckMove(items,positions.get(items[i].get_square(alphachart,numchart))[0],positions.get(items[i].get_square(alphachart,numchart))[1],items[i].get_color(),items[i].get_piece(),positions,wboard,bboard)
                                allmoves=checkmove.get_moves()

                                if allmoves:
                                    if items[i].get_color()=="W":
                                        whitemoves.extend(allmoves)
                                    elif items[i].get_color()=="B":
                                        blackmoves.extend(allmoves)
                                        
                            whitemoves=list(set(whitemoves))
                            blackmoves=list(set(blackmoves))                                        

                            sq=items['BlackKing'].get_square(alphachart,numchart)
                            sq2=items['WhiteKing'].get_square(alphachart,numchart)
                            
                            if turn[0]=="White":
                                
                                if sq in whitemoves and cont==0:
                                    check=1
                                    print("White gives check")
                                
                                elif sq2 in blackmoves and cont==0:
                                    wboard.remove(alphachart.get(int(x2/60))+numchart.get(int(y2/60)))
                                    wboard.append(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                                    moveset=pieceset(items,checkclick,wboard,bboard,whitemoves,blackmoves,turn,positions,alphachart,numchart,items[checkclick].get_square(alphachart,numchart))
                                    if alphachart.get(int(x2/60))+numchart.get(int(y2/60)) in moveset:
                                        check=0
                                    else:
                                        check=1
                                        print("Wrong Move")
                                        print(moveset)
                                        
                            elif turn[0]=="Black":
                                
                                if sq2 in blackmoves and cont==0:
                                    check=1
                                    print("White gives check")
                                
                                elif sq in whitemoves and cont==0:
                                    bboard.remove(alphachart.get(int(x2/60))+numchart.get(int(y2/60)))
                                    bboard.append(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                                    moveset=pieceset(items,checkclick,wboard,bboard,whitemoves,blackmoves,turn,positions,alphachart,numchart,items[checkclick].get_square(alphachart,numchart))
                                    if alphachart.get(int(x2/60))+numchart.get(int(y2/60)) in moveset:
                                        check=0
                                    else:
                                        check=1
                                        print("Wrong Move")
                                        print(moveset)
                                    

                                
                            if check==0 or cont==1:
                                if piece_delete:
                                    del items[piece_delete]
                                items[checkclick].updateloc_permanent(new[0],new[1])
                                checkclick=""
                                render=0
                                turn.reverse()
                                
                                
                            else:
                                new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                                items[checkclick].updateloc_permanent(new[0],new[1])
                                checkclick=""
                                render=0
                                
                                
     
                        else:
                           
                            new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                            items[checkclick].updateloc_permanent(new[0],new[1])
                            checkclick=""
                            render=0
                            
                    else:
                        new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                        items[checkclick].updateloc_permanent(new[0],new[1])
                        checkclick=""
                        render=0
                        
                        

                else:
                    if checkclick:
                        new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                        items[checkclick].updateloc_permanent(new[0],new[1])
                        checkclick=""
                        render=0

                    
                       
        if(z==1):
            for k,v in items.items():
                if k==checkclick and render==1:
                    continue
                else:
                    items[k].update_setup()
                    
        
                    
        if down==True:
            x2,y2 = pygame.mouse.get_pos()
            items[checkclick].updateloc(x2-30,y2-30)
    
        pygame.display.flip()
        pygame.display.update()
            
    pygame.quit()
    
    
    
def pieceset(items,checkclick,wboard,bboard,whitemovescheck,blackmovescheck,turn,positions,alphachart,numchart,sq):
    color=items[checkclick].get_color() 
    updated_movementspace=[]
    #print("here")
    if turn[0][0]==color:
        #print("here2")
        checkmove=CheckMove(items,positions.get(items[checkclick].get_square(alphachart,numchart))[0],positions.get(items[checkclick].get_square(alphachart,numchart))[1],items[checkclick].get_color(),items[checkclick].get_piece(),positions,wboard,bboard)
        piece=items[checkclick].get_piece()
        movementspace=[]
        
        if piece=="P":
            movementspace=checkmove.Pawn()                                
            movementspace=movementspace[0]
            print(movementspace)
            updated_movementspace.extend(checkfree(items,movementspace,sq,turn[0],checkclick,positions,wboard,bboard,alphachart,numchart,whitemovescheck,blackmovescheck))
        if piece=="K":
            movementspace=checkmove.King()
            print("here",movementspace)
            for i in movementspace:
                    if checkclick=='WhiteKing':
                        if i not in blackmovescheck:
                            updated_movementspace.append(i)
                    elif checkclick=='BlackKing':
                        if i not in whitemovescheck:
                            updated_movementspace.append(i)
        if piece=="Q":
            movementspace=checkmove.Queen()                                
            updated_movementspace.extend(checkfree(items,movementspace,sq,turn[0],checkclick,positions,wboard,bboard,alphachart,numchart,whitemovescheck,blackmovescheck))
        if piece=="B":
            movementspace=checkmove.Bishop()                                
            updated_movementspace.extend(checkfree(items,movementspace,sq,turn[0],checkclick,positions,wboard,bboard,alphachart,numchart,whitemovescheck,blackmovescheck))
        if piece=="R":
            movementspace=checkmove.Rook()                                
            updated_movementspace.extend(checkfree(items,movementspace,sq,turn[0],checkclick,positions,wboard,bboard,alphachart,numchart,whitemovescheck,blackmovescheck))
        if piece=="N":
            movementspace=checkmove.Knight()                                
            updated_movementspace.extend(checkfree(items,movementspace,sq,turn[0],checkclick,positions,wboard,bboard,alphachart,numchart,whitemovescheck,blackmovescheck))
            
    #print("movementspace",updated_movementspace)
    return updated_movementspace
            
            
    
                    
def checkfree(items,movementspace,sq,color,checkclick,positions,wboard,bboard,alphachart,numchart,whitemovescheck,blackmovescheck):
    truemoves=[]    
    wboardsub=copy.deepcopy(wboard)
    bboardsub=copy.deepcopy(bboard)
    #print(color)
    for j in movementspace:       
        allmoves=[]
        whitemoves=[]
        blackmoves=[]


        if color=="White": 
            
            refitb=0

            wboardsub[wboardsub.index(sq)] = j
            if j in bboardsub:
                bboardsub.remove(j)
                refitb=1
            for i in items.keys():

                if items[i].get_color()=="B" and items[i].get_square(alphachart,numchart)!=j:
                    checkmove=CheckMove(items,positions.get(items[i].get_square(alphachart,numchart))[0],positions.get(items[i].get_square(alphachart,numchart))[1],items[i].get_color(),items[i].get_piece(),positions,wboardsub,bboardsub)
                    allmoves=checkmove.get_moves()

                    if allmoves:
                        blackmoves.extend(allmoves)
            if items['WhiteKing'].get_square(alphachart,numchart) not in blackmoves:
                truemoves.append(j)
            wboardsub[wboardsub.index(j)] = sq
            if refitb==1:
                bboardsub.append(j)
                    
                    
        elif color=="Black": 
            
            refitw=0
            
            bboardsub[bboardsub.index(sq)] = j
            if j in wboardsub:
                wboardsub.remove(j)
                refitw=1
            for i in items.keys():
                if items[i].get_color()=="W" and items[i].get_square(alphachart,numchart)!=j:
                    checkmove=CheckMove(items,positions.get(items[i].get_square(alphachart,numchart))[0],positions.get(items[i].get_square(alphachart,numchart))[1],items[i].get_color(),items[i].get_piece(),positions,wboardsub,bboardsub)
                    allmoves=checkmove.get_moves()
                    if allmoves:
                        whitemoves.extend(allmoves)
                        
            if items['BlackKing'].get_square(alphachart,numchart) not in whitemoves:
                truemoves.append(j)
            bboardsub[bboardsub.index(j)] = sq
            if refitw==1:
                wboardsub.append(j)
    
        
            
    return truemoves
                    


main()
            
    


