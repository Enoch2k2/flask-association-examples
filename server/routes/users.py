
from flask_restful import Resource
from models.models import User
from config import api


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200


class UserDetails(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first().to_dict()
        return user, 200


api.add_resource(Users, "/api/users")
api.add_resource(UserDetails, "/api/users/<int:id>")
