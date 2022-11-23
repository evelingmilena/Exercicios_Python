import numpy as np
import matplotlib.pyplot as plt
import runge_kutta4 as rk

def f(t,y):
    return t
    


y0, t0, tN = 1, 0, 10
hs = [1, 0.1, 0.01, 0.001]

plt.figure(0)
for h in hs:
    N = int((tN-t0)/h)
    trk, yrk = rk.RK4(y0, t0, h, N, f)
    tee, yee = rk.euler_explicito(y0, t0, h, N, f)
    plt.plot(trk, yrk, label="RK4 h={}".format(h), ls="-")
    plt.plot(tee, yee, label="EE h={}".format(h), ls="--")
plt.legend()
plt.show()
