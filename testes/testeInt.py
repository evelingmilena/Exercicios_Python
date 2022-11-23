from scipy.integrate import quad,dblquad
from scipy.special import sph_harm,lambertw,lpmv
import numpy as np

import matplotlib.pyplot as plt

a = 2
b = 2
c = 0
def integrand(y,x,z):
    func = (a*x**2 + b*np.sin(z) + np.exp(y))*c
    return func

integrand = np.vectorize(integrand)

def integrated(z):
    return dblquad(integrand, 0, 1, -2, 2, args=(z,))[0]

integrated = np.vectorize(integrated)
z = np.linspace(-5,5,100)

final_integrated = integrated(z)

plt.plot(z,final_integrated)
plt.show()














