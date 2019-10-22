from http import HTTPStatus
import re
from flask import Blueprint
from flask import request, jsonify
from webargs.flaskparser import use_args

from connections.models.person import Person
from connections.models.connection import Connection, ConnectionType
from connections.schemas import ConnectionSchema, PersonSchema

blueprint = Blueprint('connections', __name__)


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
    person.save()
    return PersonSchema().jsonify(person), HTTPStatus.CREATED

# /connections takes in a from_id and returns all people that id is connected to with their info
@blueprint.route('/connections', methods=['GET'])
def get_connections():
    from_id = request.args.get('from_id', None)
    connection_schema = ConnectionSchema(many=True)
    people_schema = PersonSchema(many=True)
    people_list = []
    connections = Connection.query.filter(Connection.from_person_id == from_id).all()
    for x in connections:
        person = Person.query.get(x.to_person_id)
        new_obj = {
            "first_name" : person.first_name,
            "last_name" : person.last_name,
            "id": person.id,
            "email": person.email,
            "connection_type": x.connection_type.value,
            "connection_id": x.id
        }
        people_list.append(new_obj)
    return jsonify(people_list), HTTPStatus.OK

@blueprint.route('/connections/<connection_id>', methods=['PATCH'])
def patch_connections(connection_id):
    type = request.json['type'] # get new connection type
    if hasattr(ConnectionType, type): # verify that the Connection Type has the attribute you're trying to change to
        connection_schema = ConnectionSchema() 
        connection = Connection.query.get(connection_id) # find existing connection
        connection.connection_type = type # update the local version of the connection
        connection.update() # use pre build CRUD update to update live record in DB
        return connection_schema.jsonify(connection), HTTPStatus.OK # return updated value
    else:
        return jsonify({'error': "Invalid Type"}), HTTPStatus.BAD_REQUEST

    

@blueprint.route('/connections', methods=['POST'])
@use_args(ConnectionSchema(), locations=('json',))
def create_connection(connection):
    connection.save()
    return ConnectionSchema().jsonify(connection), HTTPStatus.CREATED
