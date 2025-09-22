class Pessoas:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
       
    @nome.setter
    def nome(self, novo_nome:str):
        if isinstance(novo_nome, str) and novo_nome :
             self._nome = novo_nome
        else:
            print("precisa de uma str, não vazia")

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor:int):
        if isinstance(valor, int) and valor > 0:
            self._idade = valor
        else:
            print("valor incoreto")

pessoa = Pessoas("Thiago", 21)

"""print(pessoa.nome)
pessoa.nome = "tiago"
print(pessoa.nome)"""

pessoa.idade = -5
print(pessoa.idade)
