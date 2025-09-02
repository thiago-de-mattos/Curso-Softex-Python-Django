"""
Comércio Padaria
1- o progama tem que rodar em loop infinito até ser parado
2- cliente pedir tipo de pão ( francês, doce, forma)
3- cada pão vai ter uma quantidade 
4- valor do pão
5- pedir forma de pagamento (dinheiro, cartão)
6- forma de entrega
7- dados do cliente (se for entregar)
8- valor de frete por bairro
9- nome do atendente
10- codigo da entrega
"""
# desafio.py
# nomes dos pães
nome_frances =  'frances'
nome_doce =  'doce'
nome_forma =  'forma'
#valores dos pães
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.00
#quantidade de pães
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18
#nome do atendente
nome_atendente = 'maria'
#nomes dos bairros
bairro_baroco = 'barroco'
bairro_sao_jose = 'sao_jose'
#valores do frete
frete_barroco = 5.00
frete_sao_jose = 15.00
#codigo de venda
codigo_venda = 98568

while True:
    print(f'-- bem-vindo a padaria Desespero, sou a atendente {nome_atendente}--')
    escolha = input(f'temos os pâes:{nome_frances}, {nome_doce}, {nome_forma} qual pao voce deseja?: ')
    if escolha == nome_frances:
        quantidade = int(input(f'quantos pães {nome_frances} voce deseja? '))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            print(f'voce pediu {pedido_de_paes} pães {nome_frances}, o valor total é {quantidade * valor_frances}')
        else:
            print(f'infelizmente so temos {quantidade_frances} pães {nome_frances} disponiveis')
            break
    
    forma_retirada = input('é para entregar ou retirar? ')
    if forma_retirada.lower() == 'entregar':
        bairro_entrega = input(f'qual o seu bairro? (1:{bairro_baroco}.2:{bairro_sao_jose}) ')
        if bairro_entrega == '1':
          valor_frete = frete_barroco
          print(f'valor do frete para {bairro_baroco} é {valor_frete}')
        elif bairro_entrega == '2':
          valor_frete = frete_sao_jose
          print(f'valor do frete para {bairro_sao_jose} é {valor_frete}')   
        else:
          print('fora da area de entrega')
          break
    elif forma_retirada.lower() == 'retirar':
        print('voce escolheu retirar o pedido')
        valor_frete = 0
    else:
        break

    dados_do_cliente = input('por favor, informe seu nome: ')
    forma_pagamento = input('qual a forma de pagamento? (1:dinheiro. 2:cartão) ')
    if forma_pagamento == '1':
        forma_pagamento = 'dinheiro'
    else:
       forma_pagamento = 'cartão'
    
    codigo_atual = codigo_venda + 1

    print(f'O valor total do seu pedido é: {quantidade * valor_frances + valor_frete}')
    break
