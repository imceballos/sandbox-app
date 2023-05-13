from flask import Flask, jsonify
from blueprints.main_routes import main_bp


app = Flask(__name__)


app.register_blueprint(main_bp, url_prefix='/main')