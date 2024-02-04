from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# from flask_migrate import Migrate
# from ..config import ProductionConfig, DevelopmentConfig

from application.config import ProductionConfig, DevelopmentConfig

import os

# db = SQLAlchemy()
# sess = Session() 


def create_app():
    ## https://github.com/il-gen/basic_Docker-Flask/blob/main/services/web/project/__init__.py
    app = Flask(__name__, instance_relative_config=True)
    config = os.environ.get('FLASK_ENV')

    if config=="production":
        app.config.from_object(ProductionConfig)
      
    elif config=="development":
        app.config.from_object(DevelopmentConfig)
        
  
    else:
        app.logger.info("Flask_ENV is Null !!!")

    #############SQLAcademy INIT#############
    ##First init db and create Tables if you want
    # db.init_app(app)

    ############# NOTE: SESSION INIT#############
    
    # sess.init_app(app)

     #############BLUEPRINTS REGISTER#############     
    
    # blueprint for non-auth routes of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

        
    # # blueprint for auth routes in our app
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)
    @app.route("/")
    def hello_world():
        return "Hello World!"
    
    return app