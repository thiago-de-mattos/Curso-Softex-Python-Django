from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self._matricula = matricula
        self._notas = {} 

    @property
    def notaS(self):
        return self.nota
    
    def adicionar_nota(self, materia: str, nota: float):
        if materia not in self._notas:
            self._notas[materia] = []
        self._notas[materia].append(nota) 
        print(f"Nota: {nota} adicionda em {materia}")
        

