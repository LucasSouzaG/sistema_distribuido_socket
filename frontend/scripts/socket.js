class SocketConnection {
    constructor(port) {
        this.socket = io(`http://localhost:${port}`);
        console.log(`Socket connection established on port ${port}`)
        this.socket.on('connect', () => {
            console.log('Socket connection established');
            // encode message in utf8
            const message = new TextEncoder().encode('Hello from the browser');
            this.socket.emit('message', message);
        });
    }
    connection(port) {}
}

new SocketConnection();

export default SocketConnection;