import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.event import Event

class Event_repository(DbConnection.Model, Event):
    __tablename__ = 'event'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    title = DbConnection.Column(DbConnection.String(50), nullable=False)
    theme = DbConnection.Column(DbConnection.String(100), nullable=False)
    description = DbConnection.Column(DbConnection.String(100), nullable=False)
    date_time = DbConnection.Column(DbConnection.DateTime, nullable=False)
    platform = DbConnection.Column(DbConnection.String(20), nullable=False)
    access_link = DbConnection.Column(DbConnection.String(50), nullable=False)
    administrator_id = DbConnection.Column(DbConnection.Integer, nullable=False)

    def __init__(self, id=0, title="", theme="", description="", date_time="", platform="", access_link="", administrator_id=0):
        Event.__init__(self, id, title, theme, description, date_time, platform, access_link, administrator_id)

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
            return DbConnection.session.query(Event_repository).filter(Event_repository.id == id).first()
        except Exception as e:
            print(e)
            return None

    def getAll(self):
        try:
            return DbConnection.session.query(Event_repository).all()
        except Exception as e:
            print(e)
            return None
