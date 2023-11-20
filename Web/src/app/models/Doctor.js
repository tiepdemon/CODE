const { default: mongoose } = require("mongoose");

const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

const Doctor = new Schema({
  name: { type: String,},
  age: {type: Number},

});

module.exports = mongoose.model('Doctor',Doctor);