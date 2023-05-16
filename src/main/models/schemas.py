import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType,  SQLAlchemyConnectionField
from models import User

class SchemaUsers(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)

class Query(grapheme.Objecttype):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(SchemaUsers.collection)

schema = graphene.Schema(query=Query)


