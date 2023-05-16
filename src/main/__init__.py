from flask import Flask, jsonify
from .blueprints.main_routes import main_bp
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object("main.config.Config")

db = SQLAlchemy(app)

app.register_blueprint(main_bp)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email