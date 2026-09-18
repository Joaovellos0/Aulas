import os


def limpar():
    os.system("cls")


class Conta:
    def __init__(self, titular: str, numero: str):
        self._titular = titular
        self._numero = numero
        self._saldo = 1600

    def __add__(self, other):
        if isinstance(other, Conta):
            return self._saldo + other._saldo

    def depositar(self):
        saldo_atual = self._saldo
        print(f"Carteira = R$: {saldo_atual:.2f}\n")
        deposito = float(input("Quanto deseja depositar?:\n"))
        self._saldo += deposito
        print(f"Você depositou R$: {deposito:.2f}\nCarteira: R$: {self._saldo:.2f}\n")

    def sacar(self):
        saque = float(input("Quanto deseja sacar?:\n"))
        if saque > self._saldo:
            print(f"Valor acima do que você tem na carteira.\n")
            limpar()
        else:
            self._saldo -= saque
            print(f"Você sacou R$: {saque:.2f}\nCarteira: R$: {self._saldo:.2f}\n")
            limpar()


class ContaCorrente(Conta):
    def __init__(self, titular: str, numero: str):
        super().__init__(titular, numero)
        self._limite_especial = 2000.0

    def sacar(self):
        saque = float(input("Quanto deseja sacar?:\n"))
        if self._saldo - saque >= -self._limite_especial:
            self._saldo -= saque
            print(f"Você sacou R$: {saque:.2f}\nCarteira: R$: {self._saldo:.2f}\n")
            limpar()
        else:
            print("Saque negado.")
            limpar()


class ContaPoupanca(Conta):
    def __init__(self, titular: str, numero: str):
        super().__init__(titular, numero)
        self.taxa_rendimento = 0.05

    def aplicar_rendimento(self):
        self._saldo = self._saldo * (1 + self.taxa_rendimento)
        print(f"Novo saldo: {self._saldo:.2f}")


user = ContaCorrente("Pedrinho", "12345")
user2 = ContaPoupanca("Marcello MAMA MIA", "67891")


resultado = user.__add__(user2)
print(f"O saldo de {user._titular} + o saldo de {user2._titular} é {resultado}")
