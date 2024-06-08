from flask import jsonify, request
from flask_marshmallow import Marshmallow
from app.serde.userSchema import UserSchema
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from app import db
from app.controller.decorator import token_required
from app.models.user import User
import marshmallow
import random 
import time




class UserView(Resource):
    
    def post(self):
        try:
            data = UserSchema(unknown=marshmallow.INCLUDE).load(request.get_json())
            
            if not data['name'] or not data['phone'] or not  data['email'] :
                return jsonify({'msg':'Plese enter all details'})

            if User.query.filter_by(email=data['email']).count():
                return str('This user name is already exist')
            
            hashPass = data['password']
            current_time = int(time.time())
            random.seed(current_time)
            accNo = random.randint(1000000000, 9999999999)
            data.pop('password',"")
            newUser = User(password=hashPass,accountNo=accNo,**data)

            db.session.add(newUser)
            db.session.commit()

            return jsonify({'msg':'User Registered'},{'Your Account NUmber : ':accNo})
        
        except Exception as e:
            return str(e)

        
    def get(self):
        alldata = User.query.all()
        allUser = UserSchema(many=True).dump(alldata)
        return jsonify(allUser)



class UserDataView(Resource):

    def get(self,id):
        id=id
        data = User.query.filter_by(id=id).first()
        if data is None:
            return str({'msg':'This id has no Data'})
        user = UserSchema().dump(data)
        return jsonify(user)

    def put(self,id):
        data = UserSchema().load(request.get_json())
        userdata = User.query.filter_by(id=id).first()
        if data is None:
            return str({'msg':'This id has no Data'})
        else:
            userdata.name=data['name']
            userdata.email=data['email']
            userdata.phone=data['phone']
            userdata.address=data['address']
            userdata.pin=data['pin']
            userdata.accountPin=data['accountPin']
            userdata.password=data['password']
            db.session.commit()
        return jsonify({'msg':'data updated'})

    def delete(self,id):
        try:
            data = User.query.filter_by(id=id).first()
            if data is None:
                return str({'msg':'This id has no Data'})
            db.session.delete(data)
            db.session.commit()
            return jsonify({'msg':'data deleted'})
        except Exception as e:
                return str(e)
