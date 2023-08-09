
from flask_restful import Resource
from models.models import Artist
from config import api


class Artists(Resource):
    def get(self):
        artists = [artist.to_dict() for artist in Artist.query.all()]
        return artists, 200


class ArtistDetails(Resource):
    def get(self, id):
        artist = Artist.query.filter_by(id=id).first().to_dict()
        return artist, 200


api.add_resource(Artists, "/api/artists")
api.add_resource(ArtistDetails, "/api/artists/<int:id>")
