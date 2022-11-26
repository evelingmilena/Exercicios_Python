import numpy as np
import matplotlib.pyplot as plt

def matrixB(t):
    matrixB = np.array([2*np.sin(t), 2*(np.cos(t)-np.sin(t))])
    return matrixB
     
def Rk4(y1_start,y2_start,t_start,t_end,N_steps):

    ht = (t_end - t_start)/N_steps
    t = np.empty(N_steps + 1)
    I = np.eye(2)
    
    y = np.zeros((2, N_steps + 1))

    matrixA = np.array([[-2,1],[1,-2]])

    y[:,0] = [y1_start, y2_start]

    for n in range(N_steps):
        k1 = matrixA@y[:,n] + matrixB(t[n])
        k2 = matrixA@(y[:,n] + (ht/2)*k1) + matrixB(t[n] + ht/2)
        k3 = matrixA@(y[:,n] + (ht/2)*k2) + matrixB(t[n] + ht/2)
        k4 = matrixA@(y[:,n] + ht*k3) + matrixB(t[n] + ht)

        y[:,n+1] = y[:,n] + (ht/6)*(k1 + 2*k2 + 2*k3 + k4)
        t[n+1] = t[n] + ht

    return y,t

def exact_soluction(t):
    y_exact = np.zeros((2,N_steps + 1))
    y_exact[0,:] = 2*np.exp(-t) + np.sin(t)
    y_exact[1,:] = 2*np.exp(-t) + np.cos(t)
    return y_exact

y1_start = 2
y2_start = 3
t_start = 0
t_end = 30
N_steps = 300

t = np.linspace(t_start,t_end,N_steps + 1)

y,t_Rk4 = Rk4(y1_start,y2_start,t_start,t_end,N_steps)
y_exact = exact_soluction(t)

plt.figure(0)
plt.plot(t_Rk4,y[0],'ro--',label='Approximate')
plt.plot(t,y_exact[0],'k',label='Exact')
plt.grid()
plt.xlabel('t')
plt.ylabel('f\u2081(t)')
plt.title('Approximate and Exact Solution \
for f\u2081(t) - Runge Kutta 4')
plt.legend(loc='best')

plt.figure(1)
plt.plot(t_Rk4,y[1],'ro--',label='Approximate')
plt.plot(t,y_exact[1],'k',label='Exact')
plt.grid()
plt.xlabel('t')
plt.ylabel('f\u2082(t)')
plt.title('Approximate and Exact Solution \
for f\u2082(t) - Runge Kutta 4')
plt.legend(loc='best')

plt.show()
