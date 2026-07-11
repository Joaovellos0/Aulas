nota_usuario = float(input("Digite sua nota: "))

while (nota_usuario < 0 or nota_usuario > 10) and nota_usuario != None:
   
    print("ERRO! Apenas notas de 0 a 10.")
    
    nota = float(input("Digite sua nota: "))

