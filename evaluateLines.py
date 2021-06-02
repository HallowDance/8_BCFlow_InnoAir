# In this file we take the mock data structures and give a score to each bus
# line. The score depends on the sum of pollution scores of all the squares the
# line traverses.

import numpy as np
from squares import mapPlot

with open("buslines.dat", "r") as f:
    for line in f:
        li=line.strip()
        if not li.startswith('#'):
            print(line.rstrip())

mapPlot()
