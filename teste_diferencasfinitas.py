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
    delta_x = (xf - x0)/N
    vetor_x = np.linspace(x0 + delta_x, xf - delta_x, N-1)
    dim_sist = N - 1
    A = np.zeros((dim_sist, dim_sist))
    b = np.zeros(dim_sist)

    #Montagem da matriz A
    for i in range(dim_sist):
        x = vetor_x[i]
        for j in range(dim_sist):
            if i == j:
                A[i][j] = 2 + q(x)*pow(delta_x,2)
            elif i == (j+1):
                A[i][j] = -1 - p(x)*delta_x/2
            elif i == (j-1):
                A[i][j] = -1 + p(x)*delta_x/2
            else:
                A[i][j] = 0   
        
    #Montagem do vetor b
    for i in range(dim_sist):
        x = vetor_x[i]
        if i == 0:
            b[i] = (1 + p(x)*delta_x/2)*y0 - r(x)*pow(delta_x,2)
        elif i == (dim_sist - 1):
            b[i] = (1 - p(x)*delta_x/2)*yf - r(x)*pow(delta_x,2)
        else:
            b[i] = -r(x)*pow(delta_x,2)
    #resolucao do sistema linear Ay+b

    y = np.linalg.solve(A,b)
    return y

y = diferencas_finitas(0, 0, 5, 50, 301)

#for i in range(len(y)):
 #   vetor_x = np.linspace(0, 1 , 9)
    #print("y(%f) = %f" %(vetor_x[i],y[i]))

plt.figure(0)
vetor_x = np.linspace(0, 5 , 300)

plt.plot(vetor_x,y)

x = np.linspace(0, 5, 100)
f = -(10/2)*x**2 + 35*x
plt.plot(x,f)

plt.show()
