# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    firstname = StringField("Firstname", validators=[InputRequired()])
    lastname = StringField("Lastname", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    biography = StringField("Biography", validators=[InputRequired()])
    profile = FileField(
        "Profile Photo",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png"], "Only images"),
        ],
    )


class LoginForm(FlaskForm):
    username = TextAreaField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class PostForm(FlaskForm):
    description = StringField("Caption", validators=[InputRequired()])
    photo = FileField(
        "Post Photo",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png"], "Only images"),
        ],
    )
