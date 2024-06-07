from flask import Flask
"""Function that creates the app, it will hold its logical interactions"""
app = Flask(__name__)

#Je voulais un accueil, on pourra l'enlever dans de futures implémentations
#ou le déplacer avec les futur routes. A méditer.
@app.route("/")
def home():
    """Function that handles index"""
    return "Welcome to HBnB !"

#Ces lignes servent à importer et "enregistrer" les routes dans l'appli

import api.user_api


if __name__ == "__main__":
    app.run()
