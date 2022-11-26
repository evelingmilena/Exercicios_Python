import numpy as np
import matplotlib.pyplot as plt


def solve(y1_start, y2_start, t_start,t_end,N_steps):
    y = np.zeros((2, N_steps + 1))
    ht = (t_end - t_start)/N_steps
    t = np.linspace(t_start,t_end,N_steps + 1)
    I = np.eye(2)

    matrixA = np.array([[-2,1],[998,-999]])
    matrixB = np.array([2*np.sin(t), 998*(np.cos(t)-np.sin(t))])
    
    y[:,0] = [y1_start, y2_start]
    
    for i in range(0,N_steps):
        y[:,i+1] = np.linalg.inv(I-ht*matrixA)@(y[:,i]+ht*matrixB[:,i+1]) # ou np.dot(A,B)

    return y

def exact_solution(t):
    y_exact = np.zeros((2, N_steps + 1))
    y_exact[0,:] = 2*np.exp(-t) + np.sin(t)
    y_exact[1,:] = 2*np.exp(-t) + np.cos(t)
    return y_exact  
    
y1_start = 2  
y2_start = 3
t_start = 0
t_end = 30
N_steps = 300

y = solve(y1_start, y2_start, t_start,t_end,N_steps)
t = np.linspace(t_start,t_end,N_steps + 1)
y_exact = exact_solution(t)

plt.figure(0)
plt.plot(t,y[0],'mo--',label='Approximate')
plt.plot(t,y_exact[0],'k',label='Exact')
plt.xlabel('t')
plt.ylabel('f\u2081(t)')
plt.grid()
plt.legend(loc='best')
plt.title('Approximate and Exact Solution \
for f\u2081(t) - Backward Euler method')

plt.figure(1)
plt.plot(t,y[1],'mo--',label='Approximate')
plt.plot(t,y_exact[1],'k',label='Exact')
plt.xlabel('t')
plt.ylabel('f\u2082(t)')
plt.grid()
plt.legend(loc='best')
plt.title('Approximate and Exact Solution \
for f\u2082(t) - Backward Euler method')

plt.show()
    



