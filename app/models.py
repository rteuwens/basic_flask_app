# third-party
from flask_user import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

# local
from app import db, bcrypt


class User(db.Model, UserMixin):

    """ table structure for the app's users
        based on patterns found on: http://exploreflask.com/en/latest/users.html
                                and https://flask-user.readthedocs.io/en/latest/quickstart_app.html
    """

    # renaming to the plural
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    
    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(60, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email_confirmed_at = db.Column(db.DateTime())
    
    # User information
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    
    # password_hash = db.Column(db.String(128))
    # 
    # @hybrid_property
    # def password(self):
        # return self._password
    # 
    # @password.setter
    # def _set_password(self, plaintext):
    #    In Python 3, you need to use decode(‘utf-8’) on generate_password_hash() 
    #    https://flask-bcrypt.readthedocs.io/en/latest/
        # self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')
    # 
    # def is_correct_password(self, plaintext):
    #    return bcrypt.check_password_hash(self._password, plaintext)


# Set up user_loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))