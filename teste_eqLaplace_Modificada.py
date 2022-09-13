import numpy as np
import matplotlib.pyplot as plt

N = 50
h = np.pi/N
w = 1.1
N_it = 1000
matrizU = np.zeros((N+1,N+1),float)

#Atribuindo condicao de contorno x = pi. As outras automaticamente são nulas. Portanto, não precisa ser atualizado, pois a matriz foi declarada nula no início.
for j in range(N+1):
    matrizU[N][j] = np.sinh(np.pi)*np.sin(j*h)

#Método SOR
for k in range(N_it):
    for i in range(1,N):
        for j in range(1,N):
           matrizU[i][j] = (w/(2. + 2.*i*h)) * ( matrizU[i+1][j] + matrizU[i-1][j] + i*h*(matrizU[i][j+1] + matrizU[i][j-1]) ) + ( 1. - w ) * matrizU[i][j]

print(matrizU[i][j])    

x  = range(0,N+1)
y = range(0,N+1)
X,Y = np.meshgrid(x,y) 
def f():
    z = matrizU[X,Y]  
    return z;

Z = f()

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='binary')
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='autumn',edgecolor='none')
ax.set_title('Equação de Laplace - Solução Numérica', fontsize=18)
ax.set_xlabel('Eixo X',fontsize=15)
ax.set_ylabel('Eixo Y',fontsize=15)
ax.set_zlabel('Eixo Z',fontsize=15)
ax.view_init(60,45)

plt.show()


