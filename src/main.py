from flask import Flask

def create_app(test_config=None):
    """
    Return an instance of the flask applicaion
    """
    app = Flask(__name__)
  

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app 

