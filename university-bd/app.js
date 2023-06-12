import express from 'express';
import Routes from './routes/routes.js';

class App {
    constructor(port, enabled = true) {
        this.port = port;
        this.express = express();
        this.setupRoutes();
        this.middleware();
        this.enable();
    }

    middleware() {
        this.express.use(express.json());
        this.express.use(express.urlencoded({ extended: false }));
    }

    setupRoutes() {
        const routes = new Routes();
        this.express.use('/', routes.routes());
    }

    enable() {
        this.express.listen(this.port, () => {
            console.log(`Listening on port ${this.port}`);
        });
    }
}

export default App;