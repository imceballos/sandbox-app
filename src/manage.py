from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy
from main.blueprints.main_route import app
from main import db


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    try:
        db.drop_all()
        db.create_all()
        db.session.commit()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()