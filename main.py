from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

from routes.addvm import addvm_bp
from routes.login import login_bp

# A simple / protected endpoint that requires a valid JWT
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Get the identity of the user from the JWT
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

app.register_blueprint(addvm_bp)
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run()
