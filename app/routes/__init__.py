# app/__init__.py

from flask import Flask
from app.routes.profile_routes import profile_bp
from app.routes.plan_routes import plan_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(profile_bp, url_prefix="/api/profile")
    app.register_blueprint(plan_bp, url_prefix="/api/plan")
    return app
