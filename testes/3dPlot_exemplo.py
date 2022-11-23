from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    ar = np.sin(np.sqrt(x**2 + y**2))
    return ar
    
x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)

X,Y = np.meshgrid(x,y)

Z = f(X,Y)

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='binary')
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='winter',edgecolor='none')
ax.set_title('Gráfico de superfície no Espaço 3D', fontsize=18)
ax.set_xlabel('Eixo X',fontsize=15)
ax.set_ylabel('Eixo Y',fontsize=15)
ax.set_zlabel('Eixo Z',fontsize=15)
ax.view_init(60,45)

plt.show()
