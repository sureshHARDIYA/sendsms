from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField,
    ListField, ReferenceField, StringField, EmailField
)
import uuid


class Role(Document):
    meta = {'collection': 'role'}
    name = StringField()

class User(Document):
    meta = {'collection': 'user'}
    uuid = StringField(required=True, primary_key= True, default=uuid.uuid4())
    firstName = StringField(required=True, max_length=200)
    middleName = StringField()
    lastName = StringField()
    email= EmailField(required=True, unique=True)
    createdOn = DateTimeField(default=datetime.now)
    lastActiveOn = DateTimeField(default=datetime.now)
    roles = ListField(ReferenceField(Role))
