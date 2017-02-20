import sendgrid
import os
from sendgrid.helpers.mail import *


def sendMail(MailFrom, MailTo, MailMessage, MailSubject, ApiKey=None):
    '''
    Send an email with smtp login
    Args:
        MailFrom:       mail from
        MailTo:         delivery adress
        MailMessage:    The Message wich should be deliver
        MailSubject:    Mail Subject
        ApiKey:         Sendgrid API Key

    Returns:
    '''
    # Create message

    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python

    sg = sendgrid.SendGridAPIClient(apikey=ApiKey)
    from_email = Email(MailFrom)
    subject = MailSubject
    to_email = Email(MailTo)
    content = Content("text/plain", MailMessage)
    mail = Mail(from_email, subject, to_email, content)
    sg.client.mail.send.post(request_body=mail.get())
