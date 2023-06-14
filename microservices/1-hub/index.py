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

    if message['step'] == 'login':
        login = socket.socket()
        login.connect(('127.0.0.2', 8080))
        login.send(str.encode(f"{message['login']}{message['password']}"))
        response_server_login = login.recv(1024).decode('UTF-8')
        response_server_login = json.loads(response_server_login)

        if response_server_login['user_type'] != None :
            socketio.emit('json_message', response_server_login)
    
    elif message['step'] == 'portal-aluno':
        if response_server_login['user_type'] == 'al':
            aluno = socket.socket()
            aluno.connect(('127.0.0.2', 8065))
            aluno.send(str.encode({"login": "lucassza099", "key": "sisdis"}))
            response_server_aluno = login.recv(1024).decode('UTF-8')  

        if type(response_server_aluno) is dict:
            socketio.emit('json_message', response_server_aluno)

@socketio.on('disconnect')
def handle_disconnect():
    print('Conexão fechada pelo cliente')

if __name__ == '__main__':
    #ATENÇÃO VOCE PRECISA ALTERAR DOS ARQUIVOS ABAIXO DE ACORDO COM A SUA MAQUINA!!!
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\university-bd && node index.js"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\university-backup && node index.js"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\microservices\\2-login && py index.py"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Back_LEOO\\sistema_distribuido_socket\\microservices\\4-chamadas-respostas && py index.py"', shell=True)
    
    socketio.run(app, host='localhost', port=8080)