# Interpolation function for squares that contain no data
# This can be imporved/tweeked further
# It DOES NOT interpolate the edges correctly
import numpy as np

def interpolate(gridSize,squareNumber,pollution):
    #average over neighbours
    neighbours=[]
    for j in range(3):
        for i in range(3):
            neighbours.append(squareNumber+gridSize+i-2+j-2)
    counter=0
    value=0
    for square in neighbours:
        if not np.isnan(pollution[square]):
            value+=pollution[square]
            counter+=1.
    #not taking the average but assuming more pollution
    #in tests it would seem that this behaviour replicates
    #reallity better
    value=min(100,1.3*value/counter)
    return(value)
