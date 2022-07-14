"""
Este codigo recebe informacoes de um usuario para a criacao de um perfil na internet.
"""

import perfil_package as perfil

nomecompleto = perfil.nome_completo("Eveling","Costa")
data = perfil.data_nascimento("03","07","1991")
endereco = perfil.endereco_pessoa("Rua Trajano Reis", 185,"Jardim das Vertentes","Sao Paulo","SP")
profissao = perfil.profissao_pessoa("Estudante")
email = perfil.email_pessoa("evelingmilena@usp.br")



#Agora vamos imprimir as informacoes do usuario

print("***** Perfil de Usuario *****\n")
print("Nome completo:",nomecompleto)
print("Endereco:",endereco)
print("Data de Nascimento:",data)
print("Profissao:",profissao)
print("E-mail:",email)




