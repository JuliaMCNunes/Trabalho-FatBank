# Importando a classe historico
from Classe_Historico import *

# Criação a classe conta
class Conta:
    # Aqui criamos os atributos da classe conta
    def __init__(self, objeto, saldo=0.0):
        # Para o atributo titular, vamos pegar o nome já adquirido na classe cliente
        self.titular = objeto.titular
        self.cpf = objeto.cpf
        self.data = objeto.data
        self.cont = objeto.cont
        self.usuario = objeto.usuario
        self.senha = objeto.senha
        self.saldo = saldo
        # O atributo historico irá ajudar a enviar as informações de deposito, saque e transferência para a lista "tran"
        self.historico = Historico()

    # Aqui criamos o método deposito, o valor informado pelo usuário será adcionado a conta do cliente
    def dados2(self, deposi):
        self.saldo += deposi
        # Essa linha é a responsável por enviar os valores do deposito para a lista "tran"
        self.historico.tran.append(f'Deposito de {deposi}')
        return self.saldo

    # Aqui criamos o método saque, o valor informado pelo usuário será subtraido da conta do cliente, mas isso só será possível se o saldo da conta for suficiente
    def dados3(self, saque):
        if self.saldo > saque:
            self.saldo -= saque
            # Essa linha é a responsável por enviar os valores do saque para a lista "tran"
            self.historico.tran.append(f'Saque de {saque}')
            return self.saldo

    # Aqui criamos o método transferência, o valor informado pelo usuário será subtraido da conta do cliente 1 e adcionado a conta do cliente 2
    def dados4(self, transfe, conta):
        self.saldo -= transfe
        conta.saldo += transfe
        # Essa linha é a responsável por enviar os valores da transferência para a lista "tran"
        self.historico.tran.append(f'Transferência de {transfe}')
        return self.saldo

    # Aqui criamos o método extrato, todas as transações feitas pelo cliente serão armazenadas em uma lista denominada "tran", depois será exibida para o cliente
    def dados5(self):
        self.historico.transacoes()

    def dados6(self):
        self.historico.imprimir()
