import os

def limpar():
     os.system("cls")

alunos = []
medias = []

for i in range(10):

    usuario_alunos = input("Escreva o nome do aluno:\n")
    alunos.append(usuario_alunos)
    usuario_medias = float(input("Escreva a média deste aluno:\n"))
    limpar()

    while usuario_medias < 0 or\
          usuario_medias > 10:
          print("A média não pode ser menor do que 0 ou maior do que 10.")

          usuario_medias = float(input("Escreva a média deste aluno:\n"))

    medias.append(usuario_medias)

for i in range(len(alunos)):
     
     if medias[i] >= 6:
        print(f"Aluno: {alunos[i]} | Média: {medias[i]} |Aprovado!|")

     elif medias[i] < 6:
          print(f"Aluno: {alunos[i]} |Reprovado.|")