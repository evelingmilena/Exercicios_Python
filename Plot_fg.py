import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Análise das matrizes A e B

x = np.linspace(1,20,50)
y = np.linspace(-0.9,0.9,50)
alpha = 0.2

def fg(x,y,alpha):
    a = (x**2)-(y**2) + (alpha**2)*(x**2-1)
    b = 4*(alpha**2)*(x**2)*(1-(y**2))
    c = 4*(alpha**2)*(y**2)*((x**2)-1)
    d = (x**2)-(y**2) + (alpha**2)*((x**2)-1)**2
    e = (1+(alpha**2))*((x**2)-(y**2))
 
    function_f = ((a**2)+b)/(d**2-c)
    function_g = ((a**2)+b)**2/(e**4)

    return function_f,function_g

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

X, Y = np.meshgrid(x, y)
Z,H = fg(X,Y,alpha)
surf = ax.plot_surface(X, Y, H, cmap = plt.cm.cividis)
plt.show()
