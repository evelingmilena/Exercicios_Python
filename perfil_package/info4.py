import perfil_package.info1 as info1
import perfil_package.info2 as info2
import perfil_package.info3 as info3

def monta_perfil(nome, sobrenome, profissao,senha):
    nomecompleto = info1.nome_completo
    perfil = [nomecompleto]
    return perfil
    
def atualiza_perfil(perfil,dado):
    perfil.append(dado)
    
def print_perfil(perfil):

