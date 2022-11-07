'''
Eqs dif parciais com sympy
'''

from sympy.abc import t
from sympy import Function, Eq
from sympy.solvers.ode import dsolve

x = Function('x')

dxdt = x(t).diff(t)
d2xdt2 = x(t).diff(t, t)

eq = Eq( d2xdt2 + x(t) , 0)
res = dsolve(eq, ics={x(0): 0, x(t).diff(t).subs(t, 0): 4})
print(res)



