from flask import Blueprint, jsonify, request
from models.users import User
from persistence.datamanager import DataManager
user_api = Blueprint("user_api", __name__)

@user_api.route("/user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    new_user = User(user_data["email"] , user_data["first_name"], user_data["last_name"])
    try:
        with open("User.json", 'r') as f:
            if user_data["email"] in f.read():
                return jsonify("user already exist"), 400
    except FileNotFoundError:
        pass
    if not new_user:
        return jsonify("Error setting up new user")
    else:
        DataManager().save(new_user.to_dict())
        return jsonify("User added", new_user.to_dict()), 201
