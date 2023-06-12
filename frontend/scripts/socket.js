class SocketConnection {
    constructor(port) {
        const socket = io(`http://localhost:${port}`);
        this.socket = socket;
        
        // Evento chamado quando a conexão é estabelecida
        this.socket.on('connect', () => {
            console.log(`Conexão estabelecida no servidor ${port}`);
            socket.send(JSON.stringify({message: "Imposto é roubo"}));
        });

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
    }
    connection(port) {}
}

// Realizar a reconexão com o servidor 
// new SocketConnection();

// export default SocketConnection;