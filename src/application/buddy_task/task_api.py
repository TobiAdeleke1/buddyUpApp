from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)
# from application import db
from .models import Task
from application.get_db import get_db_connection


bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/all')
def index():
    db = get_db_connection()
    alltask = db.session.execute(db.select(Task).all())
    print(alltask)
    return render_template('task/login.html')