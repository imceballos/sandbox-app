from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy
from main.blueprints.main_route import app
from main import db
from main.business.accounts import get_accounts
from main.models.models import Account

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    try:
        db.drop_all()
        db.create_all()
        db.session.commit()
    except Exception as e:
        print(e)

@cli.command("seed_db")
def seed_db():
    accounts = get_accounts()
    for account in accounts:
        instance_account = Account(account['id'], account['remote_id'], account['name'] ,account['description'], 
              account['classification'], account['type'], account['status'], account['current_balance'],
              account['currency'], account['account_number'], account['parent_account'],
              account['company'], account['remote_was_deleted'], account['modified_at'], account['remote_data'])
        db.session.add(instance_account)
        db.session.commit()

if __name__ == "__main__":
    cli()