class Analise:

    def __init__(self):
        self.produtos_unicos = set()
        self.vendas = [('Teclado', 50, 1),
                                 ('Mouse', 25.50, 4),
                                 ('Monitor', 700, 1),
                                 ('Fone', 45, 1),
                                 ('Webcan', 75.20, 2)]       
        self.vendas_filtradas = []

    def filtragem(self):
         for produto, preco, qtd in self.vendas:
             self.soma = preco*qtd
             if self.soma >=100:
                self.vendas_filtradas.append(produto, preco, qtd)
                self.produtos_unicos.add(produto)
                
        

analise = Analise()
print(f'Vendas filtradas: {analise.filtragem()} ')
