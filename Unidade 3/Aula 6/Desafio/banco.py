import os

def limpar():
    os.system("cls")


class Conta:
    def __init__(self, titular: str, numero: str):
        self._titular =titular
        self._numero =numero
        self._saldo = 0

    def depositar(self):
        saldo_atual = self._saldo
        print(f"Carteira = R$: {saldo_atual}\n")
        deposito = float(input("Quanto deseja depositar?:\n"))
        self._saldo += deposito
        print(f"Você depositou R$: {deposito}\nCartira: R$: {self._saldo:.2f}")

    def sacar(self):
        saque = float(input("Quanto deseja sacar?:\n"))
        if saque > self._saldo:
            print(f"Valor acima do que você tem na carteira.\n")
        else:
            self._saldo -= saque
            print(f"Você sacou R$: {saque}\n\nCarteira: R$: {self._saldo:.2f}")
                

class ContaCorrente(Conta):
    def __init__(self, titular: str, numero: str, saldo:float):
        super().__init__(titular, numero, saldo)
        self._limite_especial = 2000.0


class ContaPoupança(Conta):
    def __init__(self, titular:str, numero: str, saldo: float, taxa_rendimento: float):
        super().__init__(titular, numero, saldo)
        self._taxa_rendimento = taxa_rendimento

user = ContaCorrente("Pedrinho", "12345")

print(f"Bem Vindo {user._titular}\n")
print("Faça seu primeiro deposito.")
user.depositar()

while True:
    escolha = input("O que deseja fazer agora? (DEPOSITAR) (SACAR) (SAIR)\n").upper()
    if escolha == "DEPOSITAR":
        user.depositar()
    elif escolha == "SACAR":
        user.sacar()
    elif escolha == "SAIR":
        break


