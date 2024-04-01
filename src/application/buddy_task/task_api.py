from flask import (
	Blueprint, flash, redirect, render_template, request, url_for, send_from_directory
)
from application import db
from .models import Task


bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/')
def index():
    # alltask = db.session.execute(db.select(Task)).all()
    alltask = db.session.execute(db.select(Task)).all()
    # or 
    get_alltask = Task.query.all()

    print(alltask)
    print("Alternative: ",get_alltask)
    return render_template('task/login.html')

@bp.route('/create')
def create_task():
    """
     TODO: Create the method, check permissions, do validation and then commit task
    """
    newtask = Task()
    db.session.add(newtask)
    db.session.coomit

@bp.route('/update')
def update_task():
    """
    
    """
    # newtask = 
    pass

@bp.route('/delete')
def delete_task():
    # newtask = 
    pass