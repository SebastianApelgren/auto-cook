from flask import Flask, request, jsonify
from dendrite_sdk import Dendrite
from dendrite_key import DENDRITE_API_KEY

from predefined_recipes import chicken_recipes, chorizo_recipes
from predefined_sales import products_updated as sales_items
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
        time.sleep(4)
        query = data.get("query", "").lower()  # Get the query from the request and convert it to lowercase
        if "chicken" in query:
            return jsonify(chicken_recipes), 200
        if "chorizo" in query:
            return jsonify(chorizo_recipes), 200
        # Search for the recipe in the predefined recipes
        return jsonify(chorizo_recipes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/checkout', methods=['POST'])
def openai_query():
    time.sleep(10)
    try:
        return jsonify({"message": "Hello checkout!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_sale_items', methods=['POST'])
def get_sale_items():
    try:

        return jsonify(sales_items), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
""" @app.route('/get_items_price', methods=['POST'])
def get_items_price():
    try:
        data = request.get_json()
        items = data.get("items", [])

        return jsonify({"total_price": total_price}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500 """

if __name__ == '__main__':
    app.run(debug=True)