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
    def __init__(self):
        self.estoque = []

    def adicionar_itens(self, item):
        return self.estoque.append(item)

    def remover_item(self, nome):
        if self.estoque != []:
           try:
               for i in range(len(self.estoque)):
                   if self.estoque[i].nome == nome:
                       item_removido = self.estoque.pop(i)
                       print(f'item {item_removido.nome} removido com sucesso!')
                       return
               raise ValueError(f"Item '{nome}' não encontrado no estoque.")
           except ValueError as e:
               print('erro', e)
        else:
            print("estoque vazio nada para remover")