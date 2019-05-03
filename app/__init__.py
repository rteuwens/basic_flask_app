# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

# local imports
from config import app_config # used in the application factory

# initializing extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_name):
    """ designing the application factory
    
    Arguments:
        config_name {string} -- dictionary key for the app_config variab
    
    Returns:
        object -- our app
    """

    # setting up the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # initializing extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # setting up the login manager
    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page.'
    login_manager.login_view = 'auth.login'

    # our table structures
    from app import models

    # bellw code can be used if you want to force creation of the tables. We will use flask-migrate's "flask db init" and other commands instead.
    # with app.app_context():
    #     db.create_all()

    # importing and registering blueprints
    load_blueprints(app)

    # delivering the initialized application
    return app


def load_blueprints(app):
    """ registers the blueprints
    
    Arguments:
        app {object} -- our flask app, to which we append our blueprints.

    Returns:
        object -- our app
    """

    # importing them from their respective folders
    from .landing_page import landing
    from .auth import auth 

    # registering them
    app.register_blueprint(landing)
    app.register_blueprint(auth, url_prefix='/auth')

    # delivering the application with registered blueprints
    return app