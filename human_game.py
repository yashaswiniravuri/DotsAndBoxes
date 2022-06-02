from PlayGame import *
from Chain import *

class human_game():
    def __init__(self,PlayGame):
        self.game=PlayGame
        self.is_right_move=False
        print("enter starting point coordinates (x1,y1): ")
        row0=int(input("enter x1: "))
        col0=int(input("enter y1: "))
        print("enter ending point coordinates (x2,y2): ")
        row1=int(input("enter x2: "))
        col1=int(input("enter y2: "))

        self.is_update=self.update_move(row0,col0,row1,col1)
        if not self.is_update: 
            print("Invalid coordinates!!! Please enter again.")

    def update_move(self,row0,col0,row1,col1):
        if (row0==row1 and abs(col0-col1)==1 and self.game.hor_line_matrix[row0,col0]==0):
            self.game.hor_line_matrix[row0,col0]=1
            self.game.Count_points(row0,col0,0)
            self.game.hor_moves.append([row0,col0])
            x,y,mode,value=self.game.chain.is_chain(row0,col0,0)
            if mode==1:
                self.game.chain.append(x,y,value)
            elif mode==2:
                self.game.chain.remove(x,y,value)
            return True

        elif(col0==col1 and abs(row0-row1)==1 and self.game.ver_line_matrix[row0,col0]==0):
            self.game.ver_line_matrix[row0,col0]=1
            self.game.Count_points(row0,col0,1)
            self.game.ver_moves.append([row0,col0])
            x,y,mode,value=self.game.chain.is_chain(row0,col0,1)
            if mode==1:
                self.game.chain.append(x,y,value)
            elif mode==2:
                self.game.chain.remove(x,y,value)
            return True
        return False

        
        