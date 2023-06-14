# Nome do Microsserviço: resposta-chamada
# Autor: Nicolas G
# Data de Criação: 14/06/2023

import socket
from requests import get
import json

# Serviço usado pelo perfil de aluno

def create_socket():
    try:
        global s
        global host
        global port
        s = socket.socket()
        host = "127.0.0.2"
        port = 8065
    except socket.error as msg:
        print("Erro ao tentar criar socket_RESPOSTA-CHAMADA: " + str(msg))

def bind_socket():
    try:
        global s
        global host
        global port

        print("Bind_RESPOSTA-CHAMADA na porta: " + str(port))

        s.bind((host, port))
        s.listen(30)
    except socket.error as msg:
        print("Erro ao tentar bind_RESPOSTA-CHAMADA: " + str(msg))


def socket_accept():
    conn, address = s.accept()
    print("[RESPOSTA-CHAMADA] Conexão realizada com sucesso")
    print("IP: " + str(address[0]) + " | Port: " + str(address[1]))

    count_limit = 0

    while True:
        # recebe dados da resposta da chamada
        # RECV Y.1
        # {"login": "lucassza099", "key": "sisdis"}
        count_limit = count_limit + 1

        presence_call_data = conn.recv(1024).decode("utf-8")
        rp_valid = valid_pc_data(presence_call_data)
        

        if rp_valid == 'Chamada realizada com sucesso':
            conn.send(str.encode(rp_valid))
            break
        elif count_limit == 3:
            conn.send(str.encode("Desculpe, você excedeu o número de tentativas, vamos fechar a conexão agora"))
            break
    
    conn.close()

def valid_pc_data(data):

    data = json.loads(data)
    login = data["login"]
    key = data["key"]
    by_pass = 'Algo deu errado'

    try:
        students = get('http://localhost:3000/students/')
        all_students = students.json()
    except:
        students = get('http://localhost:3001/students/')
        all_students = students.json()

    try:
        classes = get('http://localhost:3000/classes/')
        all_classes = classes.json()
    except:
        classes = get('http://localhost:3001/classes/')
        all_classes = classes.json()

    for cl in all_classes["classes"]:
        if key == cl["code_name"]:
            key_valid = True
            semester_cl = cl["semester"]
            break
    
    for student in all_students["student"]:
        if login == student["login"]:
            login_valid = True
            semester_st = student["semester"]
            break

    if (key_valid and login_valid) and (semester_cl == semester_st):
        by_pass = 'Chamada realizada com sucesso'
    else:
        return by_pass
    
    return by_pass


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()