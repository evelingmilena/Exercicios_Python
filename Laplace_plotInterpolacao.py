import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import csv

x = []
y = []
z = []

xN = np.arange(0,np.pi,0.1)
yN = np.arange(0,np.pi,0.1)

with open ('novatabelaLaplace.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
f = interpolate.interp2d(x,y,z, kind = "linear")

zN = f(xN,yN)

fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

X, Y = np.meshgrid(xN, yN)
surf = ax.plot_surface(X, Y, zN, cmap = plt.cm.cividis)
plt.show()
