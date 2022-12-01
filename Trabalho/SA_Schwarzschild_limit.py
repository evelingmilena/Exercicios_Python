import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv,lambertw
from mpl_toolkits.mplot3d import Axes3D


# Parametros do calculo numerico
N = 1000
t0 = 0
tf = 500
ht = (tf-t0)/(N)
l = 1
xmin = -1000
xmax = 700
hxtilde = (xmax-xmin)/N
xtilde0 = 500

# Definindo a matriz
U = np.zeros((N+1,N+1),float)
xtilde = np.linspace(xmin, xmax, N+1)
x = np.array(1+2*lambertw((0.5)*np.sqrt(np.exp(xtilde-1))),dtype=float)
t = np.linspace(t0,tf,N+1)

# Condicoes Iniciais
for i in range(N+1):
    # U(0)
    gaussian = np.sqrt(2/np.pi)*np.exp(-(xtilde[i]-xtilde0)**2)
    U[i][0] = gaussian
    #dU/dt(0)
    U[i][1] = gaussian + (0.5)*(ht**2)*gaussian*(4*(xtilde[i]-xtilde0)**2-2) - \
              (l*(l+1)+2/(x[i]+1))*((x[i]-1)/(x[i]+1)**3)*gaussian
  
# Diferencas Finitas
for j in range(0,N):
    for i in range(2,N):
        U[i][j+1] = -U[i][j-1] + 2*U[i][j] + \
                    ((ht/hxtilde)**2)*(U[i+1][j]-2*U[i][j]+U[i-1][j]) + \
                    -(ht**2)*(l*(l+1)+2/(x[i]+1))*((x[i]-1)/(x[i]+1)**3)*U[i][j]
# Plots
plt.figure(1)
for i in range(10):
    plt.plot(t,U[i*N//10,:])
           
TT, XX = np.meshgrid(t,xtilde)

fig,ax = plt.subplots()
ax.set_title("")
ax.set_ylabel("xtilde")
ax.set_xlabel("time")
surf = ax.imshow(U)
fig.colorbar(surf)

plt.show()
