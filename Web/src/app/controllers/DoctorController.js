const Doctor = require('../models/Doctor');

class DoctorController {
    //[GET] /news
    home(req, res,next) {
        Doctor.find().lean()
            .then(doctors => {
                res.render('doctor/doctor_home',{
                    doctors,
                    layout: 'doctor',
                },)
            })
            .catch(next);
    }

    create(req, res, next){
        res.render('doctor/create');
    }
    
    store(req, res, next){
        const fromData = req.body;
        const doctor = new Doctor(fromData);
        doctor.save()
            .then(() => res.redirect('/doctor'))
            .catch(Error =>{
                console.error();
            })
    }
}

module.exports = new DoctorController();
