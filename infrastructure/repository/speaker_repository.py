import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.speaker import Speaker

class Speaker_repository(DbConnection.Model):
    __tablename__ = 'speaker'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    ac_level = DbConnection.Column(DbConnection.String(50), nullable=False)
    description = DbConnection.Column(DbConnection.String(100), nullable=False)
    especiality = DbConnection.Column(DbConnection.String(50), nullable=False)
    phone = DbConnection.Column(DbConnection.String(50), nullable=False)

    def __init__(self):
        Speaker.__init__(self)
    
    def __init__(self, id, name, email, password, ac_level, description, especiality, phone):
        Speaker.__init__(self, id, name, email, password, ac_level, description, especiality, phone)
    
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
            return DbConnection.session.query(Speaker_repository).filter(Speaker_repository.id == id).first()
        except Exception as e:
            print(e)
            return None

    def getAll(self):
        try:
            return DbConnection.session.query(Speaker_repository).all()
        except Exception as e:
            print(e)
            return None
