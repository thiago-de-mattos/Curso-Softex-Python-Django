class FormaGeometrica:
    def __init__(self, cor):
        self.cor = cor

    def calcular_area():
        pass

    def exibir(self):
        return self.cor

class Retangulo(FormaGeometrica):
    def __init__(self, cor, altura, largura):
        super().__init__(cor)
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura
    
class Quadrado(FormaGeometrica):
    def __init__(self, cor, lado):
        super().__init__(cor,)
        self.lado = lado
    
    def calcular_area(self):
        return self.lado + self.lado

resumo:tuple[FormaGeometrica] = (
    Retangulo(" Retangulo azul", 5, 10),
    Quadrado("Quadrado verde", 5)
    )

soma_area = 0

for i in resumo:
    area = i.calcular_area()
    print(f"{i.exibir()} calculo das area: {area}")
    area += soma_area

print(f"soma das Areas: {area}")
        


    
