import plyer

estoque = []

poduto = {
    "tipo": "Café",
    "preco_unitario": 28.99,
    "quantidade": 300
}

def adicionar_produtos():

    try:
        produto = {
            "tipo": input("Digite o produto que deseja adicionar: "),
            "preco_unitario": float(input("Digite o preço desse produo: ")),
            "quantidade": int(input("Digite a quantidade deste produto: "))
        }

        estoque.append(produto)
        
    except:
        print("Algo deu errado.")

def listar_produtos():
    for produto in estoque:
        print(f"Produto: {produto["tipo"]} - Quantidade: {produto["quantidade"]}")

def somar_total():
    total_geral = 0

    for produto in estoque:
        total_geral += produto["preco_unitario"] * produto["quanidade"]

    print(f"Total geral do estoque: {total_geral}")


def somar_quantidade_total():
    total_geral = 0

    for produto in estoque:
        total_geral += produto["quantidade"]
    
    for produto in estoque:
        print(f"{produto["tipo"]}")

    print(f"Total geral do estoque: {total_geral}")

def buscar_produto():
    busca = input("Digite o produto que deseja encontrar: ")

    for produto in estoque:
        if produto["tipo"] == busca:

            print(produto["quantidade"])
            print(produto["preco_unitario"])

def mostrar_abaixo():

    for produto in estoque:

        if produto["quantidade"] < 50:
            plyer.notification.notify(
                title="Alerta de estoque baixo",
                message=f"Atenção! O produto {produto["tipo"]} tem poucas unidades: {produto["quantidade"]}",
                app_name="Sistema de Estoque",
                timeout=5
            )

while True:

    opcao = input("Escolha:\n1-Adicionar produto\n2-Listar produtos\n3-Preço Total\n4-Quanidade Total\n5-Estoque crítio:\n")

    if opcao == "1":
        adicionar_produtos()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        somar_total()

    elif opcao == '4':
        somar_quantidade_total()
    
    elif opcao == "5":
        mostrar_abaixo()