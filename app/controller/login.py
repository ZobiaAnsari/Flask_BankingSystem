from flask import request, jsonify, make_response
from flask_restful import Resource
from app.models.user import User
from app.serde.userSchema import UserSchema
import jwt
# from  jwt import encode
import datetime
from app import app

class loginView(Resource):

    def post(self):
        try:
            data = UserSchema().load(request.get_json())
            accountNo = data['accountNo']
            accountPin = data['accountPin']

            if not accountNo or not accountPin:
                return jsonify({'msg':'enter credentials'})

            userdata = User.query.filter_by(accountNo=accountNo).first()
            if  not userdata:
                return jsonify({'msg':'Account Not Found'})
            if accountPin!=userdata.accountPin:
                return jsonify({'msg':'Invalid Pin'})
            #  aifccountNo!=userdata.accountNo:
            #     return jsonify({'msg':'Account number  does not match'})
            else:
            # try:
                access_token = jwt.encode({'user_id': userdata.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, str(app.config['SECRET_KEY']), algorithm='HS256')
            # except Exception as e:
            #     return str(e)
                response = make_response(jsonify({"message": "Login Successfully"}))
                response.set_cookie('access_token_cookie',access_token, httponly=True)
                return response
        except Exception as e:
                return str(e)

class logoutView(Resource):
    def get(self):
        response = make_response(jsonify({"message": "Successfully Logout"}))
        response.set_cookie('access_token_cookie', expires=0)
        return response
    