import numpy as np
import sympy as sp



A = np.array([[1,1,-2], [1, 1,-1],[3,1,-1]])

#det_A = np.linalg.det(A) calculo de determinante

B = np.array([1,3,3])

#X = np.linalg.inv(A).dot(B) funcao que calcula a inversa de A e multiplica por B

X = np.linalg.solve(A,B) 

print(X)

#outra forma de calcular o sistema linear

x, y, z = sp.symbols("x y z")


eq1 = sp.Eq(x+y-2*z,1)
eq2 = sp.Eq(x+y-z,3)
eq3 = sp.Eq(3*x+y-z,3)

#resultado = sp.linsolve((eq1,eq2,eq3),(x,y,z))
#outra forma de imprimir o resultado:
resultado = sp.solve((eq1,eq2,eq3),(x,y,z))
print(resultado)

x, y = sp.symbols("x y")
a = sp.symbols("a")

eq4 = sp.Eq(a*x+y,1)
eq5 = sp.Eq(x-a*y,1)

res = sp.solve((eq4,eq5),(x,y))
print(res)

A = sp.Matrix([[a,1],[1,-a]])
detA = A.det()
print(detA)


