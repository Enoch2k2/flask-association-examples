from config import db
from sqlalchemy_serializer import SerializerMixin


class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="artists")
    songs = db.relationship("Song", back_populates="artist")
    genres = db.relationship(
        "Genre", secondary="songs", back_populates="artists")

    serialize_rules = ('-user.artists', '-song.artists',
                       '-genres.artists', '-genres.songs')

    def __repr__(self):
        return f"<Artist id={self.id} name={self.name}>"
