import smtplib
import ssl
import os
import sys

from configparser import ConfigParser

def send_email(subject, to_addr, text_body, development=True):
    """
    Sends an emailS
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, 'email.ini')

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting ..")
        sys.exit(1)
    
    # Get Config files
    smtp_server =  cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")
    port = cfg.get("smtp", "port")
    password = cfg.get("smtp", "password")

    # Create Text Body
    BODY = "\r\n".join((
        "From: %s"% from_addr,
        "To: %s"% to_addr,
        "Subject: %s" %subject,
        "",
        text_body
    ))

    if development:
        ## Using local python email server
        server = smtplib.SMTP('localhost',1025)
        server.sendmail(from_addr,to_addr,BODY)
        server.quit(1)
        return None

    ## Use ssl to create a secure connection to GMAIL's SMTP server
    context = ssl.create_default_context()
    ## Context manager so it automatically quits
    with smtplib.SMTP_SSL(smtp_server,port, context=context) as server:
        server.login(from_addr, password)
        server.send_message(from_addr, to_addr, BODY) # NOTE: This might require sendmail method instead
    
    
if __name__== "__main__":
    subject = "Test email module"
    to_addr = "test@gmail.com"
    text_body = "It simiply is at it is"
    send_email(subject,to_addr,text_body)