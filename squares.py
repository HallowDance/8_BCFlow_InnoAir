import matplotlib.pyplot as plt
import numpy as np
import random


def mapPlot(squares,gridSize,dataInterpolated,linesDictSquares):
    for m in range(gridSize):
        for n in range(gridSize):
            #check if square has a defined pollution level
            if not np.isnan((squares[m*gridSize+n])):
                #assign color
                color_Num=(min(1,1.5*squares[m*gridSize+n]/100.0), min(0.9,2.5*(100-squares[m*gridSize+n])/100.0), 0.0)
                #draw square
                rectangle = plt.Rectangle((n,m), 1, 1, fc=color_Num ,ec='white')
            else:
                #handle missing data points before interpolation. set color to white
                rectangle = plt.Rectangle((n,m), 1, 1, fc='white', ec='white')
                #print("no data, visualising as white square")
            plt.gca().add_patch(rectangle)
<<<<<<< HEAD
    colorSetBus=['black', 'blue', 'yellow', 'teal']
=======
    plt.axis('scaled')
    plt.axis('off')
>>>>>>> 222f11ee638d06ac7cd275cd2563995528a38cb3
    for key in linesDictSquares:
        a = linesDictSquares[key]
        x1 = [int(i)%gridSize+0.5 for i in a]
        y1 = [int(int(i)/gridSize)+0.5 for i in a]
        plt.plot(x1, y1)
    if(dataInterpolated):
        plt.savefig('img/interpolated.png')
    else:
        plt.savefig('img/pre-interpolated.png')
