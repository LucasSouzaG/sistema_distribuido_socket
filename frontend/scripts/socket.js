class SocketConnection {
    constructor(port) {
        this.socket = io(`http://localhost:${port}`);    

        // Evento chamado quando uma mensagem é recebida do servidor
        this.socket.on('message', function(data) {
            console.log('Dados recebidos do servidor:', data);
        });

        this.socket.on('json_message', function(data) {
            console.log(data);
        });

        // Evento chamado quando a conexão é fechada
        this.socket.on('disconnect', function() {
            console.log('Conexão fechada');
        });
    }

    get() {
        return this.socket;
    }

    connection(port) {}
}

// Realizar a reconexão com o servidor 
new SocketConnection();

export default SocketConnection;