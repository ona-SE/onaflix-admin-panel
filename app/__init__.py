from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gitpod:gitpod@localhost:5432/onaflix_admin'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config:
        app.config.update(config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.routes.dashboard import dashboard_bp
    from app.routes.movies import movies_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(movies_bp, url_prefix='/movies')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'admin-panel'}

    return app
