import fs from 'fs';
import { Router } from 'express';

class Students {
    constructor() {
        this.router = Router();
    }

    initRoutes() {
        this.router.get('/', async (req, res) => {
            const students = this.getStudents();
            res.json(students);
        });
    }

    getStudents() {
        const loadJSON = (path) => JSON.parse(fs.readFileSync(new URL(path, import.meta.url)));
        const data = loadJSON('../database/university.students.json');
        return data;
    }

    routes() {
        this.initRoutes();
        return this.router;
    }
}

export default Students;