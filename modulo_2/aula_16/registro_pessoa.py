class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"nome:{self.nome} idade:{self.idade} anos")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"nome:{self.nome} idade:{self.idade} anos, curso:{self.curso}")

pessoa_1 = Pessoa("Ana", 30)
pessoa_2 = Estudante("Thiago", 21, "Engenharia de Software")

pessoas:list[Pessoa] = [pessoa_1, pessoa_2]

for p in pessoas:
    p.apresentar()
    