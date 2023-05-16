from flask import Blueprint

main_bp = Blueprint('main_bp', __name__, url_prefix='/main')

@main_bp.route('/admin') 
def first_route():
    return "Hello Admin!"