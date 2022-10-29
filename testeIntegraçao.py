import matplotlib.pyplot as plt
import numpy as np
from math import cos, exp, pi
from scipy.integrate import quad

from scipy.integrate import quad, dblquad
def I(n):
    return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)

x = np.linspace(-5,5,1000) 
# function we want to integrate
def f(x):
    return np.cos(x**3)

ff = f(x)
f1=f(2)

print(f1)

plt.plot(x,ff)
plt.show()


