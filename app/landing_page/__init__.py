from flask import Blueprint

landing = Blueprint(
    'landing'
    ,__name__
    ,template_folder='templates'
)

from . import routes