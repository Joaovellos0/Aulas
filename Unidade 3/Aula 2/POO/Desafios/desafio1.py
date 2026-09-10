import os


def limpar():
    os.system("cls")


class Musica:
    def __init__(self, titulo:str, artista:str):
        self.titulo = titulo
        self.artista = artista
        self.views = 0

    def play(self):
        self.views += 1
        print(f"A musicia {self.titulo} de {self.artista} esta sendo tocada")
        print(f"Vezes tocadas: {self.views}")


escolha_usuario = Musica(
    input("Escreva o nome da musica:\n"), input("Escreva o nome do artista:\n")
)


while True:

    escolha_usuario.play()
    opcao = input("Aperte (0) caso queira parar. ")

    if opcao == "0":
        break
    else:
        limpar()
        continue
