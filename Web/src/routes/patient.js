const express = require('express');
const router = express.Router();
// const list_recordRouter = require('./list_record')

const patientController = require('../app/controllers/PatientController');

router.post('/store',patientController.store);
router.get('/create_record',patientController.create_record);
router.use('/information',patientController.information);
router.use('/list_record',patientController.list_record);
// router.get('/create_qr',patientController.create_qr);
router.use('/medical_record',patientController.medical_record);
router.use('/',patientController.home);

module.exports = router;