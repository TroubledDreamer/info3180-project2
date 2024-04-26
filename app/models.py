# Add any model classes for Flask-SQLAlchemy here
from werkzeug.security import generate_password_hash

from app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    location = db.Column(db.String(100))
    biography = db.Column(db.String(100))
    profile_photo = db.Column(db.String(100))
    joined_on = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(
        self,
        firstname,
        lastname,
        username,
        password,
        email,
        location,
        biography,
        profile_photo,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = generate_password_hash(password, method="pbkdf2:sha256")
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo


class Follows(db.Model):
    __tablename__ = "follows"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)


class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(100))
    photo = db.Column(db.String(100))
    user_id = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, caption, photo, user_id):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id


class Likes(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
