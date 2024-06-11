from flask import Blueprint, jsonify, request
from models.review import Review
from persistence.datamanager import DataManager
import json
review_api = Blueprint("review_api", __name__)
datamanager = DataManager(flag=4)


@review_api.route("/places/<string:id>/reviews", methods=["POST", "GET"])
def handle_place_review(id):
    """
    Function used to create and retriew reviews of a place
    """
    if request.method == "POST":
        review_data = request.get_json()
        if not review_data:
            return jsonify({"Error": "Problem during review creation"}), 400

        rating = review_data.get("rating")
        if not isinstance(rating, int):
            return jsonify({"Error": "rating must be an integer."}), 400
        if not 1 <= rating <= 5:
            return jsonify({"Error":
                            "rating must be included between 1 and 5."}), 400

        comment = review_data.get("comment")
        if not isinstance(comment, str):
            return jsonify({"Error": "comment must be a string."}), 400

        try:
            with open("User.json", 'r', encoding='UTF-8') as f:
                users = json.load(f)
            user_id = review_data.get("user_id")
            for user in users:
                if user.get("uniq_id") == user_id :
                    break
                else:
                    return jsonify({"Error": "User not found"}), 404
                    
        except TypeError as e:
            return jsonify({"Error": str(e)}), 404
        place_id = id

        if not all([user_id, place_id, rating, comment]):
            return jsonify({"Error": "Missing recquired field"}), 409

        new_review = Review(user_id, place_id, rating, comment)
        if not new_review:
            return jsonify({"Error": "adding new review"}), 500
        else:
            datamanager.save(new_review.to_dict())
            return jsonify({"Success": "Review added"}), 201

    else:
        try:
            with open("Review.json", 'r', encoding='UTF-8') as f:
                reviews = json.load(f)
                return jsonify(reviews), 200
        except FileNotFoundError:
            return jsonify({"Error": "Review not found"}), 404
