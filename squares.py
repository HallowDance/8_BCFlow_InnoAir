import matplotlib.pyplot as plt
import numpy as np
import random


def mapPlot():

    plt.axes()

    gridSize=50

    for m in range(gridSize):
        for n in range(gridSize):
            #color_Num='#'+(str(random.randint(0,9))+str(random.randint(0,9)))+(str(random.randint(0,9))+str(random.randint(0,9)))+(str(random.randint(0,9))+str(random.randint(0,9)))
            color_Num=(random.random(), random.random(), random.random())
            rectangle = plt.Rectangle((n,m), 1, 1, fc=color_Num ,ec=color_Num)
            plt.gca().add_patch(rectangle)

    #rectangle = plt.Rectangle((0,1), 1, 1, fc='blue',ec="red")
    #plt.gca().add_patch(rectangle)


    plt.axis('scaled')
    plt.show()
