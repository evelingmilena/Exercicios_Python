def e_psi(x,y,alpha):
    a = (x-1)/(x+1)
    b = (x**2-y**2+(alpha**2)*(x**2-1))**2
    c = 4*(alpha**2)*(x**2)*(1-y**2)
    d = (x**2-y**2+(alpha**2)*(x-1)**2)**2
    e = 4*(alpha**2)*(y**2)*(x**2-1)
    f = (b+c)/(d-e)

    return a*(f**2)
    
def rz_xy(r,z,k):
    x = (1/(2*k))*(np.sqrt(r**2+(z+k)**2)+np.sqrt(r**2+(z-k)**2))
    y = (1/(2*k))*(np.sqrt(r**2+(z+k)**2)-np.sqrt(r**2+(z-k)**2)) 
    
    return x,y

import numpy as np
import matplotlib.pyplot as plt

k = 1
z = 2*k
alpha = 0    
r = np.linspace(0,20,500)/k    

x = rz_xy(r,z,k)
y = rz_xy(r,z,k)
epsi = e_psi(x,y,alpha)

plt.plot(r,epsi)
plt.show()
    
    
