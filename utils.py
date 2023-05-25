import socket

# cria e liga o socket
def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind((HOST, PORT)) # liga o socket ao endereço e porta especificados. OBS: Com bind(socket.gethostname(), 80) é o IP local da maquina
    # server_socket.listen(1) # espera por conexões


def start_socket(server_socket):
    return server_socket.listen(1)

# def close_socket(server_socket):
#     return server_socket.listen(1)

