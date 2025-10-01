from escola import Escola
from estudante import Estudante
from pessoa import Pessoa

escola = Escola("Escolinha do Anderson")

aluno1  = Estudante("Thiago", 21, "ra2035")
aluno2  = Estudante("Ana", 22, "ra9387")

aluno1.adicionar_nota("Matematica", 9.0)
aluno1.adicionar_nota("Historia", 8.0)

aluno2.adicionar_nota("Matematica", 8.0)
aluno2.adicionar_nota("Historia", 7.0)

escola.adicionar_estudante(aluno1)
escola.adicionar_estudante(aluno2)