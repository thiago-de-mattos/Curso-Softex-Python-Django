class Cadastrar_usuario:

    def __init__(self,nome,senha):
        self.Cadastrar_usuario = []       
        self.Cadastrar_sucesso = set()         

    def adicionar_acesso(self, usuario, status_opcao):
        
        if status_opcao not in [1, 2]:
            print("Opção de status inválida.")
            return

        registro = (usuario,)
        self.registros_acessos.append(registro)

        if status == "sucesso":
            self.usuarios_sucesso.add(usuario)
            self.tempo_total_sucesso += duracao

        print("Registro adicionado!\n")
