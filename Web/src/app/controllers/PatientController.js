const Patient = require('../models/Patient');
const Record = require('../models/Record');

class PatientController{
    home(req, res,next) {
        // Thực hiện lại truy vấn để lấy danh sách các bản ghi mới nhất
        Record.find().lean()
            .then(records => {
                // Render trang chủ và truyền danh sách các bản ghi mới
                res.render('patient/patient_home', {
                    layout: 'patient',
                    records: records, // Truyền danh sách các bản ghi mới cho trang chủ
                });
            })
            .catch(next);
    };
    
    register(req,res,next){
        res.render('patient/patient_register',{layout: 'patient',});
    }

    information(req,res,next){
        Patient.find().lean()
            .then(patients => {
                res.render('patient/patient_infor',{
                    patients,
                    layout: 'patient',
                })
            })
            .catch(next);
    };

    list_record(req,res,next){
        Record.find().lean()
            .then(records => {
                res.render('patient/patient_list_record',{
                    records,
                    layout: 'patient',
                })
            })
            .catch(next);
    };
    
    create_record(req,res){
        res.render('patient/create_record',{layout: 'patient',});
    };
    
    medical_record(req,res,next){
        Patient.find().lean()
            .then(patients => {
                res.render('patient/medical_record',{
                    patients,
                    layout: 'patient',
                })
            })
            .catch(next);
    };

    store(req, res, next){
        const fromData = req.body;
        const record = new Record(fromData);
        record.save()
            .then(() => res.redirect('/patient/home'))
            .catch(Error =>{
                console.error();
            })
    }
    // store(req, res, next){
    //     const fromData = req.body;
    //     const patient = new Patient(fromData);
    //     patient.save()
    //         .then(() => res.redirect('/patient/medical_record'))
    //         .catch(Error =>{
    //             console.error();
    //         })
    // }
}

module.exports = new PatientController();
