import configparser

import ssl 
ssl._create_default_https_context = ssl._create_unverified_context 
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail

config=configparser.ConfigParser()

config.read("config.ini")

def sendMailUsingSendGrid(API, from_email, to_email, subject,html_content): 
    if API!=None and from_email!=None and len(to_email)>0: 
        message= Mail(from_email, to_email, subject,html_content) 
        try:
            sg = SendGridAPIClient(API) 
            response = sg.send(message) 
            print(response.status_code) 
            print(response.body) 
            print(response.headers) 
        except Exception as e: 
            print(e.message)
