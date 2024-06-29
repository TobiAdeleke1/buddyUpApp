from .helper_funcs import send_async_mail, format_email
from application import celery, mail, app


@celery.task
def bulk_send_mail(task_item, buddy_item):
    status, data = format_email(task_item, buddy_item)
    error = None
    with app.app_context():
        mail_to_send = send_async_mail(**data)
        try:
            mail.send(mail_to_send)
        except Exception as err:
            print(err)
            error = "Email Failed to send"
    return error