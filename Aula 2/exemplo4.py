nota_do_aluno = float(input("Informe sua nota: "))

if nota_do_aluno > 95:
    print("Aprovado, ótimo desempenho!")
elif nota_do_aluno >= 60:
    print("Aprovado")
elif nota_do_aluno > 40:
    print("Recuperação")    
else:
    print("Reprovado")
        