

pot_max = 3
expoente=0
while expoente < pot_max:
    total = 0
    n = 10 ** expoente
    expoente = expoente + 1
    i = 0
    while i < n:
        fracao = 1 / n
        total = total + fracao
        i = i + 1
    erro = total-1
    print("O erro de ponto flutuante para n=10**",expoente," e: ",erro)
