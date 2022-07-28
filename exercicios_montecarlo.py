#Exercicios sobre o metodo de monte carlo

import numpy as np
import matplotlib.pyplot as plt

#Exercicio 1: Estimar o valor de pi utilizando o metodo de Monte Carlo

N = 10000
r = 0.5

x = np.random.rand(N)
y = np.random.rand(N)

x_circulo = np.linspace(0,2*r,100)
y_circ_superior = np.sqrt(r**2-(x_circulo-r)**2)+r
y_circ_inferior = -np.sqrt(r**2-(x_circulo-r)**2)+r

plt.scatter(x,y)
plt.plot(x_circulo,y_circ_superior, c="r")
plt.plot(x_circulo,y_circ_inferior, c="r")

plt.xlim(0,1)
plt.ylim(0,1)
plt.show()

cont = 0
tentativas = 100
soma = 0
lista_PI = []
while cont < tentativas:
    N_dentro = 0
    for i in range(N):
            x = np.random.rand(1)
            y = np.random.rand(1)
            z = (x-r)**2 + (y-r)**2
            if (z <= r**2):
                N_dentro = N_dentro + 1
    PI = 4*N_dentro/N
    lista_PI.append(PI)
    cont = cont + 1
 
print(lista_PI)

for i in lista_PI:
    soma = soma + i
    
media = soma/tentativas

print("A media dos valores de pi e:", media)

soma_diferenca = 0
for i in lista_PI:
    soma_diferenca = soma_diferenca + (i-media)**2

desvio_padrao = np.sqrt(soma_diferenca/len(lista_PI))
print("O desvio padrao e:", desvio_padrao)

