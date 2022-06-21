# Criação a classe cliente
class Cliente:
    # Aqui criamos os atributos da classe cliente
    def __init__(self, titular, cpf, data, usuario, senha, cont): 
        self.titular = titular
        self.cpf = cpf
        self.data = data
        self.usuario = usuario
        self.senha = senha
        self.cont = cont
        