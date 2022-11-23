import numpy as np
import sympy as sp

x = sp.symbols("x")
f = x**2 + x
dfdx = sp.diff(f,x)
print(dfdx)

#derivada com mais de uma variavel

y = sp.symbols("y")
h = sp.cos(x*y)+(3*x+y)/(y**2+1)
dhdx = sp.diff(h,x)
print(dhdx)
