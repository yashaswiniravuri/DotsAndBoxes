
import math
from re import M
import numpy as np
from PlayGame import *
from computer_game import *
from human_game import *
class Chain():
    def __init__(self,PlayGame):
        self.game=PlayGame
        #0-no chain
        #1-hor chain
        self.hor_chain_length=[]
        self.ver_chain_length=[]
    
    def is_chain(self,r,c,type):
        n=self.game.no_of_dots
        mode=0
        if type==0:
            if r>=1:#check if there is already a chain up
                if self.game.chain_list[r-1,c]==0 and self.game.ver_line_matrix[r-1,c]==0 and self.game.ver_line_matrix[r-1,c+1]==0 and self.game.hor_line_matrix[r-1,c]==1:
                    mode=1
                    return r-1,c,mode,1
                if self.game.chain_list[r-1,c]!=0:
                    mode=2
                    return r-1,c,mode,0
            if r<=n-2:#check if there is already a chain down
                if self.game.chain_list[r,c]==0 and self.game.hor_line_matrix[r+1,c]==1 and self.game.ver_line_matrix[r,c]==0 and self.game.ver_line_matrix[r,c+1]==0:
                    mode=1
                    return r,c,mode,1
                if self.game.chain_list[r,c]!=0:
                    mode=1
                    return r,c,mode,0
        if type==1:
            if c>=1:
                if self.game.chain_list[r,c-1]==0 and self.game.ver_line_matrix[r,c-1]==1 and self.game.hor_line_matrix[r,c-1]==0 and self.game.hor_line_matrix[r-1,c-1]==0:
                    mode=1
                    return r,c-1,mode,2
                if self.game.chain_list[r,c-1]!=0:
                    return r-1,c,mode,1
            if c<=n-2:
                if self.game.chain_list[r,c]==0 and self.game.ver_line_matrix[r,c+1]==1 and self.game.hor_line_matrix[r,c]==0 and self.game.hor_line_matrix[r-1,c]==0:
                    mode=1
                    return r,c,mode,2
                if self.game.chain_list[r,c]!=0:
                    return r,c,mode,1
        return r,c,mode,0

    def append(self,x,y,value):
        self.game.chain_list[x,y]=value
    
    def remove(self,x,y,value):
        self.game.chain_list[x,y]=0

    def make_chain(self):
        is_made_chain=False
        mode=0
        for x,y in self.game.hor_moves:
            if x>=0 and x<self.game.no_of_dots-1 and not is_made_chain:
                r,c,mode,value=self.game.chain.is_chain(x+1,y,0)
                if mode==1 and not is_made_chain and self.game.chain_list[r,c]==0 and self.game.hor_line_matrix[x+1,y]==0:
                    self.game.hor_line_matrix[x+1,y]=1
                    self.game.hor_moves.append([x+1,y])
                    self.game.chain.append(r,c,value)
                    is_made_chain=True
            elif x<=self.game.no_of_dots-1 and x<=1 and not is_made_chain:
                r,c,mode,value=self.game.chain.is_chain(x-1,y,0)
                if mode==1 and not is_made_chain and self.game.chain_list[r,c]==0 and self.game.hor_line_matrix[x-1,y]==0:
                    self.game.hor_line_matrix[x-1,y]=1
                    self.game.hor_moves.append([x-1,y])
                    self.game.chain.append(r,c,value)
                    is_made_chain=True

        for x,y in self.game.ver_moves:
            if y>=0 and y<self.game.no_of_dots-1 and not is_made_chain:
                r,c,mode,value=self.game.chain.is_chain(x,y+1,1)
                if mode==1 and not is_made_chain and self.game.chain_list[r,c]==0 and self.game.ver_line_matrix[x,y+1]==0:
                    self.game.ver_line_matrix[x,y+1]=1
                    self.game.ver_moves.append([x,y+1])
                    self.game.chain.append(r,c,value)
                    is_made_chain=True
            elif y<=self.game.no_of_dots-1 and y<=1 and not is_made_chain:
                r,c,mode,value=self.game.chain.is_chain(x,y-1,1)
                if mode==1 and not is_made_chain and self.game.chain_list[r,c]==0 and self.game.ver_line_matrix[x,y-1]==0:
                    self.game.ver_line_matrix[x,y-1]=1
                    self.game.ver_moves.append([x,y-1])
                    self.game.chain.append(r,c,value)
                    is_made_chain=True
        if is_made_chain==False:
            self.select_random()
    
    def close_chain(self):
        self.get_chain_lengths()
        start,end,length,type=self.get_min_length()
        is_updated=False
        if length!=0:
            x1=start[0]
            y1=start[1]
            x2=end[0]
            y2=end[1]
            if type==0:
                if self.game.ver_line_matrix[x1,y1]==0 and not is_updated:
                    self.game.ver_line_matrix[x1,y1]=1
                    self.game.ver_moves.append([x1,y1])
                    self.game.chain.remove(x1,y1,1)
                    is_updated=True
                elif self.game.ver_line_matrix[x2,y2+1]==0 and not is_updated:
                    self.game.ver_line_matrix[x2,y2+1]=1
                    self.game.ver_moves.append(x2,y2+1)
                    self.game.chain.remove(x2,y2,1)
                    is_updated=True
            if type==1:
                if self.game.hor_line_matrix[x1,y1]==0 and not is_updated:
                    self.game.hor_line_matrix[x1,y1]=1
                    self.game.hor_moves.append([x1,y1])
                    self.game.chain.remove(x1,y1,2)
                    is_updated=True
                elif self.game.hor_line_matrix[x2+1,y2]==0 and not is_updated:
                    self.game.hor_line_matrix[x2+1,y2]=1
                    self.game.hor_moves.append([x2+1,y2])
                    self.game.chain.remove(x2,y2,2)
                    is_updated=True
        if not is_updated: 
            made_chain=self.make_chain()


    def extend_chain(self):
        self.get_chain_lengths()
        start,end,length,type=self.get_max_length()
        is_updated=False
        if length==0:
            self.close_chain()
            is_updated=True
        else:
            x1=start[0]
            y1=start[1]
            x2=end[0]
            y2=end[1]
            if type==0 and not is_updated:
                #make left horizontal chain
                if y1>=1:
                    if self.game.hor_line_matrix[x1,y1-1]==1 and self.game.hor_line_matrix[x1+1,y1-1]==0 and not is_updated:
                        self.game.hor_line_matrix[x1+1,y1-1]=1
                        self.game.hor_moves.append([x1+1,y1-1])
                        self.game.chain.append(x1,y1-1,1)
                        is_updated=True
                    elif self.game.hor_line_matrix[x1,y1-1]==0 and self.game.hor_line_matrix[x1+1,y1-1]==1 and not is_updated:
                        self.game.hor_line_matrix[x1,y1-1]=1
                        self.game.hor_moves.append([x1,y1-1])
                        self.game.chain.append(x1,y1-1,1)
                        is_updated=True
                #make right horizontal chain
                if y2<=self.game.no_of_dots-3:
                    if self.game.hor_line_matrix[x2,y2+1]==0 and self.game.hor_line_matrix[x2+1,y2+1]==1 and not is_updated:
                        self.game.hor_line_matrix[x2,y2+1]=1
                        self.game.hor_moves.append([x2,y2+1])
                        self.game.chain.append(x2,y2+1,1)
                        is_updated=True
                    elif self.game.hor_line_matrix[x2,y2+1]==1 and self.game.hor_line_matrix[x2+1,y2+1]==0 and not is_updated:
                        self.game.hor_line_matrix[x2+1,y2+1]=1
                        self.game.hor_moves.append([x2+1,y2+1])
                        self.game.chain.append(x2,y2+1,1)
                        is_updated=True
                #extend chains
                #left
                if y1>=1:
                    if self.game.hor_line_matrix[x1,y1-1]==0 and self.game.hor_line_matrix[x1+1,y1-1]==0 and not is_updated:
                        self.game.hor_line_matrix[x1,y1-1]=1
                        self.game.hor_moves.append([x1,y1-1])
                        is_updated=True
                if y2<=self.game.no_of_dots-3:
                    #right
                    if self.game.hor_line_matrix[x2,y2+1]==0 and self.game.hor_line_matrix[x2+1,y2+1]==0 and not is_updated:
                        self.game.hor_line_matrix[x2,y2+1]=1
                        self.game.hor_moves.append([x2,y2+1])
                        is_updated=True
                
            if type==1 and not is_updated:
                #make upper vertical chain
                if x1>=1:
                    if self.game.ver_line_matrix[x1-1,y1]==0 and self.game.ver_line_matrix[x1-1,y1+1]==1  and not is_updated:
                        self.game.ver_line_matrix[x1-1,y1]=1
                        self.game.ver_moves.append([x1-1,y1])
                        self.game.chain.append(x1-1,y1,2)
                        is_updated=True
                    elif self.game.ver_line_matrix[x1-1,y1]==1 and self.game.ver_line_matrix[x1-1,y1+1]==0 and not is_updated:
                        self.game.ver_line_matrix[x1-1,y1+1]=1
                        self.game.ver_moves.append([x1-1,y1+1])
                        self.game.chain.append(x1-1,y1,2)
                        is_updated=True
                #make lower vertical chain
                if x2<=self.game.no_of_dots-3:
                    if self.game.ver_line_matrix[x2+1,y2]==0 and self.game.ver_line_matrix[x2+1,y2+1]==1 and not is_updated:
                        self.game.ver_line_matrix[x2+1,y2]=1
                        self.game.ver_moves.append([x2+1,y2])
                        self.game.chain.append(x2+1,y2,2)
                        is_updated=True
                    elif self.game.ver_line_matrix[x2+1,y2]==1 and self.game.ver_line_matrix[x2+1,y2+1]==0 and not is_updated:
                        self.game.ver_line_matrix[x2+1,y2+1]=1
                        self.game.ver_moves.append([x2+1,y2+1])
                        self.game.chain.append(x2+1,y2,2)
                        is_updated=True
                if x1>=1:
                #extend chains upper and lower:
                    if self.game.ver_line_matrix[x1-1,y1]==0 and self.game.ver_line_matrix[x1-1,y1+1]==0 and not is_updated:
                        self.game.ver_line_matrix[x1-1,y1]=1
                        self.game.ver_moves.append([x1-1,y1])
                        is_updated=True
                if x2<=self.game.no_of_dots-3:
                    if self.game.ver_line_matrix[x2+1,y2]==0 and self.game.ver_line_matrix[x2+1,y2+1]==0 and not is_updated:
                        self.game.ver_line_matrix[x2+1,y2]=1
                        self.game.ver_moves.append([x2+1,y2])
                        is_updated=True

        if not is_updated:
            self.close_chain()

    def get_chain_lengths(self):
        hor_chains=np.argwhere([self.game.chain_list==1])
        ver_chains=np.argwhere([self.game.chain_list.transpose()==2])
        if hor_chains.shape[0]!=0:
            len=1
            start=[hor_chains[0][1],hor_chains[0][2]]
            end=[hor_chains[0][1],hor_chains[0][2]]
            self.hor_chain_length=[]
            if hor_chains.shape[0]<2:
                self.hor_chain_length.append([start,end,len])
            else:
                for i in range(1,hor_chains.shape[0]):
                    if(abs(hor_chains[i][1] - hor_chains[i-1][1]) == 0 and abs(hor_chains[i][2] - hor_chains[i-1][2]) == 1):
                        len+=1
                        end=[hor_chains[i][1],hor_chains[i][2]]
                    else:
                        self.hor_chain_length.append([start,end,len])
                        start=[hor_chains[i][1],hor_chains[i][2]]
                        end=[hor_chains[i][1],hor_chains[i][2]]
                        len=1
                    if i==hor_chains.shape[0]-1:
                            self.hor_chain_length.append([start,end,len])
        if ver_chains.shape[0]!=0:
            self.ver_chain_length=[]
            len=1
            start=[ver_chains[0][2],ver_chains[0][1]]
            end=[ver_chains[0][2],ver_chains[0][1]]
            if ver_chains.shape[0]<2:
                self.ver_chain_length.append([start,end,len])
            else:
                for i in range(1,ver_chains.shape[0]):
                    if(abs(ver_chains[i][1] - ver_chains[i-1][1]) == 0 and abs(ver_chains[i][2] - ver_chains[i-1][2]) == 1):
                        len+=1
                        end=[ver_chains[i][2],ver_chains[i][1]]
                    else:
                        self.ver_chain_length.append([start,end,len])
                        start=[ver_chains[i][2],ver_chains[i][1]]
                        end=[ver_chains[i][2],ver_chains[i][1]]
                        len=1
                    if i==ver_chains.shape[0]-1:
                            self.ver_chain_length.append([start,end,len])

    def get_min_length(self):
        min_hor_start=[]
        min_hor_end=[]
        min_hor_len=math.inf
        min_ver_start=[]
        min_ver_end=[]
        min_ver_len=math.inf
        if len(self.hor_chain_length)!=0:
            for chain in self.hor_chain_length:
                start=chain[0]
                end=chain[1]
                length=chain[2]
                if length<min_hor_len:
                    min_hor_len=length
                    min_hor_start=start
                    min_hor_end=end
        if len(self.ver_chain_length)!=0:
            for chain in self.ver_chain_length:
                start=chain[0]
                end=chain[1]
                length=chain[2]
                if length<min_ver_len:
                    min_ver_len=length
                    min_ver_start=start
                    min_ver_end=end
        if min_hor_len<=min_ver_len:
            return min_hor_start,min_hor_end,min_hor_len,0
        else:
            return min_ver_start,min_ver_end,min_ver_len,1              

    def get_max_length(self):
        max_hor_start=[]
        max_hor_end=[]
        max_hor_len=0
        max_ver_start=[]
        max_ver_end=[]
        max_ver_len=0
        if len(self.hor_chain_length)!=0:
            for chain in self.hor_chain_length:
                start=chain[0]
                end=chain[1]
                length=chain[2]
                if length>max_hor_len and length!=self.game.no_of_dots-1:
                    max_hor_len=length
                    max_hor_start=start
                    max_hor_end=end
        if len(self.ver_chain_length)!=0:
            for chain in self.ver_chain_length:
                start=chain[0]
                end=chain[1]
                length=chain[2]
                if length>max_ver_len and length!=self.game.no_of_dots-1:
                    max_ver_len=length
                    max_ver_start=start
                    max_ver_end=end
        if max_hor_len>=max_ver_len:
            return max_hor_start,max_hor_end,max_hor_len,0
        else:
            return max_ver_start,max_ver_end,max_ver_len,1

    def select_random(self):
        updated=False
        if (self.game.hor_line_matrix==0).any():
            myarray=np.argwhere(self.game.hor_line_matrix==0)
            i,j=myarray[0]
            self.game.hor_line_matrix[i,j]=1  
            self.game.hor_moves.append([i,j])
            if self.game.is_box(i,j,0):
                print("BOX MADE")
                self.game.points[self.game.player]+=1
            else:
                x,y,mode,value=self.game.chain.is_chain(i,j,0)
                if mode==1:
                    self.game.chain.append(x,y,value)
                elif mode==2:
                    self.game.chain.remove(x,y,value)
            return True
        elif (self.game.ver_line_matrix==0).any() and not updated:
            myarray=np.argwhere(self.game.ver_line_matrix==0)
            i,j=myarray[0]
            self.game.ver_line_matrix[i,j]=1
            self.game.ver_moves.append([i,j])
            if self.game.is_box(i,j,1):
                print("BOX MADE")
                self.game.points[self.game.player]+=1
            else:
                x,y,mode,value=self.game.chain.is_chain(i,j,1)
                if mode==1:
                    self.game.chain.append(x,y,value)
                elif mode==2:
                    self.game.chain.remove(x,y,value)
            return True
        return False