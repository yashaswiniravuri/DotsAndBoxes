import tkinter as tk
import pandas as pd


def is_box(r,c):
    if line_type==0:
        if r!=0 or r==n_dots-1:
            if rows.iloc[r-1,c]!=0 and cols.iloc[r-1,c]!=0 and cols.iloc[r-1,c+1]!=0:
                return True
        else:
            if(rows.iloc[r+1,c]!=0 and cols.iloc[r,c]!=0 and cols.iloc[r,c+1]!=0):
                return True
        
    if line_type==1:
        
        if c!=0 or c==n_dots-1:
            if cols.iloc[r,c-1]!=0 and rows.iloc[r,c-1]!=0 and rows.iloc[r+1,c-1]!=0:
                return True
        else:
            if (cols.iloc[r,c+1]!=0 and rows.iloc[r,c]!=0 and rows.iloc[r+1,c]!=0):
                return True
    return False


line_type=0#0 for rows and 1 for columns
mybool=True#wrong clicks
dots=[]
n_dots=2#size of one side to the dot matrix
while(n_dots<3):
    n_dots=int(input("Enter the matrix size: "))
dots=[[0 for y in range(n_dots)] for x in range (n_dots)]
dots=pd.DataFrame(dots)#dots array
rows=[[0 for y in range(n_dots-1)] for x in range (n_dots)]
rows=pd.DataFrame(rows)#row line array
cols=[[0 for y in range(n_dots)] for x in range (n_dots-1)]
cols=pd.DataFrame(cols)#col line array
player1=True
player1_points=0
player2_points=0
while(rows.eq(0).any().any() and cols.eq(0).any().any()):
    row0=int(input("enter row0: "))
    col0=int(input("enter col0: "))
    row1=int(input("enter row1: "))
    col1=int(input("enter col1: "))
    print(rows)
    print(cols)
    if (row0==row1):
        line_type=0
        rows.iloc[row0,col0]=1
    elif (col0==col1):
        line_type=1
        cols.iloc[row0,col0]=1
    else:
        mybool=False
    if mybool:
        if is_box(row0,col0):
            if player1==True:
                player1_points+=1
                player1=False
            else:
                player2_points+=1
                player1=True
        player1=not player1


if(player1_points>player2_points):
    print("WINNER: PLAYER1")
elif(player1_points<player2_points):
    print("WINNER: PLAYER2")
else:
    print("IT'S A TIE!")