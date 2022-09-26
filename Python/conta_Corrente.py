class ContaCorrente:
    def __init__(self, numeroDaConta, nomeDoCorrentista, saldo = 0) -> None:
        self.numberConta = numeroDaConta
        self.nome = nomeDoCorrentista
        self.saldo = saldo

    def mostrarDados(self):
        print(f'{self.nome}, {self.numberConta}, {self.saldo}')

    def alterarNome(self, mudarNome):
        self.nome = mudarNome

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self, saque):
        self.saldo -= saque

'''p1 = ContaCorrente(8801002132, 'Joao Amin', 50000)

p1.mostrarDados()
p1.alterarNome('Angelo da silva')
p1.deposito(4000)
p1.saque(259)
p1.mostrarDados()
'''