"""
Este codigo recebe informacoes de um usuario para a criacao de um perfil na internet.
"""

import perfil_package as perfil

nomecompleto = perfil.nome_completo("Eveling","Costa")
idade = perfil.idade_pessoa(18)
sexo = perfil.sexo_pessoa("feminino")
end = perfil.endereco_pessoa("Rua Trajano Reis, nº 185, Jardim das Vertentes")
nac = perfil.nacionalidade_pessoa("brasileira")
cidade = perfil.naturalidade_pessoa("Sao Luis - MA")
prof = perfil.profissao_pessoa("Estudante")
email1 = perfil.email_pessoa("evelingmilena@usp.br")
tel = perfil.telefone_pessoa("(98) 98179-0084")

#Agora vamos imprimir as informacoes do usuario

print("***** Perfil de Usuario *****\n")
print("Nome completo:",nomecompleto)
print("Idade:",idade)
print("Sexo:",sexo)
print("Endereco:",end)
print("Nacionalidade:",nac)
print("Naturalidade:",cidade)
print("Profissao:",prof)
print("E-mail:",email1)
print("Telefone:",tel)

