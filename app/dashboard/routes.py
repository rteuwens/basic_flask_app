# third-party
from flask_user import login_required, roles_required

# local
from . import dash # refers to /dash/__init__.py

@dash.route('/dashboard')
@login_required
@roles_required('admin')
def login():
    return 'this page requires you to be an admin'