from flask import Flask
from config import config

from .db import db
from .ext import migrate, api, ma

# from .resources.auth.model import User
from .models import *

def create_app(settings):
    app = Flask(__name__)
    app.config.from_object(config[settings])
    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    api.init_app(app)

    from .resources.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app