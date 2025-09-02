class Codificador_Decodificador:

    def codificar(self,frase:str):
        codificada = frase.replace('a','1').replace('e','2').replace('i','3').replace('o', '4').replace('u','5')
        return codificada
    
    def decodificar(self,frase_codificada:str):
        descodificada = frase_codificada.replace('1','a').replace('2','e').replace('3','i').replace('4', 'o').replace('5','u') 
        return descodificada
    
texto = input('Digite uma frase: ').lower()

cripito = Codificador_Decodificador()

frase_codificada = cripito.codificar(texto)
print(f'frase codificada: {frase_codificada}')

frase_decodificada = cripito.decodificar(texto)
print(f'frase decodificada: {frase_decodificada}')