from flask import Blueprint

main_bp = Blueprint(
    'main_bp')

@main_bp.route('/admin') 
def first_route():
    return "Hello Admin!"