class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        return print("método de classe")
    
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    
    def fazer_som(self):
        print("au au")

class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie
    
    def fazer_som(self):
        return print("miau!!")

cao = Cachorro("rex", 3, "vira-lata")
print(f"{cao.idade} anos")
print(cao.nome)
print({cao.raca})

gato = Gato("Felix", 2, "persa")
print(gato.nome)
print(gato.idade)
def emetir_som(animal:Animal):
    animal.fazer_som()

emetir_som(cao)
emetir_som(gato)
