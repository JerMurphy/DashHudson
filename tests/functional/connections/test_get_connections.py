from http import HTTPStatus

from tests.factories import ConnectionFactory, PersonFactory


EXPECTED_FIELDS = [
    'id',
    'from_person_id'
    'to_person_id'
    'connection_type'
]


def test_can_get_connection(db, testapp):
    res = testapp.get('/connections?from_id=1')

    assert res.status_code == HTTPStatus.OK #assert it returned an OK
    for connection in res.json:
        for field in EXPECTED_FIELDS:
            assert field in connection #assert all required fields are present in response
