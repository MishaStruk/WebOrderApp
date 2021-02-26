from flask import Blueprint,render_template,request,flash,url_for,redirect
from flask_login import login_user,login_required,logout_user,current_user
from website import DatabaseMoudle
from website.models import User,Order

views = Blueprint('views',__name__)


@views.route('/',methods = ['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        db = DatabaseMoudle.userDatabase()
        userid = request.form.get('userid')
        print("Getting here")
        print(userid)
        password = request.form.get('password')
        print(password)
        if(len(userid)<1):
            flash("Enter user id",category='error')
        elif(len(password)<1):
            flash("Enter password",category='error')
        else:
            print("Message login test")
            if(db.CheckIfUserIdExist(userid)):
                print("login in user "+userid)
                userlist = db.fetchUserInfo(userid)
                print(userlist)
                user = User(userlist[0],userlist[1],userlist[2])
                if(password == userlist[1]):
                    #login user
                    login_user(user, remember=False)
                    return redirect(url_for('auth.UserPage'))
                else:
                    flash("Incrrect password",category='error')
            else:
                flash("No user",category='error')
    if(request.method == 'GET'):
        if(current_user is not None):
            logout_user()
        return render_template("Login.html")
    return render_template("Login.html")
    