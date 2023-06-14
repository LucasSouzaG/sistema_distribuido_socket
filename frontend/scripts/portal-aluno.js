class PortalAluno {
    constructor() {
        const greetings = document.querySelector('.greetings');
        const user = JSON.parse(localStorage.getItem('user'));
        greetings.textContent = `Olá, ${user.name}`;
    }
}

new PortalAluno();