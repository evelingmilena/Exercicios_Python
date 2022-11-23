import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad,dblquad


def integrand(y,x,z):
    a = 2
    b = 2
    return a*x**2 + np.exp(y)+ b*np.sin(z)

integrand = np.vectorize(integrand)

def integrated(z):
    return dblquad(integrand,0,1,-2,2,args=(z,))[0]

integrated = np.vectorize(integrated)
z = np.linspace(-5,5,100)

result = integrated(z)

plt.plot(z,result)
plt.show()
