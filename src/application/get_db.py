import sqlite3
from flask import current_app, g

def get_db_connection():
    """ Create database connection if none exist,
        Else returns the connection that already exist in g
    """
    if 'db' not in g:
        g.db =  g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db():
    """ Close any database connection that exists in g """
    db = g.pop('db', None)

    if db is not None:
        db.close()