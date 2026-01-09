# app/validators/profile_validator.py

from jsonschema import validate, ValidationError
from app.schemas.profile_schema import PROFILE_SCHEMA


def validate_profile(profile_json):
    validate(instance=profile_json, schema=PROFILE_SCHEMA)
    return True
