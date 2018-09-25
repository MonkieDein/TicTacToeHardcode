"""
Created on Sun Sep 23 15:08:21 2018
@author: Monkie
Python Review Solve TicTacToe with MDP

"""
import numpy as np
import random

board = np.matrix('1 2 3; 4 5 6; 7 8 9')
board = board * 0 


class Player:
    
    def __init__(self, row, col, board, indicator):
        self.row = row-1
        self.col = col-1
        self.board = board
        self.indicator = indicator
    
    def move(self):            
        self.board[self.row,self.col] = self.indicator
        print (self.board)
        return self.board
    
    def update(self):
        b = ( self.board == self.indicator )
        if (np.sum(b.sum(axis=1)==3) + np.sum(b.sum(axis=0)==3) + (np.sum(b.diagonal())==3) + (np.sum(b[::-1].diagonal())==3) > 0) :
            print("Player",self.indicator," win the game !!!")
            return 1
        if (np.sum(self.board == 0) == 0 ):
            print("tied")
            return 0.000001
        return 0
    
    def autoplay(self):
        b = np.where( (self.board != self.indicator) & (self.board != 0) )
        if (len(b[0]) > 0 ) :
            e_indicator = self.board[b[0][0],b[1][0]]
        
        b = np.where(self.board == 0)
        length = len(b[0])
        
        if (self.board[1,1]==0):
            self.board[1,1]=self.indicator
            print("CompCheckMove0")
            print (self.board)
            return(self.board)
            
        if (np.sum(self.board==0)==8):
            rs = [0,0,2,2]
            random.shuffle(rs)
            self.board[rs[0],rs[1]]=self.indicator
            print("COMPbestSTART")
            print (self.board)
            return(self.board)
            
            
            
        if ((np.sum(self.board==0)==6) & ((np.sum(self.board.diagonal()!=0)==3) + (np.sum(self.board[::-1].diagonal()!=0)==3) > 0)):
            rs = [0,1]
            rs2 = [0,1]
            mat = np.matrix('0 2; 1 1')
            random.shuffle(rs)
            random.shuffle(rs2)
            self.board[mat[rs[0],rs2[0]],mat[rs[1],rs2[0]]]=self.indicator
            print("CompHardCodeSITUATION")
            print (self.board)
            return(self.board)
            
            
            
        for i in range(0,(length)):
            tryboard = np.matrix.copy(self.board)
            tryboard[b[0][i],b[1][i]] = self.indicator
            k = ( tryboard == self.indicator )
            if (np.sum(k.sum(axis=1)==3) + np.sum(k.sum(axis=0)==3) + (np.sum(k.diagonal())==3) + (np.sum(k[::-1].diagonal())==3) > 0) :
                print("CompWinningMove")
                print (tryboard)
                return(tryboard)
            
            
        for i in range(0,(length)):
            tryboard = np.matrix.copy(self.board)
            tryboard[b[0][i],b[1][i]] = e_indicator
            k = ( tryboard == e_indicator )
            if (np.sum(k.sum(axis=1)==3) + np.sum(k.sum(axis=0)==3) + (np.sum(k.diagonal())==3) + (np.sum(k[::-1].diagonal())==3) > 0) :
                tryboard[b[0][i],b[1][i]] = self.indicator
                print("CompCheckMove")
                print (tryboard)
                return(tryboard)
                
                
                
        for i2 in range(0,(length)):
            summ = 0
            for i3 in range(0,(length)):
                if (i3 != i2):
                    tryboard = np.matrix.copy(self.board)
                    tryboard[b[0][i2],b[1][i2]] = e_indicator
                    tryboard[b[0][i3],b[1][i3]] = e_indicator
                    k = ( tryboard == e_indicator )
                    if (np.sum(k.sum(axis=1)==3) + np.sum(k.sum(axis=0)==3) + (np.sum(k.diagonal())==3) + (np.sum(k[::-1].diagonal())==3) > 0) :
                        summ = summ + 1
                        if (summ == 2):
                            tryboard[b[0][i2],b[1][i2]] = self.indicator
                            tryboard[b[0][i3],b[1][i3]] = 0
                            print("p1DualCheck")
                            print (tryboard)
                            return(tryboard)
                
        row_empty = np.where(self.board==0)[0] 
        col_empty = np.where(self.board==0)[1] 
        
        randact=random.randint(0,(len(row_empty)-1))
        self.board[row_empty[randact],col_empty[randact]] = self.indicator
        print("p1randomMove")
        print (self.board)
        return (self.board)
        

lose = 0
win = 0
for iteration in range(0,1000):
    stop = 0 
    board = board * 0 
    print("please answer with yes/no !     if you want to quit type (Q)")
    start = input("Do you wanna Start?")
    if (start=="Q"):
        break
    
    while ((start != "yes")&(start != "no")):
        print("please answer with yes/no !")
        start = input("Do you wanna Start?")
        
    if (start == "no"):
        comp = Player(0,0,board,2) 
        board = comp.autoplay()
        comp = Player(0,0,board,2) 
        stop = comp.update()
        win = win + stop

    
    while (stop == 0):
        row_loc = int(input("Which row do you wanna play?"))
        col_loc = int(input("Which column do you wanna play?"))
    
        while (board[row_loc-1 ,col_loc-1 ] != 0):
            print("please select an empty element")
            row_loc = int(input("Which row do you wanna play?"))
            col_loc = int(input("Which column do you wanna play?"))

           
        player1 = Player(row_loc,col_loc,board,1)  
        board = player1.move()
        stop = player1.update()
        lose = lose + stop
               
        if (stop==0):    
            comp = Player(0,0,board,2) 
        
            board = comp.autoplay()
            comp = Player(0,0,board,2) 
            stop = comp.update()
            win = win + stop
        
            
            
            
'''
            row_empty = np.where(board==0)[0] + 1
            col_empty = np.where(board==0)[1] + 1
    
            randact=random.randint(0,(len(row_empty)-1))
            
            player2 = Player(row_empty[randact],col_empty[randact],board,2) 
            print ("p2moving")
            board = player2.move()
            player2 = Player(row_empty[randact],col_empty[randact],board,2) 
            stop = player2.update()
            lose = stop + lose
''' 








