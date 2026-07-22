import os

def limpar():
    os.system("cls")

nomes = []
bairros = []

for i in range(5):

    nomes_usuario = input("Digite o nome de alguem:\n")
    nomes.append(nomes_usuario)

    bairros_usuario = input("Digite o bairro onde esta pessoa mora:\n")
    bairros.append(bairros_usuario)

nomes.sort()

for i in range(len(nomes)):

    print(f"Nome: {nomes[i]} | Bairro: {bairros[i]}")