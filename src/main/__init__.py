from flask import Flask, jsonify
from .blueprints.main_routes import main_bp
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object("main.config.Config")

db = SQLAlchemy(app)

app.register_blueprint(main_bp)
