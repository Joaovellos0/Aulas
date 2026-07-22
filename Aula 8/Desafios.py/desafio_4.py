import os

def limpar():
    os.system("cls")

numeros = []

contador_par, contador_impar = 0, 0

for i in range(7):

    num_usuario = int(input("Digite um número:"))
    numeros.append(num_usuario)
    limpar()
    
    if num_usuario % 2 == 0:
        contador_par += 1

    elif num_usuario % 2 != 0:
        contador_impar += 1

print(f"Lista dos seus números escolhidos: {numeros}.")
print(f"Quantidade de números pares da lista: {contador_par}.")    
print(f"Quantidade de números ímpares da lista: {contador_impar}.")
