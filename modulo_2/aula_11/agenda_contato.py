class Agenda:

    def __init__(self):
        self.contato =  {}
        
    def agenda_contato(self):
        while True:
            
            try:
                print("meus contatos escolhas \n(1) para adicionar contatto \n(2)para buscar um contato \n(3) para sair")
                escolha = input("digite sua escolha: ")
                if escolha == '3':
                    print('voce saiu até a proxima')
                    break
                elif escolha == '1':
                    nome = input("digite o nome do novo contato: ").lower()
                    self.contato [nome] = input('digite o numero: ')
                    self.lista = []
                    self.lista.append(self.contato)

                elif escolha == "2":
                    buscar = input("digite o nome do contato que você busca: ").lower()
                    
                    if buscar in self.contato:
                        print("voce achou!!")
                        print(self.contato)
                    else:
                        print('não existe!!')
                        print(self.contato)
                else:
                    print('opção não encontrada')

            except ValueError:
                print("error")
                
agenda = Agenda()
agenda.agenda_contato()