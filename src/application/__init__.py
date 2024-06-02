from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery 
from flask_mail import Mail
from application.config import ProductionConfig, DevelopmentConfig

import bcrypt
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
celery = Celery(app.name, broker=app.config.get('CELERY_BROKER_URL'))
celery.conf.update(app.config)
mail = Mail(app)
JWT_SECRETKEY = bcrypt.hashpw(app.config.get('SECRET_KEY'), bcrypt.gensalt())
 #############BLUEPRINTS REGISTER#############       
from .users import user_api 
app.register_blueprint(user_api.bp)

from .buddy_task import task_api 
app.register_blueprint(task_api.bp)  


