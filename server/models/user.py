from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)

    songs = db.relationship("Song", back_populates="user")
    artists = db.relationship("Artist", back_populates="user")

    serialize_rules = ('-songs.user', '-artists.user')

    @validates("username")
    def check_username(self, key, username):
        if (not username):
            raise ValueError({"message": "Username must exist"})
        length = len(username)
        if (length < 3 or length > 20):
            raise ValueError(
                {"message": "Username must be between 3 and 20 characters long"})

        return username

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"
