import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base Object For different Enivronment Configuratin """
    ROOT_PATH = basedir
    SECRET_KEY = os.environ.get("SECRET_KEY").encode('UTF-8')
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DATABASE_URL")
                               or
                               'sqlite:////'+os.path.join(basedir, 'app.db')
                               )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    STATIC_FOLDER = f"{basedir}/templates"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"

    # EMAIL configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    # Celery with Redis Broker
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'


class ProductionConfig(Config):
    """"""
    DEBUG = False
    TESTING = False
    LOGIN_DISABLED = False


class DevelopmentConfig(Config):
    """Development configuration"""
    # DEBUG = True
    TESTNG = True
    LOGIN_DISABLED = False
    FLASK_DEBUG = 1


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
