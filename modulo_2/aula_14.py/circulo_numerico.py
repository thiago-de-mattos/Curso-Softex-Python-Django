class Circulo:

    def __init__(self, valor):
        self._raio = valor

    @property
    def raio(self) -> int:
        return self._raio
    
    @raio.setter
    def raio(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._raio = valor
        else:
            print("erro!")

    def calcula_area(self):
        calculo = 3.14 *(self._raio ** 2)
        return calculo
    
calculo_area = Circulo(10)
print(calculo_area.calcula_area())
