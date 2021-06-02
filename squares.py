import matplotlib.pyplot as plt
import numpy as np
import random


def mapPlot(squares,gridSize):

    plt.axes()
    for m in range(gridSize):
        for n in range(gridSize):
            #color_Num='#'+(str(random.randint(0,9))+str(random.randint(0,9)))+(str(random.randint(0,9))+str(random.randint(0,9)))+(str(random.randint(0,9))+str(random.randint(0,9)))
            color_Num=(min(1,1.5*squares[m*gridSize+n]/100.0),
                    min(0.9,2.5*(100-squares[m*gridSize+n])/100.0), 0.0)
            rectangle = plt.Rectangle((n,m), 1, 1, fc=color_Num ,ec='white')
            plt.gca().add_patch(rectangle)

    #rectangle = plt.Rectangle((0,1), 1, 1, fc='blue',ec="red")
    #plt.gca().add_patch(rectangle)


    plt.axis('scaled')
    plt.show()
