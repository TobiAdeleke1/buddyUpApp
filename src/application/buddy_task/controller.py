from datetime import datetime
from flask import (
    request, session
)
from application import db 
from .models import Task, BuddyContact

class TaskController:
    def addNew(self):
        task_title = request.form.get('tasktitle')
        task_description  = request.form.get('description')
        task_duedate = request.form.get('duedate')
        buddy_email = request.form.get('buddyemail')

        error = None
        if not task_title:
            error = 'A Title Is Required'
        if not task_duedate:
            error = "A Due Date is required"
            
        if error is  None:
            try: 
                newtask = Task(
                    title=task_title,
                    description=task_description,
                    user_id=session.get('user_id'),
                    due_date= datetime.fromisoformat(task_duedate) 
                )
                db.session.add(newtask)
                db.session.commit()
                
                # Add to buddy table
                BuddyContactController().addBuddy(newtask.id,newtask.user_id , buddy_email)
            except Exception as err:
                print(err)
                error = "Task was not added"
            else:
                return True   
        return error

    def findAllTask(self, user_id):
        error = None
        try: 
            tasks = db.session.query(Task).filter(Task.user_id==user_id).all()
        except:
            error = "No Tasks Founds"
            return (False, error)
        return (True, tasks)

    def findTask(self, task_id, user_id):
        try: 
            task = db.session.query(Task).filter(Task.user_id==user_id).filter(Task.id==task_id).first()
        except Exception as err:
            print(err)
            error = "Task Not found"
            return (False, error)
        return (True, task)

    def update(self, task_id):

        status, taskresponse = self.findTask(task_id,session.get('user_id'))
       
        if status:
            task_title = request.form.get('tasktitle')
            task_description  = request.form.get('description')
            task_duedate = request.form.get('duedate') 
            buddy_email = request.form.get('buddyemail') ## TODO update
           
            taskresponse.title = task_title
            taskresponse.description = task_description.strip()
            
            print(task_duedate)
            if task_duedate:
                taskresponse.due_date = datetime.fromisoformat(task_duedate)

            try:
                # https://docs.sqlalchemy.org/en/14/orm/tutorial.html#querying-with-joins
    
                db.session.add(taskresponse)  
                db.session.commit()
                taskresponse = "Task was Updated"
                # buddy = BuddyContactController().find(taskresponse.id)
                # buddy.first_buddy_email = buddy_email 
                # db.session.add(buddy)
                # db.session.commit()
               
            except Exception as err:
                print(err)
                status = False
                taskresponse = "Task was not updated"     
        return (status, taskresponse)
        
    def delete(self, task_id):
        user_id = session.get('user_id') 
        status, taskresponse = self.findTask(task_id,user_id)
        if status:
            try: 
                db.session.delete(taskresponse)
                db.session.commit()
                taskresponse = "Task deleted !"

            except Exception as err:
                print(err)
                status = False 
                taskresponse = "Task not deleted"

        return (status, taskresponse )



class BuddyContactController:
    def addBuddy(self, task_id, user_id, buddy_email):
        error = None
        if not buddy_email:
            error = "Need To add a buddy email"
        if error is  None:
            try:
                new_buddy = BuddyContact(
                    task_id=task_id,
                    user_id=user_id,
                    first_buddy_email= buddy_email
                )

                db.session.add(new_buddy)
                db.session.commit()
    
            except:
                error = "Buddy Contanct was not added"
            else:
                return True 
        else:
            return error
    
    def find(self, task_id):
        try: 
            buddy = db.session.query(BuddyContact).filter(BuddyContact.task_id==task_id).first()
        except Exception as err:
            print(err)
            error = "Buddy Contact Not found"
            return (False, error)
        return (True, buddy)
