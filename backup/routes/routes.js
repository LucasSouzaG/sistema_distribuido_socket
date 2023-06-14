import express from 'express';
import { Router } from 'express';
import Logins from './login.js';
import Students from './students.js';
import Classes from './classes.js';
import Professors from './professors.js';
import PresenceCall from './presenceCall.js';

class Routes {
    constructor() {
        this.router = Router();
        this.initRoutes();
    }

    initRoutes() {
        this.router.get('/', (req, res) => {
            res.json({ message: 'Welcome to the University Simulation API' });
        });

        const logins = new Logins();
        this.router.use('/logins', logins.routes());
        const students = new Students();
        this.router.use('/students', students.routes());
        const classes = new Classes();
        this.router.use('/classes', classes.routes());
        const professors = new Professors();
        this.router.use('/professors', professors.routes());
        const presenceCall = new PresenceCall();
        this.router.use('/presenceCall', presenceCall.routes());

    }

    routes() {
        return this.router;
    }
}

export default Routes;