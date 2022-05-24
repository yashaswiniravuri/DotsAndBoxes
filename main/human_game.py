from PlayGame import *
class human_game():
    def __init__(self,PlayGame):
        self.game=PlayGame
        print("enter starting point coordinates (x1,y1): ")
        row0=int(input("enter x1: "))
        col0=int(input("enter y1: "))
        print("enter ending point coordinates (x2,y2): ")
        row1=int(input("enter x2: "))
        col1=int(input("enter y2: "))
        
        if (row0==row1 and abs(col0-col1)==1):
            self.game.line_type=0#line type-horizontal
            if self.game.hor_line_matrix[row0,col0]==0:
                self.game.hor_line_matrix[row0,col0]=1
            else:
                self.game.is_right_move=False#wrong input


        elif(col0==col1 and abs(row0-row1)==1):
            self.game.line_type=1#line type-vertical
            if self.game.ver_line_matrix[row0,col0]==0:
                self.game.ver_line_matrix[row0,col0]=1
            else:
                self.game.is_right_move=False#wrong input
        else:
            print("heyyyy")
            self.game.is_right_move=False#wrong input

        self.game.Count_points(row0,col0)
        