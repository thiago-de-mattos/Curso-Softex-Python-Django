class simulador_pedidos:
    def __init__(self):
        self.hamburger = 10.99
        self.codigo = 596079
        self.nome = 'x-tudo'


    def escolha(self,produto):
        if self.nome == produto:
            return True

    def usar_cupom (self, cupom):
        if cupom == self.codigo:
            print('cupo valido 10% de desconto valido')
            return self.hamburger * 0.10
        else:
            print('cupom invalido, nenhum desconto aplicado!!')
            return self.hamburger

def main():
    pedido = simulador_pedidos()

    while True:
        produto = input('digite o nome do produto: ').lower
        if pedido.escolha(produto):
            print(f'Você escolheu: {pedido.nome} - R$ {pedido.hamburger:.2f}')
            break
        else