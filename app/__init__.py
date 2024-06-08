from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/bank'


db = SQLAlchemy()

def create_app():
    global app
    # app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/bank'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SECRET_KEY']='banking project'
    db.init_app(app)

    from app.controller import bank_blueprint

    app.register_blueprint(bank_blueprint,url_prefix=f'{bank_blueprint.url_prefix}/api/')
    

    # with app.app_context():
    #     db.create_all()

    return app

