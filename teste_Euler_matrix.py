import numpy as np
import matplotlib.pyplot as plt


def solve(y1_start, y2_start, t_start,t_end,N_steps):
    y = np.zeros((2, N_steps + 1))
    ht = (t_end - t_start)/N_steps
    t = np.linspace(t_start,t_end,N_steps + 1)
    I = np.eye(2)

    matrixA = np.array([[-2,1],[1,-2]])
    vectorB = np.array([2*np.sin(t), 2*(np.cos(t)-np.sin(t))])
    
    y[:,0] = [y1_start, y2_start]
    
    for i in range(0,N_steps):
        y[:,i+1] = np.linalg.inv(I-ht*matrixA)@(y[:,i]+ht*vectorB[:,i+1]) # ou np.dot(A,B)

    return y

y1_start = 2  
y2_start = 3
t_start = 0
t_end = 30
N_steps = 200

y = solve(y1_start, y2_start, t_start,t_end,N_steps)

t = np.linspace(t_start,t_end,N_steps + 1)

plt.figure(0)
plt.plot(t,y[0])
plt.plot(t,y[1])
plt.show()
    



