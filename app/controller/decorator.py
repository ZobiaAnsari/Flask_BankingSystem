from flask import request
import jwt
from functools import wraps
from app import app
from app.models.user import User

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.cookies.get('access_token_cookie')
        if not token:
            return str("token does not exist or expired"), 401
        try:
            secret_key = str(app.config['SECRET_KEY'])
            user_data = jwt.decode(token, secret_key, algorithms = ['HS256'])
            user = User.query.get(user_data['user_id'])
        
        except jwt.ExpiredSignatureError:
            return str({"message":"Token is expired"}), 401
        
        except jwt.InvalidTokenError:
            return str("message" "Invalid Token"), 401
        
        except Exception as e:
            return {"message":"Error decoding token", "error":str(e)}, 401
        return f(*args, **kwargs)
    
    return decorator

def permission(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token = request.cookies.get('access_token_cookie')
        if not token:
            return str("token does not exist or expired"), 401
        secret_key = str(app.config['SECRET_KEY'])
        try:
            user_data = jwt.decode(token, secret_key, algorithms = ['HS256'])
            user = User.query.filter_by(id=user_data['user_id']).first()
        except:
            pass
        if user.is_admin == True:
            # return f(user)
            return f(*args,**kwargs)
        else:
            return "permission denied"
    return decorator


    