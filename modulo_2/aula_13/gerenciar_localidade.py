def cadastrar_localidade(bairros: dict)-> None:
    '''permite ao atendente cadastrar um novo bairro para entrega'''
    nome_bairro = input("digite o nome do bairro:  ").lower().strip()
    if nome_bairro in bairros:
        print("Erro! bairro já cadastrado")
        return
    try:
        nome_completo = input("Digite o nome completo do bairro: ").strip()
        valor_frete = float(input(f"Digite o valor do frete para o bairro {nome_completo}: "))

        if nome_bairro and valor_frete >= 0 and nome_completo:
            bairros = [nome_bairro] = {"nome": nome_completo, "frete": valor_frete}
            print(f"Localidade {nome_completo} com frete de {valor_frete:.2f} cadastrado com sucesso")

        else:
            print("Dados inválidos. O cadastro não foi realizado")
            return
    except ValueError:
        print("entrada invalida! O valor do frete deve ser um numero.")
