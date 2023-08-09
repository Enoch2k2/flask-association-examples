
from flask_restful import Resource
from models.models import Song
from config import api


class Songs(Resource):
    def get(self):
        songs = [song.to_dict() for song in Song.query.all()]
        return songs, 200


class SongDetails(Resource):
    def get(self, id):
        song = Song.query.filter_by(id=id).first().to_dict()
        return song, 200


api.add_resource(Songs, "/api/songs")
api.add_resource(SongDetails, "/api/songs/<int:id>")
