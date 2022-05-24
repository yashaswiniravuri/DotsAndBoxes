from random import randint
from select import select
from PlayGame import *
import numpy as np
class computer_game():
    def __init__(self,PlayGame):
        self.game=PlayGame
        self.make_move()

    def make_move(self):
        count=0
        for x in range(self.game.no_of_dots):
            for y in range(self.game.no_of_dots-1):
                if self.game.hor_line_matrix[x,y]==0:
                    self.game.line_type=0
                    if self.game.is_box(x,y):
                        self.game.hor_line_matrix[x,y]=1
                        self.game.points[self.game.player]+=1
                        count+=1
        if count==0:
            for x in range(self.game.no_of_dots-1):
                for y in range(self.game.no_of_dots):
                    if self.game.ver_line_matrix[x,y]==0:
                        self.game.line_type=1
                        if self.game.is_box(x,y):
                            self.game.ver_line_matrix[x,y]=1
                            self.game.points[self.game.player]+=1
                            count+=1
        if count==0:
            self.select_next_edge()
            self.game.switch_player()
        print("horizontal line matrix:\n",self.game.hor_line_matrix)
        print("vertical line matrix: \n",self.game.ver_line_matrix)
    
    def select_next_edge(self):
        if (self.game.hor_line_matrix==0).any():
            myarray=np.argwhere(self.game.hor_line_matrix==0)
            self.game.line_type=0
            i,j=myarray[0]
            self.game.hor_line_matrix[i,j]=1            
            
        elif (self.game.ver_line_matrix==0).any():
            myarray=np.argwhere(self.game.ver_line_matrix==0)
            self.game.line_type=1
            i,j=myarray[0]
            self.game.ver_line_matrix[i,j]=1