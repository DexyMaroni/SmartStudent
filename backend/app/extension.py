from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.auth.models import User  # Local import to avoid circular dependency
    return User.query.get(int(user_id))
