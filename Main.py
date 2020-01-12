import pygame
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
from Tela import *
from Player import *
from Questao import *
from Cliente import *
#from time import sleep

t = Tela()
q = Questao()
pygame.init()

pygame.mixer.music.load('trilha.mp3')
pygame.mixer.music.play()

while True:

    tela = t.criaTela("entrar")
    nome = t.getName(tela)
    p1 = Player(nome)

    for i in q.getPerguntas():
        tela = t.criaTela(i)
        op = t.getOpcoes(tela)
        p1.setOpcao(op)
        pontos = q.pontosQuest(i, p1.getOpcao())
        print(pontos)

        dados_pontuacao = '2-%s-%d' % (p1.getNome(), pontos)
        p1.player_cliente.envia_dados(dados_pontuacao)

    tela = t.criaTela("podio")
    t.criarPodio(tela, p1)

    for event in pygame.event.get():
        if event.type == QUIT:
            p1.sai_jogo()
            pygame.quit()
            exit()
