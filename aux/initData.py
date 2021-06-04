# Creates an array of clustered initial pollution data
# Seems to work sufficiently well, although performance 
# might not be optimal for large grids of data


import random as rd
import numpy as np
a = np.zeros((30,30))

for i in range(29):
    for j in range(29):
        print
        if rd.random()>0.9:
            a[i][j]=100

for count in range(5):
    for i in range(29):
        for j in range(29):
            a[i][j]=min(100,(rd.random()+0.5)*(a[i][j]+a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1])/4.0)

b = np.zeros(900)

for i in range(29):
    for j in range(29):
        b[30*i+j]=a[i][j]

for row in b:
    print(row)
