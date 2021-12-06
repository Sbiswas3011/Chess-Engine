# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:47:50 2021

@author: Snehangsu
"""

import pygame 
from pygame.locals import *
import copy
from playsound import playsound
        
class Pieces(pygame.sprite.Sprite):
    
    def __init__(self,name,wPH,x,y,s,color,piece,move):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.wPH = wPH
        self.x = x
        self.y = y
        self.s = s
        self.color=color
        self.piece=piece
        self.move=move
        
    def updatemove(self):
        self.move+=1
        
    def get_moves(self):
        return self.move
        
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
    
    def __init__(self,items,prevx,prevy,newx,newy,color,piece,pos_table,wboardstate,bboardstate,prev_move_piece):
        self.items=items
        self.newx=newx
        self.newy=newy
        self.prevx=prevx
        self.prevy=prevy
        self.color=color
        self.piece=piece
        self.pos_table=pos_table
        self.wboardstate=wboardstate
        self.bboardstate=bboardstate
        self.prev_move_piece=prev_move_piece
        self.columns=["A","B","C","D","E","F","G","H"]
        self.rows=["1","2","3","4","5","6","7","8"]
        self.alphachart={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}
        self.numchart={0:"8",1:"7",2:"6",3:"5",4:"4",5:"3",6:"2",7:"1"}
        #if self.piece=="K":
            #self.king()
            
    def update_wboard(self,piece,move):
        self.wboardstate[piece]=move
        
    def update_bboard(self,piece,move):
        self.bboardstate[piece]=move
            
    def checkmate(self,move):
        
        bboardstate=copy.deepcopy(self.bboardstate)
        wboardstate=copy.deepcopy(self.wboardstate)
        
        square=""
        for k,v in self.pos_table.items():
            if v==(self.prevx,self.prevy):
                square=k
                break
        #print(square,move)    
        
        if self.color == "W":
            
            #print("wboard",self.wboardstate)
            
            for piece,loc in self.bboardstate.items():#deepcopy required
                if loc==move:    
                    self.bboardstate.pop(piece)
                    break
                    
            for piece,loc in self.wboardstate.items():
                if loc==square:
                    self.wboardstate[piece]=move
                    break
                
            #print("wboard",self.wboardstate)
            
            tot_movement=[]
            for k,v in self.items.items():
                if self.items[k].get_color()=="W":
                    pieceinitial=self.items[k].get_piece()
                    movementspace=[]
                        
                    if pieceinitial=="P": # special case the functions
                        movementspace=self.Pawn(self.wboardstate.get(k),True,"W")  
                        #print("pawn")
                                      
                    elif pieceinitial=="K":
                        movementspace=self.King(self.wboardstate.get(k),True,"W")
                        #print("king")
                                                  
                    elif pieceinitial=="Q":
                        movementspace=self.Queen(self.wboardstate.get(k),True,"W")
                        #print("queen")
                                                    
                    elif pieceinitial=="B":
                        movementspace=self.Bishop(self.wboardstate.get(k),True,"W")  
                        #print("bishop")
                            
                    elif pieceinitial=="R":
                        movementspace=self.Rook(self.wboardstate.get(k),True,"W")   
                        #print("rook")
                            
                    elif pieceinitial=="N":
                        movementspace=self.Knight(self.wboardstate.get(k),True,"W")
                        #print("knight")
                    #print(movementspace)                             
                    tot_movement.extend(movementspace)
            #print("White",set(tot_movement))   
            if self.items["BlackKing"].get_square(self.alphachart,self.numchart) in tot_movement:
                print("BlackKing ",end="")
                return 1          
            else:
                return 0
            
        elif self.color == "B":
            
            for piece,loc in self.wboardstate.items():#deepcopy required
                if loc==move:    
                    self.wboardstate.pop(piece)
                    break
                    
            for piece,loc in self.bboardstate.items():
                if loc==square:
                    self.bboardstate[piece]=move
                    break
            
            tot_movement=[]
            for k,v in self.items.items():
                if self.items[k].get_color()=="B":
                    pieceinitial=self.items[k].get_piece()
                    movementspace=[]
                        
                    if pieceinitial=="P": # special case the functions
                        movementspace=self.Pawn(self.bboardstate.get(k),True,"B")   
                                      
                    elif pieceinitial=="K":
                        movementspace=self.King(self.bboardstate.get(k),True,"B")
                                                  
                    elif pieceinitial=="Q":
                        movementspace=self.Queen(self.bboardstate.get(k),True,"B")
                                                    
                    elif pieceinitial=="B":
                        movementspace=self.Bishop(self.bboardstate.get(k),True,"B")                       
                            
                    elif pieceinitial=="R":
                        movementspace=self.Rook(self.bboardstate.get(k),True,"B")                  
                            
                    elif pieceinitial=="N":
                        movementspace=self.Knight(self.bboardstate.get(k),True,"B")
                                                 
                    tot_movement.extend(movementspace)
                
            #print("Black",set(tot_movement))    
            if self.items["WhiteKing"].get_square(self.alphachart,self.numchart) in tot_movement:
                print("WhiteKing ",end="")
                return 1
            else:
                return 0
                
   

    def verify(self,movespace,s=[0],en=[0]):
        square=""
        remove=[]
        castlevalue=[]
        for k,v in self.pos_table.items():
            if v==(self.prevx,self.prevy):
                square=k
                break
        #print(square)
        
        #print("movespace",movespace) 
        if self.color == "W":
            castlevalue=["G1","C1"]
            for move in movespace:
                bboardstate=copy.deepcopy(self.bboardstate)
                wboardstate=copy.deepcopy(self.wboardstate)
                #print(move,square)
                #print("wboard",self.wboardstate)
                
                for piece,loc in self.bboardstate.items(): #deepcopy required
                    if loc==move:    
                        self.bboardstate.pop(piece)
                        break
                    elif loc in en:
                        self.bboardstate.pop(piece)
                        break
                                      
                for piece,loc in self.wboardstate.items():
                    if loc==square:
                        self.wboardstate[piece]=move
                        if move=="G1" and move in s:
                            self.wboardstate["WhiteRookH"]="F1"
                        if move=="C1" and move in s:
                            self.wboardstate["WhiteRookA"]="D1"
                        break

                tot_movement=[]
                for piece,loc in self.bboardstate.items():
                    
                    pieceinitial=self.items[piece].get_piece()
                    movementspace=[]
                    
                    if pieceinitial=="P": # special case the functions
                        movementspace=self.Pawn(loc,True,"B")   
                        #print("pawn")

                    elif pieceinitial=="K":
                        movementspace=self.King(loc,True,"B")
                        #print("king")
                        
                    elif pieceinitial=="Q":
                        movementspace=self.Queen(loc,True,"B")
                        #print("queen")
                        
                    elif pieceinitial=="B":
                        movementspace=self.Bishop(loc,True,"B")
                        #print("bishop")
                        
                    elif pieceinitial=="R":
                        movementspace=self.Rook(loc,True,"B")
                        #print("rook")
                        
                    elif pieceinitial=="N":
                        movementspace=self.Knight(loc,True,"B")
                        #print("knight")
                        
                    tot_movement.extend(movementspace)
                    #print("tot_movement",tot_movement)
                    
                if self.piece=="K":
                    kpos=move
                else:
                    kpos=self.items["WhiteKing"].get_square(self.alphachart,self.numchart)
                    
                #if s==0:    
                    
                if move=="G1" and move in s:
                    if kpos in tot_movement or "F1" in tot_movement or "E1" in tot_movement:
                        remove.append(move)
                        castlevalue.remove(move)
                elif move=="C1" and move in s:
                    if kpos in tot_movement or "D1" in tot_movement or "E1" in tot_movement:
                        remove.append(move)
                        castlevalue.remove(move)
                elif kpos in tot_movement:
                    remove.append(move)
                  
                    
                self.bboardstate=copy.deepcopy(bboardstate)
                self.wboardstate=copy.deepcopy(wboardstate)
                
                
        elif self.color == "B":
            castlevalue=["G8","C8"]
            #print("earlier movespace",movespace)
            for move in movespace:
                bboardstate=copy.deepcopy(self.bboardstate)
                wboardstate=copy.deepcopy(self.wboardstate)
                #print(move,square)
                for piece,loc in self.wboardstate.items(): #deepcopy required
                    if loc==move:    
                        self.wboardstate.pop(piece)
                        break
                    elif loc in en:
                        self.wboardstate.pop(piece)
                        break
                    
                for piece,loc in self.bboardstate.items():
                    if loc==square:
                        self.bboardstate[piece]=move
                        if move=="G8" and move in s:
                            self.bboardstate["BlackRookH"]="F8"
                        if move=="C8" and move in s:
                            #print("in here and s is",s,"and move is",move)
                            self.bboardstate["BlackRookA"]="D8"
                        break

                #print("WBOARD",self.wboardstate)    
                tot_movement=[]
                for piece,loc in self.wboardstate.items():
                    
                    pieceinitial=self.items[piece].get_piece()
                    movementspace=[]
                    
                    if pieceinitial=="P": # special case the functions
                        movementspace=self.Pawn(loc,True,"W")                          
                        #movementspace=movementspace[0]   
                        #print("pawn")
                        
                    elif pieceinitial=="K":
                        movementspace=self.King(loc,True,"W")
                        #print("king")
                        
                    elif pieceinitial=="Q":
                        movementspace=self.Queen(loc,True,"W")
                        #print("queen")
                        
                    elif pieceinitial=="B":
                        movementspace=self.Bishop(loc,True,"W")
                        #print("bishop")
                        
                    elif pieceinitial=="R":
                        movementspace=self.Rook(loc,True,"W")
                        #print("rook")
                        
                    elif pieceinitial=="N":
                        movementspace=self.Knight(loc,True,"W")
                        #print("knight")
                    
                    
                    tot_movement.extend(movementspace)
                    #print("tot_movement",tot_movement)
                    
                if self.piece=="K":
                    kpos=move
                else:
                    kpos=self.items["BlackKing"].get_square(self.alphachart,self.numchart)
                    
                #if s==0:    
                #print("final tot_movement",tot_movement)

                if move=="G8" and move in s:
                    if kpos in tot_movement or "F8" in tot_movement or "E8" in tot_movement:
                        remove.append(move)
                        castlevalue.remove(move)
                elif move=="C1" and move in s:
                    if kpos in tot_movement or "D8" in tot_movement or "E8" in tot_movement:
                        remove.append(move)
                        castlevalue.remove(move)
                elif kpos in tot_movement:
                    remove.append(move)

              
                self.bboardstate=copy.deepcopy(bboardstate)
                self.wboardstate=copy.deepcopy(wboardstate)
                      

        if self.piece=="K": 
            #print("s",s)
            if s:
                castlevalue=set(movespace).intersection(castlevalue)
                #print("in here")
            else:
                castlevalue=[]
            l4=[]
            #print("movespace",movespace)
            #print("remove",remove)
            l3 = [x for x in movespace if x not in remove]
            #print("L3",l3)
            l4.append(l3)
            l4.append(list(castlevalue))
            return l4
        else:

            l3 = [x for x in movespace if x not in remove]
            return l3

                
                  
            
    def King(self,squa=(0,0),r=False,color="W"):
        
        square=""
        #castle=0
        #ver=False
        if r==True:
            square=squa
        else:
            for k,v in self.pos_table.items():
                if v==(self.prevx,self.prevy):
                    square=k
                    break
            color=copy.deepcopy(self.color)
        
        posibilityspace=[]
        finalmovespace=[]
        specialcase=[]
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
            
        if color=="W":    
            if r==False:
                if self.items["WhiteKing"].get_moves()==0 and self.items["WhiteRookH"].get_moves()==0 and "F1" not in self.wboardstate.values() and "F1" not in self.bboardstate.values() and "G1" not in self.wboardstate.values() and "G1" not in self.bboardstate.values() :
                    #ver=self.verify_castle("WhiteKing","WhiteRookH")
                    #if ver==True:
                    posibilityspace.append("G1")
                        #castle=1
                    specialcase.append("G1")
                if self.items["WhiteKing"].get_moves()==0 and self.items["WhiteRookA"].get_moves()==0 and "D1" not in self.wboardstate.values() and "D1" not in self.bboardstate.values() and "C1" not in self.wboardstate.values() and "C1" not in self.bboardstate.values() and "B1" not in self.wboardstate.values() and "B1" not in self.bboardstate.values():
                    #ver=self.verify_castle("WhiteKing","WhiteRookA")
                    #if ver==True:
                    posibilityspace.append("C1")
                        #castle=2
                    specialcase.append("C1")
               
            c = [x for x in posibilityspace if x not in self.wboardstate.values()]
            if r==False and specialcase:
                finalmovespace.append(specialcase)
                finalmovespace.append(c)
            elif r==False:
                finalmovespace.append(specialcase)
                finalmovespace.append(c)  
            else:
                finalmovespace=c
                
            if r==True:
                return finalmovespace
            else:
                #print(finalmovespace)
                movement=self.verify(finalmovespace[1],finalmovespace[0])
                return movement
            
        elif color=="B":

            if r==False:
                if self.items["BlackKing"].get_moves()==0 and self.items["BlackRookH"].get_moves()==0 and "F8" not in self.wboardstate.values() and "F8" not in self.bboardstate.values() and "G8" not in self.wboardstate.values() and "G8" not in self.bboardstate.values() :
                    #ver=self.verify_castle("BlackKing","BlackRookH")
                    #if ver==True:
                    posibilityspace.append("G8")
    
                    specialcase.append("G8")
                if self.items["BlackKing"].get_moves()==0 and self.items["BlackRookA"].get_moves()==0 and "D8" not in self.wboardstate.values() and "D8" not in self.bboardstate.values() and "C8" not in self.wboardstate.values() and "C8" not in self.bboardstate.values() and "B8" not in self.wboardstate.values() and "B8" not in self.bboardstate.values() :
                    #ver=self.verify_castle("BlackKing","BlackRookA")
                    #if ver==True:
                    posibilityspace.append("C8")
    
                    specialcase.append("C8")
                       
            c = [x for x in posibilityspace if x not in self.bboardstate.values()]
            
            if r==False and specialcase:
                finalmovespace.append(specialcase)
                finalmovespace.append(c)
            elif r==False:
                finalmovespace.append(specialcase)
                finalmovespace.append(c) 
            else:
                finalmovespace=c
                 
            if r==True:
                return finalmovespace
            else:
                print(finalmovespace)
                movement=self.verify(finalmovespace[1],finalmovespace[0])
                return movement
        
    def Queen(self,squa=(0,0),r=False,color="W"):
        
        square=""
        if r==True:
            square=squa
        else:
            for k,v in self.pos_table.items():
                if v==(self.prevx,self.prevy):
                    square=k
                    break
            color=copy.deepcopy(self.color)
    
        col=square[0:1]
        row=square[1:2]
        #print(col,row)
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate.values(),self.bboardstate.values()]
        if color=="W":
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
        
        if r==True:
            return vertical
        else:
            movement=self.verify(vertical)
            return movement
        
    
    def Bishop(self,squa=(0,0),r=False,color="W"):
        
        square=""
        if r==True:
            square=squa
        else:
            for k,v in self.pos_table.items():
                if v==(self.prevx,self.prevy):
                    square=k
                    break
            color=copy.deepcopy(self.color)
            
        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate.values(),self.bboardstate.values()]
        if color=="W":
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
        if r==True:
            return leftbegin
        else:
            movement=self.verify(leftbegin)
            return movement
    
    def Rook(self,squa=(0,0),r=False,color="W"):
        
        square=""
        if r==True:
            square=squa
        else:
            for k,v in self.pos_table.items():
                if v==(self.prevx,self.prevy):
                    square=k
                    break
            color=copy.deepcopy(self.color)

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
        
        boardst=[self.wboardstate.values(),self.bboardstate.values()]
        if color=="W":
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
        if r==True:
            return vertical
        else:
            movement=self.verify(vertical)
            return movement
    
    def Knight(self,squa=(0,0),r=False,color="W"):
        
        square=""
        if r==True:
            square=squa
        else:
            for k,v in self.pos_table.items():
                if v==(self.prevx,self.prevy):
                    square=k
                    break
            color=copy.deepcopy(self.color)

        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate.values(),self.bboardstate.values()]
        if color=="W":
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
                    
                    
        if r==True:
            return move
        else:
            movement=self.verify(move)
            return movement
    
    def Pawn(self,squa=(0,0),r=False,color="W"):
        square=""
        enpassant=[]
        enpassant=[]
        if r==True:
            square=squa
        else:
            for k,v in self.pos_table.items():
                if v==(self.prevx,self.prevy):
                    square=k
                    break
            color=copy.deepcopy(self.color)
            

        col=square[0:1]
        row=square[1:2]
        col_index=self.columns.index(col)
        row_index=self.rows.index(row)
        orig_col=copy.deepcopy(col_index)
        orig_row=copy.deepcopy(row_index)
        
        boardst=[self.wboardstate,self.bboardstate]
        if color=="W":
            boardst=boardst
        else:
            boardst.reverse()
            
        main=[]    
        move=[]
        cp=[]

        if color=="W" and row_index<7:
            if row_index==1:
                if self.columns[col_index]+self.rows[row_index+2] not in self.wboardstate.values() and self.columns[col_index]+self.rows[row_index+1] not in self.bboardstate.values():
                    move.append(self.columns[col_index]+self.rows[row_index+2])
                              
            if self.columns[col_index]+self.rows[row_index+1] not in self.wboardstate.values() and self.columns[col_index]+self.rows[row_index+1] not in self.bboardstate.values():
                move.append(self.columns[col_index]+self.rows[row_index+1])
                
            if col_index-1>-1 and self.columns[col_index-1]+self.rows[row_index+1] in self.bboardstate.values():
                move.append(self.columns[col_index-1]+self.rows[row_index+1])
            
            if col_index-1>-1 and row_index==4 and self.items[self.prev_move_piece].get_piece()=="P" and self.items[self.prev_move_piece].get_square(self.alphachart,self.numchart)==self.columns[col_index-1]+self.rows[row_index] and self.items[self.prev_move_piece].get_moves()==1:
                move.append(self.columns[col_index-1]+self.rows[row_index+1])
                enpassant.append(self.columns[col_index-1]+self.rows[row_index+1])
    
            if col_index+1<8 and self.columns[col_index+1]+self.rows[row_index+1] in self.bboardstate.values():
                move.append(self.columns[col_index+1]+self.rows[row_index+1])
                
            if col_index+1<8 and row_index==4 and self.items[self.prev_move_piece].get_piece()=="P" and self.items[self.prev_move_piece].get_square(self.alphachart,self.numchart)==self.columns[col_index+1]+self.rows[row_index] and self.items[self.prev_move_piece].get_moves()==1:
                move.append(self.columns[col_index+1]+self.rows[row_index+1])
                enpassant.append(self.columns[col_index+1]+self.rows[row_index+1])
                
                    
        if color=="B" and row_index>0:
            if row_index==6:
                if self.columns[col_index]+self.rows[row_index-2] not in self.wboardstate.values() and self.columns[col_index]+self.rows[row_index-2] not in self.bboardstate.values():
                    move.append(self.columns[col_index]+self.rows[row_index-2])
            
            
            if self.columns[col_index]+self.rows[row_index-1] not in self.wboardstate.values() and self.columns[col_index]+self.rows[row_index-1] not in self.bboardstate.values():
                move.append(self.columns[col_index]+self.rows[row_index-1])
                
            if col_index-1>-1 and self.columns[col_index-1]+self.rows[row_index-1] in self.wboardstate.values():
                move.append(self.columns[col_index-1]+self.rows[row_index-1])
                
            if col_index-1>-1 and row_index==3 and self.items[self.prev_move_piece].get_piece()=="P" and self.items[self.prev_move_piece].get_square(self.alphachart,self.numchart)==self.columns[col_index-1]+self.rows[row_index] and self.items[self.prev_move_piece].get_moves()==1:
                move.append(self.columns[col_index-1]+self.rows[row_index-1])
                enpassant.append(self.columns[col_index-1]+self.rows[row_index-1])
                
            if col_index+1<8 and self.columns[col_index+1]+self.rows[row_index-1] in self.wboardstate.values():
                move.append(self.columns[col_index+1]+self.rows[row_index-1])
                
            if col_index+1<8 and row_index==3 and self.items[self.prev_move_piece].get_piece()=="P" and self.items[self.prev_move_piece].get_square(self.alphachart,self.numchart)==self.columns[col_index+1]+self.rows[row_index] and self.items[self.prev_move_piece].get_moves()==1:
                move.append(self.columns[col_index+1]+self.rows[row_index-1])
                enpassant.append(self.columns[col_index+1]+self.rows[row_index-1])
                
        if color=="B" and row_index==1:
            cp.append(1)
        elif color=="W" and row_index==6:
            cp.append(2)
             
        main.append(move) 
                    
        if r==True:
            remove_list=[]
            for i in main[0]: 
                if i[0]==col:                    
                    remove_list.append(i)
            l3 = [x for x in main[0] if x not in remove_list]
            return l3
        
        else:
            print(self.prev_move_piece)
            print("enpassant",enpassant,main[0])
            movementspace=self.verify(main[0])
            print("movementspace",movementspace)
            move=[]
            if not enpassant:
                move.append(movementspace)
                move.append(cp)
            else:
                move.append(movementspace)
                move.append(enpassant)
                
            print("move",move)

            return move
    
                            
def main():
    pygame.init()
    
    pygame.font.init()
    surface = pygame.display.set_mode((500,500))
    colorw = (235,235,208) 
    colorb = (119, 148, 85)
    pygame.display.set_caption('CHESS')
    font = pygame.font.SysFont('Comic Sans MS', 15)

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
    
    items={'WhiteKing':Pieces("WhiteKing",wK,240,420,surface,"W","K",0),'BlackKing':Pieces("BlackKing",bK,240,0,surface,"B","K",0),'WhiteQueen':Pieces("WhiteQueen",wQ,180,420,surface,"W","Q",0),'BlackQueen':Pieces("BlackQueen",bQ,180,0,surface,"B","Q",0),
           'BlackRookA':Pieces("BlackRookA",bRA,0,0,surface,"B","R",0),'BlackRookH':Pieces("BlackRookH",bRH,420,0,surface,"B","R",0),'WhiteRookA':Pieces("WhiteRookA",wRA,0,420,surface,"W","R",0),'WhiteRookH':Pieces("WhiteRookH",wRH,420,420,surface,"W","R",0),
           'BlackKnightB':Pieces("BlackKnightB",bNB,60,0,surface,"B","N",0),'BlackKnightG':Pieces("BlackKnightG",bNG,360,0,surface,"B","N",0),'WhiteKnightB':Pieces("WhiteKnightB",wNB,60,420,surface,"W","N",0),'WhiteKnightG':Pieces("WhiteKnightG",wNG,360,420,surface,"W","N",0),
           'BlackBishopC':Pieces("BlackBishopC",bBC,120,0,surface,"B","B",0),'BlackBishopF':Pieces("BlackBishopF",bBF,300,0,surface,"B","B",0),'WhiteBishopC':Pieces("WhiteBishopC",wBC,120,420,surface,"W","B",0),'WhiteBishopF':Pieces("WhiteBishopF",wBF,300,420,surface,"W","B",0),
           'BlackPawnA':Pieces("BlackPawnA",bPA,0,60,surface,"B","P",0),'BlackPawnB':Pieces("BlackPawnB",bPB,60,60,surface,"B","P",0),'BlackPawnC':Pieces("BlackPawnC",bPC,120,60,surface,"B","P",0),'BlackPawnD':Pieces("BlackPawnD",bPD,180,60,surface,"B","P",0),
           'BlackPawnE':Pieces("BlackPawnE",bPE,240,60,surface,"B","P",0),'BlackPawnF':Pieces("BlackPawnF",bPF,300,60,surface,"B","P",0),'BlackPawnG':Pieces("BlackPawnG",bPG,360,60,surface,"B","P",0),'BlackPawnH':Pieces("BlackPawnH",bPH,420,60,surface,"B","P",0),
           'WhitePawnA':Pieces("WhitePawnA",wPA,0,360,surface,"W","P",0),'WhitePawnB':Pieces("WhitePawnB",wPB,60,360,surface,"W","P",0),'WhitePawnC':Pieces("WhitePawnC",wPC,120,360,surface,"W","P",0),'WhitePawnD':Pieces("WhitePawnD",wPD,180,360,surface,"W","P",0),
           'WhitePawnE':Pieces("WhitePawnE",wPE,240,360,surface,"W","P",0),'WhitePawnF':Pieces("WhitePawnF",wPF,300,360,surface,"W","P",0),'WhitePawnG':Pieces("WhitePawnG",wPG,360,360,surface,"W","P",0),'WhitePawnH':Pieces("WhitePawnH",wPH,420,360,surface,"W","P",0)}

    
    down=False
    prev_checkclick=""
    checkclick=""
    sq=""
    x=0
    y=0
    x2=0
    y2=0
    render=0
    turn=["White","Black"]

    while running:
        clock.tick(120)
        
        wboard={}
        bboard={}
        
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
        

        
        check=0
        play=0
        encounter=0
        
        
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
                #print(enpassantwhite,enpassantblack)
                
                for k,v in items.items():

                    if(items[k].get_color()=="W"):
                        wboard[k]=items[k].get_square(alphachart,numchart)
                    else:
                        bboard[k]=items[k].get_square(alphachart,numchart)
                        
                                        
                if bool(alphachart.get(int(x2/60))) == True and bool(numchart.get(int(y2/60))) == True and bool(checkclick) == True and checkclick[0:5]==turn[0] and check==0:

                    previous_location=alphachart.get(int(x/60))+numchart.get(int(y/60))
                    move=alphachart.get(int(x2/60))+numchart.get(int(y2/60))
                    new=positions.get(move)
                    print
                
                    checkmove=CheckMove(items,positions.get(previous_location)[0],positions.get(previous_location)[1],positions.get(move)[0],positions.get(move)[1],items[checkclick].get_color(),items[checkclick].get_piece(),positions,wboard,bboard,prev_checkclick)
                    piece=items[checkclick].get_piece()
                    movementspace=[]
                    castlespace=[]
                    enpassantspace=[]
                    if piece=="P": 
                        movementspace=checkmove.Pawn()
                        print("final list ",movementspace)
                        if movementspace[1]==[2]:
                            items[checkclick].change_piece(imgw,"W","Q")
                        elif movementspace[1]==[1]:
                            items[checkclick].change_piece(imgb,"B","Q")   
                        enpassantspace=movementspace[1]        
                        movementspace=movementspace[0] 
                        
                        print(enpassantspace)
                        
                        #print("enpassant",enpassantspace)
                        
                    elif piece=="K":
                        #print(items[checkclick].get_moves())
                        movementspace=checkmove.King()
                        print("king",movementspace)
                        castlespace=movementspace[1]
                        
                        movementspace=movementspace[0]
                                              
                    elif piece=="Q":
                        movementspace=checkmove.Queen()
                        
                    elif piece=="B":
                        movementspace=checkmove.Bishop()
                        
                    elif piece=="R":
                        movementspace=checkmove.Rook()
                        
                    elif piece=="N":
                        movementspace=checkmove.Knight()
                        
                        
                    if move in castlespace:
                        items[checkclick].updateloc_permanent(new[0],new[1])
                        if move=="G1":
                            items["WhiteRookH"].updateloc_permanent(300,420)
                            items["WhiteRookH"].updatemove()
                            checkmove.update_wboard("WhiteRookH","F1")
                        elif move=="C1":
                            items["WhiteRookA"].updateloc_permanent(180,420)
                            items["WhiteRookA"].updatemove()
                            checkmove.update_wboard("WhiteRookA","D1")
                        elif move=="G8":
                            items["BlackRookH"].updateloc_permanent(300,0)
                            items["BlackRookH"].updatemove()
                            checkmove.update_bboard("BlackRookH","F8")
                        elif move=="C8":
                            items["BlackRookA"].updateloc_permanent(180,0)
                            items["BlackRookA"].updatemove()
                            checkmove.update_bboard("BlackRookA","D8")
                        items[checkclick].updatemove()
                        prev_checkclick=copy.deepcopy(checkclick)
                        checkclick=""
                        render=0
                        turn.reverse()
                        check=checkmove.checkmate(move)
                        play=1

                            
                        if check==1:
                            print("In Check")
                            
                    elif move in enpassantspace:
                        print("in here")
                        items[checkclick].updateloc_permanent(new[0],new[1])
                        del items[prev_checkclick]
                        items[checkclick].updatemove()
                        prev_checkclick=copy.deepcopy(checkclick)
                        checkclick=""
                        render=0
                        turn.reverse()
                        check=checkmove.checkmate(move)
                        play=1
                        
                        
                        if check==1:
                            print("In Check")
                        
                                               
                    elif move in movementspace:
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
                            if piece_delete:
                                del items[piece_delete]
                                encounter=1
                            items[checkclick].updateloc_permanent(new[0],new[1])
                            items[checkclick].updatemove()
                            prev_checkclick=copy.deepcopy(checkclick)
                            checkclick=""
                            render=0
                            turn.reverse()
                            check=checkmove.checkmate(move)
                            play=1

                            
                        else:                                  
                            new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                            items[checkclick].updateloc_permanent(new[0],new[1])
                            checkclick=""
                            render=0
                            
                        if check==1:
                            print("In Check")
                            
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
        
        if check==1 and play==1:
            playsound('C:/Users/babai/Desktop/chess_sounds/CHECK_MED_SHORT.wav')#has to get shorter           
        elif encounter==1 and play==1:
            playsound('C:/Users/babai/Desktop/chess_sounds/ELECTRIC_POP.wav')#has to get shorter 
        elif play==1:
            playsound('C:/Users/babai/Desktop/chess_sounds/POP.wav')
            
    pygame.quit()


main()
            
    


