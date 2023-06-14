# Nome do Microsserviço:
# Autor:
# Data de Criação:

# SERVIDOR

import socket
from json import load

def create_socket():
    try:
        global host
        global port 
        global s
        host = "localhost"
        port = 5500
        s = socket.socket() 
    except socket.error as msg:
        print("Erro ao tentar criar o socket_LOGIN: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s

        print("Bind_LOGIN na porta: " + str(port))

        s.bind((host, port))
        s.listen(1) 
    except socket.error as msg:
        print("Erro ao dar bind_LOGIN: " + str(msg))
    

def socket_accept():
    conn, address = s.accept()
    print("[LOGIN] Conexão realisada com sucesso")
    print('IP: ' + str(address[0]) + ' | Port: ' + str(address[1]))
    login = conn.recv(1024).decode("utf-8")
    typer_user = handle_login(login)

    if typer_user is not None:
        conn.send(str.encode(typer_user))
    else:
        conn.sendall(b'Erro')

    print('[LOGIN-HUB] Conexão encerrada')
    conn.close


def handle_login(login):
    with open('C:\\Users\\Nicol\\OneDrive\\Área de Trabalho\\sistDistr-trab-chamada\\sistema_distribuido_socket\\db_netuno.json', encoding='UTF-8') as db_data:
        login_members = load(db_data)
    
    for login_member in login_members['login_members']:
        if login == str(login_member['user'] + login_member['password']):
            return login_member['type_user']
        
    return None
        


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()