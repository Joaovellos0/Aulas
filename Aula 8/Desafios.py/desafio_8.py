import os

def limpar():
    os.system("cls")

nomes = []
telefones = []
cidades = []

for i in range(10):

    nomes_usuario = input("Digite nome de alguem:\n")
    nomes.append(nomes_usuario)

    telefones_usuario = int(input("Digite o telefone desta pessoa:\n"))
    telefones.append(telefones_usuario)

    cidades_usuario = input("Digite a cidade desta pessoa:\n")
    cidades.append(cidades_usuario)

    limpar()

cidade = "Campo Grande"

for i in range(len(cidades)):

    if cidades[i] == cidade:

        print(f"Nome: {nomes[i]} | Telefone: {telefones[i]}")