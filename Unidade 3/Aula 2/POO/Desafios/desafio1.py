class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.views = 0

    def play(self):
        self.views += 1
        print(f"A musicia {self.titulo} esta sendo tocada")

titulo = input("")


      