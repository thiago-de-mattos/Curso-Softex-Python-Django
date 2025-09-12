class Calculadora:

    def __init__(self):
        self.numero_1 = 0
        self.numero_2 = 0
        self.escolha = ''

    def soma(self):
        return self.numero_1 + self.numero_2
    
    def subtracao(self):
        return self.numero_1 - self.numero_2
    
    def multiplicacao(self):
        return self.numero_1 * self.numero_2
    
    def divisao(self):
        if self.numero_2 == 0:
            print("\nErro: Divisão por zero!")
            return None
        return self.numero_1 / self.numero_2
    
    def main(self):
        while True:
            print('\n=== CALCULADORA ===')
            print('Escolhas:\n 1-Somar\n 2-Subtrair\n 3-Multiplicar\n 4-Dividir\n 5-Sair')
            
            self.escolha = input('Digite a sua escolha entre essas 5 opções: ')
            
            if self.escolha == "5":
                print('\nVocê saiu!!!')
                break

            try:
                self.numero_1 = int(input('Digite o primeiro número: '))
                self.numero_2 = int(input('Digite o segundo número: '))
            except ValueError:
                print('\nErro: Digite somente números!')
                continue

            if self.escolha == '1':
                resultado = self.soma()
                print(f'\nO resultado da soma é: {resultado}')
            elif self.escolha == '2':
                resultado = self.subtracao()
                print(f'\nO resultado da subtração é: {resultado}')
            elif self.escolha == '3':
                resultado = self.multiplicacao()
                print(f'\nO resultado da multiplicação é: {resultado}')
            elif self.escolha == '4':
                resultado = self.divisao()
                if resultado is not None:
                    print(f'\nO resultado da divisão é: {resultado}')
            else:
                print('\nEscolha inválida! Digite somente as opções mencionadas.')

calculadora = Calculadora()
calculadora.main()
