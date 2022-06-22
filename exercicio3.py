# Esse codigo serve para verificar se o triangulo e equilatero, isosceles ou obtuso dado 3 lados.

x = 6
y = 3
z = 3

if x<=y+z and y<=x+y and z<=x+y:
   if x==y and y==z:
      print("O triangulo e equilatero.")
   elif x==y and y!=z or x!=y and y==z or x==z and x!=y:
      print("O triangulo e isoceles.")
   else:
      print("O triangulo e obtuso.")
else:
   print("Os lados do triangulo nao satisfazem a desigualdade triangular.")
