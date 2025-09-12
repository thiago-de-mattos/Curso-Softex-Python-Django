class Analisador:

    def __init__(self, frase:str):
        self.frase = frase
        self.frase_limpa = frase.lower()
        
    def contador_de_palavras(self):
        return len(self.frase.split())
    
    def contador_de_vogais(self):
        contador = 0
        vogais = 'aeiou'
        for letra in self.frase_limpa:
            if letra in vogais:
                contador += 1
        return contador
    
    def contador_consoantes(self):
        contador = 0 
        vogais = "aeiou"
        for letra in self.frase_limpa:
            if letra.isalpha() and letra not in vogais:
                contador += 1
        return contador
        
    def eh_palindromo(self):
        farse_junta = "".join(self.frase_limpa.split())
        return farse_junta == farse_junta[::-1]
    
    def resultados(self):
        print('\n### Resumo da análise ###')
        print(f'quantidade de palavras: {self.contador_de_palavras()}')
        print(f'quantidade de vogais: {self.contador_de_vogais()}')
        print(f'quantidade de consoantes: {self.contador_consoantes()}')
        print(f'é um palíndromo: {self.eh_palindromo()}')

frase_digitada = input('digite a frase que vai ser analisada: ')
analisador = Analisador(frase_digitada)
analisador.resultados()