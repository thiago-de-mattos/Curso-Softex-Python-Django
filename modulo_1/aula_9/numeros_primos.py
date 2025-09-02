class Primo:
    def __init__(self):
        self.numero = [2,3,4,5,6,7,8,9,10]
        self.primos = []

    def verifica_primos(self):
        for i in self.numero:
            self.eh_primo = True
            for j in range(2, i):
                if i % j == 0:
                    self.eh_primo = False
                    break
            if self.eh_primo:
                    self.primos.append(i)
        
        print(self.primos)

primo = Primo()
primo.verifica_primos()