from flask import Flask, request, jsonify

from predefined_recipes import all_recipes
from flask_cors import CORS
import time
import os

app = Flask(__name__)

CORS(app, origins=["http://localhost:8080"])

#Step 1
@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        query = data.get("query", "").lower()  # Get the query from the request and convert it to lowercase
        # Search for the recipe in the predefined recipes
        return jsonify(all_recipes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/checkout', methods=['POST'])
def openai_query():
    try:
        return jsonify({"message": "Hello checkout!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)