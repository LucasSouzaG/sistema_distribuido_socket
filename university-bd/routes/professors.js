import fs from 'fs';
import { Router } from 'express';

class Professors {
    constructor() {
        this.router = Router();
    }

    initRoutes() {
        this.router.get('/', async (req, res) => {
            const professors = this.getProfessors();
            res.json(professors);
        });
    }

    getProfessors() {
        const loadJSON = (path) => JSON.parse(fs.readFileSync(new URL(path, import.meta.url)));
        const data = loadJSON('../database/universitybd.professors.json');
        return data;
    }

    routes() {
        this.initRoutes();
        return this.router;
    }
}

export default Professors;