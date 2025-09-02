class Numero_telefone:
    def __init__(self,numero):
        self.numero = numero
    
    def validacao(self):
        if not self.numero.isdigit():
            return False,'o numero deve conter apenas digitos'
        
        if len(self.numero) != 11:
            return False , 'o numero deve conter exatamente 11 carecteres'
        
        for i in self.numero:
            cout = 0
            for d in self.numero:
                if d == i:
                    cout += 1
            if cout >= 3:
                return False, f'o numero{self.numero} não pode ter 3 digitos repitidos '
        

