from flask.cli import FlaskGroup
from application import app, db
from users.models import User

# app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
# def create_db():
#     db.drop_app(app=app)
#     db.create_all(app=app)
#     db.session.commit()
@cli.command("seed_db")
def seed_db():
    db.session.add(User("rewTobi", "rewTobi@gmail.com", "preq9004"))
    db.session.commit()

if __name__ == "__main__":
    cli()