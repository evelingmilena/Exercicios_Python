import numpy as np
import matplotlib.pyplot as plt

def solve(y1_start,y2_start,t_start,t_end,N_steps):
    ht = (t_end - t_start)/N_steps
    y = np.zeros((2,N_steps + 1))
    t = np.linspace(t_start,t_end,N_steps + 1)
    I = np.eye(2)

    matrixA = np.array([[-2,1],[1,-2]])
    matrixB = np.array([2*np.sin(t), 2*(np.cos(t)-np.sin(t))])

    y[:,0] = [y1_start,y2_start]

    for n in range(0,N_steps):
        y[:,n+1] = (I + ht*matrixA)@y[:,n] + ht*matrixB[:,n]
    return y

def exact_solution(t):
    y_exact = np.zeros((2,N_steps + 1))
    y_exact[0,:] = 2*np.exp(-t) + np.sin(t)
    y_exact[1,:] = 2*np.exp(-t) + np.cos(t)
    return y_exact

N_steps = 300
y1_start = 2
y2_start = 3
t_start = 0
t_end = 30

t = np.linspace(t_start,t_end,N_steps + 1)

y = solve(y1_start,y2_start,t_start,t_end,N_steps)
y_exact = exact_solution(t)

plt.figure(0)
plt.plot(t,y[0],'co--',label='Approximate')
plt.plot(t,y_exact[0],'k',label='Exact')
plt.grid()
plt.xlabel('t')
plt.ylabel('f\u2081(t)')
plt.legend(loc='best')
plt.title('Approximate and Exact Solution \
for f\u2081(t) - Forward Euler method')

plt.figure(1)
plt.plot(t,y[1],'co--',label='Approximate')
plt.plot(t,y_exact[1],'k',label='Exact')
plt.grid()
plt.xlabel('t')
plt.ylabel('f\u2082(t)')
plt.legend(loc='best')
plt.title('Approximate and Exact Solution \
for f\u2082(t) - Forward Euler method')

plt.show()

