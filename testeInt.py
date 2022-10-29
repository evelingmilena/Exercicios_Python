from scipy.integrate import quad,dblquad
from scipy.special import sph_harm,lambertw
import numpy as np
import matplotlib.pyplot as plt


def integrand(x, z, y):
    a = 2
    b = 2
    return a*x**2 + b*np.sin(y) + np.exp(z)

integrand = np.vectorize(integrand)

def integrated(y):
    return dblquad(integrand, 0, 1, -2, 2, args=(y,))[0]

integrated = np.vectorize(integrated)
y = np.linspace(-5,5,100)

final_integrated = integrated(y)

j = np.linspace(-1,1,700)
Y = sph_harm(0, 7, 0, np.arccos(j))*np.conjugate(sph_harm(0, 7, 0, np.arccos(j)))

k = np.linspace(-5,5,100)
l = lambertw(k)

xN = 1 + 2*lambertw((1/2)*np.sqrt(np.exp(k-1)))
plt.plot(k,xN)

#plt.plot(y,final_integrated)
plt.show()












