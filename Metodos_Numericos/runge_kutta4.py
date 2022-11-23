import numpy as np
import matplotlib.pyplot as plt

def RK4(y0, t0, h, N, f):
    
    t = np.empty(N+1) #[t0]
    y = np.empty(N+1)
    
    t[0], y[0] = t0, y0
    
    for i in range(N):
        k1 = f(t[i], y[i])
        k2 = f(t[i]+h/2, y[i]+k1*h/2)
        k3 = f(t[i]+h/2, y[i]+k2*h/2)
        k4 = f(t[i]+h, y[i]+k3*h)
        y[i+1] = y[i]+(k1+2*k2+2*k3+k4)*h/6
        t[i+1] = t[i]+h
        
    return t, y
    
def euler_explicito(y0, t0, h, N, f):

    t = np.empty(N+1) #[t0]
    y = np.empty(N+1)
    
    t[0], y[0] = t0, y0
    
    for i in range(N):
        y[i+1] = y[i] + h*f(t[i], y[i])
        t[i+1] = t[i]+h
        
    return t,y
        
          
def g(t, y):
    return y
    
f0 = 1
x0 = 0
d = 0.1
N = 100

x_EE, f_EE = euler_explicito(f0, x0, d, N, g)
x_RG4, f_RG4 = RK4(f0, x0, d, N, g)

plt.figure(0)
plt.title("Solucao")
plt.plot(x_EE, f_EE, label="Euler Explicito")
plt.plot(x_RG4, f_RG4, label="Runge-Kutta 4")
plt.plot(x_RG4, np.exp(x_RG4), label="Analitico")
plt.legend()

plt.figure(1)
plt.title("Erro")
plt.plot(x_EE, f_EE-np.exp(x_RG4), label="Euler Explicito")
plt.plot(x_RG4, f_RG4-np.exp(x_RG4), label="Runge-Kutta 4")
plt.legend()
plt.show()

