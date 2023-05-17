import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType,  SQLAlchemyConnectionField
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(128), primary_key=True) 
    remote_id = db.Column(db.String(128))
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    classification = db.Column(db.String(128))
    type = db.Column(db.String(128))
    status = db.Column(db.String(128))
    current_balance = db.Column(db.DECIMAL(10,2))
    currency = db.Column(db.String(128))
    account_number = db.Column(db.String(128))
    parent_account = db.Column(db.String(128))
    company = db.Column(db.String(128))
    remote_was_deleted = db.Column(db.Boolean())
    modified_at = db.Column(db.String(128))
    remote_data = db.Column(db.String(128))


    def __init__(self, remote_id, name, description, classification, type, status):
        self.remote_id = remote_id
        self.name = name
        self.description = description
        self.classification = classification
        self.type = type
        self.status = status
        self.current_balance = current_balance
        self.currency = currency
        self.account_number = account_number
        self.parent_account = parent_account
        self.company = company
        self.remote_was_deleted = remote_was_deleted
        self.modified_at = modified_at
        self.remote_data = remote_data

class SchemaUsers(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(SchemaUsers.connection)

schema = graphene.Schema(query=Query)
