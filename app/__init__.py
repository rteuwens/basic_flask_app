# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import UserManager

# local imports
import os, datetime
from config import app_config # used in the application factory

# initializing extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    """ designing the application factory
    
    Arguments:
        config_name {string} -- dictionary key for the app_config variab
    
    Returns:
        object -- our app, with db, bcrypt, migrate, and login_manager 
    """

    # setting up the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    
    # initializing extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # our table structures
    from app.models import User, Role, UserRoles  # refers to the classes for our database inside models.py

    """
        To create the table structures, one would usually open a python ide and command "from app import db", then "db.create_all()"
        In the case of an application factory, however, this is a bit trickier because you need the app_context. You also 
        don't want to run the command every time you launch the app. Instead, we integrate it in a try-except clause, so it should only run once.
        For all the other database functionality, we opt for flask-migrate and its command line options such as "flask db init".
        
        Commands can be found on: https://flask-migrate.readthedocs.io/en/latest/
    """

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    # Create an administrator profile if the tables exists. If the query fails, create_all.
    # https://github.com/lingthio/Flask-User/blob/master/example_apps/basic_app.py
    with app.app_context():
        try:
            if not User.query.filter(User.email == 'user@example.com').first():
                password = os.environ.get('MYSQL_PASSWORD')
                user = User(
                    username='administrator',
                    email='user@example.com',
                    email_confirmed_at=datetime.datetime.now(),
                    password=user_manager.hash_password(password),
                )
                user.roles.append(Role(name='admin'))
                db.session.add(user)
                db.session.commit()
        except:
            db.create_all()

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
    
    # registering them
    app.register_blueprint(landing)
    app.register_blueprint(dash)

    # delivering the application with registered blueprints
    return app