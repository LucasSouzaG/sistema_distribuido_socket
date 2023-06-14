# Nome do Microsserviço: Hub
# Autor:
# Data de Criação:

from flask import Flask, render_template
from flask_socketio import SocketIO
from utils import login
import subprocess
import socket

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
    print('Mensagem recebida:', message, type(message))   
    
    login = socket.socket()
    login.connect(('127.0.0.2', 5501))
    login.send(str.encode(message))

    # access = login(message)
    # socketio.emit('json_message', {'message': access})

@socketio.on('disconnect')
def handle_disconnect():
    print('Conexão fechada pelo cliente')

if __name__ == '__main__':

    subprocess.Popen('start cmd /K "cd C:\Projetos\sistema_distribuido_socket\microservices\\2-login && py main.py"', shell=True)
    
    socketio.run(app, host='localhost', port=8080)