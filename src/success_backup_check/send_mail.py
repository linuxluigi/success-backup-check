import smtplib
from email.mime.text import MIMEText

def sendMail(MailFrom, MailTo, MailMessage, MailSubject, ServerUsername, ServerPassword, ServerHostname, ServerPort):
    '''
    Send an email with smtp login
    Args:
        MailFrom:       mail from
        MailTo:         delivery adress
        ServerUsername: Username for SMTP Server
        ServerPassword: Password for SMTP Server
        MailMessage:    The Message wich should be deliver
        MailSubject:    Mail Subject
        ServerHostname: SMTP Hostname
        ServerPort:     SMTP Port

    Returns:
    '''
    # Create message

    msg = MIMEText(str(MailMessage))
    msg['Subject'] = MailSubject
    msg['From'] = MailFrom
    msg['To'] = MailTo

    # Create server object with SSL option
    server = smtplib.SMTP_SSL(ServerHostname, ServerPort)

    # Perform operations via server
    server.login(ServerUsername, ServerPassword)
    server.sendmail(MailFrom, [MailTo], msg.as_string())
    server.quit()