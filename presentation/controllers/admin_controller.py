import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from flask import jsonify
from flask import request
from flask import abort
from flask import Blueprint
from flask_cors import cross_origin

from infrastructure.repository.admin_repository import Administrator_repository

admin_blueprint = Blueprint('admin_blueprint', __name__)
admin = Administrator_repository

@admin_blueprint.route('/admin', methods=['POST'])
@cross_origin()
def create_admin():
    if not request.json:
        abort(400)
    admin = Administrator_repository(request.json['id'], request.json['name'], request.json['email'], request.json['password'])
    admin = admin.insert()
    return jsonify(admin)

@admin_blueprint.route('/admin', methods=['GET'])
@cross_origin()
def get_admins():
    admins = admin.get_all()
    return jsonify(admins)

@admin_blueprint.route('/admin/<int:id>', methods=['GET'])
@cross_origin()
def get_admin(id):
    admin = admin.get(id)
    return jsonify(admin)

@admin_blueprint.route('/admin/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_admin(id):
    admin = admin.delete(id)
    return jsonify(admin)
