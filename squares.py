import matplotlib.pyplot as plt
import numpy as np
import random


def mapPlot(squares,gridSize,linesDictSquares, linesDictPollution, printNumber, noDraw):
    #don't draw anything
    if(noDraw):
        return
    #proceed as normal
    else:
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
                plt.gca().add_patch(rectangle)
        plt.axis('scaled')
        plt.axis('off')
        #plotting bus lines. each has it's own distinct color
        colorList=['Purple','black','navy','grey','brown']
        for index, key in enumerate(linesDictSquares):
            a=linesDictSquares[key]
            x1=[int(i)%gridSize+0.5 for i in a]
            y1=[int(int(i)/gridSize)+0.5 for i in a]
            plt.plot(x1, y1, linewidth=3.5, color='white')
            plt.plot(x1, y1, linewidth=2.5, color=colorList[index])

        #printing legend
        labels=[]
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        for key in linesDictPollution:
            labels.append(key+': '+str(linesDictPollution[key]))

        if not labels:
            labels='[\'Purple: 0000\', \'Black: 0000\', \'Blue: 0000\', \'Green: 0000\', \'Brown: 0000\']'
        text=plt.text(1.5,-1,labels ,fontsize=6,
        horizontalalignment='left', verticalalignment='top',
                bbox=props)
        #finalizing and saving pictures
        plt.savefig('img/'+str(printNumber)+'-bcflow.png',
                    bbox_inches='tight', dpi=200)
        text.set_text('')
