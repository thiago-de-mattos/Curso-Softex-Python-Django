class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"

meu_filme = Filme("De Volta para o Futuro", "Robert Zemeckis", 1985)

print(meu_filme)
