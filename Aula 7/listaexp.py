#Comando para adição

compras = ["Maçã","Uva"]
compras.append("Café")

for item in compras:
    print(item)

#Comando para inserir item à lista

compras.insert(0,"Pão")

for item in compras:
    print(item)

#Juntar listas

compras_2 = ["Manteiga"]
compras.extend(compras_2)
print(compras)

#Comando para remover

compras.remove("Café")
print(compras)

#Comando de remover o pimeiro valor da lista

compras.pop(0)
print(compras)

#Comando para limpar todo conteúdo da lista

compras.clear()
print(compras)


numeros = [5, 4, 3, 2, 1]
print(len(numeros))



numeros.sort()
print(numeros)



numeros.reverse()
print(numeros)