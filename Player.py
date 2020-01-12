from Cliente import *
from Servidor import PORTA

class Player():

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.opcao = ''
        self.inicializa_cliente()

    def inicializa_cliente(self):
        dados = '1-%s-0' % (self.getNome())

        self.player_cliente = Cliente()
        self.player_cliente.conecta_servidor(PORTA)
        self.player_cliente.envia_dados(dados)
    
    def setPontuacao(self, valor):
        self.pontuacao += valor
    
    def setOpcao(self, op):
        self.opcao = op
    
    def getOpcao(self):
        return self.opcao

    def getPontuacao(self):
        return self.pontuacao
    
    def getNome(self):
        return self.nome

    def sai_jogo(self):
        dados = '0-%s-%d' % (self.getNome(), self.getPontuacao())
        self.player_cliente.envia_dados(dados)
        self.player_cliente.fecha_conexao()
    
