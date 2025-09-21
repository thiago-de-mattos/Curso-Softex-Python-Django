class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0  

    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Abastecido com {litros} litros. Combustível atual: {self.nivel_combustivel} litros.")

    def dirigir(self, distancia):
        consumo = distancia / 10  
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"O carro {self.modelo} percorreu {distancia} km.")
            print(f"Combustível restante: {self.nivel_combustivel:.1f} litros.")
        else:
            print("Combustível insuficiente para a viagem.")

carro1 = Carro("Mustang")

carro1.abastecer(5)     
carro1.dirigir(30)       
carro1.dirigir(30)