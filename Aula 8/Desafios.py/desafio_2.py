import os

def limpar():
    os.system("cls")

numeros = []

for i in range(8):
    
    num_usuario = int(input("Digite um número:\n"))
    numeros.append(num_usuario)
    limpar()

maior = max(numeros)
menor = min(numeros)

print(numeros)
print(f"O maior valor é {maior}")
print(f"O menor valor é: {menor}")