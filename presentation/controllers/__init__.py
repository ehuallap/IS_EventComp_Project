from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response

import sys
from pathlib import Path

from infrastructure.repository.db_connection import setup_db

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

def create_app():
    app = Flask(__name__)
    setup_db(app)
    return app