import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType,  SQLAlchemyConnectionField
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = "accounts"

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
    remote_was_deleted = db.Column(db.Boolean)
    modified_at = db.Column(db.String(128))
    remote_data = db.Column(db.String(128))


    def __init__(self, remote_id, name, description, classification, type, 
        status, current_balance, currency, account_number, parent_account, company, 
        remote_was_deleted, modified_at, remote_data):

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

class SchemaAccounts(SQLAlchemyObjectType):
    class Meta:
        model = Account
        interfaces = (relay.Node,)

class QueryAccounts(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(SchemaAccounts.connection)
    user_by_name = graphene.Field(List(SchemaAccounts), name=String())

    def resolve_user_by_name(self, info, name):
        return Account.query.filter_by(name=name).all()

schema = graphene.Schema(query=QueryAccounts)

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.String(128), primary_key=True) 
    transaction_type = db.Column(db.String(128))
    remote_id = db.Column(db.String(128))
    remote_data = db.Column(db.String(128))
    number = db.Column(db.String(128))
    transaction_date = db.Column(db.String(128))
    account = db.Column(db.String(128))
    contact = db.Column(db.String(128))
    total_amount = db.Column(db.String(128))
    currency = db.Column(db.String(128))
    remote_was_deleted = db.Column(db.Boolean)

    def __init__(self, transaction_type, remote_id, remote_data, number, transaction_date, 
                account, contact, total_amount, currency, remote_was_deleted):
        
        self.transaction_type = transaction_type
        self.remote_id = remote_id
        self.remote_data = remote_data
        self.number = number
        self.transaction_date = transaction_date
        self.account = account
        self.contact = contact
        self.total_amount = total_amount
        self.currency = currency
        self.remote_was_deleted = remote_was_deleted

class SchemaTransactions(SQLAlchemyObjectType):
    class Meta:
        model = Transaction
        interfaces = (relay.Node,)

class QueryTransactions(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(SchemaTransactions.connection)
    user_by_name = graphene.Field(List(SchemaTransactions), name=String())

    def resolve_user_by_name(self, info, name):
        return Transaction.query.filter_by(name=name).all()

schema1 = graphene.Schema(query=QueryTransactions)