from database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from flask_uuid import FlaskUUID

app = Flask(__name__)
FlaskUUID(app)

app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    init_db()
    app.run()
