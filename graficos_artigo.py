def e_psi(x,y,alpha):
 
    a = (x-1)/(x+1)
    b = (x**2-y**2+(alpha**2)*(x**2-1))**2
    c = 4*(alpha**2)*(x**2)*(1-y**2)
    d = (x**2-y**2+(alpha**2)*(x-1)**2)**2
    e = 4*(alpha**2)*(y**2)*(x**2-1)
    f = (b+c)/(d-e)
    
    return a*(f**2)
    
def rz_xy(r,z,k):
    w = r**2/k**2
    x = (1/(2*k))*(np.sqrt(r**2+(z+k)**2)+np.sqrt(r**2+(z-k)**2))
    y = (1/(2*k))*(np.sqrt(r**2+(z+k)**2)-np.sqrt(r**2+(z-k)**2)) 
    
    return x,y


import numpy as np
import matplotlib.pyplot as plt

k=1
r_min = 0
r_max = 20
N = 500
r = np.linspace(r_min,r_max,N)/k
z = 2*k
alpha=0

x,y = rz_xy(r,z,k)

plt.figure(0)
plt.xlabel("r/k")
plt.ylabel(r"$e^\Psi$",rotation=0)

#plt.title("")

#for alpha_cent in range(20,45,5):
 #   alpha = alpha_cent/100 
  #  epsi = e_psi(x,y,alpha)
   # plt.plot(r,epsi,label=r"$\alpha = {0:.02f}$".format(alpha))

alphas = [0,0.2,0.3,0.35,0.4]
qtd_alphas = len(alphas)
for i in range(qtd_alphas):
    epsi = e_psi(x,y,alphas[i])
    plt.plot(r,epsi,label=r"$\alpha = {0:.02f}$".format(alphas[i]))
    

plt.grid()
plt.legend(loc="best")
plt.show()
