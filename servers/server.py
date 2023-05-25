"""SERVIDOR"""

import socket

HOST = 'localhost'  # endereço IP do servidor, vazio significa todos os IPs disponíveis
PORT = 5000  # porta para escutar as conexões

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liga o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# espera por conexões
s.listen(1)

print('Servidor aguardando conexões...')

# aceita uma conexão
conn, addr = s.accept()
print('Conectado por', addr)
input()

while True:
    # recebe dados do cliente
    data = conn.recv(1024)
    if not data:
        break
    print('Mensagem do Cliente:', repr(data)) #Nao sera necessario utilizar a funcao repr()

    # envia dados de volta ao cliente
    conn.sendall(b'Recebi sua mensagem')

# fecha a conexão
conn.close()