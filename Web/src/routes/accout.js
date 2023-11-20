const express = require('express');
const router = express.Router();

const accoutController = require('../app/controllers/AccoutController');

router.post('/store',accoutController.store);
router.get('/register',accoutController.register);
// router.post('/login',accoutController.login);
router.get('/',accoutController.home);

module.exports = router;