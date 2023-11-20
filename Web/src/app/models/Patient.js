const { default: mongoose } = require("mongoose");

const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

const Patient = new Schema({
    Username : {type: String,maxlength: 20},
    Password : {type: String,maxlength: 20},
    Userfirstname : {type: String,maxlength: 255},
    Userlastname : {type: String,maxlength: 255},
    Date : {type: Date},
    CCCD : {type: Number,length: 10},
    Useradress : {type: String,maxlength: 2000},
    Userphone:{type: Number,maxlength: 12},
    Sex : {type: String,maxlength: 15},
    Nation : {type: String,maxlength: 50},
    Religon : {type: String,maxlength: 50},
    Job : {type: String,maxlength: 50},
    Insurancecode : {type: String,maxlength: 25},
    Familyfirstname : {type: String,maxlength: 255},
    Familylastname : {type: String,maxlength: 255},
    Familyadress : {type: String,maxlength: 2000},
    Familyphone:{type: String,maxlength: 12},
})

module.exports = mongoose.model('Patient',Patient);