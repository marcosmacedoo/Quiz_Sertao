import socket

IP = '127.0.0.1'

class Cliente():

    def __init__(self):
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conecta_servidor(self, porta):
        try:
            self.cliente_socket.connect((IP, porta))
        except socket.error as e:
            print('Erro de conexão com o servidor')
            str(e)
    
    def envia_dados(self, data):
        try:
            data_convertida_bytes = bytes(data, 'utf-8')
            self.cliente_socket.send(data_convertida_bytes)
        except socket.error as e:
            print('Erro na transferencia de dados')
            str(e)

    def fecha_conexao(self):
        self.cliente_socket.close()