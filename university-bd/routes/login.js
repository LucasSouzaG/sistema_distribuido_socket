import fs from 'fs';
import { Router } from 'express';

class Logins {
    constructor() {
        this.router = Router();
    }

    initRoutes() {
        this.router.get('/', async (req, res) => {
            const logins = this.getLogins();
            res.json(logins);
        });
    }

    getLogins() {
        const loadJSON = (path) => JSON.parse(fs.readFileSync(new URL(path, import.meta.url)));
        const data = loadJSON('../database/universitydb.login.json');
        return data;
    }

    routes() {
        this.initRoutes();
        return this.router;
    }
}

export default Logins;