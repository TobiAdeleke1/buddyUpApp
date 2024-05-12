from datetime import datetime, timedelta
import bcrypt
from flask import (
    request, make_response,redirect, url_for, session
)

from application import JWT_SECRETKEY
from application import db
from .models import User

class LoginController:
    """ 
    TODO
     Handles Login, creating access-token, setting cookies, and log-out
    """
    def login(self):   
        # status, userResponse = UserController().find()
        # if status:
        #     session.clear()
        #     session['user_id'] = userResponse.id 
        #     return userResponse 
        # return 
        pass

class UserController:
    def addNew(self):
       
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        error = None
        
    
        if not username:
            error = 'Username is required.'
        elif not password: 
            error = 'Password is required.'  
        elif not email: 
            error = 'Email is required.'
     
        if error is None:
            try:
                user = User(
                    username=username,
                    email=email,
                    password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
                )
                db.session.add(user)
                db.session.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered"
            else:       
                return True
        return error

    def find(self):
        email = request.form.get('email')
        password = request.form.get('password')

        error = None
     
        try: 
            user = db.session.query(User).filter(User.email == email).first()
       
        except: 
            error = 'User Not Found'
        
        
        if user is None:
            error = 'Incorrect Username'
        elif not bcrypt.checkpw(password.encode('utf-8'), user.password):
            error = 'Incorrect Password'
        
        if error is None:
            return (True, user)
        
        return (False, error)
    
    def findById(self, user_id=None):
        user, error = None, None
 
        if user_id :
            try: 
                user = db.session.query(User).filter(User.id == user_id).first()
            except: 
                error = 'User Not Found'  
 
        if error is None:
            return (True, user) 
        return (False, error)


class LoginErr:
    pass