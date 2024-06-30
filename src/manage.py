from flask.cli import FlaskGroup
from application import app, db
from application.users.models import User
from application.buddy_task.models import Task, BuddyContact
from datetime import datetime, timedelta


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():

    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():

    db.session.add(User("rewTobi", "rewTobi@gmail.com", "preq9004"))
    db.session.add(User("Jenny", "Jenny@outlook.com", "frrry90056"))
    # db.session.add(Task(datetime.today() ,"Go Dancing", 1,"Open", datetime.today()+timedelta(days=5) ))
    db.session.add(Task("Exercise", "Go Dancing", 1, datetime.today()+timedelta(days=5)))
    db.session.add(Task("Exercise", "Go Skiing", 1, datetime.today()+timedelta(days=10)))
    db.session.add(Task("Academy", "Reading", 2, datetime.today()+timedelta(days=20)))

    db.session.commit()


if __name__ == "__main__":
    cli()
