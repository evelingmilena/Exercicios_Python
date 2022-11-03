import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad,quad
from scipy.special import lpmv,lambertw
from mpl_toolkits.mplot3d import Axes3D


def wrapper_int_matriz_A(m,l,k,alpha,N1,N2):
	def int_matriz_A(y,x):
		'''
		Definindo o integrando da matriz A
		'''
	   
		a = (x**2)-(y**2) + (alpha**2)*(x**2-1)
		b = 4*(alpha**2)*(x**2)*(1-(y**2))
		c = 4*(alpha**2)*(y**2)*((x**2)-1)
		d = (x**2)-(y**2) + (alpha**2)*((x**2)-1)**2
		e = (1+(alpha**2))*((x**2)-(y**2))

		f = ((a**2)+b)/(d**2-c)
		g = ((a**2)+b)**2/(e**4)

		ratio_fg = f**4/g**2
		
		matriz_A = 2*np.pi*ratio_fg*N1*N2*lpmv(m,l,y)*lpmv(m,k,y)
		return matriz_A
	return int_matriz_A


def wrapper_int_matriz_b(m,l,k,alpha,N1,N2):
	def int_matriz_b(y,x):
		'''
		Definindo o integrando da matriz b
		'''
		a = (x**2)-(y**2) + (alpha**2)*(x**2-1)
		b = 4*(alpha**2)*(x**2)*(1-y**2)
		c = 4*(alpha**2)*(y**2)*(x**2-1)
		d = (x**2)-(y**2) + (alpha**2)*(x**2-1)**2
		e = (1+alpha**2)*(x**2-y**2)

		f = (a**2+b)/(d**2-c)
		g = (a**2+b)**2/(e**4)

		constant_b = (f**4/g**2)*(g**2-1)/(1-y**2)

		matriz_b = 2*np.pi*constant_b*N1*N2*lpmv(m,l,y)*lpmv(m,k,y)
		return matriz_b
	return int_matriz_b
    

def integrated(x,m,l,k,alpha,N1,N2):
    '''
    Definindo a funcao que integra a matriz
    '''
    int_matriz_A = wrapper_int_matriz_A(m,l,k,alpha,N1,N2)
    int_matriz_b = wrapper_int_matriz_b(m,l,k,alpha,N1,N2)
    
    vec_int_matriz_A = np.vectorize(int_matriz_A)
    vec_init_matriz_v = np.vectorize(int_matriz_b)
    return quad(vec_int_matriz_A, -1, 1, args=(x,))[0], quad(vec_init_matriz_v, -1, 1, args=(x,))[0]


def init_matriz_B(x, matriz_A, matriz_b):
    veff = l*(l+1)+(2/(x+1))
    matriz_B = ((x-1)/(x+1)**3)*(matriz_A*veff+(m**2)*matriz_b)
    return matriz_B
    

#Definindo as constantes
#m = 2
l = 4
k = 2
alpha = 0.2

x = np.linspace(1.2,5,1000)
integrated = np.vectorize(integrated)

"""
plt.figure(0)
plt.title("Matriz A, com \u03B1=0.2, l=k=4 e m variando.")
plt.xlabel("x")
plt.ylabel("A(x)")
for m in range(-2,3):
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    plt.plot(x, matriz_A, label="m = {0:.0f}".format(m)) 
plt.legend(loc="best")
"""
"""
plt.figure(0)
plt.title("Matriz A, com l=k=4, m=2 e \u03B1 variando.")
plt.xlabel("x")
plt.ylabel("A(x)")
alphas = [0,0.1,0.2,0.3]
for alpha in alphas:
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    plt.plot(x, matriz_A, label="\u03B1={0:.01f}".format(alpha)) 
plt.legend(loc="best")
"""
"""
plt.figure(0)
plt.title("Matriz A, com m=0, \u03B1=0.2 e l e k variando.")
plt.xlabel("x")
plt.ylabel("A(x)")
for l,k in zip(range(1,5),range(1,5)): #laço para plotar a matriz com l=k variando e m fixo
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    plt.plot(x, matriz_A, label="l=k={0:.0f}".format(l)) 
plt.legend(loc="best")
"""

"""
plt.figure(1)
plt.title("Matriz b com \u03B1=0.2, l=k=4 e m variando.")
plt.xlabel("x")
plt.ylabel("b(x)")
for m in range(0,l+1):
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    plt.plot(x, matriz_b, label="m = {0:.0f}".format(m)) 
plt.legend(loc="best")
"""
plt.figure(1)
plt.title("Matriz b com \u03B1=0.2, l=4, k=2 e m variando.")
plt.xlabel("x")
plt.ylabel("b(x)")
for m in range(-k,k+1):
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    plt.plot(x, matriz_b, label="m = {0:.0f}".format(m)) 
plt.legend(loc="best")
"""
plt.figure(1)
plt.title("Matriz b com m=2, l=k=4 e \u03B1 variando.")
plt.xlabel("x")
plt.ylabel("b(x)")
alphas = [0,0.1,0.2,0.3]
for alpha in alphas:
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    plt.plot(x, matriz_b, label="\u03B1={0:.01f}".format(alpha)) 
plt.legend(loc="best")
"""
"""
plt.figure(2)
plt.title("Matriz B, com \u03B1=0.2, l=4, m=1 e k variando")
plt.xlabel("x")
plt.ylabel("B(x)")
for k in range(1,5):
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    matriz_B = init_matriz_B(x, matriz_A, matriz_b)
    plt.plot(x, matriz_B, label="k={0:.0f}".format(k)) 
plt.legend(loc="best")
"""
"""
plt.figure(0)
plt.title("Matriz B, com m=0, \u03B1=0.2 e l e k variando.")
plt.xlabel("x")
plt.ylabel("B(x)")
for l,k in zip(range(1,5),range(1,5)): #laço para plotar a matriz com l=k variando e m fixo
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    matriz_B = init_matriz_B(x, matriz_A, matriz_b)
    plt.plot(x, matriz_B, label="l=k= {0:.0f}".format(l)) 
plt.legend(loc="best")
"""
"""
plt.figure(0)
plt.title("Matriz B, com m=0, \u03B1=0.2 e l e k variando.")
plt.xlabel("x")
plt.ylabel("B(x)")
alphas = [0,0.1,0.2,0.3]
for alpha in alphas: #laço para plotar a matriz com l=k fixos,m fixo e alpha variando
    N1 = np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-m))/(np.math.factorial(l+m))))
    N2 = np.sqrt(((2*k+1)/(4*np.pi))*((np.math.factorial(k-m))/(np.math.factorial(k+m))))
    matriz_A, matriz_b = integrated(x,m,l,k,alpha,N1,N2)
    matriz_B = init_matriz_B(x, matriz_A, matriz_b)
    plt.plot(x, matriz_B, label="\u03B1={0:.01f}".format(alpha)) 
plt.legend(loc="best")
"""
plt.show()



    
    
