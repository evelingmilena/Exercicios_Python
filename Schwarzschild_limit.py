import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv,lambertw



N = 10
h = 0.25
N_it = 100
l = 1
x_tilde = np.arange(0,N+1,h)
x = np.array(1+2*lambertw((0.5)*np.sqrt(np.exp(x_tilde-1))),dtype=float)
t = np.arange(0,N+1,h)


U = np.zeros((len(x),len(t)),float)

initialConditions = np.sqrt(2/np.pi)*np.exp(-x**2)
U[:,0] = initialConditions

for k in range(N_it):
    for i in range(1,len(x)-1):
        for j in range(1,len(t)-1):
            U[i][j] = ((((i*h+1)**4)/h**2)/(2.*(i*h-1)-l*(l+1)*(h**2.+1.)))*(U[i-1][j]+U[i+1][j]-U[i][j-1]-U[i][j+1])

#print(U)         
#plt.plot(U)
#plt.show()



