"""CLIENTE/SERVIDOR"""

import socket
from json import load

# Criando o socket [Server]
def create_socket():
    try:
        global host
        global port 
        global s
        host = "localhost"
        port = 5000
        s = socket.socket() 
    except socket.error as msg:
        print("Erro ao tentar criar o socket_HUB: " + str(msg))

# Abrindo a conexão [Server]
def bind_socket():
    try:
        global host
        global port
        global s

        print("Bind_HUB na porta: " + str(port))

        s.bind((host, port))
        s.listen(1) 
    except socket.error as msg:
        print("Erro ao dar bind_HUB: " + str(msg))

# Aceitando as conexões [Server]
def socket_accept():
    conn, address = s.accept()
    print("[HUB] Conexão realisada com sucesso")
    print('IP: ' + str(address[0]) + ' | Port: ' + str(address[1]))
    login = connect_login_server(conn)
    
    conn.send(str.encode(login))
    
    # [Curadoria] A conexão com o cliente não deve acabar aqui
    # precisamos descobrir qual é o tipo de usuário e dar pra ele as opções do que ele pode fazer
    # baseando-se na resposta do cliente chamamos a função que irá se conectar com o serviço 
    # que irá realizar a função que o usuário quer fazer
    print('[HUB-CLIENT] Conexão Encerrada')
    conn.close

# Conectando ao serviço de login [Client]
def connect_login_server(conn):
    login = str(conn.recv(1024).decode('utf-8'))
    
    s_login = socket.socket()
    host_login = "localhost"
    port_login = 5500

    s_login.connect((host_login, port_login))

    s_login.send(str.encode(login))
    response_login_server = s_login.recv(1024).decode("utf-8")
    
    print("[HUB-LOGIN] Conexão Encerrada")
    s_login.close()
    
    return response_login_server

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()

# # endereço IP do servidor, vazio significa todos os IPs disponíveis
# HOST = '127.0.0.1'
# PORT = 5000  # porta para escutar as conexões

# # cria o socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # liga o socket ao endereço e porta especificados
# s.bind((HOST, PORT))

# # espera por conexões
# print('Servidor aguardando conexões...')
# s.listen(1)

# conn, addr = s.accept()
# print('Conectado por', addr)

# while True:
#     login = str(conn.recv(1024).decode('UTF-8'))

#     with open('C:\\Users\\Nicol\\OneDrive\\Área de Trabalho\\sistDistr-trab-chamada\\sistema_distribuido_socket\\db_netuno.json', encoding='UTF-8') as db_data:
#         login_members = load(db_data)

#     for login_member in login_members['login_members']:
#         if login == str(login_member['user'] + login_member['password']):
#             # envia dados de volta ao cliente
#             conn.sendall(b'OK')
#             print('[SERVIDOR] fecha a conexão')
#             conn.close()
#     else:
#         conn.sendall(b'NOT FOUND')

# # print('[SERVIDOR] fecha a conexão')
# # conn.close()
