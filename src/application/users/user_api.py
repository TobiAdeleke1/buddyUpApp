from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
   
    return render_template('auth/login.html')

@bp.route('/register')
def register():
    #  return render_template('auth/sign-in.html')
    return render_template('auth/sign-up.html')