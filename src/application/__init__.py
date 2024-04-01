from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from application.config import ProductionConfig, DevelopmentConfig

import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    config = os.environ.get('FLASK_ENV')
    

    if config=="production":
        app.config.from_object(ProductionConfig)
      
    elif config=="development":
        app.config.from_object(DevelopmentConfig)
        
  
    else:
        app.logger.info("Flask_ENV is Null !!!")
   
 
    @app.route("/")
    def hello():
        return render_template("index.html")
    
    return app

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app,db)

 #############BLUEPRINTS REGISTER#############       
from .users import user_api 
app.register_blueprint(user_api.bp)

from .buddy_task import task_api 
app.register_blueprint(task_api.bp)  
