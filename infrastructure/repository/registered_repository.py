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

    def __init__(self, id=0, name="", email="", password=""):
        Registered_person.__init__(self, id, name, email, password)

    def insert(self):
        try:
            DbConnection.session.add(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
        
    def update(self):
        try:
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
    
    def delete(self):
        try:
            DbConnection.session.delete(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
    
    def get(self, id):
        try:
            return DbConnection.session.query(Registered_repository).filter(Registered_repository.id == id).first()
        except Exception as e:
            print(e)
            return None
    
    def getAll(self):
        try:
            return DbConnection.session.query(Registered_repository).all()
        except Exception as e:
            print(e)
            return None
