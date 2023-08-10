
from flask import request
from flask_restful import Resource
from models.models import User
from config import api, db
from sqlalchemy.exc import IntegrityError
# import ipdb


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200

    def post(self):
        data = request.get_json()
        username = data.get("username")
        try:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

            return user.to_dict(), 201
        except IntegrityError:
            return {"error": "Username already exist"}, 422
        except ValueError as error:
            return {"error": str(error)}


class UserDetails(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first().to_dict()
        return user, 200


api.add_resource(Users, "/api/users")
api.add_resource(UserDetails, "/api/users/<int:id>")
