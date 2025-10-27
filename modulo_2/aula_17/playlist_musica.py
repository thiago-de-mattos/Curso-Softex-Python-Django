class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista


class Playlist:
    def __init__(self):
        self.musicas = []  

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)

    def tocar_playlist(self):
        print(" Tocando playlist:")
        for musica in self.musicas:
            print(f"Tocando '{musica.titulo}' de {musica.artista}")


m1 = Musica("Imagine", "John Lennon")
m2 = Musica("Shape of You", "Ed Sheeran")
m3 = Musica("Bohemian Rhapsody", "Queen")


p = Playlist()
p.adicionar_musica(m1)
p.adicionar_musica(m2)
p.adicionar_musica(m3)

p.tocar_playlist()

p.remover_musica(m2)

print("\nApós remover uma música:")
p.tocar_playlist()
