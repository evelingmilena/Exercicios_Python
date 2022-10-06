import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import csv

x = []
y = []
psi = []

xN = np.arange(5,25,0.1)
yN = np.arange(-0.9,0.9,0.1)

nome_arquivo = "novatabelaPsi5.csv"

with open(nome_arquivo,"r") as arquivo:
    linhas = csv.reader(arquivo, delimiter = ',')
    for linha in linhas:
        x.append(float(linha[0]))
        y.append(float(linha[1]))
        psi.append(float(linha[2]))
f = interpolate.interp2d(x, y, psi, kind = "cubic")
psiN = f(xN,yN)

fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection = "3d")

X,Y = np.meshgrid(xN, yN)
surf = ax.plot_surface(X, Y, psiN, cmap = plt.cm.cividis)

plt.show()
