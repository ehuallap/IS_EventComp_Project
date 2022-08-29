from flask import Flask

import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[1]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import setup_db
from controllers.admin_controller import admin_blueprint
from controllers.event_controller import event_blueprint
from controllers.participant_controller import participant_blueprint
from controllers.registered_controller import registered_blueprint
from controllers.speaker_controller import speaker_blueprint

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(participant_blueprint)
    app.register_blueprint(registered_blueprint)
    app.register_blueprint(speaker_blueprint)
    setup_db(app)
    return app
