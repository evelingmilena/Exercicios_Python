'''
Essa e uma docstring. Ela e a explicacao do codigo.
'''
# Normalmente os imports ficam nas primeiras linhas do código (antes mesmo das variaveis globais, mas depois da docstring


import modulo_aula6

circ = modulo_aula6.circunferencia(5)
print("A circunferencia de raio 5 tem comprimento", circ)
print(modulo_aula6.PI)


import modulo_aula6 as mod6 #melhor usar essa maneira

circ = mod6.circunferencia(5)
print("A circunferencia de raio 5 tem comprimento", circ)
print(mod6.PI)


from modulo_aula6 import circunferencia

circ = circunferencia(5)
print("A circunferencia de raio 5 tem comprimento", circ)
#print(PI)


from modulo_aula6 import *

circ = circunferencia(5)
print("A circunferencia de raio 5 tem comprimento", circ)
print(PI)


# Exercicio: criar um pacote que cria um perfil para alguem em um site
