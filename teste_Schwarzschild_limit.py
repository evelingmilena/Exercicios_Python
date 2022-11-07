import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv,lambertw



#Definindo a matriz
N = 10
h = 0.25
l = 1
N_it = 100
U = np.zeros((N+1,N+1),float)

for i in range(N+1):
    x = np.array(1+2*lambertw((0.5)*np.sqrt(np.exp(i*h-1))),dtype=float)
    U[i][0] = np.sqrt(2/np.pi)*np.exp(-x**2)
    

for k in range(N_it):
    for i in range(1,N):
        for j in range(1,N):
            x = np.array(1+2*lambertw((0.5)*np.sqrt(np.exp(i*h-1))),dtype=float)
            U[i][j] = ((((x+1)**4)/h**2)/(l*(l+1)*(x**2-1)+2*(x-1)))*(U[i-1][j]+U[i+1][j]-U[i][j-1]-U[i][j+1])


print(U)            
plt.plot(U)
plt.show()
