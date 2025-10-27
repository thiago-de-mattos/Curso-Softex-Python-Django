class Teclado:
    def __init__(self):
        pass
    def ligar(self):
        print('O teclado esta ligando')

class Mouse:
    def __init__(self):
        pass
    def ligar(self):
        print('O mouse esta ligando')

class Monitor:
    def __init__(self):
        pass
    def ligar(self):
        print('O monitor esta ligando')

class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()
        
    def ligar_computador(self):
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()
        print('\npc esta ligando')

computador = Computador()
computador.ligar_computador()