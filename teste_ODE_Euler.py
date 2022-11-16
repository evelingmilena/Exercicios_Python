import numpy as np
import matplotlib.pyplot as plt
from sympy import*


def f1(y1,y2,t):
    dy1dt = -2*y1 + y2 + 2*np.sin(t)
    return dy1dt

def f2(y1,y2,t):
    dy2dt = y1 -2*y2 + 2*(np.cos(t)-np.sin(t))
    return dy2dt

def backward_euler(y1,y2,t):   
    for i in range(0,N_steps):
        result_y1 = y1[i+1] - y1[i] - ht*f1(y1[i+1],y2[i+1],t[i+1])
        y1[i+1] = solve(result_y1,y1[i+1])
        result_y2 = y2[i+1] - y2[i] - ht*f2(y1[i+1],y2[i+1],t[i+1])
        y2[i+1] = solve(result_y2,y2[i+1])
    return result_y1,result_y2

def exact_function(t):
    y1_ex = 2*np.exp(-t) + np.sin(t)
    y2_ex = 2*np.exp(-t) + np.cos(t)
    return y1_ex, y2_ex

N_steps = 300
y1_start = 2
y2_start = 3
t_start = 0
t_end = 30
ht = (t_end - t_start)/N_steps

y1 = np.zeros(N_steps + 1)
y2 = np.zeros(N_steps + 1)

t = np.linspace(t_start,t_end,N_steps + 1)

y1[0] = y1_start
y2[0] = y2_start

Y1,Y2 = backward_euler(y1,y2,t)
Y1_ex,Y2_ex = exact_function(t)

plt.figure(0)
plt.plot(t,Y1)
plt.plot(t,Y1_ex)

plt.figure(1)
plt.plot(t,Y2)
plt.plot(t,Y2_ex)

plt.show()
