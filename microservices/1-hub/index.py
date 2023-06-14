# Nome do Microsserviço: Hub
# Autor:
# Data de Criação:

from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import socket
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Conexão estabelecida com o cliente')

    socketio.send('Eae craque.')

@socketio.on('message')
def handle_message(message):
    print('Mensagem recebida:', message)   
    message = json.loads(message)
    global LOGIN_

    try:
        LOGIN_ = message['login']
    except:
        ...

    if message['step'] == 'login':
        login = socket.socket()
        login.connect(('127.0.0.2', 8080))
        login.send(str.encode(f"{LOGIN_}{message['password']}"))
        response_server_login = login.recv(1024).decode('UTF-8')
        try:
            response_server_login = json.loads(response_server_login)
            print(f'[STATUS]: {response_server_login}')
            if response_server_login['user_type'] != None :
                socketio.emit('json_message', response_server_login)
            else:
                print(f'[ERROR]: {response_server_login}')
                socketio.emit('json_message', {'status': False})
        except:
            print('Não foi possivel realizar o login')
            subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\microservices\\2-login && py index.py"', shell=True)
    
    elif message['step'] == 'portal-aluno':
        aluno = socket.socket()
        aluno.connect(('127.0.0.2', 8065))
        aluno.send(str.encode(json.dumps({'login' : LOGIN_, 'key' : message['code']})))
        response_server_aluno = aluno.recv(1024).decode('UTF-8')
        print(f'[STATUS]: {response_server_aluno}')

        if response_server_aluno == 'Chamada realizada com sucesso':
            socketio.emit('json_message', {'status': True})
        else:
            print('[STATUS]: Não foi possivel realizar a chamada')
            subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\microservices\\3-chamadas-respostas && py index.py"', shell=True)
            socketio.emit('json_message', {'status': False})

@socketio.on('disconnect')
def handle_disconnect():
    print('Conexão fechada pelo cliente')

if __name__ == '__main__':
    #ATENÇÃO VOCE PRECISA ALTERAR DOS ARQUIVOS ABAIXO DE ACORDO COM A SUA MAQUINA!!!
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\university-bd && node index.js"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\university-backup && node index.js"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\microservices\\2-login && py index.py"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\microservices\\3-chamadas-respostas && py index.py"', shell=True)
    
    socketio.run(app, host='localhost', port=8080)