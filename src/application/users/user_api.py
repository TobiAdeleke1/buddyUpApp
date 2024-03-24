from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.route('/')
# def index():
   
#     return render_template('auth/login.html')

@bp.route('/register')
def index():
    #  return render_template('auth/sign-in.html')
    return render_template('auth/login.html')