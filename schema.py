import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import User as UserModel
from models import Role as RoleModel

class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)


class User(MongoengineObjectType):

    class Meta:
        model = UserModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(User)
    all_roles = MongoengineConnectionField(Role)
    role = graphene.Field(Role)


schema = graphene.Schema(query=Query, types=[User, Role])
