import os

def limpar():
    os.system("cls")

numeros = []

contador = 0

for i in range(10):
    
    num_usuario = int(input("Digite um número:\n"))
    numeros.append(num_usuario)
    limpar()
    if num_usuario > 10:
        contador += 1

print(f"Seus números são: {numeros}.")
print(f"Número de algarismos maiores que 10: {contador}.")