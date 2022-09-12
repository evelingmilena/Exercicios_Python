import numpy as np
import matplotlib.pyplot as plt

N = 10
M = 22
hx = 1/N
hy = 1/M
N_it = 10000
w = 1.2
b = (1/np.pi**2)*(N**2/M)


#definindo as matrizes nulas
matriz_N = np.zeros((N+1, M+1),float) #matriz numerica
matriz_E = np.zeros((N+1, M+1),float) #matriz exata
matriz_e = np.zeros((N+1, M+1),float) #matriz de erros

#aplicando as condições de contorno
for i in range(N+1):
    matriz_N[i][0] = (1/np.pi**2) * np.sin(np.pi*i*hx)
    matriz_N[i][M] = (1/(np.exp(1)*np.pi**2)) * np.sin(np.pi*i*hx)

#aplicando o método SOR
for k in range(N_it):
    for i in range(1,N):
        for j in range(1,M):
            matriz_N[i][j] = w *((1 + 2.*b)* matriz_N[i][j+1] - b* (matriz_N[i+1][j+1] + matriz_N[i-1][j+1])) + (1. - w) * matriz_N[i][j]
            
#montando a matriz exata e o erro
erro_quad = 0.0
for i in range(N+1):
    for j in range(M+1):
        matriz_E[i][j] = (1/np.pi**2)*np.exp(-j*hy) * np.sin(np.pi*i*hx)
        matriz_e[i][j] = matriz_E[i][j] - matriz_N[i][j]
        erro_quad = erro_quad + matriz_e[i][j]**2

print("A matriz numérica é:", matriz_N)
print("\n\nO erro quadratico é:", erro_quad)
        
#plot do gráfico 3D
x  = range(0,N+1)
y = range(0,M+1)
X,Y = np.meshgrid(x,y) 
def f():
    z = matriz_N[X,Y]  
    return z;

Z = f()

def g():
    r = matriz_E[X,Y]
    return r
    
R = g()

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='binary')
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='autumn',edgecolor='none')
ax.set_title('Equação de Difusão - Solução Numérica', fontsize=18)
ax.set_xlabel('Eixo X',fontsize=15)
ax.set_ylabel('Eixo Y',fontsize=15)
ax.set_zlabel('Eixo Z',fontsize=15)
ax.view_init(60,45)

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,R,50,cmap='binary')
ax.plot_surface(X,Y,R,rstride=1,cstride=1,cmap=  'autumn',edgecolor='none')
ax.set_title('Equação de Difusão - Solução Exata', fontsize=18)
ax.set_xlabel('Eixo X',fontsize=15)
ax.set_ylabel('Eixo Y',fontsize=15)
ax.set_zlabel('Eixo Z',fontsize=15)
ax.view_init(60,45)

plt.show()

