// const Doctor = require('../models/Doctor');

class TechnicanController {
    //[GET] /news
    home(req, res) {
        res.render('home');
        // Doctor.find()
        //     .then(doctors => {
        //         res.json(doctors);
        //     })
        //     .catch(error => {
        //         console.error('Error fetching doctors:', error);
        //         res.status(500).json({ error: 'Internal server error' });
        //     });
    }
}

module.exports = new TechnicanController();
