import socket
from _thread import *
import time

ENDERECO = '0.0.0.0'
PORTA = 6000


class Servidor():

    def __init__(self):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientes = []

    def inicializa_servidor(self):
        try:
            self.servidor.bind((ENDERECO, PORTA))
            self.servidor.listen(3)

            print('Servidor no ar %s:%d' % (ENDERECO, PORTA))
        except socket.error as e:
            print('Erro ao subir servidor')
            str(e)

    def adiciona_cliente(self, player):
        self.clientes.append(player)

        print(player, ' adicionado')
        # print(self.clientes)

    def remove_cliente(self, player):
        #self.clientes.remove(player)
        for i in range(len(self.clientes)):
            if self.clientes[i]['nome'] == player['nome']:
                self.clientes.pop(i)

        print(player, ' removido')
        # print(self.clientes)

    def atualiza_pontuacao(self, player):
        for i in range(len(self.clientes)):
            if self.clientes[i]['nome'] == player['nome']:
                self.clientes[i]['pontuacao'] += player['pontuacao']

    def envia_ranking(self, cliente_socket, player):
        ranking = ''
        for c in self.clientes:
            if c['nome'] == player['nome']:
                ranking += '%s-%d' % (c['nome'], c['pontuacao'])
                data = bytes(ranking, 'utf-8')
        cliente_socket.send(data)

    def thread_cliente(self, cliente_socket):

        while True:
            dados_cliente = cliente_socket.recv(1024)
            dados_decodificados = dados_cliente.decode('utf-8').split('-')

            player = {'nome': dados_decodificados[1], 'pontuacao': int(
                dados_decodificados[2])}

            if dados_decodificados[0] == '1':
                self.adiciona_cliente(player)
            elif dados_decodificados[0] == '0':
                self.remove_cliente(player)
                break
            elif dados_decodificados[0] == '2':
                self.atualiza_pontuacao(player)
            elif dados_decodificados[0] == '3':
                self.envia_ranking(cliente_socket, player)
                break

            print(self.clientes)

        cliente_socket.close()

    def main(self):
        self.inicializa_servidor()

        while True:
            try:
                cliente_socket, endereco_cliente = self.servidor.accept()

                start_new_thread(self.thread_cliente, (cliente_socket,))

                print(endereco_cliente, 'entrou no sevidor')
            except socket.error as e:
                str(e)

        self.servidor.close()


if __name__ == "__main__":
    servidor = Servidor()
    servidor.main()
