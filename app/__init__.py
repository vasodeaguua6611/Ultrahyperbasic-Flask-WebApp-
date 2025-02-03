from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
import logging

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'

    # Register blueprints
    try:
        from app.main import bp as main_bp
    except ImportError:
        main_bp = None

    try:
        from app.auth import bp as auth_bp
    except ImportError:
        auth_bp = None

    try:
        from app.api import bp as api_bp
    except ImportError:
        api_bp = None

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')

    # Configure logging
    if not app.debug:
        logging.basicConfig(filename='app.log', level=logging.INFO)

    return app