'''
Leitura de arquivos txt
'''

nome_arquivo = "poema.txt"
arquivo = open(nome_arquivo, "r")

print(arquivo)

linhas = arquivo.readlines()

print(type(arquivo), type(linhas))
print(linhas)

for linha in arquivo: #linhas:
    print(linha, end="")

arquivo.close()


novo_arquivo = "poema_copiado.txt"

with open(novo_arquivo, "w") as arquivo:
    arquivo.write("Título: Canção do Exílio\n\n")
    for linha in linhas:
        arquivo.write(linha)


# Importante estudar os outros modos: r+, a, a+
