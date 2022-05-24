import tkinter as tk
import numpy as np
from computer_game import *
from computer_game import computer_game
from human_game import *
class PlayGame():
    def __init__(self):
        self.line_type=0#0 for hor_line_matrix and 1 for columns
        self.is_right_move=True#wrong clicks
        self.no_of_dots=2#size of one side to the dot matrix
        #get number of dots
        #Number of dots should be less than 3 
        self.get_noOfDots()
        #create a horizontal line matrix of size [no_of_dots x no_of_dots-1]
        self.hor_line_matrix=np.zeros([self.no_of_dots,self.no_of_dots-1])
        #create a vertical line matrix of size [no_of_dots-1 x no_of_dots]
        self.ver_line_matrix=np.zeros([self.no_of_dots-1,self.no_of_dots])
        self.game_type=0
        while(self.game_type!=1 and self.game_type!=2):
            self.game_type=int(input("Press 1 for human game. Press 2 for computer game."))
        self.no_of_players=int(input("Enter number of players: "))
        self.player=0 #current player id = 0
        self.points=[0 for x in range(self.no_of_players)]

    def get_noOfDots(self):
        while(self.no_of_dots<3):
            self.no_of_dots=int(input("Enter the matrix size: "))
    
    def start(self):
        
        while((self.hor_line_matrix==0).any() and (self.ver_line_matrix==0).any()):#Loop until all the elements are filled i.e., 
            #all boxes are formed in any of the matrices
            #take input of the coordinates of the line a player draws
            if self.game_type==1:
                print("Player",self.player+1,"is playing")
                human_game(self)
            else:
                if self.player==self.no_of_players-1:
                    print("Computer is playing")
                    computer_game(self)
                else:
                    print("Player ",self.player+1," is playing")
                    human_game(self)
        self.display_winner()


    def display_winner(self):
        max_value = max(self.points)
        max_index = self.points.index(max_value)
        if self.game_type==2 and max_index==self.no_of_players-1:
            print("WINNER: COMPUTER of points ",max_value)
        else:
            print("WINNER: PLAYER ",max_index+1," of points ",max_value)

 
    def Count_points(self,r0,c0):
        if self.is_right_move:
            if self.is_box(r0,c0):
                self.points[self.player]+=1
            else:
                self.switch_player()
        else:
            print("wrong move!!!! please play again")
    
        print("horizontal line matrix:\n",self.hor_line_matrix)
        print("vertical line matrix: \n",self.ver_line_matrix)

    def switch_player(self):
       self.player=((self.player+1)%self.no_of_players) #next player


    def is_box(self,r,c):
        if self.line_type==0:#horizontal line check
            if r!=0 or r==self.no_of_dots-1:#edge rows of the matrix
                if self.hor_line_matrix[r-1,c]!=0 and self.ver_line_matrix[r-1,c]!=0 and self.ver_line_matrix[r-1,c+1]!=0:
                    return True
            elif(r+1<=self.no_of_dots):
                if(self.hor_line_matrix[r+1,c]!=0 and self.ver_line_matrix[r,c]!=0 and self.ver_line_matrix[r,c+1]!=0):
                    return True
        
        if self.line_type==1:#vertical line check
            if c!=0 or c==self.no_of_dots-1:#edge cols of the matrix
                if self.ver_line_matrix[r,c-1]!=0 and self.hor_line_matrix[r,c-1]!=0 and self.hor_line_matrix[r+1,c-1]!=0:
                    return True
            else:
                if (self.ver_line_matrix[r,c+1]!=0 and self.hor_line_matrix[r,c]!=0 and self.hor_line_matrix[r+1,c]!=0):
                    return True
        return False