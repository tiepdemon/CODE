const patientRouter = require('./patient');
const doctorRouter = require('./doctor');
const adminRouter = require('./admin');
const recordRouter = require('./records');
const accoutRouter = require('./accout');
const technicanRouter = require('./technican');

function route(app) {
    app.use('/patient',patientRouter);
    app.use('/doctor',doctorRouter);
    app.use('/admin',adminRouter);
    app.use('/records',recordRouter);
    app.use('/technican',technicanRouter);
    app.use('/',accoutRouter);
}

module.exports = route;
