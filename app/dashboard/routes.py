# third-party
from flask_user import login_required

# local
from . import dash # refers to /dash/__init__.py

@dash.route('/dashboard')
@login_required
def login():
    return 'this page does not yet require to be logged in'