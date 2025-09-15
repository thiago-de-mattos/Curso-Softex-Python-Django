from banco_dados import dados
from calcular_frete import calcula_frete
from dados_clientes import obter_dados_cliente
from dados_pagamento import solicitar_forma_pagamento
from gerar_codigo import gerar_codigo_venda
from gerenciar_localidade import cadastrar_localidade
from gerenciar_produto import cadastrar_produto, atualizar_produto
from processar_pedido import processar_pedido

def iniciar_programa() -> None:
    """ Função que inicia o loop principal do progama de vendas """
    banco_dados = dados()
    atendente = banco_dados["atendente"]
    paes_estoque = banco_dados["paes"]
    bairros_disponiveis = banco_dados["bairros"]
    codigo_venda = banco_dados["codigo_venda_base"]

    while True:
        print(f"-- Bem vindo(a) a Padaria Desespero, sou o(a) atendente {atendente}")
        print("-- Menu Principal --")
        print("1. Iniciar vendas")
        print("2. Gerenciar produtos")
        print("3. Cadastrar nova localidade")
        print("4. Sair do sistema")

        opcao = input("Escolha a uma opção: ")

        if opcao == "1":
            pedido = processar_pedido(paes_estoque)
            
            if not pedido:
                continue

            pao_escolhio, qtd_pedido, valor_compra, paes_estoque = pedido
            print(f"Seu pedido foi de {qtd_pedido} {pao_escolhio['nome']} ficou em R${valor_compra:.2f} ")
            
            forma_retirada = input("É para 1. retirar ou 2. entregar?: ")
            valor_frete = 0.0
            
            if forma_retirada == "2":
                bairro, valor_frete = calcula_frete(bairros_disponiveis)
                print(f"Valor do frete para o bairro {bairros_disponiveis[bairro]['nome']} é de R${valor_frete:.2f}")                

            elif forma_retirada != "1":
                print("opção inválida!")
                continue
            dados_cliente = obter_dados_cliente()
            forma_pagamento = solicitar_forma_pagamento()

            valor_total_compra = valor_frete + valor_compra
            codigo_venda = gerar_codigo_venda(codigo_venda)
            banco_dados["codigo_venda_base"] = codigo_venda

            print("-- Resumo da venda --")
            print(f" Cliente: {dados_cliente['nome']}")
            print(f"Valor dos paes: R${valor_compra:.2f}")
            print(f"Valor do frete: R${valor_frete:.2f}")
            print(f"Forma de pagamento: {forma_pagamento}")
            print(f"Valor total da compra: R${valor_total_compra}")
            print(f"Codigo da entrega:{codigo_venda}")

        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            print("Saindo do sitema. Áte a proxima")
            break
        else:
            print(f"Opção {opcao} invalida!")

i = iniciar_programa()