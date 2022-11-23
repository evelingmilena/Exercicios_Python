import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 50
h = np.pi/N
w = 1.1
N_it = 10000
matrizU = np.zeros((N+1,N+1),float)
matrizU_exata = np.zeros((N+1,N+1),float)
matrizU_erro = np.zeros((N+1,N+1),float)

#Atribuindo condicao de contorno x = pi. As outras automaticamente são nulas. Portanto, não precisa ser atualizado, pois a matriz foi declarada nula no início.
for j in range(N+1):
    matrizU[N][j] = np.sinh(np.pi)*np.sin(j*h)

#print(matrizU)

#Método SOR
for k in range(N_it):
    for i in range(1,N):
        for j in range(1,N):
           matrizU[i][j] = 0.25 * w * ( matrizU[i+1][j] + matrizU[i-1][j] + matrizU[i][j+1] + matrizU[i][j-1] ) + ( 1. - w ) * matrizU[i][j]

#print(matrizU)    

erro_quad = 0.0
for i in range(N+1):
    for j in range(N+1):
        matrizU_exata[i][j] = np.sinh(i*h)*np.sin(j*h)
        matrizU_erro[i][j] = matrizU_exata[i][j] - matrizU[i][j]
        erro_quad += matrizU_erro[i][j]**2
		
#print(matrizU)
#print("\nA matriz exata e:", matrizU_exata)
print("\nA média do erro quadrático é:", erro_quad/N**2)


x  = range(0,N+1)
y = range(0,N+1)
X,Y = np.meshgrid(x,y) 
def f():
    z = matrizU[X,Y]  
    return z;

Z = f()

def g():
    r = matrizU_exata[X,Y]
    return r
    
R = g()

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='binary')
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='autumn',edgecolor='none')
ax.set_title('Equação de Laplace - Solução Numérica', fontsize=18)
ax.set_xlabel('Eixo X',fontsize=15)
ax.set_ylabel('Eixo Y',fontsize=15)
ax.set_zlabel('Eixo Z',fontsize=15)
ax.view_init(60,45)

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,R,50,cmap='binary')
ax.plot_surface(X,Y,R,rstride=1,cstride=1,cmap=  'autumn',edgecolor='none')
ax.set_title('Equação de Laplace - Solução Exata', fontsize=18)
ax.set_xlabel('Eixo X',fontsize=15)
ax.set_ylabel('Eixo Y',fontsize=15)
ax.set_zlabel('Eixo Z',fontsize=15)
ax.view_init(60,45)

plt.show()


