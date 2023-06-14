import SocketConnection from './socket.js';
import './storage.js';

class PortalAluno {
    constructor(socketConnection) {
        this.socketConnection = socketConnection.get();
        const greetings = document.querySelector('.greetings');
        const user = JSON.parse(localStorage.getItem('user'));
        greetings.textContent = `Olá, ${user.name}`;
        this.setForm();
    }

    setForm() {
        const portalForm = document.getElementById('portal-aluno-form');
        this.form = portalForm;
        portalForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const code = portalForm.code.value;
            const step = 'portal-aluno'
            this.presence(code, step);
        });
    }

    presence(code, step) {
        this.socketConnection.send(JSON.stringify({code, step}));
        // Acesso Valido: {"login":"lucassza099","password":"senha123"}    

        this.socketConnection.on('json_message', function(data) {
           const response = data;
           if(typeof(response) == 'object') {
            localStorage.setItem('user', JSON.stringify(response));
           } else {
            /*if (!document.querySelector('.error')) {
                // add p error after form
                const p = document.createElement('p');
                p.textContent = 'Login ou senha incorretos';
                p.style.color = 'red';
                p.style.marginTop = '20px';
                p.classList.add('error');
                loginClass.form.appendChild(p);
            }*/
           }
        });
    }
}

new PortalAluno(new SocketConnection(8080));