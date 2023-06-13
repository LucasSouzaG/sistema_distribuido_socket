from flask import Flask, render_template
from flask_socketio import SocketIO
from utils import login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == '__main__':
    socketio.run(app, host='locallhost/login', port=8080)