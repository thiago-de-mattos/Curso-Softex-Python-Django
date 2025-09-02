class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def positivos(self):
        return self.a > 0 and self.b > 0 and self.c > 0 
    
    def soma(self):
        return (self.a < self.b + self.c) and (self.b < self.a + self.c) and (self.c < self.a + self.b)
    
    def diferenca(self):
        return (self.a > abs(self.b - self.c)) and (self.b > abs(self.a - self.c)) and (self.c > abs(self.a - self.b))
    
    def triangulo(self):
        if self.positivos() and self.soma() and self.diferenca():
            print("Os lados formam um triângulo!\n")
        else:
            print("Os lados NÃO formam um triângulo.\n")


while True:
    a = input("Digite o lado A: ")
    b = input("Digite o lado B: ")
    c = input("Digite o lado C: ")

    
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit() and c.replace('.', '', 1).isdigit()):
        print("Por favor, digite apenas números positivos.\n")
        continue

    
    a, b, c = float(a), float(b), float(c)

    triangulo = Triangulo(a, b, c)
    triangulo.triangulo()

