from config import db
from sqlalchemy_serializer import SerializerMixin


class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey(
        "genres.id", name="fk_song_genre"))

    user = db.relationship("User", back_populates="songs")
    artist = db.relationship("Artist", back_populates="songs")
    genre = db.relationship("Genre", back_populates="songs")

    serialize_rules = (
        '-user.songs',
        '-artist.songs',
        '-artist.user.songs',
        '-user.artists'
    )

    def __repr__(self):
        return f"<Song id={self.id} title={self.title}>"
