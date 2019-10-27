from connections.database import CreatedUpdatedMixin, CRUDMixin, db, Model


class Person(Model, CRUDMixin, CreatedUpdatedMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(145), unique=True, nullable=False)
    connections = db.relationship('Connection', foreign_keys='Connection.from_person_id')
    
    def mutual_friends(self,target):
         result = []
         for selfcon in self.connections:
             for targetcon in target.connections:
                if selfcon.to_person_id == targetcon.to_person_id and selfcon.connection_type.value == "friend" and targetcon.connection_type.value == 'friend':
                    result.append(selfcon)
         return result
