from config import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)

    songs = db.relationship("Song", back_populates="user")
    artists = db.relationship("Artist", back_populates="user")

    serialize_rules = ('-songs.user', '-artists.user',)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"
