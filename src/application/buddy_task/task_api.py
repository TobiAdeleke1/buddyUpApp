from flask import (
	Blueprint, flash, redirect, render_template,
    request, url_for, send_from_directory,
    session
)
from application import db
from .models import Task,BuddyContact
from .controller import TaskController

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/')
def index():
    # alltask = db.session.execute(db.select(Task)).all()
    # or 
    alltasks = Task.query.all()

    return render_template('task/tasks.html', tasks=alltasks)

@bp.route('/my-task/<int:user_id>')
def user_task(user_id):
    """
    Filter the task table by the user id collected from the 
    """
    status, taskresponse = TaskController().findAllTask(user_id)
    if status:
        return render_template('task/tasks.html', tasks=taskresponse)
    
    return render_template('task/add_task.html')

@bp.route('/task/<int:task_id>', methods=('GET',))
def get_task(task_id):
    user_id = session.get('user_id')
    status, task = TaskController().findTask(task_id, user_id)
    if status:
        return render_template('task/tasks.html', tasks=task)
    
    return redirect(url_for('task.user_task', user_id=user_id))


@bp.route('/create', methods=('GET', 'POST'))
# @login_required
def create_task():
    """
     TODO : Create the method, check permissions, do validation and then commit task
    """
    if request.method == "POST":
        taskresponse = TaskController().addNew()
        if taskresponse == True:
            user_id = session.get('user_id')
            return redirect(url_for('task.user_task', user_id=user_id))
        else:
            flash(taskresponse)
           
    return render_template('task/add_task.html')

@bp.route('/edit/<int:task_id>', methods=('GET', 'POST'))
def update_task(task_id):
    """
    
    """
    user_id = session.get(user_id)
    status, response = TaskController().update(task_id)
    flash(response)
    # newtask = 
    redirect(url_for('task.user_task', user_id=user_id))

@bp.route('/delete/<int:task_id>',  methods=('POST',))
def delete_task(task_id):
    # newtask = 
    user_id = session.get(user_id)
    status, response = TaskController().delete(task_id)
    flash(response)
    redirect(url_for('task.user_task', user_id=user_id)) 