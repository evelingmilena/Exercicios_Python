# Programacao Orientada a Objetos


# e uma classe
class perfil():
    
    # as funcoes de uma classe sao chamadas metodos pq so funcionam para a propria classe
    
    # init e obrigatoria
    # self e apenas o objeto
    def __init__(self, email, senha):
    
        # atributos
        self.email = email
        self.senha = senha
        
    def dados_pessoais(self, nomecompleto, nascimento, endereco):
    
        self.nome = nomecompleto
        self.nascimento = nascimento
        self.endereco = endereco
        
    def altera_senha(self, novasenha):
        if novasenha==self.senha:
            print("Digite uma senha diferente!")


email = "paulo@usp.br"
senha = "paulao123"
perfilpaulo = perfil(email, senha)
nome = "Paulo Henrique"
data = "07/08/1980"
end = "SP"


print(type(perfilpaulo))
print(type(9))

print(perfilpaulo.email)

perfilpaulo.dados_pessoais(nome, data, end)

print(perfilpaulo.nome)



class dados_pessoais():
    
    def __init__(self):
        pass
