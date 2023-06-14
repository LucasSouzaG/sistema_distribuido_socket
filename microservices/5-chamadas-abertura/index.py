# Nome do Microsserviço: chamadas-abertura
# Autor: Nicolas G
# Data de Criação: 14/06/2023


# Esse serviço será usado pelo perfil de professor

import socket
from requests import get

def create_socket():
    try:
        global s
        global host
        global port
        s = socket.socket()
        host = "127.0.0.2"
        port = "8060"
    except socket.error as msg:
        print("Erro ao tentar criar socket_CHAMADAS_ABERTURA: " + str(msg))

def bind_socket():
    try:
        global s
        global host
        global port

        print("Bind_CHAMADAS_ABERTURA na porta: " + str(port))

        s.bind((host, port))
        s.listen(30)
    except socket.error as msg:
        print("Erro ao tentar bind__CHAMADAS_ABERTURA: " + str(msg))

def socket_accept():
    conn, address = s.accept()
    print("[CHAMADAS_ABERTURA] Conexão realizada com sucesso")
    print("IP: " + str(address[0]) + " | Port: " + str(address[1]))

    # Espero o login do prefessor como resposta e o código da classe
    # {"login": "igorbtl456", "code_name": "sisdis",}
    data_class = conn.recv(1024).decode("utf-8")
    
    # DÙVIDAS:
    # Como o professor vai selecionar qual matéria ele quer fazer a chamada?

    # -- terminar função

# def open_presence_call(data_class):
#     # chamar o main do serviço
