# Normalmente as variaveis globais sao definidas nas primeiras linhas do codigo

PI = 3.1415926 # PI: global

def dobra_lista(lista):
    nova_lista = [] #variavel local
    for elemento in lista:
        nova_lista.append(2*elemento)
    return nova_lista
    
def circunferencia(R):
    #PI = 5 # variavel local sempre tem preferencia
    return 2*PI*R  # R e local, PI e global


if __name__=="__main__":  #essa linha de comando faz com que ao importar o modulo em outros codigos, tudo que esta dentro desse if nao seja executado no codigo. Por exemplo, essas informacoes contidas dentro do if so serao executadas se o codigo modulo_aula6 for executado. Quando importamos o modulo na aula 6, apenas a funcao que estamos executando na aula 6 eh executada.

    lista1 = [3,5,6,1]
    dobro_lista1 = dobra_lista(lista1)
    print(dobro_lista1)

    r = 3
    circ = circunferencia(r)
    print(r, circ)
