const express = require('express');
const router = express.Router();

const technicanController = require('../app/controllers/TechnicanController');

router.use('/',technicanController.home);

module.exports = router;