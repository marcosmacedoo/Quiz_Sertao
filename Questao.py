
class Questao():
    def __init__(self):
        self.perguntas = ['p%s' % i for i in range(1, 11)]
        self.respostas = ['A', 'A', 'P', 'B', 'D', 'B', 'P', 'D', 'N', 'A']
        self.pontos = [5, 10, 10, 5, 5, 15, 10, 20, 10, 5]

    def pontosQuest(self, pergunta, resposta):
        ponto = 0
        for i in range(len(self.perguntas)):
            if self.perguntas[i] == pergunta and resposta == self.respostas[i]:
                ponto = self.pontos[i]
                break
        return ponto

    def getPerguntas(self):
        return self.perguntas
