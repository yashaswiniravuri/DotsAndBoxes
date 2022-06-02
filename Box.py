from numpy import place
from PlayGame import *
from Chain import *

class Box():
    def __init__(self,PlayGame):
        self.game=PlayGame
        
    def check_box(self):
        self.found_box=False
        #check if any box can be made:
        for x,y in (self.game.hor_moves):
            if self.found_box==True:
                    break
            #two kinds of boxes: upper and lower
            #lower box:            
            if x>=0 and x<self.game.no_of_dots-1 and not self.found_box:
                is_ver=False
                is_hor=False
                value=[0,0]
                count=0
                if self.game.ver_line_matrix[x,y]==0:
                    count+=1
                    is_ver=True
                    value=[x,y]
                if self.game.hor_line_matrix[x+1,y]==0:
                    count+=1
                    is_hor=True
                    value=[x+1,y]
                if self.game.ver_line_matrix[x,y+1]==0:
                    count+=1
                    is_ver=True
                    value=[x,y+1]
                if count==1:
                    self.make_box(value[0],value[1],is_ver,is_hor)
            #upper box:
            if x<=self.game.no_of_dots-1 and x>0 and not self.found_box:
                is_ver=False
                is_hor=False
                value=[0,0]
                count=0
                if self.game.hor_line_matrix[x-1,y]==0:
                    count+=1
                    is_hor=True
                    value=[x-1,y]
                if self.game.ver_line_matrix[x-1,y]==0:
                    count+=1
                    is_ver=True
                    value=[x,y+1]
                if self.game.ver_line_matrix[x-1,y+1]==0:
                    count+=1
                    is_ver=True
                    value=[x,y+1]
                if count==1:
                    self.make_box(value[0],value[1],is_ver,is_hor)
            
        if self.found_box==False:
            for x,y in (self.game.ver_moves):
                if self.found_box==True:
                    break
                #right box:
                if y>=0 and y<self.game.no_of_dots-1 and not self.found_box:
                    is_ver=False
                    is_hor=False
                    value=[0,0]
                    count=0
                    if self.game.ver_line_matrix[x,y+1]==0:
                        count+=1
                        is_ver=True
                        value=[x,y+1]
                    if self.game.hor_line_matrix[x,y]==0:
                        count+=1
                        is_hor=True
                        value=[x,y]
                    if self.game.hor_line_matrix[x+1,y]==0:
                        count+=1
                        is_hor=True
                        value=[x+1,y]
                    if count==1:
                        self.make_box(value[0],value[1],is_ver,is_hor)
                #left box:
                elif y<=self.game.no_of_dots-1 and y>0 and not self.found_box:
                    is_ver=False
                    is_hor=False
                    value=[0,0]
                    count=0
                    if self.game.hor_line_matrix[x,y-1]==0:
                        count+=1
                        is_hor=True
                        value=[x,y-1]
                    if self.game.ver_line_matrix[x,y-1]==0:
                        count+=1
                        is_ver=True
                        value=[x,y-2]
                    if self.game.hor_line_matrix[x+1,y-1]==0:
                        count+=1
                        is_hor=True
                        value=[x+1,y-1]
                    if count==1:
                        self.make_box(value[0],value[1],is_ver,is_hor)
    
    def make_box(self,r,c,is_ver,is_hor):
        #a box can be drawn with 'value' coordinates.
        if is_ver and not self.found_box:
            self.game.ver_line_matrix[r,c]=1
            self.game.ver_moves.append([r,c])
            x,y,mode,value=self.game.chain.is_chain(r,c,1)
            if mode==1:
                self.game.chain.append(x,y,value)
            elif mode==2:
                self.game.chain.remove(x,y,value)
            #self.game.chain.update_chain(r,c,1)
            self.game.points[self.game.player]+=1
            self.found_box=True
        if is_hor and not self.found_box:
            self.game.hor_line_matrix[r,c]=1
            self.game.hor_moves.append([r,c])
            #self.game.chain.update_chain(r,c,0)
            x,y,mode,value=self.game.chain.is_chain(r,c,0)
            if mode==1:
                self.game.chain.append(x,y,value)
            elif mode==2:
                self.game.chain.remove(x,y,value)
            self.game.points[self.game.player]+=1
            self.found_box=True
        else: self.found_box=False