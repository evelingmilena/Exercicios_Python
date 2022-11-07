# Esse codigo serve para verificar se o triangulo e equilatero, isosceles ou obtuso dado 3 lados.

x = 2
y = 3
z = 4

if x==y and y==z:
   print("O triangulo e equilatero.")
elif x==y and y!=z:
   print("O triangulo e isoceles.")
else:
   print("O triangulo e obtuso.")
