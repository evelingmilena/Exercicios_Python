class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def pessoa(self):
        print("Meu nome é",self.nome,"e tenho", self.idade, "anos.")


p1 = Pessoa("Eveling", 31)

p1.pessoa()
