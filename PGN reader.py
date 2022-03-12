# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:22:33 2022

@author: babai
"""
import pandas as pd
from tqdm import tqdm
import fileinput
import numpy as np
import random
fileinput.close()

pd.set_option("display.max_colwidth", None)
#df = pd.read_csv('D:/Chess shit/Games.csv', low_memory=False)
count=0
line=""
gamenumber=random.randint(0, 3000000)
for lines in tqdm(fileinput.input(["D:/Chess shit/all_with_filtered_anotations_since1998.txt"])):
    
    
    if count in [gamenumber+5]:
        line=lines
        print(lines)
    count+=1
    if count>gamenumber+5:
        break
        
moves=line.split("### ")[1].split(" ")
moves.remove("\n")
print(moves)
#player=""
#moves=['W18.d4=Q']
FEN_start="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
def PGN_readerv1(moves):
    promotion_dictionary={"K":"King","Q":"Queen","R":"Rook","B":"Bishop","N":"Knight"}
    pieces=["K","Q","R","B","N"]
    pawn=["a","b","c","d","e","f","g","h"]
    rank=["1","2","3","4","5","6","7","8"]
    prev_move=""
    for i in range(len(moves)):
        move=moves[i].split(".")
        if(move[0][0]=="W"):
            #print("Player is White")
            player="White"
        elif(move[0][0]=="B"):
            #print("Player is Black")
            player="Black"        
        move_number=move[0][1]
        
        if move[1]=="O-O":
            print(player,"King side Castle")
            
        elif move[1]=="O-O-O":
            print(player,"Queen side Castle")
            
        elif move[1][0] in pieces:
            
            if move[1][0] == "K":
                piece="King"
                if len(move[1])>3:
                    if move[1][1]=="x":
                        print(player,piece,"takes on",move[1][2]+move[1][3])
                else:
                    print(player,piece,"moves to",move[1][1]+move[1][2])
                    
            elif move[1][0] == "Q":
                piece="Queen"
                if move[1][1] in pawn:
                    if len(move[1])>3:
                        if move[1][3]=="+":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with check")
                        elif move[1][3]=="#":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with checkmate")
                    else:
                        print(player,piece,"moves to",move[1][1]+move[1][2])
                        
                elif move[1][1] == "x":
                    if len(move[1])>4:
                        if move[1][4]=="+":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with check")
                        elif move[1][4]=="#":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with checkmate")
                    else:
                        print(player,piece,"takes on",move[1][2]+move[1][3])
                    
    
            elif move[1][0] == "B":
                piece="Bishop"
                if move[1][1] in pawn:
                    if len(move[1])>3:
                        if move[1][3]=="+":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with check")
                        elif move[1][3]=="#":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with checkmate")
                    else:
                        print(player,piece,"moves to",move[1][1]+move[1][2])
                        
                elif move[1][1] == "x":
                    if len(move[1])>4:
                        if move[1][4]=="+":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with check")
                        elif move[1][4]=="#":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with checkmate")
                    else:
                        print(player,piece,"takes on",move[1][2]+move[1][3])
                
            elif move[1][0] == "R":
                piece="Rook"
                if move[1][1] in pawn and move[1][2]!="x":
                    if len(move[1])==4:
                        if move[1][3]=="+":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with check")
                        elif move[1][3]=="#":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with checkmate")
                        else:
                            print(player,piece,move[1][1],"moves to",move[1][1]+move[1][2])
    
                    elif len(move[1])==5: #case with piece ambiguity
                        if move[1][4]=="+":
                            print(player,piece,move[1][1],"moves to",move[1][2]+move[1][3],"with check")
                        elif move[1][4]=="#":
                            print(player,piece,move[1][1],"moves to",move[1][2]+move[1][3],"with checkmate")
                    else:
                        print(player,piece,"moves to",move[1][1]+move[1][2])
                
                elif move[1][1] in pawn and move[1][2]=="x": #case with piece ambiguity
                    #print("here")
                    if len(move[1])==6:
                        #print("here")
                        if move[1][5]=="+":
                            print(player,piece,move[1][1],"moves to",move[1][3]+move[1][4],"with check")
                        elif move[1][5]=="#":
                            print(player,piece,move[1][1],"moves to",move[1][3]+move[1][4],"with checkmate")
                    else:
                        print(player,piece,move[1][1],"moves to",move[1][3]+move[1][4])
                        
                elif move[1][1]=="x":
                    if len(move[1])==5:
                        if move[1][4]=="+":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with check")
                        elif move[1][4]=="#":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with checkmate")
                    else:
                        print(player,piece,"takes on",move[1][2]+move[1][3])
      
                    
            elif move[1][0] == "N": #column or row code karo or download code
                piece="Knight"
                if move[1][1] in pawn and move[1][2]!="x":
                    if len(move[1])==4:
                        if move[1][3]=="+":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with check")
                        elif move[1][3]=="#":
                            print(player,piece,"moves to",move[1][1]+move[1][2],"with checkmate")
                        else:
                            print(player,piece,move[1][1],"moves to",move[1][1]+move[1][2])
    
                    elif len(move[1])==5: #case with piece ambiguity
                        if move[1][4]=="+":
                            print(player,piece,move[1][1],"moves to",move[1][2]+move[1][3],"with check")
                        elif move[1][4]=="#":
                            print(player,piece,move[1][1],"moves to",move[1][2]+move[1][3],"with checkmate")
                    else:
                        print(player,piece,"moves to",move[1][1]+move[1][2])
                
                elif move[1][1] in pawn and move[1][2]=="x": #case with piece ambiguity
                    if len(move[1])==6:
                        if move[1][5]=="+":
                            print(player,piece,move[1][1],"moves to",move[1][3]+move[1][4],"with check")
                        elif move[1][5]=="#":
                            print(player,piece,move[1][1],"moves to",move[1][3]+move[1][4],"with checkmate")
                    else:
                        print(player,piece,move[1][1],"moves to",move[1][3]+move[1][4])
                        
                elif move[1][1]=="x":
                    if len(move[1])==5:
                        if move[1][4]=="+":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with check")
                        elif move[1][4]=="#":
                            print(player,piece,"takes on",move[1][2]+move[1][3],"with checkmate")
                    else:
                        print(player,piece,"takes on",move[1][2]+move[1][3])
                
                
        elif move[1][0] in pawn:
            if move[1][1] in rank:
                #print("here")
                if len(move[1])>2:
                    if move[1][2]=="=":
                        if move[1][3] in pieces:
                            print(player,move[1][0]+" pawn to "+move[1][0]+move[1][1]+" promoting to "+promotion_dictionary[move[1][3]])                         
                    elif move[1][2]=="+":
                        print(player,move[1][0]+" pawn to "+move[1][0]+move[1][1]+" with check")
                    elif move[1][2]=="#":
                        print(player,move[1][0]+" pawn to "+move[1][0]+move[1][1]+" with checkmate")
                else:
                    print(player,move[1][0]+" pawn to "+move[1][0]+move[1][1])
            elif move[1][1]=="x":
                if move[1][2] in pawn and move[1][3] in rank:
    
                    if len(move[1])>4:
                        if move[1][4]=="=":
                            if move[1][5] in pieces:
                                print(player,move[1][0]+" pawn takes on "+move[1][2]+move[1][3]+" promoting to "+promotion_dictionary[move[1][5]]) 
                        elif move[1][4]=="+":
                            print(player,move[1][0]+" pawn takes on "+move[1][2]+move[1][3]+" with check")
                        elif move[1][4]=="#":
                            print(player,move[1][0]+" pawn takes on "+move[1][2]+move[1][3]+" with checkmate")
                    else:
                        print(player,move[1][0]+" pawn takes on "+move[1][2]+move[1][3])
            
        
PGN_readerv1(moves)
    
#print(df.columns)
#indices=df[df['ResultCorrupt'].isnull()].index.tolist()
#print(indices)


