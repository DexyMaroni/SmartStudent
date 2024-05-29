from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartStudent.db'
    app.config['SECRET_KEY'] = 'a239bf6b2b6b2e2298d000da76c71499'

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.auth.models import User
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.notes.routes import notes_bp
    from app.events.routes import events_bp
    from app.auth.routes import auth_bp

    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    with app.app_context():
        db.create_all()
    return app
