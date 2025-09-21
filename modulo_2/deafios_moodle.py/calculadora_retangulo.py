class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)



retangulo = Retangulo(5, 3)


print(f"Área: {retangulo.calcular_area()}")
print(f"Perímetro: {retangulo.calcular_perimetro()}")