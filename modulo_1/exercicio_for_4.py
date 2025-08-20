altura = int(input('digite a altura da piramide: '))
for i in range(altura):
    linha = ''
    for j in range(i + 1):
        linha += '*'
    print(linha)