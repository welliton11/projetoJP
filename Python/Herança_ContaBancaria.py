import string
#from abc import ABC, abstractmethod

class ContaBancaria:
    def __init__(self, Cliente, Numero_da_Conta, Saldo) -> None:
        self.cliente = string(Cliente)
        self.num_conta = int(Numero_da_Conta)
        self.saldo = float(Saldo)
    def sacar(self, Saque):
        if self.saldo - Saque < 0:
            print('Você não pode sacar um valor que você não tem!')
        else:
            self.saldo -= Saque
            print(f'Você sacou {Saque}, seu valor em conta é {self.saldo}')
    def depositar(self, Deposito):
        self.saldo += Deposito
class ContaPoupança(ContaBancaria):
    def __init__(self, Cliente, Numero_da_Conta, Saldo, Dia_de_Rendimento) -> None:
        super().__init__(Cliente, Numero_da_Conta, Saldo)
        self.rendimento = int(Dia_de_Rendimento)
    def NovoSaldo(self):
        self.saldo += (self.saldo*0.002)*self.rendimento
        return self.saldo
class ContaEspecial(ContaBancaria):
    def __init__(self, Cliente, Numero_da_Conta, Saldo, Limite) -> None:
        super().__init__(Cliente, Numero_da_Conta, Saldo)
        self.limite = float(Limite)
    def sacar(self, Saque):
        if self.saldo - Saque < -(Saque+self.limite):
            print('Você não tem saldo suficiente')
        else:
            self.saldo -= Saque
        return self.saldo