class Produto:

    def __init__(self, nome, valor:float):
        self.nome =nome
        self.valor = valor

    def apresentar(self):
       print(f"{self.nome} tem o valor R$:{self.valor:.2f}")
    
produto_1 = Produto("Caderno",15.50)
produto_2 = Produto("Caneta",3.00)

produto_1.apresentar()
produto_2.apresentar()