from flask import Flask, request, jsonify
from services.functions import check_mutual_follow
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/check-follow', methods=['POST'])
def check_follow():
    data = request.get_json()

    if not data or 'id_user_1' not in data or 'id_user_2' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        id_user_1 = int(data['id_user_1'])
        id_user_2 = int(data['id_user_2'])
    except ValueError:
        return jsonify({"error": "Invalid user IDs"}), 400

    response, code = check_mutual_follow(id_user_1, id_user_2)
    return jsonify(response), code #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
