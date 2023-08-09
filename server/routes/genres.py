
from flask_restful import Resource
from models.models import Genre
from config import api


class Genres(Resource):
    def get(self):
        genres = [genre.to_dict() for genre in Genre.query.all()]
        return genres, 200


class GenreDetails(Resource):
    def get(self, id):
        genre = Genre.query.filter_by(id=id).first().to_dict()
        return genre, 200


api.add_resource(Genres, "/api/genres")
api.add_resource(GenreDetails, "/api/genres/<int:id>")
