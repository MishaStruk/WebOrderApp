from flask import Blueprint,render_template,request,flash,url_for,redirect
from flask_login import login_user,login_required,logout_user,current_user
from flask import Blueprint
from website import DatabaseMoudle
import time
import datetime

FOODDICT={"pizza": 0, "toast":1, "falafel":2}
auth = Blueprint('auth',__name__)

@auth.route('/UserPage')
@login_required
def UserPage():
    return render_template("UserPage.html",user = current_user)

@auth.route('/logout',methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/ShowOrders')
@login_required
def ShowOrders():
    db = DatabaseMoudle.userDatabase()
    orders = db.fetchOrders(current_user.userid)
    print(orders)
    return render_template("ShowOrders.html",user = current_user,orders = orders)

@auth.route('/AdminOrders')
@login_required
def AdminOrders():
    db = DatabaseMoudle.userDatabase()
    orders=db.fetchAllOrders()
    print(orders)
    return render_template("AdminOrders.html",user = current_user,orders = orders)

@auth.route('/AddOrder', methods = ['GET', 'POST'])
@login_required
def AddOrder():
    if(request.method == 'POST'):
        db = DatabaseMoudle.userDatabase()
        foodType = request.form.get('foodType')
        time = datetime.datetime.now()
        time_str = time.strftime(("%d/%m/%y")) # String of the date
        print(foodType)
        if(foodType is None):
            flash("Please chose a food",category='error')
        else:
            if(db.checkIfOrderExist(current_user.userid,time_str)):
                flash("You already ordered toady",category='error')
                return redirect(url_for('auth.UserPage'))
            else:
                db.addOrder(current_user.userid,foodType,time_str)
                return redirect(url_for('auth.UserPage'))
        
    return render_template("AddOrder.html",user = current_user)
