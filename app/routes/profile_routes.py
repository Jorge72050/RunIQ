# app/routes/profile_routes.py

from flask import Blueprint, request, jsonify
from jsonschema import ValidationError
from app.validators.profile_validator import validate_profile

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/validate", methods=["POST"])
def validate_profile_route():
    profile = request.get_json()

    try:
        validate_profile(profile)
    except ValidationError as e:
        return jsonify({
            "valid": False,
            "error": e.message
        }), 400

    return jsonify({"valid": True})
