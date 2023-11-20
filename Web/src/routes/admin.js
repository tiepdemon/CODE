const express = require('express');
const router = express.Router();

const adminController = require('../app/controllers/AdminController');

router.use('/create_user',adminController.home);
router.use('/manage_user',adminController.home);
router.use('/room',adminController.room);
router.use('/',adminController.home);

module.exports = router;