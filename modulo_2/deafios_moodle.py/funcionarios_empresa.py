class Funcionario:
    
    percentual_bonus = 1.10  

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        print(f"{self.nome} recebeu bônus. Novo salário: R${self.salario:.2f}")

funcionario_1 = Funcionario("Ana", 2000)
funcionario_2 = Funcionario("Thiago", 15000)

funcionario_1.aplicar_bonus()
funcionario_2.aplicar_bonus()