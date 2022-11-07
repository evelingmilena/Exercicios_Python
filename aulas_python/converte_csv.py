nome_arquivo = "tabelaPsi5.csv"
novo_arquivo = "nova" + nome_arquivo

with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

with open(novo_arquivo, "w") as arquivo:
    for linha in linhas:
        nova_linha = linha.replace('}","{', '\n').replace("*^", "e").replace('"{','').replace('}"','')
        arquivo.write(nova_linha)
