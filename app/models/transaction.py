from app import db
from datetime import datetime


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    user = db.relationship('User', backref=db.backref('transactions', lazy=True))