import os

def limpar():
    os.system("cls")

print("O programa calculará a media de 10 números que você digitar.")

soma = 0

for i in range(10):

    num_usuario = float(input("Digite um número:\n"))
    soma += num_usuario
    limpar()

print(f"A soma dos números digitados é:\n{soma}")

soma = soma /10

print(f"A média é {soma}")


