const express = require('express');
const router = express.Router();

const doctorController = require('../app/controllers/DoctorController');

router.post('/store',doctorController.store);
router.get('/create',doctorController.create);
router.use('/',doctorController.home);

module.exports = router;