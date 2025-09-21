class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        self.acervo = []  

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' de {livro.autor} adicionado ao acervo.")

    def listar_livros(self):
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            print("\n Livros na biblioteca:")
            for livro in self.acervo:
                print(f"- {livro.titulo}, de {livro.autor}")

biblioteca = Biblioteca()


livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Hobbit", "J.R.R. Tolkien")
livro3 = Livro("20.000  léguas submarinas", "Julio Verne")


biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)


biblioteca.listar_livros()