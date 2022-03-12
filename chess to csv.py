# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:07:06 2022

@author: babai
"""


import fileinput
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd

fileinput.close()
def checkfiles():  
    #time at the start of program is noted
    start = time.time()
    years=[]  
    exceptions=[]
    #keeps a track of number of lines in the file
    count = 0
    Id=[]
    Date=[]
    Result=[]
    White_ELO=[]
    Black_ELO=[]
    Number_of_moves=[]
    DateCorrupt=[]
    ResultCorrupt=[]
    White_ELOCorrupt=[]
    Black_ELOCorrupt=[]
    EdateCorrupt=[]
    SetupCorrupt=[]
    FenCorrupt=[]
    Result_2Corrupt=[]
    OyrangeCorrupt=[]
    BlenCorrupt=[]
    GamePGN=[]
    for lines in tqdm(fileinput.input(["D:/Chess shit/all_with_filtered_anotations_since1998.txt"])):
        #print(lines.split(" ")[1].split(".")[0])
        #years.append(lines.split(" ")[1].split(".")[0])
        #print(lines.split(" ")[2])
        '''if lines.split(" ")[1].split(".")[0] in ['#\n','filein','program','????','1','datetime']:
            exceptions.append(count)
        if count in [0, 1, 2, 3, 4, 34796, 1797667, 2221643, 2934416, 3250289]:
            #print(count)
            print(lines)
        '''
        
        
        
        if count not in [0,1,2,3,4]:
            line=lines.split(" ")
            line.remove("###")
            line.remove("\n")
            #print(line)
            #print(len(line))
            gamepgn=""
            for i in range(16,len(line)):
                gamepgn+=line[i]
                gamepgn+=" "
            #print(gamepgn)
            Id.append(line[0])
            Date.append(line[1])
            Result.append(line[2])
            White_ELO.append(line[3])
            Black_ELO.append(line[4])
            Number_of_moves.append(line[5])
            DateCorrupt.append(line[6])
            ResultCorrupt.append(line[7])
            White_ELOCorrupt.append(line[8])
            Black_ELOCorrupt.append(line[9])
            EdateCorrupt.append(line[10])
            SetupCorrupt.append(line[11])
            FenCorrupt.append(line[12])
            Result_2Corrupt.append(line[13])
            OyrangeCorrupt.append(line[14])
            BlenCorrupt.append(line[15])
            GamePGN.append(gamepgn)
        
            
            #dic = {'Id': [line[0]], 'Date': [line[1]], 'Result': [line[2]], 'White_ELO': [line[3]], 'Black_Elo': [line[4]], 'Number_of_moves': [line[5]], 'DateCorrupt': [line[6]], 'ResultCorrupt': [line[7]], 'White_ELOCorrupt': [line[8]], 'Black_ELOCorrupt': [line[9]], 'EdateCorrupt': [line[10]], 'SetupCorrupt': [line[11]], 'FenCorrupt': [line[12]],  'Result_2Corrupt': [line[13]], 'OyrangeCorrupt': [line[14]], 'BlenCorrupt': [line[15]], 'GamePGN': gamepgn}
            
            #df = pd.DataFrame(dic) 
            #df.to_csv('D:/Chess shit/Games.csv', index=False)
    

        count = count + 1
        
        if count >3561470:
            break
        
        
    '''file=fileinput.input(["D:/Chess shit/all_with_filtered_anotations_since1998.txt"])
    for i in tqdm(range(5,3561470)):
        print(file[i].split(" ")[1].split(".")[0])'''
        

    #dic = {'Id': Id, 'Date': Date, 'Result': Result, 'White_ELO': White_ELO, 'Black_Elo': Black_ELO, 'Number_of_moves': Number_of_moves, 'DateCorrupt': DateCorrupt, 'ResultCorrupt': ResultCorrupt, 'White_ELOCorrupt': White_ELOCorrupt, 'Black_ELOCorrupt': Black_ELOCorrupt, 'EdateCorrupt': EdateCorrupt, 'SetupCorrupt': SetupCorrupt, 'FenCorrupt': FenCorrupt,  'Result_2Corrupt': Result_2Corrupt, 'OyrangeCorrupt': OyrangeCorrupt, 'BlenCorrupt': BlenCorrupt, 'GamePGN': GamePGN}
    
    #df = pd.DataFrame(dic) 
    #df.to_csv('D:/Chess shit/Games.csv', index=False)      
    #time at the end of program execution is noted
    end = time.time()
      
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))
    print("No. of lines printed: ",count)
    print("Exceptions: ",set(Date))
    #return years

Number_of_Games=3561470
'''with open("D:/Chess shit/all_with_filtered_anotations_since1998.txt") as f:
    lines_to_read = [5]
    for position, line in enumerate(f):
        if position in lines_to_read:
            print(line.split(" ")[1])'''
            
#gameyears=checkfiles()
#print(set(gameyears))

checkfiles()

#for i in tqdm (range (100), desc="Loading..."):
    #pass


#print(firstLine)
