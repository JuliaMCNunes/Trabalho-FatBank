# Criação da classe historico
class Historico:
    # Aqui criamos os atributos da classe historico
    def __init__(self):
        # Essa lista será preenchida no decorrer da execução do programa
        self.tran = []

    # Aqui criamos um método para imprimir as informações da lista "tran"
    def transacoes(self):
        for cont in self.tran:
            print("", cont)
