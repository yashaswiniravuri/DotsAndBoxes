import tkinter as tk
import numpy as np
from human_game import *
from computer_game import *
from Chain import *
from Box import *
class PlayGame():
    def __init__(self):
        self.no_of_dots=2#size of one side to the dot matrix
        #get number of dots
        #Number of dots should be less than 3 
        self.get_noOfDots()
        #create a horizontal line matrix of size [no_of_dots x no_of_dots-1]
        self.hor_line_matrix=np.zeros([self.no_of_dots,self.no_of_dots-1])
        #create a vertical line matrix of size [no_of_dots-1 x no_of_dots]
        self.ver_line_matrix=np.zeros([self.no_of_dots-1,self.no_of_dots])
        self.chains=np.zeros([self.no_of_dots-1,self.no_of_dots-1])
        self.game_type=0
        while(self.game_type!=1 and self.game_type!=2 and self.game_type!=3):
            self.game_type=int(input("Press 1 for human vs human game. Press 2 for human vs computer game. Press 3 for computer vs computer game: "))
        self.no_of_players=int(input("Enter number of players:"))
        print("\n\n")

        self.player=0 #current player id = 0
        self.points=[0 for x in range(self.no_of_players)]
        self.turn=0#stores the turns taken by players
        #stores the moves made by the players
        self.hor_moves=[]
        self.ver_moves=[]
        self.chain_list=np.zeros([self.no_of_dots-1,self.no_of_dots-1])
        self.chain=Chain(self)
        self.box=Box(self)
        

    def get_noOfDots(self):
        while(self.no_of_dots<3):
            self.no_of_dots=int(input("Enter the matrix size: "))
    

    def start(self):
        while((self.hor_line_matrix==0).any() and (self.ver_line_matrix==0).any()):#Loop until all the elements are filled i.e., 
            #all boxes are formed in any of the matrices
            #take input of the coordinates of the line a player draws
            
            for i in range(0,(self.no_of_dots*2)-1):
                if i%2==0:
                  for j in range(0,(self.no_of_dots*2)-1):  
                        if j%2==1:
                            p=int(i/2)
                            q=int((j-1)/2)
                            if self.hor_line_matrix[p,q]==1:
                                print('-',end=" ")
                            else:
                                print(" ",end=" ")
                        else: print("x",end=" ")
                else:
                    for j in range(0,(self.no_of_dots*2)-1):
                        if j%2==0:
                            p=int((i-1)/2)
                            q=int(j/2)
                            if self.ver_line_matrix[p,q]==1:
                                print('|',end=" ")
                            else:
                                print(" ",end=" ")
                        else: print(" ",end=" ")
                print()

            if self.game_type==1:
                for i in range(self.no_of_players):
                    print("Player ",i+1," points: ",self.points[i])
                print("\nPLAYER",i+1,"IS PLAYING\n")
                human_game(self)
            elif self.game_type==2:
                for i in range(self.no_of_players):
                    if i==self.no_of_players-1:print("Computer points: ",self.points[i])
                    else:print("Player ",i+1," points: ",self.points[i])
                if self.player==self.no_of_players-1:
                    print("\nCOMPUTER IS PLAYING\n")
                    computer_game(self)
                else:
                    print("\nPLAYER ",self.player+1," IS PLAYING\n")
                    human_game(self)
            else:
                for i in range(self.no_of_players):
                    print("Computer ",i+1," points: ",self.points[i])
                print("\nCOMPUTER",self.player+1,"IS PLAYING\n")
                computer_game(self)
            '''print("HORIZONTAL LINE MATRIX")
            print(self.hor_line_matrix)
            print("VERTICAL LINE MATRIX")
            print(self.ver_line_matrix)
            print("CHAIN MATRIX:")
            print(self.chain_list)'''
            print("---------------------------------------")
        self.display_winner()


    def display_winner(self):
        max_value = max(self.points)
        max_index = self.points.index(max_value)
        print("--------------------------------------")
        for i in range(0,(self.no_of_dots*2)-1):
                if i%2==0:
                  for j in range(0,(self.no_of_dots*2)-1):  
                        if j%2==1:
                            p=int(i/2)
                            q=int((j-1)/2)
                            if self.hor_line_matrix[p,q]==1:
                                print('-',end=" ")
                            else:
                                print(" ",end=" ")
                        else: print("x",end=" ")
                else:
                    for j in range(0,(self.no_of_dots*2)-1):
                        if j%2==0:
                            p=int((i-1)/2)
                            q=int(j/2)
                            if self.ver_line_matrix[p,q]==1:
                                print('|',end=" ")
                            else:
                                print(" ",end=" ")
                        else: print(" ",end=" ")
                print()
        print("--------------------------------------")
        if self.game_type==2 and max_index==self.no_of_players-1:
            print("WINNER: COMPUTER of points ",max_value)
        else:
            print("WINNER: PLAYER ",max_index+1," of points ",max_value)
        

 
    def Count_points(self,r0,c0,type):
        if self.is_box(r0,c0,type):
            print("BOX MADE")
            self.points[self.player]+=1
        else:
            self.switch_player()

    def switch_player(self):
       self.player=((self.player+1)%self.no_of_players) #next player


    def is_box(self,r,c,type):
        if type==0:#horizontal line check
            if r!=0 or r==self.no_of_dots-1:#edge rows of the matrix
                if self.hor_line_matrix[r-1,c]!=0 and self.ver_line_matrix[r-1,c]!=0 and self.ver_line_matrix[r-1,c+1]!=0:
                    return True
            elif(r+1<=self.no_of_dots):
                if(self.hor_line_matrix[r+1,c]!=0 and self.ver_line_matrix[r,c]!=0 and self.ver_line_matrix[r,c+1]!=0):
                    return True
        
        if type==1:#vertical line check
            if c!=0 or c==self.no_of_dots-1:#edge cols of the matrix
                if self.ver_line_matrix[r,c-1]!=0 and self.hor_line_matrix[r,c-1]!=0 and self.hor_line_matrix[r+1,c-1]!=0:
                    return True
            else:
                if (self.ver_line_matrix[r,c+1]!=0 and self.hor_line_matrix[r,c]!=0 and self.hor_line_matrix[r+1,c]!=0):
                    return True
        return False
