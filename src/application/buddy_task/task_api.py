from flask import (
	Blueprint, flash, redirect, render_template, request, url_for, send_from_directory
)
from application import db
from .models import Task,BuddyContact


bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/')
def index():
    # alltask = db.session.execute(db.select(Task)).all()
    # alltask = db.session.execute(db.select(Task)).all()
    # or 
    alltasks = Task.query.all()

    return render_template('task/tasks.html', tasks=alltasks)

@bp.route('/my-task/<int:user_id>')
def user_task():
    """
    Filter the task table by the user id collected from the 
    """
    pass

@bp.route('/create', methods=('GET', 'POST'))
# @login_required
def create_task():
    """
     TODO: Create the method, check permissions, do validation and then commit task
    """
    
    if request.method == "POST":
        task_title = request.form.get('title')
        task_description  = request.form.get('description')
        task_duedate = request.form.get('duedate')
        buddy_email = request.form.get('buddyemail')

        error = None

        if not task_title:
            error = 'A Title Is Required'

        if not task_duedate:
            error = "A Due Date is required"
        
        if not buddy_email:
            error = "Need To something a buddy email"

        if error is not None:
            flash(error)
        else:
            # TODO ADD FORM submitions
            newtask = Task()
            newbuddy = BuddyContact()
            # db.session.add(newtask)
            # db.session.commit
             
    return render_template('task/add_task.html')

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