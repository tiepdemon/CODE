const express = require('express');
const router = express.Router();

const recordController = require('../app/controllers/RecordController');

router.use('/:Number',recordController.show);
// router.use('/',recordController.home);

module.exports = router;