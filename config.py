import os

class Config(object):
    """
    Common configurations
    Only ALL_CAPS_PARAMETERS are read
    """

    # Put any configurations here that are common across all environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # BCRYPT_LOG_ROUNDS = 12 # http://exploreflask.com/en/latest/users.html

    # Encryption
    SECRET_KEY = 'thisisasecret'

    # Flask-Mail SMTP server settings
    MAIL_SERVER = os.environ.get('SMTP_HOST')
    MAIL_PORT = os.environ.get('SMTP_PORT')
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('SMTP_USER')
    MAIL_PASSWORD = os.environ.get('SMTP_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('SMTP_USER')

    # Flask-User settings
    USER_APP_NAME = 'Your application name' # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True                # Enable email authentication
    USER_ENABLE_USERNAME = True             # Username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = os.environ.get('SMTP_USER')
    USER_AFTER_LOGIN_ENDPOINT = 'dash.welcome_back'

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    
    # fetching from user environment variables
    localhost_dbname = os.environ.get('MYSQL_LOCALHOST_DBNAME')

    # setting parameters
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql://root:admin@localhost/{localhost_dbname}'

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
    SQLALCHEMY_DATABASE_URI = f'mysql://{username}:{password}@{hostname}:{port}/{dbname}'

# The variable we import in run.py
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}