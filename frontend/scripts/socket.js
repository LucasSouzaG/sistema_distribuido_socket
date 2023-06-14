class SocketConnection {
    constructor(port) {
        this.connection(port);
    }

    connection(port) {
        this.socket = io(`http://localhost:${port}`);
        // Evento chamado quando a conexão é estabelecida
        // Evento chamado quando uma mensagem é recebida do servidor
        this.socket.on('message', function(data) {
            console.log('Dados recebidos do servidor:', data);
        });

        this.socket.on('json_message', function(data) {
            console.log('Dados recebidos do servidor:', data);
        });

        // Evento chamado quando a conexão é fechada
        this.socket.on('disconnect', function() {
            console.log('Conexão fechada');
        });

        return this.socket;
    }

    disconnect() {
        this.socket.disconnect();
    }
}

// Realizar a reconexão com o servidor 
// new SocketConnection();

export default SocketConnection;