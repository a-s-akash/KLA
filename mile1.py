import math
import numpy as np
def final(max,min,n):
    r = np.linspace(min, max, n)
    return r
def points(dia, ang):
    z = math.radians(ang)
    x = (dia/2) * math.cos(z)
    y = (dia/2) * math.sin(z)
    return x, y
for ww in range(4):
    qloc = open(f"Workshop2024//Milestone1//Input//Testcase{ww+1}.txt",'r')
    x = []
    for i in qloc:
        j = (i.split(":"))
        x.append(int(j[1]))
    dia = x[0]
    no = x[1]
    ang = x[2]
    x,y = points(dia,ang)
    maxpoint = (x,y)
    minpoint = (x*-1,y*-1)
    x = final(maxpoint,minpoint,no)
    aloc = open(f"Workshop2024//Milestone1//Input//output{ww+1}.txt",'w')
    for i in x:
        aloc.write(f'({i[0]},{i[1]})\n')
