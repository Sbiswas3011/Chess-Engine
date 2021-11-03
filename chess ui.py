# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:47:50 2021

@author: Snehangsu
"""

import pygame 
from pygame.locals import *

        
class Pieces(pygame.sprite.Sprite):
    def __init__(self,name,wPH,x,y,s):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.wPH = wPH
        self.x = x
        self.y = y
        self.s = s
      
    def update_setup(self):
        self.s.blit(self.wPH,(self.x,self.y))
        
    def updateloc(self,x,y):
        self.s.blit(self.wPH,(x,y))
        
    def check_pos(self, alpha, num, mouse):
        position=alpha.get(int(self.x/60))+num.get(int(self.y/60))
        if mouse[0]>=self.x and mouse[0]<=self.x+60 and mouse[1]>=self.y and mouse[1]<=self.y+60 :
            print(self.name,"at",position)
            
            return self.name  
        
    def get_pos(self):
        return (self.x,self.y)
 
def whiteking(items,newx,newy):
    
        
        
        
        
      
            

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
    
    items={'WhiteKing':Pieces("WhiteKing",wK,240,420,surface),'BlackKing':Pieces("BlackKing",bK,240,0,surface),'WhiteQueen':Pieces("WhiteQueen",wQ,180,420,surface),'BlackQueen':Pieces("BlackQueen",bQ,180,0,surface),
           'BlackRookA':Pieces("BlackRookA",bRA,0,0,surface),'BlackRookH':Pieces("BlackRookH",bRH,420,0,surface),'WhiteRookA':Pieces("WhiteRookA",wRA,0,420,surface),'WhiteRookH':Pieces("WhiteRookH",wRH,420,420,surface),
           'BlackKnightB':Pieces("BlackKnightB",bNB,60,0,surface),'BlackKnightG':Pieces("BlackKnightG",bNG,360,0,surface),'WhiteKnightB':Pieces("WhiteKnightB",wNB,60,420,surface),'WhiteKnightG':Pieces("WhiteKnightG",wNG,360,420,surface),
           'BlackBishopC':Pieces("BlackBishopC",bBC,120,0,surface),'BlackBishopF':Pieces("BlackBishopF",bBF,300,0,surface),'WhiteBishopC':Pieces("WhiteBishopC",wBC,120,420,surface),'WhiteBishopF':Pieces("WhiteBishopF",wBF,300,420,surface),
           'BlackPawnA':Pieces("BlackPawnA",bPA,0,60,surface),'BlackPawnB':Pieces("BlackPawnB",bPB,60,60,surface),'BlackPawnC':Pieces("BlackPawnC",bPC,120,60,surface),'BlackPawnD':Pieces("BlackPawnD",bPD,180,60,surface),
           'BlackPawnE':Pieces("BlackPawnE",bPE,240,60,surface),'BlackPawnF':Pieces("BlackPawnF",bPF,300,60,surface),'BlackPawnG':Pieces("BlackPawnG",bPG,360,60,surface),'BlackPawnH':Pieces("BlackPawnH",bPH,420,60,surface),
           'WhitePawnA':Pieces("WhitePawnA",wPA,0,360,surface),'WhitePawnB':Pieces("WhitePawnB",wPB,60,360,surface),'WhitePawnC':Pieces("WhitePawnC",wPC,120,360,surface),'WhitePawnD':Pieces("WhitePawnD",wPD,180,360,surface),
           'WhitePawnE':Pieces("WhitePawnE",wPE,240,360,surface),'WhitePawnF':Pieces("WhitePawnF",wPF,300,360,surface),'WhitePawnG':Pieces("WhitePawnG",wPG,360,360,surface),'WhitePawnH':Pieces("WhitePawnH",wPH,420,360,surface)}
    
    item_to_piece={"WhiteKing":wK,"BlackKing":bK,"WhiteQueen":wQ,"BlackQueen":bQ,"BlackRookA":bRA,"BlackRookH":bRH,"WhiteRookA":wRA,"WhiteRookH":wRH,"BlackKnightB":bNB,"BlackKnightG":bNG,"WhiteKnightB":wNB,"WhiteKnightG":wNG,
                   "BlackBishopC":bBC,"BlackBishopF":bBF,"WhiteBishopC":wBC,"WhiteBishopF":wBF,"BlackPawnA":bPA,"BlackPawnB":bPB,"BlackPawnC":bPC,"BlackPawnD":bPD,"BlackPawnE":bPE,"BlackPawnF":bPF,"BlackPawnG":bPG,"BlackPawnH":bPH,
                   "WhitePawnA":wPA,"WhitePawnB":wPB,"WhitePawnC":wPC,"WhitePawnD":wPD,"WhitePawnE":wPE,"WhitePawnF":wPF,"WhitePawnG":wPG,"WhitePawnH":wPH,}
    
    down=False
    checkclick=""
    x=0
    y=0
    x2=0
    y2=0
    render=0
    
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
        
        
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == MOUSEBUTTONDOWN:
                if down==False:
                    x,y = pygame.mouse.get_pos()
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
                checkmove=check(k,items,x2,y2)
                if bool(alphachart.get(int(x2/60))) == True and bool(numchart.get(int(y2/60))) == True and bool(checkclick) == True:
                    new=positions.get(alphachart.get(int(x2/60))+numchart.get(int(y2/60)))
                    
                    
                    for k,v in items.items():
                        if k==checkclick:
                            continue
                        elif items[k].get_pos()==(new[0],new[1]):
                            if k[0:5]==checkclick[0:5]:
                                delete= False
                            else:
                                delete=True
                                del items[k]
                                break
                                               
                    if delete==True:
                        
                        items[checkclick]=Pieces(checkclick,item_to_piece[checkclick],new[0],new[1],surface)
                        checkclick=""
                        render=0
                        
                    else:
                        
                        new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                        items[checkclick]=Pieces(checkclick,item_to_piece[checkclick],new[0],new[1],surface)
                        checkclick=""
                        render=0

                else:
                    if checkclick:
                        new=positions.get(alphachart.get(int(x/60))+numchart.get(int(y/60)))
                        items[checkclick]=Pieces(checkclick,item_to_piece[checkclick],new[0],new[1],surface)
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
    
main()
            
    


