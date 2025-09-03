class Loja:

    def __init__(self):
        self.estoque_principal = [('Camisa', 101), ('Calça', 102),('bone', 103), ('Tenis',104)]
        self.estoque_online = [('Bone', 103), ('Camisa Polo', 105), ('calça', 102), ('Chinelo',)]
        self.novo_estoque_1 = set ()
        self.novo_estoque_2 = set ()


    def descubra(self):
        em_comum = self.novo_estoque_1.intersection(self.novo_estoque_2)
        print(f'Os produtos em comum{em_comum}')
        principal = self.novo_estoque_1.difference(self.novo_estoque_2)
        print(principal)
        online = self.novo_estoque_2.difference(self.novo_estoque_1)
        principal(online)


loja = Loja()

loja.descubra()