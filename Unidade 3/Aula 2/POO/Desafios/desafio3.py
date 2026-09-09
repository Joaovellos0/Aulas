import os
import time


def limpar():
    os.system("cls")


class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.experiencia = 0

    def character_sheet(self):
        print(f"Seu Personagem\nNome: {self.nome}\nNível: {self.nivel}")

    def ganhar_xp(self):
        while self.nivel <= 10:

            if self.nivel == 10:
                print(f"{self.nome} atingiu o nivel maximo.")
                break
            else:
                escolha = input("aperte (ENTER) para ganhar xp.")
                limpar()

                if escolha == "":
                    xp = 10
                    self.experiencia += xp
                    print(f"{self.nome} ganhou +{xp} de xp")
                    print(f"Próximo nível ({self.experiencia}%)")
                    time.sleep(1.2)
                    limpar()

                    if self.experiencia >= 100:
                        nivel_anterior = self.nivel
                        self.nivel += 1
                        self.experiencia -= self.experiencia
                        print(
                            f"{self.nome} subiu de nivel: {nivel_anterior} → {self.nivel}\n"
                        )
                        novo_personagem.character_sheet()
                        time.sleep(2.5)
                        limpar()


novo_personagem = Personagem(input(f"Qual o nome do herói: "))

novo_personagem.ganhar_xp()
