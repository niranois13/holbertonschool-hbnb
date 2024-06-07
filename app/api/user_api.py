from flask import Blueprint, jsonify, request
from models.users import User
from models.base_model import BaseModel
from persistence.datamanager import DataManager
from validate_email_address import validate_email

user_api = Blueprint("user_api", __name__)


@user_api.route("/users", methods=["POST"])
def add_user():
    """Function that adss a new user"""
    user_data = request.get_json()
    if not user_data:
        return jsonify({"Error": "Invalid input"}), 400

    new_user = User(user_data["email"],
                        user_data["first_name"], user_data["last_name"])

    email = user_data["email"]
    is_valid_format = validate_email(email, check_format=True,
                    check_blacklist=False, check_dns=False, check_smtp=False)
    if not is_valid_format:
        return jsonify({"Error": "Invalid email adress"}), 400

    with open("User.json", 'r') as f:
        if email in f.read():
            return jsonify({"Error": "mail already exist"}), 409
    if not new_user:
        return jsonify({"Error": "setting up new user"})
    else:
        DataManager().save(new_user.to_dict())
        return jsonify("User added", new_user.to_dict()), 201

@user_api.route("/users", methods=["GET"])
def list_users():
    """Function that returns a list of all the users"""
    user_data = User.get(user_id)
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(user_data)
