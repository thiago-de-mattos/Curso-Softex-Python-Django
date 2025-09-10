class Padaria:
    def __init__(self):
        self.quantidade_paes = {
            'frances': 15,
            'doce': 20,
            'forma': 18
        }
        self.valor_paes = {
            'frances': 0.50,
            'doce': 0.70,
            'forma': 1.20
        }
        self.bairros = {
            '1': ('barroco', 5.00),
            '2': ('sao_jose', 15.00)
        }
        self.codigo_venda = 98568

    def dados(self) -> dict:
        """Carregar e retornar um dicionário de dados do produto"""
        return {
            'atendente': "maria",
            "paes": {
                "frances": {"nome": "pao frances", "valor": 0.50},
                "doce": {"nome": "pao doce", "valor": 0.70},
                "forma": {"nome": "pao de forma", "valor": 1.20}
            }
        }

    def escolher_pao(self):
        nomes_pao = ', '.join(self.quantidade_paes.keys())
        escolha = input(f'Temos os pães: {nomes_pao}. Qual pão você deseja?: ')
        if escolha in self.quantidade_paes:
            try:
                quantidade = int(input(f'Quantos pães {escolha} você deseja? '))
            except ValueError:
                print('Quantidade inválida.')
                return None, None
            if quantidade <= self.quantidade_paes[escolha]:
                self.quantidade_paes[escolha] -= quantidade
                return escolha, quantidade
            else:
                print(f'Infelizmente só temos {self.quantidade_paes[escolha]} pães {escolha} disponíveis')
                return None, None
        else:
            print('Pão não disponível.')
            return None, None

    def calcular_valor(self, escolha, quantidade):
        if escolha and quantidade:
            return quantidade * self.valor_paes[escolha]
        return 0

    def escolher_entrega(self):
        forma_retirada = input('É para entregar ou retirar? ')
        if forma_retirada.lower() == 'entregar':
            bairro_entrega = input('Qual o seu bairro? (1:barroco, 2:sao_jose) ')
            if bairro_entrega in self.bairros:
                bairro_nome, valor_frete = self.bairros[bairro_entrega]
                print(f'Valor do frete para {bairro_nome} é {valor_frete}')
                return valor_frete
            else:
                print('Fora da área de entrega')
                return None
        elif forma_retirada.lower() == 'retirar':
            print('Você escolheu retirar o pedido')
            return 0
        else:
            print('Opção inválida.')
            return None

    def solicitar_dados_cliente(self):
        nome = input('Por favor, informe seu nome: ')
        forma_pagamento = input('Qual a forma de pagamento? (1:dinheiro, 2:cartão) ')
        forma_pagamento = 'dinheiro' if forma_pagamento == '1' else 'cartão'
        return nome, forma_pagamento

    def realizar_pedido(self):
        dados = self.dados()
        print(f'-- Bem-vindo à padaria Desespero, sou a atendente {dados["atendente"]} --')
        escolha, quantidade = self.escolher_pao()
        if not escolha or not quantidade:
            return

        valor_total_paes = self.calcular_valor(escolha, quantidade)
        print(f'Você pediu {quantidade} pães {escolha}, o valor total é {valor_total_paes}')

        valor_frete = self.escolher_entrega()
        if valor_frete is None:
            return

        nome_cliente, forma_pagamento = self.solicitar_dados_cliente()
        self.codigo_venda += 1

        print(f'O valor total do seu pedido é: {valor_total_paes + valor_frete}')
        print(f'Cliente: {nome_cliente}, Pagamento: {forma_pagamento}, Código do pedido: {self.codigo_venda}')
        
        if __name__ == "__main__":
            padaria = Padaria()
            padaria.realizar_pedido()

        print('bairo fora da area de entrega ')
        return