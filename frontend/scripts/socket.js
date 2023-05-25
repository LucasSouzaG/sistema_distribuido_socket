class SocketConnection {
    constructor(port) {
        this.socket = io(`http://localhost:${port}`);
        console.log(`Socket connection established on port ${port}`)
    }
    connection(port) {}
}

new SocketConnection();

export default SocketConnection;