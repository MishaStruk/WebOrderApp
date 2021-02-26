from flask_login import UserMixin

class Order():
    def __init__(self,userid,foodType,date):
        self.userid = userid
        self.foodType = foodType
        self.date = date



class User(UserMixin):
    def __init__(self,userid,password,admin):
        self.userid = userid
        self.password = password
        self.admin = admin
    def ifAdmin(self):
        if (self.admin == 1):
            return True
        return False
    def get_id(self):
           return (self.userid)
        