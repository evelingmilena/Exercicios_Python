import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad,quad
from scipy.special import lpmv,lambertw
from mpl_toolkits.mplot3d import Axes3D


#definindo a transformação inversa de x.
#x_tortoise = 1+2*lambertw((1/2)*np.sqrt(np.exp(x-1)))


#Definindo as constantes
m = 1
l = 2
k = 4
alpha = 0.2 
N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    

#definindo o integrando da matriz A
def int_matriz_A(y,x):
   
    a = (x**2)-(y**2) + (alpha**2)*(x**2-1)
    b = 4*(alpha**2)*(x**2)*(1-(y**2))
    c = 4*(alpha**2)*(y**2)*((x**2)-1)
    d = (x**2)-(y**2) + (alpha**2)*((x**2)-1)**2
    e = (1+(alpha**2))*((x**2)-(y**2))

    f = ((a**2)+b)/(d**2-c)
    g = ((a**2)+b)**2/(e**4)

    ratio_fg = f**4/g**2
    
    int_matriz_A = 2*np.pi*ratio_fg*N1*N2*lpmv(m,l,y)*lpmv(m,k,y)
    return int_matriz_A

int_matriz_A = np.vectorize(int_matriz_A)

#definindo o integrando da matriz b
def int_matriz_b(y,x):
    a = (x**2)-(y**2) + (alpha**2)*(x**2-1)
    b = 4*(alpha**2)*(x**2)*(1-y**2)
    c = 4*(alpha**2)*(y**2)*(x**2-1)
    d = (x**2)-(y**2) + (alpha**2)*(x**2-1)**2
    e = (1+alpha**2)*(x**2-y**2)

    f = (a**2+b)/(d**2-c)
    g = (a**2+b)**2/(e**4)

    constant_b = (f**4/g**2)*(g**2-1)/(1-y**2)

    int_matriz_b = 2*np.pi*constant_b*N1*N2*lpmv(m,l,y)*lpmv(m,k,y)
    return int_matriz_b

int_matriz_b = np.vectorize(int_matriz_b)

#definindo a funcao que integra a matriz
def integrated(x):
    return quad(int_matriz_A, -1, 1, args=(x,))[0], quad(int_matriz_b, -1, 1, args=(x,))[0]

integrated = np.vectorize(integrated)
x = np.linspace(-5,5,100)

matriz_A, matriz_b = integrated(x)

def matriz_B(x):
    veff = l*(l+1)+(2/(x+1))
    matriz_B = ((x-1)/(x+1)**3)*(matriz_A*veff+(m**2)*matriz_b)
    return matriz_B

matriz_B = np.vectorize(matriz_B)

#plt.plot(x, matriz_A)
#plt.plot(x, matriz_b)
plt.plot(x, matriz_B)
plt.show()



    
    
