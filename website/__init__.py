from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '<Enter Secret Key>'

    login_manager = LoginManager()
    login_manager.login_view = 'view.home'
    login_manager.init_app(app)

    

    from .views import views 
    from .auth import auth

    #URL register to the app
    app.register_blueprint(views,url_perfix = '/')
    app.register_blueprint(auth,url_perfix = '/')

    from website import DatabaseMoudle
    from website import models
    
    @login_manager.user_loader
    def load_user(id):
        print(id)
        if(id is not None):
            db = DatabaseMoudle.userDatabase()
            print("Message:Run test load user")
            fetched_user_from_db = db.fetchUserInfo(id)
            user = models.User(fetched_user_from_db[0],fetched_user_from_db[1],fetched_user_from_db[2])
            return user
    return app