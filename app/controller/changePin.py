from flask import jsonify, request
import jwt
from flask_restful import Resource
from app.controller.decorator import token_required
from app.models.user import User
from app import db
from app import app

class changePin(Resource):

    @token_required
    def patch(self):
        try:
            token = request.cookies.get('access_token_cookie')
            user_data = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms = ['HS256'])
            user = User.query.filter_by(id=user_data['user_id']).first()
            data = request.get_json()
            if user:
                user.accountPin = data['pin']
                
                db.session.commit()

                return jsonify({'msg':'Pin Chnged Successfully'})
            else:
                return jsonify({'msg':'User not found'})
        
        except Exception as e:
            return str(e)