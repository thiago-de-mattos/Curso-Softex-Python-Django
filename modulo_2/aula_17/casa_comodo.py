class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = []
        
    def adicionar_comodo(self,nome):
        comodo = Comodo(nome)
        self.comodos.append(comodo)

    def listar_comodo(self):
        print('listando cômodos:')
        for comodo in self.comodos:
            print(f'-{comodo.nome}')
        
casa = Casa()
casa.adicionar_comodo("Sala")
casa.adicionar_comodo("Cozinha")
casa.adicionar_comodo("Quarto")

casa.listar_comodo()