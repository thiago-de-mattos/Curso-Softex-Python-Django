class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem motor de {self.motor.potencia} cavalos de potência.")

carro1 = Carro("Gol", 150)
carro2 = Carro("Ferrari", 500)

carro1.exibir_potencia()
carro2.exibir_potencia()