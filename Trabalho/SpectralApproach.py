import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import lpmv,lambertw


#definindo a transformação inversa de x.

#x_tortoise = 1+2*lambertw((1/2)*np.sqrt(np.exp(x-1)))

#Definindo o integrando f**4/g**2

alpha = 0.2
m = 2
l = 4
k = 2

def int_matriz_A(y,x):
   
   
    a = (x**2)-(y**2) + (alpha**2)*(x**2-1)
    b = 4*(alpha**2)*(x**2)*(1-(y**2))
    c = 4*(alpha**2)*(y**2)*((x**2)-1)
    d = (x**2)-(y**2) + (alpha**2)*((x**2)-1)**2
    e = (1+(alpha**2))*((x**2)-(y**2))

    f = ((a**2)+b)/(d**2-c)
    g = ((a**2)+b)**2/(e**4)

    ratio_fg = f**4/g**2
    
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    
    int_matriz_A = 2*np.pi*ratio_fg*N1*N2*lpmv(m,l,y)*lpmv(m,k,y)
    return int_matriz_A

#definindo a funcao que integra a matriz
int_matrizA = np.vectorize(int_matriz_A)

def integrated(x):
    return quad(int_matriz_A, -1, 1, args=(x,))[0]

integrated = np.vectorize(integrated)
x = np.linspace(1,20,100)

matriz_A = integrated(x)

plt.plot(x,matriz_A)
plt.show()



    
    
