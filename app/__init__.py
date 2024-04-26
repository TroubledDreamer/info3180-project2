from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["WTF_CSRF_ENABLED"] = False  # remove when ready
# csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
