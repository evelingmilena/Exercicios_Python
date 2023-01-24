import numpy as np
import matplotlib.pyplot as plt

def f(y,t):
    k1=20
    k2=20
    m1=2
    m2=5
    a = np.zeros((2, N_steps + 1))
    a[:,0] = [y[1], y[0] - y[2],y[3], y[0]]
    
    return a

N_steps = 5
t_start = 0
t_end = 5
h = (t_end - t_start)/N_steps
t = np.empty(N_steps + 1)

y = np.zeros((2, N_steps + 1))
y[:,0] = [1,0]

for i in range(0,len(t)-1):
    k1 =  f( y[:,i], t[i] )
   
    y[:,i+1] = y[:,i] + k1    
    t[i+1] = t[i] + h

print(y)
