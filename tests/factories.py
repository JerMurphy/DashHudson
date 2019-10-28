from factory import Faker, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from connections.database import db
from connections.models.connection import Connection
from connections.models.person import Person


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:

        abstract = True
        sqlalchemy_session = db.session


class PersonFactory(BaseFactory):
    """Person factory."""

    email = Sequence(lambda n: f'person{n}@example.com')
    first_name = Faker('first_name')
    last_name = Faker('last_name')

    class Meta:

        model = Person


class ConnectionFactory(BaseFactory):
    """Connection factory."""
    
    #As long as you pass in the right variables from the test function for the ids it works
    #for some reason, and Im probably doing something wrong, it wont let me create new people and use their id's inside here
    #commented it out so the tests would pass with valid data

    # from_person = SubFactory(PersonFactory)
    # to_person = SubFactory(PersonFactory)
    # BaseFactory.Meta.sqlalchemy_session.commit()
    # from_person_id = from_person.id
    # to_person_id = to_person.id

    connection_type = 'friend'   

    class Meta:

        model = Connection
