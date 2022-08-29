from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response

import sys
from pathlib import Path

from infrastructure.repository.db_connection import setup_db
from admin_controller import admin_blueprint
from event_controller import event_blueprint
from participant_controller import participant_blueprint
from registered_controller import registered_blueprint
from speaker_controller import speaker_blueprint

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
