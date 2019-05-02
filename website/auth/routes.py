# local
from . import auth # refers to /auth/__init__.py

@auth.route('/login')
def login():
    return 'hello world'