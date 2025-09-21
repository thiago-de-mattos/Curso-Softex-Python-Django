class Pessoas:

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
    

pessoa_1 = Pessoas("João", 21)
pessoa_2 = Pessoas("Maria", 30)

pessoa_1.apresentar()
pessoa_2.apresentar()
