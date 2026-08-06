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
    # if y == 0:
    #     return "ERRO!"
    resultado_divisao = x / y
    return resultado_divisao

while True:
    try:

        x = float(input("Digite um numero: "))
        y = float(input("Digite outro numero: "))
        operacao = input("Escolha a operação (+, -, x, /): ")

        if operacao == "+":
            print(f"Resultado:{soma(x,y)}")
        elif operacao == "-":
            print(f"Resultado:{subtracao(x,y)}")
        elif operacao == "x":
            print(f"Resultado:{multiplicacao(x,y)}")
        elif operacao == "/":
            print(f"Resultado:{divisao(x,y)}")
        else:
            print("Digite uma operação válida.")

    except (ZeroDivisionError):
        print("Não é possível dividir um número por 0.")

    except (ValueError):
        print("Utilize apenas números.")

    except (Exception) as erro:
        print("Ocorreu um erro:", erro)    







   



