"""CLIENTE"""

import socket

HOST = '127.0.0.1'  # endereço IP ou nome do servidor
PORT = 5000  # porta usada pelo servidor

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Olá bem vindo!\n')
print('Preencha as credenciais de acesso:\n')

# conecta ao servidor
s.connect((HOST, PORT))

while True:
    login = input('Login: ')
    password = input('Password: ')

    # envia dados ao servidor
    s.sendall(bytes(str(login + password), encoding='utf-8'))
    # s.sendall(bytes(password, encoding='utf-8'))

    # recebe dados do servidor
    response_server = s.recv(1024).decode('UTF-8')
    if response_server == 'OK':
        break
    else:
        print('Credenciais incorretas tente novamente:\n')

# fecha a conexão
print('[CLIENTE] fecha a conexão')
s.close()        
