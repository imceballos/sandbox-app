from flask import Flask, jsonify
from flask_graphql import GraphQLView

from main.models.models import schema, schema1

app = Flask(__name__)
app.config.from_object("main.config.Config")

app.add_url_rule(
    '/getAccountBalanceBreakdown',
    view_func=GraphQLView.as_view(
        'getAccountBalanceBreakdown',
        schema=schema,
        graphiql=True
    ),
)


app.add_url_rule(
    '/getIncomeExpenseForDate',
    view_func=GraphQLView.as_view(
        'getIncomeExpenseForDate',
        schema=schema1,
        graphiql=True
    ),
)