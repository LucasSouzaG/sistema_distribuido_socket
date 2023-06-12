import fs from 'fs';
import { Router } from 'express';

class Classes {
    constructor() {
        this.router = Router();
    }

    initRoutes() {
        this.router.get('/', async (req, res) => {
            const classes = this.getClasses();
            res.json(classes);
        });
    }

    getClasses() {
        const loadJSON = (path) => JSON.parse(fs.readFileSync(new URL(path, import.meta.url)));
        const data = loadJSON('../database/universitydb.classes.json');
        return data;
    }

    routes() {
        this.initRoutes();
        return this.router;
    }
}

export default Classes;