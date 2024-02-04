from flask import current_app, g

import psycopg2
import click


def init_db():
    """Gets the database connection, create the tables"""
    db = get_db()
    # https://flask.palletsprojects.com/en/3.0.x/appcontext/
    with current_app.app_context():
        # https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#create-the-tables
        db.create_all()

@click.command('init-db')
def init_db_command()-> None:
    """Clear the existing data and calls init_db to create new tables"""

    init_db()
    click.echo('Initialized the database ..')

def get_db():
    """
     Create database connection if none exist,
     else returns the connection that already exist in g
     NOTE: Helpful for multiple connection issus

    """

    if 'db' not in g:
        # reference: https://www.psycopg.org/docs/install.html
        g.db = psycopg2.connect( current_app.config['DATABASE'])

    return g.db



def close_db(e=None):
    """
     Close any database connection that exist in g
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()

        
def init_app(app) -> None:
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)