class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"titulo:{self.titulo} ducação:{self.duracao_seg}")

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"titulo da Musica:{self.titulo} ducação:{self.duracao_seg}seg, Artista: {self.artista}")
  
class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"titulo:{self.titulo} ducação:{self.duracao_seg}seg resolução:{self.resolucao}")


colecao = {
    "musica": [],
    "video": []
}

colecao["musica"].append(Musica("cold", 220, "Marron 5"))
colecao["musica"].append(Musica("viva la vida", 330, "Cold-play"))
colecao["musica"].append(Video("aula_python", 220, "1080p"))
colecao["musica"].append(Video("alanzoka jogando fre fire", 1000, "4k"))

for demostracao in colecao.values():
    for i in demostracao:
        i.exibir()
        
