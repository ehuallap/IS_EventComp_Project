import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.registered_person import Registered_person

class Registered_repository(DbConnection.Model):
    __tablename__ = 'registred_person'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    name = DbConnection.Column(DbConnection.String(50), nullable=False)
    email = DbConnection.Column(DbConnection.String(50), nullable=False)
    password = DbConnection.Column(DbConnection.String(50), nullable=False)
    registered_person = None
    def __init__(self, id, name, email, password):
        self.registered_person = Registered_person(id, name, email, password)
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def insert(self):
        DbConnection.session.add(self)
        DbConnection.session.commit()
        
    def update(self):
        DbConnection.session.commit()
    
    def delete(self):
        DbConnection.session.delete(self)
        DbConnection.session.commit()
    
    def get(self, id):
        return Registered_repository.query.get(id)
    
    def getAll(self):
        return Registered_repository.query.all()
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    
    def __repr__(self):
        return 'Registered: id: {}, name: {}, email: {}, password: {}'.format(self.id, self.name, self.email, self.password)