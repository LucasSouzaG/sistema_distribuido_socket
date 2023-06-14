import SocketConnection from './socket.js';
import './login.js';
import './storage.js';

class Login {
    constructor(socketConnection) {
        this.socketConnection = socketConnection;
    }

    authentication(login, password) {
        if (login && password) {
            this.socketConnection.on('connect', () => {
                console.log(`Conexão estabelecida no servidor ${port}`);
                socket.send(JSON.stringify({login, password}));
                // Acesso Valido: {"login":"lucassza099","password":"senha123"}
            });
        } 
        
    }
    isLogged() {}
}

const loginClass = new Login(new SocketConnection(8080));
const loginForm = document.getElementById('login-form');
loginForm.addEventListener('submit', (event) => {
    event.preventDefault();
    console.log("TESTE")
    const login = loginForm.login.value;
    const password = loginForm.password.value;
    console.log(login)
    console.log(password)
    loginClass.authentication(login, password);
});