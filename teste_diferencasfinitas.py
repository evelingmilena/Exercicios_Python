"""
Nesse codigo, vamos aprender a resolver um exemplo de EDO de segunda ordem pelo método
de diferenças finitas, com condições de contorno constantes.
"""
import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return 0

def q(x):
    return 0

def r(x):
    g = -10
    return g

def diferencas_finitas(x0, y0, xf, yf, N):
    # variaveis iniciais
    h = (xf - x0)/(N-1)
    vetor_x = np.linspace(x0, xf, N)
    dim = N 
    A = np.zeros((dim, dim))
    b = np.zeros(dim)
    A[0][0] = 1
    A[dim-1][dim-1] = 1
    b[0] = y0
    b[dim-1] = yf

    #Montagem da matriz A
    for i in range(1, dim-1):
        x = vetor_x[i]
        for j in range(dim):
            if i == j:
                A[i][j] = - 2/(h**2) - q(x)
            elif i == (j+1):  
                A[i][j] = 1/(h**2) - p(x)/(2*h)
            elif i == (j-1):
                A[i][j] = 1/(h**2) + p(x)/(2*h)
            else:
                A[i][j] = 0   
        
    #Montagem do vetor b
    for i in range(1, dim-1):
        x = vetor_x[i]
        b[i] = r(x)
        
    #resolucao do sistema linear Ay=b
    y = np.linalg.solve(A,b)
    return y

y = diferencas_finitas(0, 0, 5, 50, 100)

for i in range(len(y)):
    vetor_x = np.linspace(0, 5 , 100)
    print("y(%f) = %f" %(vetor_x[i],y[i]))

plt.plot(vetor_x,y)
plt.show()
