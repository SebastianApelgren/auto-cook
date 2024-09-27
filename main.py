from flask import Flask, request, jsonify
import os

app = Flask(__name__)

#Step 1
@app.route('/generate_recipe', methods=['POST'])
def generate_recipe(query):
    try:
        
        return jsonify({"message": "Hello recipe!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/checkout', methods=['POST'])
def openai_query(ingredients):
    try:
        return jsonify({"message": "Hello checkout!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)