"""CLIENTE"""

import socket

s = socket.socket()
host = "localhost"
port = 5000

print('Olá bem vindo!\n')
print('Preencha as credenciais de acesso:\n')

# conecta ao servidor
s.connect((host, port))

while True:
    login = input('Login: ')
    password = input('Password: ')

    # envia dados ao servidor
    s.send(str.encode(login + password))
    # s.sendall(bytes(str(login + password), encoding='utf-8'))
    # s.sendall(bytes(password, encoding='utf-8'))

    # recebe dados do servidor
    response_server = s.recv(1024).decode('UTF-8')
    if response_server == 'Erro':
        print("Login e/ou Senha incorreto(s) ... Tente novamente:\n")
        response_server = ''
    else:
        print("Acesso liberado")
        print("Seu login é do tipo: " + str(response_server))
        break


# fecha a conexão
print('[CLIENTE-HUB] Conexão encerrada')
s.close()
