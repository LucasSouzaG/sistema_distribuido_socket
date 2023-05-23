import socket

HOST = 'localhost'  # endereço IP ou nome do servidor
PORT = 5000  # porta usada pelo servidor

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
s.connect((HOST, PORT))

# envia dados ao servidor
s.sendall(b'Servidor, recebeu minha mensagem?')

# recebe dados do servidor
data = s.recv(1024)

print('Mensagem do Servidor:', repr(data))

# fecha a conexão
s.close()