class Sistema:

    def __init__(self):
        self.acessos = [('Pedro','sucesso'), ('Ana', 'falha'), ('Maria', 'sucesso'), ('Pedro', 'falha'), ('Ana', 'falha')]
        self.sucessos = set()
        self.falha = set ()
    
    def verificar(self):
        for usuario, login in self.acessos:
            if login == 'sucesso':
                self.sucessos.add(usuario)
            else:
                self.falha.add(usuario)

        somente_falha = self.falha - self.sucessos
        print(f'Usuarios com pelo menos um login bem-sucedido: {self.sucessos}')

        print(f'\nUsuarios com somente falhas: {somente_falha}')

sistema = Sistema()
sistema.verificar()
    