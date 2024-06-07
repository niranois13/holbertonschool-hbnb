from flask import Blueprint, jsonify, request
from models.users import User
from persistence.datamanager import DataManager
import json
user_api = Blueprint("user_api", __name__)

@user_api.route("/users", methods=["POST", 'GET'])
def add_user():
    if request.method == "POST":
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
            DataManager().save(new_user.to_dict(),1)
            return jsonify("User added", new_user.to_dict()), 201
    else:
        with open("User.json", 'r', encoding='utf-8') as f:
            users = json.load(f)
        return jsonify(users), 200
    
@user_api.route("/users/<string:id>", methods=['GET', 'DELETE','PUT'])
def get_user(id):
    if request.method == 'GET':
        users = DataManager().get("User",id,1)
        if not users:
            return jsonify("User not found"), 404
        return jsonify(users), 200
    if request.method == 'DELETE':
        users = DataManager().delete("User",id,1)
        if not users:
            return jsonify("User not found"), 404
        return jsonify("User deleted"), 200
    if request.method == 'PUT':
        user_data = request.get_json()
        user = DataManager().get("User",id,1)
        if not user:
            return jsonify("User not found"), 404
        user["email"] = user_data["email"]
        user["first_name"] = user_data["first_name"]
        user["last_name"] = user_data["last_name"]
        DataManager().update(user, id, 1)
        return jsonify("User updated", user), 200
