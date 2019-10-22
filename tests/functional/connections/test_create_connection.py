from http import HTTPStatus

from tests.factories import PersonFactory

from connections.models.connection import Connection, ConnectionType


def test_can_create_connection(db, testapp):
    person_from = PersonFactory(first_name='Diana')
    person_to = PersonFactory(first_name='Harry')
    db.session.commit()
    payload = {
        'from_person_id': person_from.id,
        'to_person_id': person_to.id,
        'connection_type': 'mother',
    }
    res = testapp.post('/connections', json=payload)

    assert res.status_code == HTTPStatus.CREATED

    assert 'id' in res.json

    connection = Connection.query.get(res.json['id'])

    assert connection is not None
    assert connection.from_person_id == person_from.id #assert that the from_id is valid from response
    assert connection.to_person_id == person_to.id #assert that the to_id is valid from response
    assert connection.connection_type.value == 'mother' #assert that the value is the one you entered above
    assert hasattr(ConnectionType, connection.connection_type.value) #assert that the value inserted is in the list of types 
