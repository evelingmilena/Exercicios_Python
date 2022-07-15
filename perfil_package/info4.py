import perfil_package.info1 as info1
import perfil_package.info2 as info2
import perfil_package.info3 as info3

def monta_perfil(nome,sobrenome,dia,mes,ano,logradouro,numero,bairro,cidade, estado,email,senha):
    nomecompleto = info1.nome_completo(nome, sobrenome)
    datanascimento = info1.data_nascimento(dia,mes,ano)
    endereco = info2.endereco_pessoa(logradouro,numero,bairro,cidade,estado)
    login = info3.acesso_usuario(email,senha)
    perfilcompleto = {"Nome":nomecompleto, "Data de Nascimento":datanascimento, "Endereco":endereco,"login":login}
    return perfilcompleto
    
def altera_login(email,senha):
    login = info3.acesso_usuario(email,senha)
    email1 = "evelingmilena@gmail.com"
    senha1 = "senhaatual"
    login.update({"email":email1,"senha":senha1})
    return login

    


