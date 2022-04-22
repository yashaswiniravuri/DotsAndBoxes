import tkinter as tk
import pandas as pd
class PlayGame():
    def __init__(self):
        self.line_type=0#0 for hor_line_matrix and 1 for columns
        self.is_right_move=True#wrong clicks
        self.no_of_dots=2#size of one side to the dot matrix
        #get number of dots
        #Number of dots should be less than 3 
        self.get_noOfDots()
        #create a horizontal line matrix of size [no_of_dots x no_of_dots-1]
        self.hor_line_matrix=[[0 for y in range(self.no_of_dots-1)] for x in range (self.no_of_dots)]
        self.hor_line_matrix=pd.DataFrame(self.hor_line_matrix)
        #create a vertical line matrix of size [no_of_dots-1 x no_of_dots]
        self.ver_line_matrix=[[0 for y in range(self.no_of_dots)] for x in range (self.no_of_dots-1)]
        self.ver_line_matrix=pd.DataFrame(self.ver_line_matrix)
        self.no_of_players=int(input("Enter number of players: "))
        self.player=0 #current player id = 0
        self.points=[0 for x in range(self.no_of_players)]

    def get_noOfDots(self):
        while(self.no_of_dots<3):
            self.no_of_dots=int(input("Enter the matrix size: "))
    
    def start(self):
        
        while(self.hor_line_matrix.eq(0).any().any() and self.ver_line_matrix.eq(0).any().any()):#Loop until all the elements are filled
            #take input of the coordinates of the line a player draws
            print("Player ",self.player+1," is playing")
            print("enter starting point coordinates (x1,y1): ")
            row0=int(input("enter x1: "))
            col0=int(input("enter y1: "))
            print("enter ending point coordinates (x2,y2): ")
            row1=int(input("enter x2: "))
            col1=int(input("enter y2: "))
            if (row0==row1 and abs(col0-col1)==1):
                self.line_type=0#line type-horizontal
                self.hor_line_matrix.iloc[row0,col0]=1
            elif(col0==col1 and abs(row0-row1)==1):
                self.line_type=1#line type-vertical
                self.ver_line_matrix.iloc[row0,col0]=1
            else:
                self.is_right_move=False#wrong input
                print("Please enter valid input")
            self.Count_points(row0,col0)
        self.display_winner()

    def display_winner(self):
        max_value = max(self.points)
        max_index = self.points.index(max_value)
        print("WINNER: PLAYER",max_index+1)
 
    def Count_points(self,r0,c0):
        if self.is_right_move:
                if self.is_box(r0,c0):
                    self.points[self.player]+=1
                else:
                    self.player=((self.player+1)%self.no_of_players) #next player
        print("horizontal line matrix:\n",self.hor_line_matrix)
        print("vertical line matrix: \n",self.ver_line_matrix)

    def is_box(self,r,c):
        if self.line_type==0:#horizontal line check
            if r!=0 or r==self.no_of_dots-1:#edge rows of the matrix
                if self.hor_line_matrix.iloc[r-1,c]!=0 and self.ver_line_matrix.iloc[r-1,c]!=0 and self.ver_line_matrix.iloc[r-1,c+1]!=0:
                    return True
            elif(r+1<=self.no_of_dots):
                if(self.hor_line_matrix.iloc[r+1,c]!=0 and self.ver_line_matrix.iloc[r,c]!=0 and self.ver_line_matrix.iloc[r,c+1]!=0):
                    return True
        
        if self.line_type==1:#vertical line check
            if c!=0 or c==self.no_of_dots-1:#edge cols of the matrix
                if self.ver_line_matrix.iloc[r,c-1]!=0 and self.hor_line_matrix.iloc[r,c-1]!=0 and self.hor_line_matrix.iloc[r+1,c-1]!=0:
                    return True
            else:
                if (self.ver_line_matrix.iloc[r,c+1]!=0 and self.hor_line_matrix.iloc[r,c]!=0 and self.hor_line_matrix.iloc[r+1,c]!=0):
                    return True
        return False
       
        
if __name__=="__main__":
    game=PlayGame()
    game.start()
