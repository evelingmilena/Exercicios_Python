'''
Matplotlib
'''

import matplotlib.pyplot as plt
import numpy as np

print("oi tudo bem \nmeu nome e eveling")

# ola um comentario pelo vi

x = np.linspace(0.1, 100, 1000) #50
y_exp = np.exp(x)
y_log = np.log(x)
y_log10 = np.log10(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(0)
plt.plot(x, y_exp)

plt.figure(10)
plt.plot(x, y_log, c="g", linestyle="dashed", label="Ln")
plt.plot(x, y_log10, c="y", linestyle="-.", label="Log10")
plt.legend(loc="best")
plt.title("Logaritmos")
plt.plot(10, 1, marker="x", c="r")

plt.figure(2)
plt.plot(x, y_sin, c="b", linestyle="--", label="Sine")
plt.plot(x, y_cos, c="r", linestyle=":", label="Cosine")
plt.legend(loc="best")
plt.title("Seno e Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel(r"$\Psi$(x)") # Latex
plt.xlim(0,np.pi)

plt.show()

plt.figure(3)
N = 500
r = 0.5
x_rand = np.random.rand(N)# seed=)
y_rand = np.random.rand(N)#, seed=2783)
x_circ = np.linspace(0,2*r,100)
#x_circ = np.concatenate(x_circ, x_circ[::-1])
y_circ_sup = np.sqrt(r**2-(x_circ-r)**2)+r
y_circ_inf = -np.sqrt(r**2-(x_circ-r)**2)+r
plt.scatter(x_rand, y_rand)
plt.plot(x_circ, y_circ_sup, c="b")
plt.plot(x_circ, y_circ_inf, c="b")
plt.xlim(0,1)
plt.ylim(0,1)
#plt.savefig("/home/bingo/Documents/Exercicios_Python/plots/circulo_monte_carlo.png")

# hist, 3d, grid, polar

#fig = plt.figure(4)
#ax = fig.add_subplots(231)
#ax[0][0].plot(x,y)
#ax[0][0].set_title()
#ax[0][0].set_xlabel()


# fazer o grafico de alguma funcao dificil (nao seja diferencial) de preferencia do artigo ou da dissertacao

# calcular pi usando monte carlo e calcular desvio padrao da medida
# calcular a integral de uma funcao usando monte carlo

