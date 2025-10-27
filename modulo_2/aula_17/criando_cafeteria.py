class GraoDeCafe:
    def __init__(self):
        pass

    def moer(self):
        print('Os grãos de café foram moidos')

class Agua:
    def __init__(self):
        pass

    def aquecer(self):
        print('A água esta aquecida')

class Cafeteria:
    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()

    def preparar_cafe(self):
        self.grao.moer()
        self.agua.aquecer()
        print('\nSeu café esta pronto')

cafeteria = Cafeteria()
cafeteria.preparar_cafe()