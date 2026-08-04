import random
import os

def limpar():
    os.system("cls")

mapa_jogador =[
    ["~", "~","~"],
    ["~", "~","~"],
    ["~", "~","~"]
]

mapa_maquina =[
    ["~", "~","~"],
    ["~", "~","~"],
    ["~", "~","~"]
]
#Escolha onde o barco do jogador ira ficar.

print("Onde colocar o barco?:")
LINHA_INICIAL_JOGADOR = int(input("Escolha uma linha:"))
COLUNA_INICIAL_JOGADOR = int(input("Escolha uma coluna:"))
mapa_jogador[LINHA_INICIAL_JOGADOR][COLUNA_INICIAL_JOGADOR] = "o"

#Escolha da máquina.

LINHA_INICIAL_MAQUINA = random.randint(0,2)
COLUNA_INICIAL_MAQUINA = random.randint(0,2)

#Inicia o jogo.
while True:

    print("Você ataca!")
    
    while True:
        escolha_linha_jogador = int(input("Escolha uma linha:"))
        escolha_coluna_jogador = int(input("Escolha uma coluna:"))
        limpar()

        if mapa_maquina[escolha_linha_jogador][escolha_coluna_jogador] == "x":
            continue
        else:
            break

    if escolha_linha_jogador == LINHA_INICIAL_MAQUINA and \
    escolha_coluna_jogador == COLUNA_INICIAL_MAQUINA:
        print(V="Você Ganhou!")
        break
    
    else:
        print("Você errou.")
        mapa_maquina[escolha_linha_jogador][escolha_coluna_jogador] = "x"
        
        for linha in mapa_maquina:
            print("  ".join(linha))

    print("É a vez da máquina")
    
    while True:
        escolha_linha_maquina = random.randint(0,2)
        escolha_coluna_maquina = random.randint(0,2)
        
        if mapa_jogador[escolha_linha_maquina][escolha_coluna_maquina] == "x":
            continue
        else:
            break

    if escolha_linha_maquina == LINHA_INICIAL_JOGADOR and \
        escolha_coluna_maquina == COLUNA_INICIAL_JOGADOR:
        print("A máquina venceu!")
        break

    else:
        print("A maquina errou.")
        mapa_jogador[escolha_linha_maquina][escolha_coluna_maquina] = "x"

        for linha in mapa_jogador:
            print("  ".join(linha))

