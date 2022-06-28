
#Codigo de ponto flutuante com laco de repeticao for.

pot_max = 3

for exp in range(pot_max):
    total = 0
    n = 10**exp
    for i in range(n):
        fracao = 1/n
        total = total + fracao
    erro = total - 1
    print("O erro para 10**",exp,"e",erro)

#Codigo de fatoracao em numeros primos utilizando laco de repeticao for.

num = 20
n = num

for i in range(2,n):
    if num%i == 0:
        num = num/i
        print(i)
   
        
        
        
        
        
        
    
    
     
    
