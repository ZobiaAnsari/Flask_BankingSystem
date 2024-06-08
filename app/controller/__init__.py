from flask import Blueprint
from flask_restful import Api
from app.controller.user import UserView, UserDataView
from app.controller.login import loginView, logoutView
from app.controller.deposit import Deposit, withdrawal, Statement
from app.controller.changePin import changePin
# from app.controller.lo



bank_blueprint = Blueprint('bank',__name__,url_prefix='/bank')

api = Api(bank_blueprint)



api.add_resource(loginView,'/login/')
api.add_resource(logoutView,'/logout/')

api.add_resource(Deposit,'/deposit/')
api.add_resource(withdrawal,'/withdrawal/')
api.add_resource(Statement,'/statement/')
api.add_resource(changePin,'/chnagepin/')
api.add_resource(UserView,'/addUser/')
api.add_resource(UserDataView,'/User/<int:id>/')