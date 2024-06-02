from flask_mail import Message

def send_async_mail(**kwargs):
    print(kwargs)
    msg = Message(
                subject=kwargs['subject'],
                sender=kwargs['sender'] ,
                recipients=kwargs['buddy'])
    msg.body = kwargs['message']
    return msg 

def get_database(database, table):
    # tasks = None
    # try: 
    #     tasks = database.session.query(table).all()
    # except:
    #     error = "No Tasks Founds"
    #     return (False, error)
    tasks = {'subject': 'Buddy Reminder',
             'sender':'olutobiadeleke@gmail.com',
              'buddy': 'tobiaadeleke@gmail.com',
              'message': '3 day- go Swiming'}
    return (True, tasks)