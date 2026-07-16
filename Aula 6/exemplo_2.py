#Importações

#Variáveis globais

#Declaraçãoes de função

#Resto do programa

def exibir_menu_infantil():
    menu_infantil = ["Relâmpago Marquinhos","Hotwheels","Pratulha Canina","Thomas e seus amigos"]
   
    for index, item in enumerate(menu_infantil):
        print(f"{index+1}:{item}")

def exibir_menu():
    menu = ["Toyota -> À partir de R$ 180.000","Mercedes-Benz -> À partir de R$ 450.000","BMW -> À partir de R$ 300.000"]
    
    for item in menu:
        print(item)
        
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

            
