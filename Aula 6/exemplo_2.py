#Importações

#Variáveis globais

#Declaraçãoes de função

#Resto do programa

def exibir_menu_infantil():
    print("Relâmpago Marquinhos")
    print("Hotwheels")
    print("Pratulha Canina")
    print("Thomas e seus amigos")

def exibir_menu():
    print("Toyota -> À partir de R$ 180.000")
    print("Mercedes-Benz -> À partir de R$ 450.000")   
    print("BMW -> À partir de R$ 300.000") 



def checar_idades(idades):
    if idades < 18:
        exibir_menu_infantil()
    else:
        exibir_menu()

    
while True:
    idades = int(input("Digite a sua idade ou 0 para sair: "))
    if idades == 0:
        break
    else:
        checar_idades(idades)

            
