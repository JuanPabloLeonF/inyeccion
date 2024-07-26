from app.services.iuserServices import IUserServices
from app.repositories.iuserRepository import IUserRepository
from app.repositories.userRepositoryImplementation import UserRepositoryImplementation
from flask import jsonify

userRepository: IUserRepository = UserRepositoryImplementation()

class UserServicesImplementation(IUserServices):

    #OVERRIDE
    def getAll(self):
        return jsonify(userRepository.getAll()), 200