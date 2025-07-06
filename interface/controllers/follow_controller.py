# app/interface/controllers/follow_controller.py
from flask import Blueprint, request, jsonify
from use_cases.check_mutual_follow import check_mutual_follow

bp = Blueprint("follow_controller", __name__)

@bp.route('/check-follow', methods=['POST'])
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
    return jsonify(response), code
