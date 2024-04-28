"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import datetime
import os
from functools import wraps

import jwt
from flask import g, jsonify, request, send_file, send_from_directory
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from app import app, db
from app.forms import LoginForm, PostForm, RegistrationForm
from app.models import Follows, Likes, Posts, Users

###
# Routing for your application.
###


@app.route("/")
def index():
    return jsonify(message="This is the beginning of our API")


@app.route("/api/v1/csrf-token", methods=["GET"])
def get_csrf():
    return jsonify({"csrf_token": generate_csrf()})


###
# The functions below should be applicable to all Flask apps.
###
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get(
            "Authorization", None
        )  # or request.cookies.get('token', None)

        if not auth:
            return (
                jsonify(
                    {
                        "code": "authorization_header_missing",
                        "description": "Authorization header is expected",
                    }
                ),
                401,
            )

        parts = auth.split()

        if parts[0].lower() != "bearer":
            return (
                jsonify(
                    {
                        "code": "invalid_header",
                        "description": "Authorization header must start with Bearer",
                    }
                ),
                401,
            )
        elif len(parts) == 1:
            return (
                jsonify({"code": "invalid_header", "description": "Token not found"}),
                401,
            )
        elif len(parts) > 2:
            return (
                jsonify(
                    {
                        "code": "invalid_header",
                        "description": "Authorization header must be Bearer + \s + token",
                    }
                ),
                401,
            )

        token = parts[1]
        try:
            payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return (
                jsonify({"code": "token_expired", "description": "token is expired"}),
                401,
            )
        except jwt.DecodeError:
            return (
                jsonify(
                    {
                        "code": "token_invalid_signature",
                        "description": "Token signature is invalid",
                    }
                ),
                401,
            )

        g.current_user = user = payload
        return f(*args, **kwargs)

    return decorated


@app.route("/api/v1/register", methods=["POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = request.files["profile"]
        profile_filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config["UPLOAD_FOLDER"], profile_filename))
        new_user = Users(
            email=email,
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            location=location,
            biography=biography,
            profile_photo=profile_filename,
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(
            {
                "message": "User Successfully added",
                "email": new_user.email,
                "username": new_user.username,
                "password": new_user.password,
                "firstname": new_user.firstname,
                "lastname": new_user.lastname,
                "location": new_user.location,
                "biography": new_user.biography,
                "profile_photo": new_user.profile_photo,
                "created_on": new_user.joined_on,
            }
        )
    else:
        errors = form_errors(form)
        return jsonify({"errors": errors}), 400


@app.route("/api/v1/auth/login", methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.session.execute(
            db.select(Users).filter_by(username=username)
        ).scalar()
        if user:
            # User exists, now verify the password
            if check_password_hash(pwhash=user.password, password=password):
                token = generate_token(user.id)
                return jsonify(
                    {
                        "message": "User Successfully logged In",
                        "token": token,
                        "id": user.id,
                    },
                    200,
                )
            else:
                return jsonify({"message": "Invalid username or password"}), 401
        else:
            return jsonify({"message": "User does not exist"}), 405
    else:
        errors = form_errors(form)
        return jsonify({"errors": errors}), 400


@app.route("/api/v1/auth/logout", methods=["POST"])
@requires_auth
def logout():
    return jsonify({"message": "User successfully logged out."})


@app.route("/api/v1/users/<user_id>/posts", methods=["POST"])
@requires_auth
def post(user_id):
    form = PostForm()
    if form.validate_on_submit():
        photo = request.files["photo"]
        photo_filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo_filename))
        description = form.description.data
        new_post = Posts(caption=description, photo=photo_filename, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Successfully created a new post"}), 200

    else:
        errors = form_errors(form)
        return jsonify({"errors": errors}), 400


@app.route("/api/user/<user_id>", methods=["GET"])
def get_info(user_id):
    user = db.session.execute(db.select(Users).filter_by(id=user_id)).scalar()
    posts_by_user = db.session.execute(
        db.select(Posts).filter_by(user_id=user_id)
    ).fetchall()
    user_post_count = len(posts_by_user)
    user_followers = db.session.execute(
        db.select(Follows).filter_by(user_id=user_id)
    ).fetchall()
    user_followers_count = len(user_followers)
    if user:
        return jsonify(
            {
                "fullname": user.firstname + " " + user.lastname,
                "location": user.location,
                "joined": user.joined_on,
                "biography": user.biography,
                "profile": user.profile_photo,
                "posts": user_post_count,
                "follows": user_followers_count,
            }
        )
    else:
        return jsonify({"error": "error occured"})


@app.route("/api/v1/users/<user_id>/posts", methods=["GET"])
@requires_auth
def get_post(user_id):
    posts = Posts.query.filter_by(user_id=user_id).all()
    post_list = []
    for post in posts:
        post_data = {
            "id": post.id,
            "user_id": user_id,
            "photo": post.photo,
            "description": post.caption,
            "created_on": post.created_on,
        }
        post_list.append(post_data)
    return jsonify({"posts": post_list})


@app.route("/api/users/<user_id>/follow", methods=["POST"])
@requires_auth
def follow_user(user_id):
    target_id = user_id
    follower_id = request.json["id"]

    # check if the follow relationship already exists
    existing_follow = Follows.query.filter_by(
        user_id=target_id, follower_id=follower_id
    ).first()
    if existing_follow:
        return jsonify({"message": "You are already following this user"}), 330
    if target_id == follower_id:
        return jsonify({"message": "cannot follow self"}), 252
    new_follow = Follows(user_id=target_id, follower_id=follower_id)
    db.session.add(new_follow)
    db.session.commit()
    return jsonify({"message": "you are now following that user."}), 200


@app.route("/api/v1/posts", methods=["GET"])
@requires_auth
def get_all_post():
    posts = Posts.query.all()
    post_list = []
    for post in posts:
        usecase = Users.query.filter_by(id=post.user_id).first()
        post_data = {
            "id": post.id,
            "user_id": post.user_id,
            "photo": post.photo,
            "description": post.caption,
            "created_on": post.created_on,
            "likes": Likes.query.filter_by(id=post.id).count(),
            "username": usecase.username,
            "profile": usecase.profile_photo,
        }
        post_list.append(post_data)
    return jsonify({"posts": post_list})


@app.route("/api/v1/posts/<post_id>/like", methods=["POST"])
@requires_auth
def like(post_id):
    user_id = request.json["user_id"]
    existing_like = Likes.query.filter_by(post_id=post_id, user_id=user_id).first()
    if existing_like:
        return jsonify({"message": "You have already liked this post"}, 400)
    new_like = Likes(post_id=post_id, user_id=user_id)
    db.session.add(new_like)
    db.session.commit()
    num_likes = Likes.query.filter_by(post_id=post_id).count()
    return jsonify({"message": "Post liked!", "Likes": num_likes}), 200


@app.route("/api/v1/uploads/<filename>")
def get_images(filename):
    return send_from_directory(
        os.path.join(os.getcwd(), app.config["UPLOAD_FOLDER"]), filename
    )


@app.route("/api/v1/generate-token/<uid>", methods=["POST"])
def generate_token(uid):
    timestamp = datetime.datetime.utcnow()
    payload = {
        "uid": uid,
        "iat": timestamp,
        "exp": timestamp + datetime.timedelta(minutes=10),
    }
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
    return token


@app.route("/api/v1/decode-token", methods=["POST"])
def decode_token():
    token = request.json
    detoken = jwt.decode(token.value, app.config["SECRET_KEY"], algorithm="HS256")
    return jsonify(token=detoken.uid)


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = "Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error,
            )
            error_messages.append(message)

    return error_messages


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response
