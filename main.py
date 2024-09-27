from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/recipe_generator', methods=['POST'])
def recipe_generator(jsonquery):
    try:
        
        return jsonify({"message": "Hello recipe!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_ingredients_prices', methods=['POST'])
def get_ingredients_prices():
    try:
        return jsonify({"message": "Hello Ingredients!"}), 200

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