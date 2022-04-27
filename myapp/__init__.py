from flask import Flask
from flask_login import LoginManager

from .extensions import db, migrate
from .config import *

# import routes
from .routes.main import main
from .routes.user_page import user_page
from .routes.user_settings import user_settings
from .routes.login import login
from .routes.logout import logout
from .routes.user_registration import user_registration
from .routes.add_book import add_book
from .routes.change_book_info import change_book_info
from .routes.give_book import give_book
from .routes.delete_book import delete_book

# import models
from .models.user import User
from .models.books import Books


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_modifications

    db.init_app(app)
    migrate.init_app(app)
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Routes
    app.register_blueprint(main)
    app.register_blueprint(user_page)
    app.register_blueprint(user_settings)
    app.register_blueprint(add_book)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(change_book_info)
    app.register_blueprint(delete_book)
    app.register_blueprint(user_registration)

    return app