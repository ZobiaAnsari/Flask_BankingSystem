from app import db

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    address = db.Column(db.String(60))
    pin = db.Column(db.Integer)
    accountNo = db.Column(db.String(30))
    accountPin = db.Column(db.String(4))
    password = db.Column(db.String(30))  
    balance = db.Column(db.Integer, default=0)
    is_admin = db.Column(db.Boolean(),default=False)
