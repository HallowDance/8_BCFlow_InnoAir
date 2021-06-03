import matplotlib.pyplot as plt
import numpy as np
import random


def mapPlot(squares,linesDictSquares,gridSize):

    plt.axes()
    for m in range(gridSize):
        for n in range(gridSize):
            #color_Num='#'+(str(random.randint(0,9))+str(random.randint(0,9)))+(str(random.randint(0,9))+str(random.randint(0,9)))+(str(random.randint(0,9))+str(random.randint(0,9)))
            color_Num=(min(1,1.5*squares[m*gridSize+n]/100.0),
                    min(0.9,2.5*(100-squares[m*gridSize+n])/100.0), 0.0)
            rectangle = plt.Rectangle((n,m), 1, 1, fc=color_Num ,ec='white')
            plt.gca().add_patch(rectangle)

            ypoints1 = np.array([3.5,2.5,3.5,2.5,1.5,2.5,3.5,4.5,5.5,6.5,5.5,4.5])
            ypoints2 = np.array([5,0,5,10,8,8,6,9,1,2,2])

    #rectangle = plt.Rectangle((0,1), 1, 1, fc='blue',ec="red")
    #plt.gca().add_patch(rectangle)
#comment
    plt.plot(ypoints1, color = 'blue')
    plt.plot(ypoints2, color = 'black')
    plt.axis('scaled')
    plt.show()
