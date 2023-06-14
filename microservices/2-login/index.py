# Nome do Microsserviço: socket login
# Autor: Nicolas Gonçalves
# Data de Criação: 12/06/2023

# SERVIDOR

import socket
from json import load
from requests import get

def create_socket():
    try:
        global host
        global port 
        global s
        host = "127.0.0.2"
        port = 8080
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

    msg_not_found = 'Not Found'
    msg_bd_error = 'BF Access Error'
    
    # vai rodar até receber o tipo de usuário e o nome dele da função handle_login
    while True:
        login = conn.recv(1024).decode("utf-8")
        typer_user = handle_login(login)

        if typer_user == msg_not_found: 
            conn.send(str.encode(msg_not_found))
        elif typer_user == msg_bd_error:
            conn.send(str.encode(msg_bd_error))
        else:
            conn.send(str.encode(typer_user))
            break 

    print('[LOGIN-HUB] Conexão encerrada')
    conn.close

# colocar o try e except, no except tentar se conectar com o bd backup
# se não conseguir acessar nesse tbm, retorna falando que 
# não é possível acessar ao banco por enquanto
def handle_login(login):
    try:
        users = get('http://localhost:3000/logins/')
        login_members = users.json()
        
        for login_member in login_members['user_logins']:
            if login == str(login_member['login'] + login_member['password']):
                r_user_type = '{"user_type":' + '"' + str(login_member["user_type"]) + '",'
                r_user_name = '"name":' + '"' + str(login_member["name"]) + '"}'
                response = str(r_user_type + r_user_name)
                return response
            
        return 'Not Found'
    except:
        try:
            user_bk = get('http://localhost:3001/logins/')
            login_members_bk = user_bk.json()

            for login_member in login_members_bk['user_logins']:
                if login == str(login_member['login'] + login_member['password']):
                    r_user_type = '{"user_type":' + '"' + str(login_member["user_type"]) + '",'
                    r_user_name = '"name":' + '"' + str(login_member["name"]) + '"}'
                    response = str(r_user_type + r_user_name)
                    return response
            
            return 'Not Found'
        except:
            return 'BD Access Error'
        


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()