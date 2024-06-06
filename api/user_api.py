from flask import Flask, jsonify, request
from persistence.IPersistenceManager import DataManager
from models import users

app = Flask(__name__)


user = {}

@app.route("/user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = users(user_data)
    if not new_user:
        return jsonify("Error setting up new user")
    else:
        return jsonify("User added") and DataManager.save(new_user)

if __name__ == "__main__":
    app.run()
