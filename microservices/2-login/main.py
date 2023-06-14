from flask import Flask, render_template
from flask_socketio import SocketIO
import socket

# endereço IP do servidor, vazio significa todos os IPs disponíveis
HOST = 'localhost/login'
PORT = 8080  # porta para escutar as conexões

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liga o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# espera por conexões
s.listen(1)

print('Servidor aguardando conexões...')

conn, addr = s.accept()
print('Conectado por', addr)
input()
