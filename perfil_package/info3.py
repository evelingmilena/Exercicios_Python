def acesso_usuario(email, senha):
    if len(senha) < 7:
        print("A senha deve conter pelo menos 8 caracteres.")
    else:
        login = {"email":email, "senha":senha}
    return login
    


    
