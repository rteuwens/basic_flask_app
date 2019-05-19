# third-party
from flask import redirect, url_for, render_template

# local
from . import landing # refers to /landing_page/__init__.py

# views
@landing.route('/')
def home():
    return render_template('home.html') 