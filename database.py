from mongoengine import connect

from models import User, Role

connect('graphene-mongo-example', host='mongomock://localhost', alias='default')

def init_db():
    admin = Role(name='admin')
    admin.save()

    practitioner = Role(name='practitioner')
    practitioner.save()

    patient = Role(name='patient')
    patient.save()

    tracy = User(
        roles=[practitioner, admin],
        uuid = 'fe4a3e33-cb4b-42ac-a29b-a8160a85af7e',
        firstName = 'Tracy',
        lastName = 'Nordmann',
        email = 'tracy@hotmail.com',
    )
    tracy.save()

    peter = User(
        roles=[admin],
        uuid = 'fe4a3e33-cb4b-42ac-a29b-a8160a85af7c',
        firstName = 'Peter',
        lastName = 'Nordmann',
        email = 'peter@hotmail.com',
    )
    peter.save()

    roy = User(
        roles=[patient],
        uuid = 'fe4a3e33-cb4b-42ac-a29b-a8160a85af7b',
        firstName = 'Roy',
        lastName = 'Nordmann',
        email = 'roy@hotmail.com',
    )
    roy.save()
