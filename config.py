import os

class Config(object):
    """
    Common configurations
    Only ALL_CAPS_PARAMETERS are read
    """

    # Put any configurations here that are common across all environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 12 # http://exploreflask.com/en/latest/users.html

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    
    # fetching from user environment variables
    localhost_dbname = os.environ.get('MYSQL_LOCALHOST_DBNAME')

    # setting parameters
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql://root:admin@localhost/{localhost_dbname}"

class ProductionConfig(Config):
    """
    Production configurations
    """

    # fetching from user environment variables
    username = os.environ.get('MYSQL_USERNAME')
    password = os.environ.get('MYSQL_PASSWORD')
    hostname = os.environ.get('MYSQL_HOSTNAME')
    port = os.environ.get('MYSQL_PORT')
    dbname = os.environ.get('MYSQL_DBNAME')
    
    # setting parameters
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mysql://{username}:{password}@{hostname}:{port}/{dbname}"

# The variable we import in run.py
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}