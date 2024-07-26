from flask import Blueprint
from app.services.iuserServices import IUserServices
from app.services.implementation import UserServicesImplementation

userRoute = Blueprint('user', __name__, url_prefix='/user')
iUserServices: IUserServices = UserServicesImplementation()

class UserController():

    @userRoute.route("/getAll", methods=["GET"])
    def getAll():
        return iUserServices.getAll()