import numpy as np
import matplotlib.pyplot as plt


def solve(y_start,t_start,t_end,N_steps):
    y = np.zeros(N_steps + 1)
    ht = (t_end - t_start)/N_steps
    t = np.linspace(t_start,t_end,N_steps + 1)
    I = np.identity(2)
    
    def matrix_A(a,b,c,d):
        A = np.array([[a,b],[c,d]])
    

    def vector_B(a,b):
        B = np.array([a,b])
    

    matrixA = matrix_A(-2,1,1,-2)
    
    for i in range(0,N_steps):
        vectorB[i] = vector_B(2*np.sin(t[i]),2*np.cos(t[i]))
        y[0] = y_start
        y[i+1] = np.linalg.inv(1-ht*matrixA).dot(y[i]+ht*vectorB[i+1])
    return y

y1 = solve(2,0,30,200)
y2 = solve(3,0,30,200)

t = np.linspace(t_start,t_end,N_steps + 1)

plt.plot(t,y1)
plt.show()
    



