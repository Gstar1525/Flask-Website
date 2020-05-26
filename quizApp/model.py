from quizApp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def laod_user(userID):
    return Users.query.get(int(userID))

class Users(db.Model, UserMixin):
    userID = db.Column(db.Integer, nullable = False, primary_key = True)
    name = db.Column(db.String, nullable = False)
    QAs = db.relationship('Q_A', backref = 'U_ID', lazy = True) 
    def get_id(self):
        return (self.userID)
    def __repr__(self):
        return f'User("{self.userID}", "{self.name}")'

class Q_A(db.Model, UserMixin):
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), nullable = False)
    QAid = db.Column(db.Integer, nullable = False, primary_key = True)
    questions = db.Column(db.String, nullable = False)
    option1 = db.Column(db.String, nullable = False)
    option2 = db.Column(db.String, nullable = False)
    option3 = db.Column(db.String, nullable = False)
    option4 = db.Column(db.String, nullable = False)
    

    def __repr__(self):
        return f'Q_A({self.questions}, {self.option1}, {self.option2}, {self.option3}, {self.option4})'