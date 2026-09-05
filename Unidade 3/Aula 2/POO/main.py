class GuitarraIbanez:
    def __init__(self, cor, captadores, modelo):
        self.cor = cor
        self.captadores = captadores
        self.modelo = modelo
        self.marca = "Ibanez"
      
    def sobre_o_produto(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nCaptação: {self.captadores}\nCor: {self.cor}")

    def fazer_escala(self):
        escala = input("Qual escala você vai fazer?:\n")
        if escala == "la menor harmonico":
            print("A B C D E F G#")
        else:
            print("Não conheço essa escala.")

guitarra1 = GuitarraIbanez("Preto BKF", "Dimarzio", "RG270")
print(guitarra1.captadores)
print(guitarra1.modelo)
guitarra1.sobre_o_produto()


        