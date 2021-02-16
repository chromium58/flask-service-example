import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    WEATHER_SITE = 'https://wttr.in'
    FLASK_LOG_LEVEL = 'DEBUG'
    ROUTE_PATH = '/api'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    ELK_HOSTNAME = ''


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING_MODE = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING_MODE = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
