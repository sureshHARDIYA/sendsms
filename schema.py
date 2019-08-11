from graphene import ObjectType, String, Schema, ID, Field, List
from collections import namedtuple

import json

data = {
    "rows": [
        {"title": "This", "id": "1", "content": "Fucking amazing." },
        {"title": "This 2", "id": "2", "content": "Fucking amazing 2." }
    ]
}

class Post(ObjectType):
    id = ID(required=True)
    title = String(required=True)
    content = String()
    # categories=List(lambda: Category)

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

class Query(ObjectType):
    posts = Field(Post)

    def resolve_posts(context, info):
        return json2obj(json.dumps(data))

Schema = Schema(query=Query)
