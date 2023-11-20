const Patient = require('../models/Patient');

class AccoutController{
    home(req,res,next){
        res.render('home');
    }

    register(req,res,next){
        res.render('register');
    }

    store(req, res, next){
        const fromData = req.body;
        const patient = new Patient(fromData);
        patient.save()
            .then(() => res.redirect('/'))
            .catch(Error =>{
                console.error();
            })
    }

    // login(req, res, next){
    //     Patient.find().lean()
    //         .then(patients => {
    //             Patient.find().lean()
    //                 .then(patients => {
    //                     res.render('patient/patient_infor',{
    //                         patients,
    //                         layout: 'patient',
    //                     })
    //                 })
    //         })
    //         .catch(next);
    // }
}

module.exports = new AccoutController();
