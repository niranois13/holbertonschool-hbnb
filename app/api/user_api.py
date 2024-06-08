from flask import Blueprint, jsonify, request
from models.users import User
from persistence.datamanager import DataManager
from validate_email_address import validate_email
import json
user_api = Blueprint("user_api", __name__)

@user_api.route("/users", methods=["POST", 'GET'])
def add_user():
    """
    Function used to create a new user, send it to the database manager
    and read a list of existing users.
    """
    if request.method == "POST":
        #Bloc that handles user inputs
        user_data = request.get_json()
        if not user_data:
            return jsonify({"Error": "Problem during user creation."}), 400

        #Bloc that stores the data for the new user and then checks validity
        email = user_data.get("email")
        first_name = user_data.get("first_name")
        last_name = user_data.get("last_name")
        if not all([email, first_name, last_name]):
            return jsonify({"Error": "Missing required field."}), 400

        #Bloc that handles email validity and user uniqueness
        is_email_valid = validate_email(email)
        if not is_email_valid:
            return jsonify({"Error": "Email not valid"}), 400
        try:
            with open("User.json", 'r') as f:
                if user_data["email"] in f.read():
                    return jsonify({"Error": "User already exists"}), 409
        except FileNotFoundError:
            pass

        #Bloc that initializes the new user with the stored data,
        #checks validity and then send it to the database
        new_user = User(email, first_name, last_name)
        if not new_user:
            return jsonify({"Error": "setting up new user"}), 500
        else:
            DataManager().save(new_user.to_dict(),1)
            return jsonify({"Success": "User added"}, new_user.to_dict()), 201

    else:
        #Bloc that handles the GET method by reading and returning the data
        #stored in the database
        try:
            with open("User.json", 'r', encoding='utf-8') as f:
                users = json.load(f)
                return jsonify(users), 200
        except FileNotFoundError:
            return jsonify({"Error": "No user found"}), 404

@user_api.route("/users/<string:id>", methods=['GET', 'DELETE','PUT'])
def get_user(id):
    """
    Function used to read, update or delete a specific user's info
    from the database
    """
    if request.method == 'GET':
        #Bloc that handles the GET mehod of the data of a specifi user
        #by returning this data, pulles from the database.
        users = DataManager().get("User",id,1)
        if not users:
            return jsonify({"Error": "User not found"}), 404
        return jsonify(users), 200

    if request.method == 'DELETE':
        #Bloc that handles the DELETE method by pulling data specific to a user
        #and calls the DataManager function to do the removal
        users = DataManager().get("User",id,1)
        if not users:
            return jsonify({"Error": "User not found"}), 404
        users = DataManager().delete("User",id,1)
        if not users:
            return jsonify({"Success": "User deleted"}), 200
        


    if request.method == 'PUT':
        #Bloc that handles the PUT method by pulling data of a specific user
        #and calling th DataManager to update the database
        user_data = request.get_json()
        user = DataManager().get("User",id,1)
        if not user:
            return jsonify({"Error": "User not found"}), 404
        user["email"] = user_data["email"]
        user["first_name"] = user_data["first_name"]
        user["last_name"] = user_data["last_name"]
        DataManager().update(user, id, 1)
        return jsonify({"Success": "User updated"}, user), 200
