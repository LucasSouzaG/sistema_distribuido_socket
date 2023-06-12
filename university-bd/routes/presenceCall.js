import fs from 'fs';
import { Router } from 'express';

class PresenceCall {
    constructor() {
        this.router = Router();
    }

    initRoutes() {
        this.router.get('/', async (req, res) => {
            const presenceCall = this.getPresenceCalls();
            res.json(presenceCall);
        });
    }

    getPresenceCalls() {
        const loadJSON = (path) => JSON.parse(fs.readFileSync(new URL(path, import.meta.url)));
        const data = loadJSON('../database/universitydb.presenceCall.json');
        return data;
    }

    routes() {
        this.initRoutes();
        return this.router;
    }
}

export default PresenceCall;