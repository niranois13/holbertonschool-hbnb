from flask import jsonify, request
from models.users import User
from app import app

@app.route("/user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = User(user_data)
    if not new_user:
        return jsonify("Error setting up new user")
    else:
        return jsonify("User added", new_user), 201


