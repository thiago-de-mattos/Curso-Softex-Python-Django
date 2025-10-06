from modulo_3.aula_18.estudante import Estudante

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []

    def adicionar_estudante(self, estudante: Estudante):
        self.estudantes.append(estudante)

    def mostrar_relatorio(self):
        print(f"Escola: {self.nome}")
        for aluno in self.estudantes:
            print(f"Nome:{aluno} {aluno}")
            
