# app/routes/plan_routes.py

from flask import Blueprint, request, jsonify
from jsonschema import ValidationError
from app.validators.profile_validator import validate_profile
from app.logic.training_plan import build_plan

plan_bp = Blueprint("plan", __name__)

@plan_bp.route("/generate-plan", methods=["POST"])
def generate_plan():
    profile = request.get_json()

    try:
        validate_profile(profile)
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Invalid profile data",
            "details": e.message
        }), 400

    plan = build_plan(profile)

    return jsonify({
        "status": "success",
        "plan": plan
    })
