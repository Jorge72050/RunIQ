# app/__init__.py
from flask import Flask
from app.routes.plan_routes import plan_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(plan_bp)
    return app
