palavra = input('digite uma frase: ').lower
vogais = 'aeiou'
contador = 0
for i in palavra:
    if i in vogais:
        contador += i
print(contador)
