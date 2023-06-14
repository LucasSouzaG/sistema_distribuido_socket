import SocketConnection from './socket.js';
import './login.js';
import './storage.js';

class Login {
    constructor(socketConnection) {
        this.socketConnection = socketConnection.get();
        this.setForm();
    }

    setForm() {
        const loginForm = document.getElementById('login-form');
        this.form = loginForm;
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const login = loginForm.login.value;
            const password = loginForm.password.value;
            loginClass.authentication(login, password);
        });
    }

    authentication(login, password) {
        this.socketConnection.send(JSON.stringify({login, password}));
        // Acesso Valido: {"login":"lucassza099","password":"senha123"}    

        this.socketConnection.on('json_message', function(data) {
           const response = data;
           if(typeof(response) === 'object') {
            localStorage.setItem('user', JSON.stringify(response));
            window.location.href ='http://127.0.0.1:5500/frontend/pages/portal-aluno.html'
           } else {
            if (!document.querySelector('.error')) {
                // add p error after form
                const p = document.createElement('p');
                p.textContent = 'Login ou senha incorretos';
                p.style.color = 'red';
                p.style.marginTop = '20px';
                p.classList.add('error');
                loginClass.form.appendChild(p);
            }
           }
        });
    }
}

const loginClass = new Login(new SocketConnection(8080));
