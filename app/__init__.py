from flask import Flask

def create_app():
    app = Flask(__name__)

    # Config
    app.config.from_object("app.config.Config")

    # Register blueprints
    from app.routes.onboarding import onboarding_bp
    app.register_blueprint(onboarding_bp)

    return app