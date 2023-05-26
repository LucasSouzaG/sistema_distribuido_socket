import express from 'express';
import { Router } from 'express';
import Courses from './courses.js';
import Students from './students.js';
import Classes from './classes.js';

class Routes {
    constructor() {
        this.router = Router();
        this.initRoutes();
    }

    initRoutes() {
        this.router.get('/', (req, res) => {
            res.json({ message: 'Welcome to the University Simulation API' });
        });

        const courses = new Courses();
        this.router.use('/courses', courses.routes());
        const students = new Students();
        this.router.use('/students', students.routes());
        const classes = new Classes();
        this.router.use('/classes', classes.routes());

    }

    routes() {
        return this.router;
    }
}

export default Routes;