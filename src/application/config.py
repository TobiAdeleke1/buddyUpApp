import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base Object For different Enivronment Configuratin """
    ROOT_PATH = basedir
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DATABASE_URL") 
                               or 
                               'sqlite:////'+os.path.join(basedir,'app.db')
                            )
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/application/templates"
    STATIC_FOLDER = f"{basedir}/templates"
    # print(os.listdir(STATIC_FOLDER))
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"   

class ProductionConfig(Config):
    """"""
    DEBUG = False
    TESTING = False
    LOGIN_DISABLED = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTNG = True
    LOGIN_DISABLED = False

class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True