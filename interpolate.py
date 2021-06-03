# Interpolation function for squares that contain no data
# This can be imporved/tweeked further
import numpy

def interpolate(gridsize,squareNumber,pollution):
    #average over neighbours
    value= numpy.average((pollution[squareNumber+gridsize],pollution[squareNumber+gridsize-1],pollution[squareNumber+gridsize+1],pollution[squareNumber-gridsize],pollution[squareNumber-gridsize-1],pollution[squareNumber-gridsize+1],pollution[squareNumber+1],pollution[squareNumber-1]))
    return(value)

