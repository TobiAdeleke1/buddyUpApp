from flask import (
	Blueprint, flash, redirect, render_template,
    request, url_for, session
)

from application.users.user_api import login_required
from .controller import TaskController,BuddyContactController

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/')
@login_required
def index():
    user_id = session.get('user_id')
    status, taskresponse = TaskController().findAllTask(user_id)
    if status:
        return render_template('task/tasks.html', tasks=taskresponse)
    return render_template('task/add_task.html')


@bp.route('/<int:task_id>', methods=('GET',))
def get_task(task_id):
    user_id = session.get('user_id')
    status, task = TaskController().findTask(task_id, user_id)
    if status:
        return render_template('task/task_detail.html', task=task)
    return redirect(url_for('task.index'))


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_task():   
    if request.method == "POST":
        taskresponse = TaskController().addNew()
        if taskresponse == True:
            return redirect(url_for('task.index'))
        else:
            flash(taskresponse)        
    return render_template('task/add_task.html')

@bp.route('/<int:task_id>/edit', methods=('GET', 'POST'))
@login_required
def update_task(task_id):
    taskstatus, taskresponse = TaskController().findTask(task_id, session.get('user_id'))
    if not taskstatus:
        flash(taskresponse)
        return redirect(url_for('task.index')) 
    
    if request.method == "POST":
        _, response = TaskController().update(task_id)
        flash(response)
        return redirect(url_for('task.get_task', task_id=task_id))

 
    _, buddyemail = BuddyContactController().find(taskresponse.id)


    # print(taskresponse.buddyemail)
    return render_template('task/update.html', task_buddy={'task': taskresponse, 'buddy': buddyemail.first_buddy_email })


@bp.route('/<int:task_id>/delete',  methods=('POST',))
@login_required
def delete_task(task_id):
    _, response = TaskController().delete(task_id)
    TaskController().delete(task_id)
    flash(response)
    return redirect(url_for('task.index')) 