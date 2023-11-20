
class AdminController{
    home(req,res){
        res.render('home');
    };

    create_user(req,res){
        res.render('home');
    };

    manage_user(req,res){
        res.render('home');
    };

    room(req,res){
        res.render('home');
    };

}

module.exports = new AdminController();