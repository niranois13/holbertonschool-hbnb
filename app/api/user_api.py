from flask import Blueprint, jsonify, request

user_api = Blueprint("user_api", __name__)

@user_api.route("/user")
def add_user():
    return 'Hello World'
