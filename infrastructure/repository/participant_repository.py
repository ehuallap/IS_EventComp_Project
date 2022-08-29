import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.participant import Participant

class Participant_repository(DbConnection.Model, Participant):
    __tablename__ = 'participant'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    universidad = DbConnection.Column(DbConnection.String(50), nullable=False)
    ciclo = DbConnection.Column(DbConnection.Integer, nullable=False)

    def __init__(self):
        Participant.__init__(self)

    def __init__(self, id, name, email, password, universidad, ciclo):
        Participant.__init__(self, id, name, email, password, universidad, ciclo)

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
            return DbConnection.session.query(Participant_repository).filter(Participant_repository.id == id).first()
        except Exception as e:
            print(e)
            return None

    def getAll(self):
        try:
            return DbConnection.session.query(Participant_repository).all()
        except Exception as e:
            print(e)
            return None
