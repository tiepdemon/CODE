const { default: mongoose } = require("mongoose");

const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

const Record = new Schema({
    Number : {type: String,maxlength: 20},
    CCCD : {type: Number,length: 10},
    Symption : {type: String,maxlength: 2000},
    Anamnesis : {type: String,maxlength: 5000},
    Request : {type: String,maxlength: 2000},
    Diagnostic : {type: String,maxlength: 2000},
    Dateofexa : {type: Date},
    RoomID : {type: Number,maxlength: 10},
    Roomname : {type: String,maxlength: 255},
    Doctorname : {type: String,maxlength: 255},
    Position:{type: Number,maxlength: 255},
    Decription : {type: String,maxlength: 500},
    Note : {type: String,maxlength: 5000},
    Testname : {type: String,maxlength: 255},
    Timein : {type: Date,maxlength: 25},
    Timeout : {type: Date,maxlength: 255},
    Personin : {type: String,maxlength: 255},
    Personout : {type: String,maxlength: 255},
    Resulttest:{type: String,maxlength: 255},
    Result:{type: String,maxlength: 255},
})

module.exports = mongoose.model('Record',Record);