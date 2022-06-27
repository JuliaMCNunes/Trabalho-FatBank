# Criação da classe historico
class Historico:
    # Aqui criamos os atributos da classe historico
    def __init__(self, mostrar=''):
        # Essa lista será preenchida no decorrer da execução do programa
        self.tran = []
        self.mostrar = mostrar
    # Aqui criamos um método para imprimir as informações da lista "tran"
    def transacoes(self):
        self.mostrar = ''
        for cont in self.tran:
            self.mostrar += '\n' + cont
    
    def imprimir(self):
        for cont in self.tran:
            print('', cont)
