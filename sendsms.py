from flask import Flask, render_template
from flask_graphql import GraphQLView
from schema import Schema
from graphql import GraphQLCachedBackend

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema, graphiql=True))

# app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=Schema, batch=True))

def create_app(path='/graphql', **kwargs):
    # backend = GraphQLCachedBackend(GraphQLQuiverBackend({"async_framework": "PROMISE"}))
    backend = None
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=Schema, backend=backend, **kwargs))
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()
