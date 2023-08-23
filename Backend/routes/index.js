const express = require('express');
const db = require('../db');
const router = express.Router();

router.get('/test', async (req,res,next) => { // route is appended to /api in server.js
    try {
        let results = {"employees":[{"firstName":"John", "lastName":"Doe"}]};
        res.json(results);
    } catch(e) {
        console.log(e);
        res.sendStatus(500);
    }
});

module.exports = router;