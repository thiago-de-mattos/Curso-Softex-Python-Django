from interscao_lista import intersecao_lista

def test_intersecao_lista():
    resultado = intersecao_lista()
    assert resultado == {1, 4}