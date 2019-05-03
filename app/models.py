# third-party
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

# local
from app import db, login_manager, bcrypt


class User(UserMixin, db.Model):

    """ table structure for the app's users
    
        based on patterns found on: http://exploreflask.com/en/latest/users.html
    """

    # renaming to the plural
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')
    
    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))