from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
   
    return render_template('auth/login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('floatingPassword')
        error = None
        
        # TODO complete to add to database
        if not username:
            error = 'Username is required.'
        elif not password: 
            error = 'Password is required.'

    return render_template('auth/sign-up.html')