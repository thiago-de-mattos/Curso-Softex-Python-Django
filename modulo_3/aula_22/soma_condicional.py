
def soma_cond():
    dados = {
    'cauan', 25,
    'bia', 30,
    'carlos', '40',
    'vitor', 10,
    'pedro', 8,
    'carol', 15,
    }

    letra_filtrar = 'c'

    contador = 0
    
    for chave, valor in dados.items():
        if chave.startswith(letra_filtrar):
            try:
                contador += (valor)
            except ValueError:
                print('valor invalido para a chave')
            except TypeError:
                print('erro de tipagem ')
    return contador