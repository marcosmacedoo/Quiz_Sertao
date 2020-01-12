import pygame 
from pygame.locals import *
from sys import exit
from Player import *
from Servidor import PORTA

class Tela():
    def __init__(self):
        self.black = (0, 0, 0)
        self.yellow = (255, 255, 0)
        self.tam = (1000, 680)
    
    def criaTela(self, nameScreen):
        img = pygame.image.load("%s.png"%nameScreen)
        w, h = img.get_size()
        redImg = pygame.transform.smoothscale(img, (int(w*0.80), int(h*0.80)))
        
        tela = pygame.display.set_mode(self.tam, 0, 32)
        tela.fill((255,255,255))
        pygame.display.set_caption("QUIZ_PY")
               
        tela.blit(redImg, (0, 0))
        pygame.display.flip()
        return tela
    
    def texto(self, tela, mensagem, posicao, cor, tam):
        arial = pygame.font.SysFont('arial', tam)
        mens = arial.render(mensagem, True, cor, 0)
        tela.blit(mens, posicao)
        
    def getName(self, screen):
        name = ""
        rect = Rect((280, 380), (750, 450))
        while True:
            self.texto(screen, name, (350, 280),self.black, 35)
            pygame.display.flip()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if event.key != pygame.K_SPACE:
                            c = pygame.key.name(event.key).upper()
                            if len(name) < 15:
                                if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:-+_":
                                    name += c
                elif event.type == QUIT:
                    #p1.sai_jogo()
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(mouse_pos):
                    return name
                   
    def getOpcoes(self, screen):
        a = Rect((50, 280), (360, 80))
        b = Rect((50, 440), (360, 80))
        c = Rect((610, 280), (360, 80))
        d = Rect((610, 440), (360, 80))
        p = Rect((220, 20), (400, 80))
        n = Rect((460, 540), (90, 110))
        
        return self.getOpcaoEscolhida([a, b, c, d, p, n])
        
    def getOpcaoEscolhida(self, rec):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                for p in rec:
                    if event.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
                        if p == rec[0]:
                            return "A"
                        if p == rec[1]:
                            return "B"
                        if p == rec[2]:
                            return "C"
                        if p == rec[3]:
                            return "D"
                        if p == rec[4]:
                            return "P"
                        if p == rec[5]:
                            return "N"
                    elif event.type == pygame.QUIT:
                        #p1.sai_jogo()
                        pygame.quit()
                        exit()

    def criarPodio(self, screen, p1):#Adiciona mais players
        c = Cliente()
        c.conecta_servidor(PORTA)
        c.envia_dados('3-%s-%d' % (p1.getNome(), p1.getPontuacao()))

        ranking = c.cliente_socket.recv(1024)
        dados = ranking.decode('utf-8').split('-')
        print(dados)

        while True:    
            self.texto(screen, dados[0], (280, 200), self.black, 45)
            self.texto(screen, str(dados[1]), (110, 200), self.black, 45)
        
            pygame.display.flip()
            p1.sai_jogo()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        