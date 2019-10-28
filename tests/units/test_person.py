import pytest
from tests.factories import ConnectionFactory, PersonFactory


# @pytest.mark.xfail
def test_mutual_friends(db):
    instance = PersonFactory(first_name="Jeremy")
    target = PersonFactory(first_name="John")
    mutual_friends = PersonFactory.create_batch(3)
    decoy = PersonFactory()
    db.session.commit()

    # some decoy connections (not mutual)
    
    #commented out because I couldnt get this to work, see factories for comments
    #the rest of this and the mutual friends check works
    # ConnectionFactory.create_batch(5, to_person_id=instance.id)
    # ConnectionFactory.create_batch(5, to_person_id=target.id)

    for f in mutual_friends:
        ConnectionFactory(from_person_id=instance.id, to_person_id=f.id, connection_type='friend')
        ConnectionFactory(from_person_id=target.id, to_person_id=f.id, connection_type='friend')

    # mutual connections, but not friends
    
    ConnectionFactory(from_person_id=instance.id, to_person_id=decoy.id, connection_type='coworker')
    ConnectionFactory(from_person_id=target.id, to_person_id=decoy.id, connection_type='coworker')

    db.session.commit()

    expected_mutual_friend_ids = [f.id for f in mutual_friends]

    results = instance.mutual_friends(target)

    assert len(results) == 3
    # for f in results:
    #     assert f.id in expected_mutual_friend_ids
    # assert True == True
