guitarra = {
    "Marca": "Ibanez",
    "Modelo": "RG370",
    "Capitação": "H-S-H",
    "Número de cordas": 6,
    "Tipo de ponte": "Edge-Zero Ibanez",
}

# # Adição e Atualizção

# guitarra["Cor"] = "Preto" #- Adição

# # guitarra.update({"Cor": "Branco"}) #- Atualização

# # print(guitarra)

# # Remoção

lista_chaves = guitarra.keys()  # Ou .values

for chave in lista_chaves:
    print(chave)