class ItemInventario:
    def __init__(self, nome, quantidade, valor_unt):
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unt = valor_unt

    def valor_total(self):
        pass

class Perecivel(ItemInventario):
    def __init__(self, nome, quantidade, valor_unt, data_validade):
        super().__init__(nome, quantidade, valor_unt,)
        self.data_validade = data_validade

class Inventario:
    def __init__(self, lista):
        self.lista = lista