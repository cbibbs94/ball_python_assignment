from flask import Blueprint

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

@bp.route('/')
def index():
    return 'The landing page'