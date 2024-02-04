from flask.cli import FlaskGroup
from application import create_app

app = create_app()
cli = FlaskGroup(app)


# @cli.command("create_db")
# def create_db():
#     db.drop_app(app=app)
#     db.create_all(app=app)
#     db.session.commit()



if __name__ == "__main__":
    cli()