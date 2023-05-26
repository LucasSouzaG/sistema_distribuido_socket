# Nome do Microsserviço: Hub
# Autor:
# Data de Criação:

# pip install python-socketio
# pip install flask-socketio
# pip install eventlet

from flask import Flask, render_template
from flask_socketio import SocketIO

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
    socketio.send('Você disse: ' + message)

    # Enviar JSON em uma mensagem separada
    data = {'name': 'John', 'age': 30}
    socketio.emit('json_message', data)

@socketio.on('disconnect')
def handle_disconnect():
    print('Conexão fechada pelo cliente')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)