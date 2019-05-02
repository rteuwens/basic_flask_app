# third-party imports
from flask import Flask

# local imports
from config import app_config # used in the application factory


# designing our app factory
def create_app(config_name):

    # initializing the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # importing and registering blueprints
    from .landing_page import landing as landing_blueprint
    app.register_blueprint(landing_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # delivering the initialized application
    return app