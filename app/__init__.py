# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_user import UserManager

# local imports
from config import app_config # used in the application factory

# initializing extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app(config_name):
    """ designing the application factory
    
    Arguments:
        config_name {string} -- dictionary key for the app_config variab
    
    Returns:
        object -- our app, with db, bcrypt, migrate, and login_manager 
                                                    to-do: add flask-admin
    """

    # setting up the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # initializing extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # our table structures
    from app import models # refers to the classes for our database inside models.py
    from app.models import User

    """
        To create the table structures, one would usually open a python ide and command "from app import db", then "db.create_all()"
        In the case of an application factory, however, this isn't possible and we instead opt for flask-migrate 
        and its command line options such as "flask db init".
        
        Commands can be found on: https://flask-migrate.readthedocs.io/en/latest/
    """

    # bellw code can be used if you want to force creation of the tables. We will use flask-migrate's "flask db init" and other commands instead.
    # with app.app_context():
    #     db.create_all()

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

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
    from .dashboard import dash 
    from .auth import auth 
    
    # registering them
    app.register_blueprint(landing)
    app.register_blueprint(dash)
    app.register_blueprint(auth, url_prefix='/auth')

    # delivering the application with registered blueprints
    return app