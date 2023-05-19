from flask import Flask, jsonify
from flask_graphql import GraphQLView

from main.models.models import schema, schema1

app = Flask(__name__)
app.config.from_object("main.config.Config")

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    ),
)


app.add_url_rule(
    '/graphql1',
    view_func=GraphQLView.as_view(
        'graphql1',
        schema=schema,
        graphiql=True
    ),
)