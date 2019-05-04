# third-party
from flask_user import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

# local
from app import db, bcrypt


class User(db.Model, UserMixin):

    """ table structure for the app's users
        based on patterns found on: https://flask-user.readthedocs.io/en/latest/quickstart_app.html
    """

    # renaming to the plural
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email = db.Column(db.String(60), index=True, unique=True)
    
    # User authentication 
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email_confirmed_at = db.Column(db.DateTime())
    
    # User information
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)