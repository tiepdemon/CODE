const mongoose = require('mongoose');

async function connect(){
    try{
        await mongoose.connect('mongodb://127.0.0.1:27017/so_y_te');
        console.log("Connected to the database successfully!!");
    } catch (error){
        console.error('Failed to connect to the database:', error);
    }
}

module.exports = { connect };
