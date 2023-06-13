# Nome do Microsserviço: Hub
# Autor:
# Data de Criação:

from flask import Flask, render_template
from flask_socketio import SocketIO
from utils import login

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
    access = login(message)
    socketio.emit('json_message', {'message': access})

@socketio.on('disconnect')
def handle_disconnect():
    print('Conexão fechada pelo cliente')

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=8080)