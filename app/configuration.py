
class Config(object):
    """
    Configuration base, for all environments.
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    BOOTSTRAP_FONTAWESOME = True
    SECRET_KEY = "TOPSECRET44"
    CSRF_ENABLED = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
