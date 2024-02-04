from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from Weekend_Projects.Contract_inspired_ideas.buddyUP.buddyUpApp.src.application.config import DevelopmentConfig


def create_app():
    """
    Return an instance of the flask applicaion
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
   
    # db = SQLAlchemy(app)
    # migrate = migrate(app, db)

    # from . import db # this uses c
    # db.init_app(app)
    # migrate = migrate(app, db) #https://dev.to/yactouat/flask-postgres-sqlalchemy-migrations-dockerized-intro-2f8p

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app 

