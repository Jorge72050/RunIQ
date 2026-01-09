import pytest
from jsonschema import ValidationError
from app.validators.profile_validator import validate_profile
from app.logic.training_plan import build_plan
from tests.userprofile_sample import valid_profile, invalid_profile


def test_valid_profile_passes_validation():
    """Valid profile should pass schema validation"""
    try:
        validate_profile(valid_profile)
    except ValidationError:
        pytest.fail("Valid profile failed validation")


def test_invalid_profile_fails_validation():
    """Invalid profile should raise ValidationError"""
    with pytest.raises(ValidationError):
        validate_profile(invalid_profile)


def test_build_plan_returns_dict():
    """Plan generator should return a dictionary"""
    plan = build_plan(valid_profile)
    assert isinstance(plan, dict)
    assert len(plan) > 0  # Make sure the plan is not empty
