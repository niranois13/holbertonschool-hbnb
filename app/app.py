from flask import Flask
from api.user_api import user_api

app = Flask(__name__)
app.register_blueprint(user_api)


if __name__ == "__main__":
    app.run(debug=True)
