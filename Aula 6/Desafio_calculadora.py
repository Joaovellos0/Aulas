def soma(x,y):
    resultado_somatorio = x + y
    return resultado_somatorio

def subtracao(x,y):
    resultado_subtracao = x - y
    return resultado_subtracao

def multiplicacao(x,y):
    resultado_multiplicacao = x * y
    return resultado_multiplicacao

def divisao(x,y):
    if y == 0:
        return "ERRO!"
    resultado_divisao = x / y
    return resultado_divisao



while True:
    x = float(input("Digite um numero: "))
    y = float(input("Digite outro numero: "))
    operacao = input("Escolha a operação (+, -, x, /): ")

    if operacao == "+":
        print(f"Resultado:{soma(x,y)}")
    if operacao == "-":
        print(f"Resultado:{subtracao(x,y)}")
    if operacao == "x":
        print(f"Resultado:{multiplicacao(x,y)}")
    if operacao == "/":
        print(f"Resultado:{divisao(x,y)}")    






   



