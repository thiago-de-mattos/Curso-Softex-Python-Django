class Analise:

    def __init__(self):
        self.produtos_unicos = set()
        self.vendas = [
            ('Teclado', 50, 1),
            ('Mouse', 25.50, 4),
            ('Monitor', 700, 1),
            ('Fone', 45, 1),
            ('Webcan', 75.20, 2)
]       
        self.vendas_filtradas = []

    def filtragem(self):
        for produto, preco, qtd in self.vendas:
             total = preco*qtd
             if total >=100:
                self.vendas_filtradas.append((produto, preco, qtd, total))
                self.produtos_unicos.add(produto)

        return self.vendas_filtradas
                
analise = Analise()
resultado = analise.filtragem()

print(f'Vendas filtradas: ')
for produto, preco, qtd, total in resultado:
    print(f" - {produto}: {qtd} un. x {preco:.2f} = {total:.2f}")

print("\nProdutos únicos filtrados:", analise.produtos_unicos)
