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
        // ON 'PRESENCA'    
        this.socketConnection.on('json_message', function(data) {
           const response = data;
           if(response == 'true') {
            alert('Presença confirmada');
           } else {
            alert('Código inválido, por favor contate seu professor ou revise seu código');
           }
        });
    }
}

new PortalAluno(new SocketConnection(8080));