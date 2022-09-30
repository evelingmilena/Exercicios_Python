import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import csv
import re

x = []
y = []
z = []

xN = np.arange(0,np.pi,0.01)
yN = np.arange(0,np.pi,0.01)

with open ('tabelaLaplace.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
f = interpolate.interp2d(x,y,z, kind = "linear")

zN = f(xN,yN)

plt.plot(zN)
plt.show()
