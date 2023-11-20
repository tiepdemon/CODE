const Record = require('../models/Record');

class RecordController {
    show(req, res,next) {
        console.log(req.params.Number);
        Record.findOne({ Number: req.params.Number })
            .then(record => {
                res.json(record.Number);
            })
            .catch(next)
    }
}

module.exports = new RecordController();
