import os

def limpar():
    os.system("cls")

nomes = []
idades = []

print("O programa irá armazenar o nome e a idade de 10 pessoas que o usuário digitará e irá retornar os dados do individuo mais novo.")

for i in range(10):

    nome_usuario = input("Digite o nome de alguem:\n")
    nomes.append(nome_usuario)
    idades_usuario = int(input("Digite a idade da pessoa:\n"))
    limpar()

    while idades_usuario <= 0:

        print("A pessoa deve ter no mínimo 1 ano de idade.")
        idades_usuario = int(input("Digite a idade da pessoa:\n"))

    idades.append(idades_usuario)  

menor_idade = idades.index(min(idades))

#for i in range(len(nomes)):
#    print(f"Nome: {nomes[i]} | Idade:{idades[i]}")

print(f"\nO individuo mais novo é {nomes[menor_idade]} com {idades[menor_idade]} anos.")