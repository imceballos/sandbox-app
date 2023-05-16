from flask import Blueprint
from models.schema import schema

main_bp = Blueprint('main_bp', __name__, url_prefix='/main')

@main_bp.add_url_rule(
    'graphql',
    schema=schema,
    graphiql=True
)