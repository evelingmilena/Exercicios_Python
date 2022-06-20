"""
Esse aqui e o codigo para decomposicao em numeros primos.

O teorema fundamental da aritmetica diz que todo numero inteiro positivo e maior que 1 pode ser escrito ou decomposto em multiplicação de numeros primos.
"""



# verificacao do teorema fundamental da aritmetica

n = 20
i = 1
j = 1

if n>0 and n>1 and type(n)==int:
    print("Esse numero pode ser decomposto em fatores primos.")
    while i<10:
        while j<10:
            if j%i==0 and j%1==j:
                print(j)
            j = j + 1
        i = i + 1           
elif type(n)!=int:
    print("O numero dever ser do tipo inteiro.")
else:
    print("Esse numero nao pode ser decomposto em fatores primos.")

