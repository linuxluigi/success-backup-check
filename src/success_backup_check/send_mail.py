import logging

from sendgrid import SendGridAPIClient


def send_mail(mail_from, mail_to, subject, message, api_key=None):
    """
    Send an email over sendgrid
    Args:
        mail_from:      mail from
        mail_to:        delivery address
        subject:        Mail Subject
        message:        The Message witch should be deliver
        api_key:        Sendgrid API Key
    """

    message = {
        'personalizations': [
            {
                'to': [
                    {
                        'email': mail_to
                    }
                ],
                'subject': subject
            }
        ],
        'from': {
            'email': mail_from
        },
        'content': [
            {
                'type': 'text/plain',
                'value': message
            }
        ]
    }
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        logging.error(e.message)

    logging.info("sendgrid mail was send")
    logging.info("statuscode: %s" % response.status_code)
    logging.info("body: %s" % response.body)
    logging.info("headers: %s" % response.headers)

    logging.info('email was send from %s to %s about %s' % (mail_from, mail_to, subject))


def send_simple_message(config, subject, message):
    """
    Simple mail send, just set subject & message. Everything else will automatic read from the config file.

    Args:
        config (object): config object from read_config
        subject:        Mail Subject
        message:        The Message witch should be deliver
    """

    send_mail(
        config['Mail']['From'],
        config['Mail']['To'],
        message,
        subject,
        config['Mail']['ApiKey']
    )
