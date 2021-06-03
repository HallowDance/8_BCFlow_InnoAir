# In this file we take the mock data structures and give a score to each bus
# line. The score depends on the sum of pollution scores of all the squares the
# line traverses.

import numpy as np
from squares import mapPlot

gridSize=10
pollutionValues=np.zeros(gridSize**2)

# get bull lines
with open("buslines.dat", "r") as f:
    for line in f:
        li=line.strip()
        if not li.startswith('#'):
            print(line.rstrip())

# get pollution info on each 
with open("squares.dat", "r") as f:
    i=0
    for line in f:
        li=line.strip()
        if not li.startswith('#'):
            print(li)
            pollutionValues[i]=li
            i+=1

mapPlot(pollutionValues,gridSize)
