import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv,lambertw
from mpl_toolkits.mplot3d import Axes3D


# Parametros do calculo numerico
N = 100
t0 = 0
tf = 4
ht= (tf-t0)/N
l = 1
xmin = -5
xmax = 5
hxtilde = (xmax-xmin)/N

# Definindo a matriz
U = np.zeros((N+1,N+1),float)
xtilde = np.linspace(xmin, xmax, N+1)
x = np.array(1+2*lambertw((0.5)*np.sqrt(np.exp(xtilde-1))),dtype=float)
t = np.linspace(t0,tf,N+1)

# Condicoes Iniciais
for i in range(N+1):
    # U(0)
    U[i][0] = np.sqrt(2/np.pi)*np.exp(-xtilde[i]**2)
    #dU/dt(0)
    U[i][1] = np.sqrt(2/np.pi)*np.exp(-xtilde[i]**2) + \
              (0.5)*(ht**2)*(np.sqrt(2/np.pi)*np.exp(-xtilde[i]**2)*(4*xtilde[i]**2-2) - \
              (l*(l+1)+2/(x[i]+1))*((x[i]-1)/(x[i]+1)**3)*np.sqrt(2/np.pi)*np.exp(-xtilde[i]**2))
  
# Diferencas Finitas
for i in range(0,N):
    for j in range(2,N):
        U[i][j+1] = -U[i][j-1] + \
                    ((ht/hxtilde)**2)*(U[i+1][j]+U[i-1][j]) + \
                    ((2-2*(ht/hxtilde)**2)-(ht**2)*(l*(l+1)+2/(x[i]+1))*((x[i]-1)/(x[i]+1)**3))*U[i][j]

# Plots

plt.figure(1)
for i in range(10):
    plt.plot(t,U[i,:])

TT, XX = np.meshgrid(t,xtilde)

print(xtilde)
print(TT)
print(XX)

fig,ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_title("")
ax.set_xlabel("xtilde")
ax.set_ylabel("time")
ax.set_zlabel("U(xtilde)")
surf = ax.plot_surface(XX, TT, U)
fig.colorbar(surf)

plt.show()
