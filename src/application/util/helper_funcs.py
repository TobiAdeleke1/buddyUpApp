from flask_mail import Message


def send_async_mail(**kwargs):
    print(kwargs)
    msg = Message(
                subject=kwargs['subject'],
                sender=kwargs['sender'],
                recipients=[kwargs['buddy']])
    msg.body = kwargs['message']
    return msg


def format_email(task_item, buddy_item):
    task = {'subject': task_item.title,
            'sender': 'olutobiadeleke@gmail.com',
            'buddy': buddy_item.first_buddy_email,
            'message': task_item.description}
    return (True, task)
