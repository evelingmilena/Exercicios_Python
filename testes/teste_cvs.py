import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import csv

x = []
y = []

xN = np.arange(0,np.pi,0.1)
with open('valorw.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
f = InterpolatedUnivariateSpline(x, y, k=1)
res = f.integral(0,np.pi)
print(res)
plt.plot(f(xN))
plt.xlabel('x')
plt.ylabel('y')
plt.show()
