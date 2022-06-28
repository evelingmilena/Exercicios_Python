"""
Esse aqui e o codigo para decomposicao em numeros primos.

"""





n = 100
i = 2
j = n

if n>1 and type(n)==int:
    print("Esse numero pode ser decomposto em fatores primos.")
    while j>1:
        while j%i==0:
            print(i)
            j = j/i
        i = i + 1           
elif type(n)!=int:
    print("O numero dever ser do tipo inteiro.")
else:
    print("Esse numero nao pode ser decomposto em fatores primos.")

