import fs from 'fs';
import { Router } from 'express';

class Courses {
    constructor() {
        this.router = Router();
    }

    initRoutes() {
        this.router.get('/', async (req, res) => {
            const courses = this.getCourses();
            res.json(courses);
        });
    }

    getCourses() {
        const loadJSON = (path) => JSON.parse(fs.readFileSync(new URL(path, import.meta.url)));
        const data = loadJSON('../database/university.courses.json');
        return data;
    }

    routes() {
        this.initRoutes();
        return this.router;
    }
}

export default Courses;