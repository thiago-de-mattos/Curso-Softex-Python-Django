posicao = 0

while True:
    print('menu de escolhas:')
    print('opçôes!')
    print('1:avançar')
    print('2:recuar')
    print('3:status')
    print('4:sair')
    escolha = int(input('digite uma das 4 opçoes:'))
    if escolha == 4:
        print('até logo')
        break
    elif escolha == 1:
        valor = int(input('digite o quanto vc quer avançar: '))
        posicao += valor
        print(f'\nrobo avançou {valor} passos\n')
    elif escolha == 2:
        valor = int(input('digite o quanto vc quer recuar: '))
        posicao -= valor
        print(f'\nrobo avançou {valor} passos\n')
    elif escolha == 3:
        print(f'\nrobo esta na {posicao}º\n')
    else:
        print('você não digitou uma das opções, digite somente numeros')
