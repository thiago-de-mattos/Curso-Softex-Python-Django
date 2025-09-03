class Notas:
    def __init__(self):
        self.notas_alunos = [
            ('Ana', 8.0), 
            ('João', 8.0), 
            ('Maria', 10.0), 
            ('Pedro', 7.5), 
            ('Ana', 10.0), 
            ('Carlos', 6.5)
        ]       
        self.notas_altas = set()
        self.notas_baixas = set()
    
    def analise(self):
        maior = float('-inf')  
        menor = float('inf')   

        for nome, nota in self.notas_alunos:
           
            if nota > maior:
                maior = nota
                self.notas_altas = {nome} 
            elif nota == maior:
                self.notas_altas.add(nome)

            if nota < menor:
                menor = nota
                self.notas_baixas = {nome}
            elif nota == menor:
                self.notas_baixas.add(nome)

        print(f"\nMaiores notas foram de {self.notas_altas} nota: {maior}")
        print(f"\nMenores notas foram de {self.notas_baixas} nota: {menor}")
      

notas = Notas()
notas.analise()
