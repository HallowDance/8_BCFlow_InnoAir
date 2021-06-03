# In this file we take the mock data structures and give a score to each bus
# line. The score depends on the sum of pollution scores of all the squares the
# line traverses.

# IMPORTS
import numpy as np
from squares import mapPlot
from interpolate import interpolate

# GLOBAL PARAMETERS
gridSize=10

pollutionValues=np.zeros(gridSize**2)
linesDictSquares={} #dictionary containing line names as keys, and routes as values
linesDictPolution={} #dictionary containing line names as keys, and pollution as values
noDataSquares=[] # to contain squares with no data (for interpolation)


# Get bus lines into a dict
with open("buslines.dat", "r") as f:
    for line in f:
        li=line.strip()
        if not li.startswith('#'):
            linesDictSquares[li.split(' ')[0]]=li.split(' ')[1:]


# Get pollution info on each
with open("squares.dat", "r") as f:
    i=0
    for line in f:
        li=line.strip()
        if not li.startswith('#'):
            try:
                #if there exeists a data point for that square
                pollutionValues[i]=li
            except:
                #if it doesn't exist insert NaN and save the index of the
                #square. We will assume an intepolated value later
                if(li==''):
                    noDataSquares.append(i)
                    pollutionValues[i]=np.nan
            i+=1


#plot map with initial pollution levels
mapPlot(pollutionValues, gridSize)

#call interpolation function for missing data
for square in noDataSquares:
    pollutionValues[square]=interpolate(gridSize,square,pollutionValues)

#plot map with interpolations
mapPlot(pollutionValues, gridSize)

# evaluate pollution levels on each line (this has to be reimplemented better)
for key in linesDictSquares:
    linePollutionLevel=0
    squaresList=linesDictSquares[key]
    for element in squaresList:
        #check if element is a number
        if not np.isnan(pollutionValues[int(element)]):
            linePollutionLevel+=pollutionValues[int(element)]
        #else we assume it's zero
    linesDictPolution[key]=linePollutionLevel


#print(linesDictPolution)
