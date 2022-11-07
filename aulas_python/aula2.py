"""
Esse programa verifica se um número é par
"""

n = 1.5

# 1) Verificar se n e inteiro

if type(n)!=int:
    print("A variavel deve ser do tipo inteiro")
    
# 2) Verificar se o resto da divisao por 2 e zero

#O elif e utilizado para dar continuidade ao primeiro if. Se a primeira condicao no if for verdadeira, a próxima linha será ignorada se for um elif, mas se for um if isso não acontecerá. Dessa forma, o código se torna mais eficiente.

elif n%2==0:
    print("O numero",n, "e par.")

# 3) Caso nao seja dizer que e impar
else:
    print("O numero",n,"e impar")
    
# operadores de comparacao:
# ==, !=, >, <, >=, <=


# poperaadores logicos: and, or

