# routes/recommend_route.py
from flask import Blueprint, jsonify, request
import pandas as pd
from config.db_config import movies_collection
from utils.recommender import get_recommendations

recommend_bp = Blueprint('recommend_bp', __name__)

@recommend_bp.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie')
    if not movie_name:
        return jsonify({"error": "Please provide a movie name like ?movie=Toy Story"}), 400

    movies = pd.DataFrame(list(movies_collection.find({}, {"_id": 0})))
    recommendations = get_recommendations(movie_name, movies)

    if not recommendations:
        return jsonify({"message": "No similar movies found."}), 404

    return jsonify({
        "movie": movie_name,
        "recommended_movies": recommendations
    })
