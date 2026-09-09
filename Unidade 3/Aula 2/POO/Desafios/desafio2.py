class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.em_estoque = 250
        self.valor_total = preco * self.em_estoque

    def detalhes_produto(self):
        print(
            f"Produto: {self.nome}\nValor da unidade: R${self.preco:.2f}\nQtd. em estoque: {self.em_estoque}\nValor do estoque: R${self.valor_total:.2f}\n"
        )

    def vender_produto(self):
        venda = int(input("Quantos itens serão vendidos?\n"))
        if venda <= self.em_estoque:
            qtd_restante = self.em_estoque - venda
            novo_valor = self.preco * qtd_restante
            print(
                f"O estoque agora possui {qtd_restante} unidades no valor de R${novo_valor:.2f}"
            )
        else:
            ("O valor excede a quantidade de items disponíveis para venda.")


item1 = Produto(
    input("Informe o produto sendo adicionado:\n"),
    float(input("Informe o valor da unidade:\n")),
)

item1.detalhes_produto()
item1.vender_produto()
