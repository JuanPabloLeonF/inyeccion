from app.repositories.iuserRepository import IUserRepository
from flask import jsonify
from app.entities.userEntity import UserEntity
from app.dtos.userDTO import UserDto
from app.configuration.database import db
from sqlalchemy.exc import IntegrityError
import json

class UserRepositoryImplementation(IUserRepository):

    #OVERRIDE
    def getAll(self):
        users = UserEntity.query.all()
        usersList = [UserDto.serialize(user) for user in users]
        return usersList