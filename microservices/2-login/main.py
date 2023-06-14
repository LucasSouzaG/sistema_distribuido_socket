import socket, time

# endereço IP do servidor, vazio significa todos os IPs disponíveis
HOST = '127.0.0.2'
PORT = 5501  # porta para escutar as conexões

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liga o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# espera por conexões
s.listen(1)

print('Servidor aguardando conexões...')

conn, addr = s.accept()
print('CONECTADO POR ', addr)

data = conn.recv(1024).decode('utf-8')
print(data)

# envia dados de volta ao cliente
conn.sendall(b'Recebi sua mensagem')
time.sleep(20)

# fecha a conexão
conn.close()
