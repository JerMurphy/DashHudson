from http import HTTPStatus
import re
from flask import Blueprint
from flask import request, jsonify
from webargs.flaskparser import use_args

from connections.models.person import Person
from connections.models.connection import Connection, ConnectionType
from connections.schemas import ConnectionSchema, PersonSchema

blueprint = Blueprint('connections', __name__,)

@blueprint.route('/people', methods=['GET'])
def get_people():
    sort = request.args.get('sort', None)
    reverse = request.args.get('reverse', None)
    people_schema = PersonSchema(many=True)
    people = Person.query.all()
    # assumes alphabetical order unless reverse param is "asc";
    reverse = True if reverse == 'asc' else reverse == False
    if(sort == 'name'):
        people.sort(key=lambda x: x.first_name, reverse=reverse)
    if(sort == 'createdAt'):
        people.sort(key=lambda x: x.created_at, reverse=reverse)
    return people_schema.jsonify(people), HTTPStatus.OK


@blueprint.route('/people', methods=['POST'])
@use_args(PersonSchema(), locations=('json',))
def create_person(person):
    isValid = checkValidity(person)
    if(isValid['passed']):
        person.save()
        return PersonSchema().jsonify(person), HTTPStatus.CREATED
    else:
        return jsonify({"errors": isValid['errors'],'description': "Input failed validation."}), HTTPStatus.BAD_REQUEST

def checkValidity(person):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(person.first_name is not None and person.last_name is not None and person.email is not None):
        if(re.search(regex,person.email)):  
            return {'passed':True} #has all fields and email is correct
        else:  
            return {'passed':False, 'errors': {'email': "Not a valid email address."}} # email is not right
    else:
        return {'passed':False, 'errors': {'error': "Missing Inputs"}} # missing params



# /connections takes in a from_id and returns all people that id is connected to with their info
@blueprint.route('/connections', methods=['GET'])
def get_connections():
    connection_schema = ConnectionSchema(many=True)
    people_list = []
    connections = Connection.query.all()
    for x in connections:
        if(x.to_person_id):
            person = Person.query.get(x.to_person_id)
            new_obj = {
                "first_name" : person.first_name,
                "last_name" : person.last_name,
                "id": person.id,
                "email": person.email,
                "connection_type": x.connection_type.value,
                "connection_id": x.id,
                "from_person_id": x.from_person_id
            }
            people_list.append(new_obj)
        else:
            print(x.id)
    return jsonify(people_list), HTTPStatus.OK

@blueprint.route('/connections/<connection_id>', methods=['PATCH'])
def patch_connections(connection_id):
    newtype = request.json['type'] # get new connection type
    if hasattr(ConnectionType, newtype): # verify that the Connection Type has the attribute you're trying to change to
        connection_schema = ConnectionSchema() 
        connection = Connection.query.get(connection_id) # find existing connection
        connection.connection_type = newtype # update the local version of the connection
        connection.update() # use pre build CRUD update to update live record in DB
        return connection_schema.jsonify(connection), HTTPStatus.OK # return updated value
    else:
        return jsonify({'error': "Invalid Type"}), HTTPStatus.BAD_REQUEST

    

@blueprint.route('/connections', methods=['POST'])
@use_args(ConnectionSchema(), locations=('json',))
def create_connection(connection):
    connection.save()
    person = Person.query.get(connection.to_person_id)
    new_obj = {
        "first_name" : person.first_name,
        "last_name" : person.last_name,
        "id": person.id,
        "email": person.email,
        "connection_type": connection.connection_type.value,
        "connection_id": connection.id,
        "from_person_id": connection.from_person_id
    }
    return jsonify(new_obj), HTTPStatus.CREATED
