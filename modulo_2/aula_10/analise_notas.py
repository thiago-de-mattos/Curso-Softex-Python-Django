class Notas:
    def __init__(self):
        self.notas_alunos = [('Ana', 8.0), 
                             ('João', 8.0), 
                             ('Maria', 10.0), 
                             ('Pedro', 7.5), 
                             ('Ana', 10.0), 
                             ('Carlos', 6.5)
]       
        self.notas_altas = set()
        self.notas_baixas = set()
    
    def analise(self):
        nota = 0
        for nome, nota in self.notas_alunos:
            if nota :
                self.notas_altas.add(nota)
                print(f'A maior nota alcançada é {self.notas_altas}')
                print(f'alunos')
