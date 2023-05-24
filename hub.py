"""CLIENTE/SERVIDOR"""

import socket
from json import load

HOST = '127.0.0.1'  # endereço IP do servidor, vazio significa todos os IPs disponíveis
PORT = 5000  # porta para escutar as conexões

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liga o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# espera por conexões
print('Servidor aguardando conexões...')
s.listen(1)

conn, addr = s.accept()
print('Conectado por', addr)

while True:
    login = str(conn.recv(1024).decode('UTF-8'))

    with open('db_netuno.json', encoding='UTF-8') as db_data:
        login_members = load(db_data)

    for login_member in login_members['login_members']:
        if login == str(login_member['user'] + login_member['password']):
            # envia dados de volta ao cliente
            conn.sendall(b'OK')
            print('[SERVIDOR] fecha a conexão')
            conn.close()
    else:
        conn.sendall(b'NOT FOUND')

# print('[SERVIDOR] fecha a conexão')
# conn.close()