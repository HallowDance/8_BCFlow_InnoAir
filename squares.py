import matplotlib.pyplot as plt
import numpy as np
import random


def mapPlot(squares,gridSize):
    plt.axes()
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
    plt.axis('scaled')
    plt.show()
