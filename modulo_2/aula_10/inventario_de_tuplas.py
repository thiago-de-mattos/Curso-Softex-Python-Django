class Loja:

    def __init__(self):
        self.estoque_principal = [
            ('Camisa', 101),
            ('Calça', 102),
            ('Boné', 103),
            ('Tênis', 104)
        ]
        self.estoque_online = [
            ('Boné', 103),
            ('Camisa Polo', 105),
            ('Calça', 102),
            ('Chinelo', 106)
        ]
        self.novo_estoque_1 = set()
        self.novo_estoque_2 = set()

    def descubra(self):
        for nome, codigo in self.estoque_principal:
            self.novo_estoque_1.add(codigo)

        for nome, codigo in self.estoque_online:
            self.novo_estoque_2.add(codigo)

        em_comum = self.novo_estoque_1.intersection(self.novo_estoque_2)
        print(f'Produtos em comum: {nome} {em_comum}')

        apenas_principal = self.novo_estoque_1.difference(self.novo_estoque_2)
        print(f'Apenas no estoque principal: {nome} {apenas_principal}')

        apenas_online = self.novo_estoque_2.difference(self.novo_estoque_1)
        print(f'Apenas no estoque online: {nome} {apenas_online}')

loja = Loja()
loja.descubra()