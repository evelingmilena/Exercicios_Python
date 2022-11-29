import numpy as np
import matplotlib.pyplot as plt

N = 10
ht = 0.1
hx = 0.1
u = 1
c = np.zeros((N+1,N+1),float)
k = 1

#metodo

for j in range(N):
    for i in range(N):
        c[i][j+1] = c[i][j] - u*(ht/hx)*(c[i][j] - c[i-1][j]) + k*(ht/hx**2)*(c[i+1][j] - 2*c[i][j] + c[i-1][j])
        
print(c)
