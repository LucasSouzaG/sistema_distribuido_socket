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
    print('Mensagem recebida:', message, type(json.loads(message)))   

    login = socket.socket()
    login.connect(('127.0.0.2', 8080))
    login.send(str.encode(f"{json.loads(message)['login']}{json.loads(message)['password']}"))
    response_server = login.recv(1024).decode('UTF-8')
    response_server = json.loads(response_server)

    if type(response_server) is dict:
        return socketio.emit('json_message', response_server)
    

@socketio.on('disconnect')
def handle_disconnect():
    print('Conexão fechada pelo cliente')

if __name__ == '__main__':
    subprocess.Popen('start cmd /K "cd C:\Projetos\sistema_distribuido_socket\microservices\\2-login && py index.py"', shell=True)
    subprocess.Popen('start cmd /K "cd C:\\Projetos\\sistema_distribuido_socket\\university-bd && node index.js"', shell=True)
    
    socketio.run(app, host='localhost', port=8080)