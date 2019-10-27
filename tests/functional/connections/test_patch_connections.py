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

    url = "/connections/{}".format(res.json['connection_id'])
    body = {
        "type":'father'
    }
    patch_res = testapp.patch(url, json=body)


    assert patch_res.status_code == HTTPStatus.OK #assert we got an OK back 
    assert 'id' in patch_res.json #assert there is still a valid connection id
    assert patch_res.json['connection_type'] == body['type'] #assert it changed to what we set it to