import random

def intersecao_lista():

    lista1 = random.sample(range(0, 11), 10)
    lista2 = random.sample(range(0, 11), 10)

    print(f'lista1: {lista1}')
    print(f'lista1: {lista2}')

    intersecao = list(set(lista1) & set(lista2))

    return intersecao

resultado = intersecao_lista()
