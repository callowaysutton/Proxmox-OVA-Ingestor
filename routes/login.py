from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

login_bp = Blueprint('login', __name__)

# Ingests an OVA image from a public endpoint
# Min./Required params:
# {
#   "image_url": "http://example.com/vm.ova",
#   "vm_id": 100,
#   "storage_location": "local-lvm"
# }
@login_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    try:
        image_url = request.json.get('image_url', None)
        vm_id = request.json.get('vm_id', None)
        storage_location = request.json.get('storage_location', None)
    except:
        return jsonify({"msg": "Malformed JSON"}), 400

    if not image_url:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not vm_id:
        return jsonify({"msg": "Missing vm_id parameter"}), 400
    if not storage_location:
        return jsonify({"msg": "Missing storage_location parameter"}), 400

    return jsonify({"msg": "Ok!"}), 200