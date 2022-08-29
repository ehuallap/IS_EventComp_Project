import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.registered_person import Registered_person

class Registered_repository(DbConnection.Model, Registered_person):
    __tablename__ = 'registred_person'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    name = DbConnection.Column(DbConnection.String(50), nullable=False)
    email = DbConnection.Column(DbConnection.String(50), nullable=False)
    password = DbConnection.Column(DbConnection.String(50), nullable=False)
    
    def __init__(self, id, name, email, password):
        Registered_person.__init__(self, id, name, email, password)

    def insert(self):
        DbConnection.session.add(self)
        DbConnection.session.commit()
        
    def update(self):
        DbConnection.session.commit()
    
    def delete(self):
        DbConnection.session.delete(self)
        DbConnection.session.commit()
    
    def get(self, id):
        return DbConnection.session.query(Registered_repository).filter(Registered_repository.id == id).first()
    
    def getAll(self):
        return DbConnection.session.query(Registered_repository).all()
