def adicionar_ao_estoque():
    while True:
        produto = {
            "tipo": input("Digite o produto que deseja adicionar: "),
            "preço unitário": float(input("Digite valor do produto: ")),
            "quanidade": int(input("Digite a quantidade que deseja adicionar ao estoque: "))
        }
        estoque.append(produto)

        pergunta = input("Deseja adicionar outro produto?\n")

        if pergunta == "nao":
            break
        elif pergunta == "sim":
            continue
      
    
           

estoque = [
    {"tipo": "arroz", "preço unitário": 4.00, "quantidade": 200}, 
    {"tipo": "feijão", "preço unitário": 7.00, "quantidade": 500},
    {"tipo": "batata", "preço unitário": 1.20, "quantidade": 350},
]

adicionar_ao_estoque()

