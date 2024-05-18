import functools
from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from .controller import UserController
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST': 
        status, userresponse = UserController().find()
        if status:
            session.clear()
            session['user_id'] = userresponse.id 
            return redirect(url_for('task.index')) 
            
    
        flash(userresponse)
    return render_template('auth/login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        userresponse = UserController().addNew()
        if userresponse == True:
            return redirect(url_for('auth.login')) 
        else:
            flash(userresponse)
    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


   
@bp.before_app_request
def load_current_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        status, userresponse = UserController().findById(user_id)
        if status:
            g.user = userresponse


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view