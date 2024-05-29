import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a239bf6b2b6b2e2298d000da76c71499'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_database.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_database.db'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///prod_database.db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
