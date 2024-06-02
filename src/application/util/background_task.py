from .helper_funcs import send_async_mail, get_database
from application import celery, mail
# from buddy_task.models import Task

@celery.task
def bulk_send_mail():
    
    status, data = get_database('', '')
    print(data)
    ## need to loop in app context
    mail_to_send = send_async_mail(**data)
    try:
     mail.send(mail_to_send)
    except Exception as err:
       print(err)

   
