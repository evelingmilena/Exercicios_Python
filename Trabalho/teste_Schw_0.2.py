import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv,lambertw
from mpl_toolkits.mplot3d import Axes3D


# Parametros do calculo numerico
N = 5000
t0 = 0
tf = 500
ht= (tf-t0)/(N)
l = 1
xmin = -1000
xmax = 700
hxtilde = (xmax-xmin)/N

# Definindo a matriz
U = np.zeros((N+1,N+1),float)
xtilde = np.linspace(xmin, xmax, N+1)
x = np.array(1+2*lambertw((0.5)*np.sqrt(np.exp(xtilde-1))),dtype=float)
t = np.linspace(t0,tf,N+1)

# Condicoes Iniciais
for i in range(N+1):
    gauss = np.sqrt(2/np.pi)*np.exp(-(xtilde[i]-200)**2)
    # U(0)
    U[i][0] = gauss
    #dU/dt(0)
    U[i][1] = gauss + \
              (0.5)*(ht**2)*gauss*(4*(xtilde[i]-200)**2-2) - \
              (l*(l+1)+2/(x[i]+1))*((x[i]-1)/(x[i]+1)**3)*gauss
  
# Diferencas Finitas
for j in range(0,N):
    for i in range(2,N):
        U[i][j+1] = -U[i][j-1] + 2*U[i][j] + \
                    ((ht/hxtilde)**2)*(U[i+1][j]-2*U[i][j]+U[i-1][j]) + \
                    -(ht**2)*(l*(l+1)+2/(x[i]+1))*((x[i]-1)/(x[i]+1)**3)*U[i][j]

# Plots

fig_path = "/home/bingo/Documents/Exercicios_Python/Trabalho/figures/"

plt.figure(1)
for i in range(10):
    plt.plot(t, U[i*N//10,:], label=r"$\tilde{x}$=".format(x[i*N//10]))
    
plt.xlabel("Time")
plt.ylabel("U(t)")
plt.title("Spatial Cuts")
plt.savefig(fig_path + "N{}_spatial_cut.png".format(i))

TT, XX = np.meshgrid(t,xtilde)

fig, ax = plt.subplots()
ax.set_title("")
ax.set_ylabel(r"$\tilde{x}$")
ax.set_xlabel("time")
surf = ax.imshow(U)
fig.colorbar(surf)
plt.savefig(fig_path + "Plot - 2D")
