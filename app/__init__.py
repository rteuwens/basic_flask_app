# third-party imports
from flask import Flask

# local imports
from config import app_config # used in the application factory


def create_app(config_name):
    """ designing the application factory
    
    Arguments:
        config_name {string} -- dictionary key for the app_config variab
    
    Returns:
        object -- our app
    """

    # initializing the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

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

    from .landing_page import landing
    from .auth import auth 

    app.register_blueprint(landing)
    app.register_blueprint(auth, url_prefix='/auth')

    return app