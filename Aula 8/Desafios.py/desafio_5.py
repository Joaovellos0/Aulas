import os

def limpar():
    os.system("cls")

numeros = []

for i in range(5):

    num_usuario = int(input("Digite um número:\n"))
    numeros.append(num_usuario)
    limpar()

numeros.sort()

print(numeros)   