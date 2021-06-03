#prints out less complete data

import random as rd

lines=[]
f = open("data/squares_full.dat", "r")
for line in f:
    lines.append(line.strip())
f.close()
lines_new = []
for index,line in enumerate(lines):
    if rd.random()>0.85:
        lines_new.append('')
    else:
        lines_new.append(line)

for line in lines_new:
    print(line)
