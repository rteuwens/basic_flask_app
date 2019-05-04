# third-party
from flask import redirect, url_for

# local
from . import landing # refers to /landing_page/__init__.py

# views
@landing.route('/')
def home():
    return 'hello world' #redirect(url_for('auth.login'))