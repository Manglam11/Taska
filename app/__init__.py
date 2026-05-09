from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from config import Config

# Initialize extensions outside factory — no app bound yet
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
socketio = SocketIO(cors_allowed_origins="*")


def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    # Bind extensions to this app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")

    # Tell Flask-Login where to redirect unauthenticated users
    login_manager.login_view = 'auth.login'

    # Register blueprints
    from app.auth import auth_bp
    from app.tasks import tasks_bp
    from app.analytics import analytics_bp
    from app.sockets.events import register_socket_events

    register_socket_events(socketio)

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(analytics_bp)

    return app