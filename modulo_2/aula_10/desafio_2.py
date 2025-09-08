class AnaliseAcessos:
    def __init__(self):
        self.registros_acessos = []       
        self.usuarios_sucesso = set()    
        self.tempo_total_sucesso = 0      

    def adicionar_acesso(self, usuario, status_opcao, duracao):
        
        if status_opcao not in [1, 2]:
            print("Opção de status inválida.")
            return

        status = "sucesso" if status_opcao == 1 else "falha"

        registro = (usuario, status, duracao)
        self.registros_acessos.append(registro)

        if status == "sucesso":
            self.usuarios_sucesso.add(usuario)
            self.tempo_total_sucesso += duracao

        print("Registro adicionado!\n")

    def mostrar_resultados(self):
        print("Registros de acessos:", self.registros_acessos)
        print("Usuários com pelo menos um acesso bem-sucedido:", self.usuarios_sucesso)
        print("Tempo total de sessões bem-sucedidas:", self.tempo_total_sucesso, "minutos")


analise = AnaliseAcessos()

while True:
    usuario = input("Digite o nome do usuário (ou 'parar' para encerrar): ")
    if usuario.lower() == "parar":
        break

    print("Escolha o status do acesso:")
    print("1 - sucesso")
    print("2 - falha")
    try:
        status_opcao = int(input("Digite a opção (1 ou 2): "))
    except ValueError:
        print("Entrada inválida. Registro descartado.\n")
        continue

    try:
        duracao = int(input("Digite a duração da sessão em minutos: "))
    except ValueError:
        print("Duração inválida. Registro descartado.\n")
        continue

    analise.adicionar_acesso(usuario, status_opcao, duracao)

analise.mostrar_resultados()
