from flask import request, jsonify
import jwt
from app import app
from app.models.user import User
from flask_restful import Resource
from app.models.transaction import Transaction
from app.serde.userSchema import UserSchema
from app.serde.transactionSchema import TransactionSchema
from app.controller.decorator import token_required 
from app import db

class Deposit(Resource):
    @token_required
    def post(self):
        token = request.cookies.get('access_token_cookie')
        user_data = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms = ['HS256'])
        user = User.query.get(user_data['user_id'])

        data=request.get_json()
        transaction_type = 'Deposit'
        if data['amount']<0:
            return jsonify({'msg':'enter valid amount'})
        else:
            tran = Transaction(user_id = user.id, transaction_type=transaction_type, amount =data['amount'])

            db.session.add(tran)
            db.session.commit()

            user.balance+=data['amount']
            db.session.commit()

            return jsonify({'msg':'TRansaction done'})

    @token_required
    def get(self):
        token = request.cookies.get('access_token_cookie')
        user_data = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms = ['HS256'])
        user = User.query.filter_by(id = user_data['user_id']).first()

        return jsonify({'your balance ':user.balance})
    

class withdrawal(Resource):

    @token_required
    def post(self):
        token = request.cookies.get('access_token_cookie')
        user_data = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms = ['HS256'])
        user = User.query.get(user_data['user_id'])
        
        data=request.get_json()
        transaction_type = 'withdrawal'
        
        if data['amount']<0:
            return jsonify({'msg':'enter valid amount'})
        else:
            tran = Transaction(user_id = user.id, transaction_type=transaction_type, amount =data['amount'])

            db.session.add(tran)
            db.session.commit()

            if data['amount']<user.balance:

                user.balance-=data['amount']
                db.session.commit()
                return jsonify({'your balance ':user.balance})

            else:
                return jsonify({'msg':'Insuffication amount'})
    
class Statement(Resource):

    @token_required
    def get(self):
        
        token = request.cookies.get('access_token_cookie')
        user_data = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms = ['HS256'])
        user = User.query.get(user_data['user_id'])

        trans = Transaction.query.filter_by(user_id=user.id)
        transData = TransactionSchema(many=True).dump(trans)
        if transData == []:
            return jsonify({'msg':'No Transaction Found'})
            
        else:
            
            return jsonify(transData)
