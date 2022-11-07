"""
Este codigo recebe informacoes de um usuario para a criacao de um perfil na internet.
"""

import perfil_package as perfil

#nomecompleto = perfil.nome_completo("Eveling","Costa")
nome = "Eveling"
sobrenome = "Costa"
dia = "03"
mes = "07"
ano = "1991"
logradouro = "Rua Trajano Reis"
numero = "185"
bairro = "Jardim das Vertentes"
cidade = "Sao Paulo"
estado = "SP"
email = "evelingmilena@usp.br"
senha = "12345678"
novoemail = "evelingmilena@gmail.com"
novasenha = "novasenha123"

perfilcompleto = perfil.monta_perfil(nome,sobrenome,dia,mes,ano,logradouro,numero,bairro,cidade, estado,email,senha)


#Agora vamos imprimir as informacoes do usuario

print("***** Perfil de Usuario *****\n")

print(perfilcompleto)
login = perfil.altera_login(email,senha,novoemail,novasenha)
perfil_alterado = perfil.monta_perfil(nome,sobrenome,dia,mes,ano,logradouro,numero,bairro,cidade, estado,novoemail,novasenha)
print("\n")
print(perfil_alterado)



