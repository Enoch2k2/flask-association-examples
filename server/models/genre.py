from config import db
from sqlalchemy_serializer import SerializerMixin


class Genre(db.Model, SerializerMixin):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    songs = db.relationship("Song", back_populates="genre")
    artists = db.relationship(
        "Artist", secondary="songs", back_populates="genres")

    serialize_rules = ("-songs.genre", "-artists.genres",
                       "-songs.user", "-artists.user", "-artists.songs")

    def __repr__(self):
        return f"<Genre id={self.id} name={self.name}>"
