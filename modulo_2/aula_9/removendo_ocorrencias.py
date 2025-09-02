class Remove:
    def __init__(self):
        self.numero = 5
        self.lista = [1, 5, 2, 5, 3, 5, 4]

    def remover(self):
        if self.numero not in self.lista:
            print('Número não existe  na lista, nada acontece')
        else:
            nova_lista = []
            for item in self.lista:
                if item != self.numero:
                    nova_lista.append(item)
            self.lista = nova_lista
        return self.lista


remove = Remove()
print(f'A lista após remover o número {remove.numero} é: {remove.remover()}')