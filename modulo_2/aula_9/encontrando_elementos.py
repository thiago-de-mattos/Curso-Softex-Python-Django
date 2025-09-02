class Elementos:

    def __init__(self):
        self.lista1 = ['vermelho', 'azul', 'verde', 'amarelo']
        self.lista2 = ['verde', 'roxo', 'azul', 'preto']
        self.lista_nova = []

    def encontrar(self):
        for i in self.lista1:
            if i in self.lista2 and i not in self.lista_nova:
                self.lista_nova.append(i)
        print(self.lista_nova)

Element = Elementos()
Element.encontrar()