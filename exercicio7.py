idade = int(input('digite a idade de uma pessoa: '))

if idade <= 12:
    print('voce é uma criança')
elif idade  <= 17:
    print('voce é um adolescente')
elif idade <= 59:
    print('voce é adulto')
elif idade <=99:
    print('vece é um idoso')
else:
    print('voce é um anciâo')