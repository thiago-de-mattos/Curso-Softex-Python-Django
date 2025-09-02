class Robo:
    def __init__(self):
        self.posicao = 0

    def avancar(self,valor:int):
        self.posicao += valor
        print(f'\nrobo avançou {valor} passos\n')

    def recuar(self, valor):
        self.posicao -= valor
        print(f'\nrobo recuou {valor} passos\n')
    
    def status(self):
       print(f' o robo esta na posição: {self.posicao}º')

def menu():
    print('menu de escolhas:\nopções\n1:avançar\n2:recuar\n3:status\n4:sair')
    return int(input('digite sua escolha: '))
        

robo = Robo()

while True:
    opcao = menu()
    if opcao == 1:
        posisao_atual = int(input('digite o quanto vc quer avançar: '))
        robo.avancar(posisao_atual)
    
    elif opcao == 2:
        posisao_atual = int(input('digite o quanto vc quer recuar: '))
        robo.recuar(posisao_atual)
    
    elif opcao == 3:
        robo.status()
    elif opcao == 4:
        print('você saiu, até logo')
        break
    else:
        print('você não digitou uma das opções, digite somente numeros')
    