from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

addvm_bp = Blueprint('addvm', __name__)
# jwt = JWTManager(add_vm)

# A simple / protected endpoint that requires a valid JWT
@addvm_bp.route('/addvm', methods=['POST'])
@jwt_required()
def protected():
    # Get the identity of the user from the JWT
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
    except:
        return jsonify({"msg": "Malformed JSON"}), 400

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    # Perform your authentication here, for example using a database
    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Create and return the JWT
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200